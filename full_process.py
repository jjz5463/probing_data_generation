import re
import full_prompts

# create a string for positive and negative keywords
first_parts = []
second_parts = []
for statement in full_prompts.format_statement:
    parts = statement.strip().split('\n')
    first_part = parts[0].split(':')[0].strip()
    second_part = parts[1].split(':')[0].strip()
    first_parts.append(first_part)
    second_parts.append(second_part)
positive_keywords = '|'.join(first_parts)
negative_keywords = '|'.join(second_parts)

set_of_features = [first_parts[i] + ' / ' + second_parts[i] for i in range(len(first_parts))]


def split_examples(example, index, sentence_per_class):
    # Extract the generated sentences string
    generated_sentences = example['generated sentences'].replace('\n', ' ')

    # Split the string into formal and informal components
    # the format is "Formal: [formal sentence] Informal: [informal sentence]"
    split_sentences = re.split(rf'\s*(?:{negative_keywords}):\s*', generated_sentences, flags=re.IGNORECASE)
    positive_sentence = re.sub(rf'({positive_keywords}):', '', split_sentences[0], flags=re.IGNORECASE)
    negative_sentence = split_sentences[1] if len(split_sentences) > 1 else ''
    # Update the example with new fields
    example['positive'] = positive_sentence.strip().strip('\"\'')
    example['negative'] = negative_sentence.strip().strip('\"\'')
    example['feature'] = set_of_features[index // sentence_per_class]
    return example