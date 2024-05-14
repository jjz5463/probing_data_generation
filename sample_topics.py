import random
import re
import nltk
import langdetect
from datasets import load_dataset
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from collections import Counter
import json
from datadreamer import DataDreamer
from datadreamer.llms import OpenAI
from datadreamer.steps import (
    DataFromPrompt,
    concat
)
from transformers import GPT2Tokenizer
from tokens import gpt_api, hf_token

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def is_english(text):
    try:
        return langdetect.detect(text) == 'en'
    except Exception:
        return False


def text_complexity(text):
    if len(re.sub(r'[^\x00-\x7F]+', '', text)) / len(text) < 0.9:
        return False

    if re.search(r'data:image\/[a-zA-Z]*;base64,[^\s]+', text):
        return False

    metadata_patterns = [
        r'\b(login|submit|posted|reply|comment)\b',
        r'\d{4}-\d{2}-\d{2}',
        r'\b(on:|at:|UTC/GMT)\b',
        r'https?:\/\/\S+',
        r'@\w+',
    ]
    if any(re.search(pattern, text, re.IGNORECASE) for pattern in metadata_patterns):
        return False

    words = word_tokenize(text)
    lexical_diversity = len(set(words)) / len(words) if words else 0
    tagged_words = pos_tag(words)
    pos_counts = Counter(tag for word, tag in tagged_words)

    noun_count = pos_counts.get('NN', 0) + pos_counts.get('NNS', 0)
    verb_count = pos_counts.get('VB', 0) + pos_counts.get('VBD', 0) + pos_counts.get('VBG', 0) + pos_counts.get('VBN', 0) + pos_counts.get('VBP', 0) + pos_counts.get('VBZ', 0)
    adjective_count = pos_counts.get('JJ', 0) + pos_counts.get('JJR', 0) + pos_counts.get('JJS', 0)

    verb_to_noun_ratio = verb_count / noun_count if noun_count > 0 else 0
    adjective_to_noun_ratio = adjective_count / noun_count if noun_count > 0 else 0

    return lexical_diversity > 0.5 and verb_to_noun_ratio > 0.3 and adjective_to_noun_ratio > 0.2


def sample_long_sentence(text):
    sentences = sent_tokenize(text)
    long_sentences = [sentence for sentence in sentences if len(sentence.split()) > 32]
    if long_sentences:
        return random.choice(long_sentences)
    else:
        return None


def process_c4_dataset(limit=800):
    dataset = load_dataset("allenai/c4", "en", split='train', streaming=True)
    processed_sentences = []

    for example in dataset:
        text = example['text']
        if is_english(text) and text_complexity(text):
            long_sentence = sample_long_sentence(text)
            if long_sentence:
                processed_sentences.append(long_sentence)
            if len(processed_sentences) >= limit:
                break

    return processed_sentences


processed_sentences = process_c4_dataset(10000)


def save_texts_to_file(texts, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(texts, file, ensure_ascii=False, indent=4)


#save_texts_to_file(processed_sentences, 'sampled_sentences_large.json')


def read_texts_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        texts = json.load(file)
    return texts


def count_gpt4_tokens(text, model_name='gpt2'):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    tokens = tokenizer.encode(text)
    token_count = len(tokens)
    return token_count


def truncate_to_gpt4_tokens(text, token_limit=8192, model_name='gpt2'):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    tokens = tokenizer.encode(text)[:token_limit]
    truncated_text = tokenizer.decode(tokens, clean_up_tokenization_spaces=True)
    return truncated_text


#texts_list = read_texts_from_file('sampled_sentences_large.json')
texts_list = processed_sentences

api = gpt_api # enter your gpt token


with (((DataDreamer("./output")))):
    gpt_4 = OpenAI(model_name="gpt-4", api_key=api)
    generation_prompts = ("What is the fine-grained topic of the following text: ")
    closing_prompts = " Only return the topic."

    constant_token_count = count_gpt4_tokens(generation_prompts + closing_prompts)

    probing_datasets = []

    for i, text in enumerate(texts_list):
        if count_gpt4_tokens(text) > 8192 - constant_token_count:
            text = truncate_to_gpt4_tokens(text, 8192 - constant_token_count)

        dataset = DataFromPrompt(
            f"common crawl sampled sentence",
            args={
                "llm": gpt_4,
                "n": 1,
                "temperature": 1,
                "instruction": (
                    generation_prompts + text + closing_prompts
                ),
            },
            outputs={
                "prompts": "Common crawl text",
                "generations": "Topics"
            },
        )
        probing_datasets.append(dataset)

    probing_dataset = concat(*probing_datasets, name='topics of sampled common crawl sentences')

    # Publish and share the synthetic dataset
    probing_dataset.publish_to_hf_hub(
        "jjz5463/topics_common_crawl_large_1.0",
        token=hf_token
        # enter your huggingface token
    )