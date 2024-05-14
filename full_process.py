import re

set_of_features = ['Polite', 'Humor']
def split_examples(example, index, sentence_per_class):
    # Extract the generated sentences string
    generated_sentences = example['generated sentences'].replace('\n', ' ')

    # Split the string into formal and informal components
    # the format is "Formal: [formal sentence] Informal: [informal sentence]"
    split_sentences = re.split(r'\s*(?:Impolite|Without Humor):\s*', generated_sentences, flags=re.IGNORECASE)
    positive_sentence = re.sub(r'(Polite|With Humor):', '', split_sentences[0], flags=re.IGNORECASE)
    negative_sentence = split_sentences[1] if len(split_sentences) > 1 else ''
    # Update the example with new fields
    example['positive'] = positive_sentence
    example['negative'] = negative_sentence
    example['feature'] = set_of_features[index // sentence_per_class]
    return example