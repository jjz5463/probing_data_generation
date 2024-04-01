from datadreamer import DataDreamer
from datadreamer.llms import OpenAI
from datasets import load_dataset
from datadreamer.steps import (
    Prompt,
    DataSource,
    DataFromAttributedPrompt,
    concat
)

prompts = [
    """
    Generate a sentence in formal language with the following attributes:
                                  1. Topic: {topic}
                                  2. Length: {length}
                                  3. Point of view: {point_of_view}
                                  4. Tense: {tense}
                                  5. Voice: {voice}
                                  6. Type of Sentence: {sentence_type}
                                  Return just the sentence, no quotation marks.
    """,
    """
    Generate a sentence using informal with the following attributes:
                                  1. Topic: {topic}
                                  2. Length: {length}
                                  3. Point of view: {point_of_view}
                                  4. Tense: {tense}
                                  5. Voice: {voice}
                                  6. Type of Sentence: {sentence_type}
                                  Return just the sentence, no quotation marks.
    """,
    """
    Generate a complex sentence with the following attributes:
                              1. Topic: {topic}
                              2. Length: {length}
                              3. Point of view: {point_of_view}
                              4. Tense: {tense}
                              5. Voice: {voice}
                              6. Type of Sentence: {sentence_type}
                              Return just the sentence, no quotation marks.
    """,
    """
    Generate a simple sentence with the following attributes:
                          1. Topic: {topic}
                          2. Length: {length}
                          3. Point of view: {point_of_view}
                          4. Tense: {tense}
                          5. Voice: {voice}
                          6. Type of Sentence: {sentence_type}
                          Return just the sentence, no quotation marks.
    """,
    """
    Generate a sentence with many contraction (eg. couldn’t: could not, didn’t: did not, doesn’t: does not) with the following attributes:
                          1. Topic: {topic}
                          2. Length: {length}
                          3. Point of view: {point_of_view}
                          4. Tense: {tense}
                          5. Voice: {voice}
                          6. Type of Sentence: {sentence_type}
                          Return just the sentence, no quotation marks.
    """,
    """
    Generate a sentence avoids contractions (eg. couldn’t: could not, didn’t: did not, doesn’t: does not) with the following attributes:
                          1. Topic: {topic}
                          2. Length: {length}
                          3. Point of view: {point_of_view}
                          4. Tense: {tense}
                          5. Voice: {voice}
                          6. Type of Sentence: {sentence_type}
                          Return just the sentence, no quotation marks.
    """,
    """
    Generate a sentence using number substitution (eg. 2morrow: tomorrow, l00k: look, 4ever: forever) with the following attributes:
                          1. Topic: {topic}
                          2. Length: {length}
                          3. Point of view: {point_of_view}
                          4. Tense: {tense}
                          5. Voice: {voice}
                          6. Type of Sentence: {sentence_type}
                          Return just the sentence, no quotation marks.
    """,
    """
    Generate a sentence that does not use any number substitution (eg. 2morrow: tomorrow, l00k: look, 4ever: forever) with the following attributes:
                          1. Topic: {topic}
                          2. Length: {length}
                          3. Point of view: {point_of_view}
                          4. Tense: {tense}
                          5. Voice: {voice}
                          6. Type of Sentence: {sentence_type}
                          Return just the sentence, no quotation marks.
    """,
]

api = '' # enter your gpt token


def load_topics_from_hf():
    dataset = load_dataset("jjz5463/topics_common_crawl_2.0")
    topics = dataset['train']['Topics']
    return topics


# Load topics, and other attributes
topics = load_topics_from_hf()
length = ['5-10 words', '10-20 words']
point_of_view = ['first-person', 'second-person', 'third-person']
tense = ['past', 'present', 'future']
voice = ['active voice', 'passive voice']
type_of_sentence = ['Standard Sentence', 'Semicolon Structure (compound)', 'Question', 'Exclamation']


with DataDreamer("./output"):
    gpt_4 = OpenAI(model_name="gpt-4", api_key=api)

    probing_datasets = []

    for i, prompt in enumerate(prompts):
        dataset = (
            DataFromAttributedPrompt(
                "Generate Probing Sentences",
                args={
                    "llm": gpt_4,
                    "n": 100,
                    "instruction": prompt,
                    "attributes": {
                        "topic": topics,
                        "length": length,
                        "point_of_view": point_of_view,
                        "tense": tense,
                        "voice": voice,
                        "sentence_type": type_of_sentence,
                    },
                },
                outputs={"generations": "generated sentences"},
            )
            .select_columns(["generated sentences"])
            .shuffle()
        )
        probing_datasets.append(dataset)

    probing_dataset = concat(*probing_datasets, name='concat-probing-dataset')

    # Publish and share the synthetic dataset
    probing_dataset.publish_to_hf_hub(
        "jjz5463/probing_dataset_2.0",
        #add your token to huggingface
    )
