starting_statement = [
# Ajay's Selection
'''
Generate a pair of polite and impolite sentences with the following attributes:
''',
'''
Generate a pair of sentences with and without humor with the following attributes:
''',
'''
Generate a pair of sentences with and without sarcasm with the following attributes:
''',
'''
Generate a pair of sentences with and without metaphors with the following attributes:
''',
'''
Generate a pair of sentences containing offensive and non-offensive language with the following attributes:
''',
# Marianna's Selections
'''
Generate a pair of sentences, one sentence expressing positive tone and one expressing negative tone, with the following attributes:
''',
'''
Generate a pair of active and passive sentences with the following attributes:
''',
'''
Generate a pair of sentences expressing certainty and uncertainty, with the following attributes:
''',
'''
Generate a pair of sentences where in one sentence the speaker is being self-centered (uses 1st person singular pronouns), and in the other the speaker is being inclusive (uses 1st person plural pronouns), with the following attributes:
''',
'''
Generate a pair of sentences where in one sentence the speaker is being self-centered (uses 1st person singular pronouns), and in the other the speaker directly addresses another person, with the following attributes:
''',
'''
Generate a pair of sentences where in one sentence the speaker is being self-centered (uses 1st person singular pronouns), and in the other the speaker only uses third-person plural pronouns, with the following attributes:
''',
'''
Generate a pair of sentences, one sentence where the speaker is being self-focused and another sentence where the speaker  addresses a third person (using third-person singular pronouns), with the following attributes:
''',
'''
Generate a pair of sentences, where one sentence using personal pronouns more frequently than the other, with the following attributes:
''',
'''
Generate a pair of sentences where one sentence contains words focusing on the present and the other contains words focusing on the future, with the following attributes:
''',
'''
Generate a pair of sentences where one sentence focuses on the present and the other sentence focuses on the past, with the following attributes:
''',
'''
Generate a pair of sentences where one sentence expresses affective processes and the other expresses cognitive processes, with the following attributes:
''',
'''
Generate a pair of sentences where one sentence expresses affective processes and the other expresses perceptual processes, with the following attributes:
''',
'''
Generate a pair of sentences where one sentence expresses cognitive processes and the other expresses perceptual processes, with the following attributes:
''',
'''
Generate a pair of sentences where one sentence using articles more frequently than the other,  with the following attributes:
''',
'''
Generate a pair of sentences where one sentence is fluent and the other is disfluent, with the following attributes:
''',
'''
Generate a pair of sentences where one sentence using function words more frequently than the other, with the following attributes:
''',
'''
Generate a pair of sentences where one sentence using common verbs more frequently than the other, with the following attributes:
''',
'''
Generate a pair of sentences where one sentence using pronouns more frequently than the other, with the following attributes:
''',
'''
Generate a pair of sentences where one sentence using prepositions more frequently than the other, with the following attributes:
''',
'''
Generate a pair of sentences where one sentence using determiners more frequently than the other, with the following attributes:
''',
'''
Generate a pair of sentences where one sentence using conjunctions more frequently than the other, with the following attributes:
''',
'''
Generate a pair of sentences with and without nominalizations with the following attributes:
''',
'''
Generate a pair of sentences where one sentence contains longer words and the other sentence contains shorter words, with the following attributes:
''',
'''
Generate a pair of where one sentence using digits more frequently than the other, with the following attributes:
''',
'''
Generate a pair of sentences with and without uppercase letters with the following attributes:
''',
'''
Generate a pair of sentences where one sentence using punctuation more frequently than the other, with the following attributes:
''',
# original four sentences
'''
Generate a pair of sentences with formal and informal tones with the following attributes:
''',
'''
Generate a pair of sentences with complex and simple structures with the following attributes:
''',
'''
Generate a pair of sentences with and without contractions with the following attributes:
''',
'''
Generate a pair of sentences with and without number substitution (internet slang where people replace characters in words with numbers) with the following attributes:
'''
]

attributes_statement = [
'''
    1. Topic: {topic}
    2. Length: {length}
    3. Point of view: {point_of_view}
    4. Tense: {tense}
    5. Type of Sentence: {sentence_type}
'''
]

coditions_statement = [
'''
Ensure that the generated sentences meet the following conditions:

    1. There is no extra information in one sentence that is not in the other. 
    2. The difference between the two sentences is subtle. 
    3. The two sentences have the same length.
'''
]

format_instruction = [
'''
Use Format:
'''
]

format_statement = [
    # Ajay's Selection
    '''
    Polite: [sentence]
    Impolite: [sentence]
    ''',
    '''
    With Humor: [sentence]
    Without Humor: [sentence]
    ''',
    '''
    With sarcasm: [sentence]
    Without sarcasm: [sentence]
    ''',
    '''
    With metaphor: [sentence]
    Without metaphor: [sentence]
    ''',
    '''
    Offensive: [sentence]
    Non-Offensive: [sentence]
    ''',
    # Marianna's Selections
    '''
    Positive: [sentence]
    Negative: [sentence]
    ''',
    '''
    Active: [sentence]
    Passive: [sentence]
    ''',
    '''
    Certain: [sentence]
    Uncertain: [sentence]
    ''',
    '''
    Self-focused: [sentence]
    Inclusive-focused: [sentence]
    ''',
    '''
    Self-focused: [sentence]
    You-focused: [sentence]
    ''',
    '''
    Self-focused: [sentence]
    Audience-focused: [sentence]
    ''',
    '''
    Self-focused: [sentence]
    Third-person singular: [sentence]
    ''',
    '''
    With personal pronouns: [sentence]
    Less frequent pronouns: [sentence]
    ''',
    '''
    Present-focused: [sentence]
    Future-focused: [sentence]
    ''',
    '''
    Present-focused: [sentence]
    Past-focused: [sentence]
    ''',
    '''
    Affective processes: [sentence]
    Cognitive processes: [sentence]
    ''',
    '''
    Affective process: [sentence]
    Perceptual process: [sentence]
    ''',
    '''
    Cognitive process: [sentence]
    Perceptual process: [sentence]
    ''',
    '''
    With articles: [sentence]
    Less frequent articles: [sentence]
    ''',
    '''
    Fluent sentence: [sentence]
    Disfluent sentence: [sentence]
    ''',
    '''
    With function words: [sentence]
    Less frequent function words: [sentence]
    ''',
    '''
    With common verbs: [sentence]
    Less frequent common verbs: [sentence]
    ''',
    '''
    With pronouns: [sentence]
    Less frequent pronouns: [sentence]
    ''',
    '''
    With prepositions: [sentence]
    Less frequent prepositions: [sentence]
    ''',
    '''
    With determiners: [sentence]
    Less frequent determiners: [sentence]
    ''',
    '''
    With conjunctions: [sentence]
    Less frequent conjunctions: [sentence]
    ''',
    '''
    With nominalizations: [sentence]
    Without nominalizations: [sentence]
    ''',
    '''
    Long average word length: [sentence]
    Short average word length: [sentence]
    ''',
    '''
    With digits: [sentence]
    Less frequent digits: [sentence]
    ''',
    '''
    With uppercase letters: [sentence]
    Without uppercase letters: [sentence]
    ''',
    '''
    With frequent punctuation: [sentence]
    Less Frequent punctuation: [sentence]
    ''',
    # original four sentences
    '''
    Formal: [sentence]
    Informal: [sentence]
    ''',
    '''
    Complex: [sentence]
    Simple: [sentence]
    ''',
    '''
    With contractions: [sentence]
    Without contractions: [sentence]
    ''',
    '''
    With number substitution: [sentence]
    Without number substitution: [sentence]
    '''
]

ending_statement = [
'''
Your response should only consist of the two sentences, without quotation marks.
'''
]

prompts = [starting_statement[i] + attributes_statement[0] +
           coditions_statement[0] + format_instruction[0] +
           format_statement[i] + ending_statement[0]
           for i in range(len(starting_statement))]