import re
def split_examples(example, index, sentence_per_class):
    # Extract the generated sentences string
    generated_sentences = example['generated sentences']

    if 0 <= index < sentence_per_class:
        # Split the string into formal and informal components
        # the format is "Formal: [formal sentence] Informal: [informal sentence]"
        split_sentences = re.split(r'\n\s*Informal: ', generated_sentences, flags=re.IGNORECASE)
        print(split_sentences)
        formal_sentence = split_sentences[0].replace('Formal: ', '')
        informal_sentence = split_sentences[1] if len(split_sentences) > 1 else ''
        # Update the example with new fields
        example['positive'] = formal_sentence
        example['negative'] = informal_sentence
        example['feature'] = 'formal'
        return example

    elif sentence_per_class <= index < 2 * sentence_per_class:
        split_sentences = re.split(r'\n\s*Simple: ', generated_sentences, flags=re.IGNORECASE)
        complex_sentence = split_sentences[0].replace('Complex: ', '')
        simple_sentence = split_sentences[1] if len(split_sentences) > 1 else ''
        example['positive'] = complex_sentence
        example['negative'] = simple_sentence
        example['feature'] = 'complex'
        return example

    elif 2 * sentence_per_class <= index < 3 * sentence_per_class:
        split_sentences = re.split(r'\n\s*Without contraction: ', generated_sentences, flags=re.IGNORECASE)
        contract_sentence = split_sentences[0].replace('With contraction: ', '')
        wo_contract_sentence = split_sentences[1] if len(split_sentences) > 1 else ''
        example['positive'] = contract_sentence
        example['negative'] = wo_contract_sentence
        example['feature'] = 'contraction'
        return example

    else:
        split_sentences = re.split(r'\n\s*Without number substitution: ', generated_sentences, flags=re.IGNORECASE)
        subs_sentence = split_sentences[0].replace('With number substitution: ', '')
        wo_subs_sentence = split_sentences[1] if len(split_sentences) > 1 else ''
        example['positive'] = subs_sentence
        example['negative'] = wo_subs_sentence
        example['feature'] = 'substitution'
        return example