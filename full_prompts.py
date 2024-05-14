prompts = [
    '''
    Generate a pair of polite and impolite sentences simulating real-life examples with the following attributes:
      	1. Topic: {topic}
      	2. Length: {length}
      	3. Point of view: {point_of_view}
      	4. Tense: {tense}
      	5. Type of Sentence: {sentence_type}

    Ensure examples meets following conditions:
      	1. Examples do not frequently use dude, Yo, guys, folks.
      	2. Do not include any extra information in the polite sentence that is not in the impolite sentence.  
      	3. difference between polite and impolite sentence is subtle.
      	4. polite and impolite example have the same length.

	Polite: [sentence]
	Impolite: [sentence]

	Return just the sentences, no quotation marks.
    ''',
    '''
    Generate a pair of with humor and without humor sentences simulating real-life examples with the following attributes:
      	1. Topic: {topic}
      	2. Length: {length}
      	3. Point of view: {point_of_view}
      	4. Tense: {tense}
      	5. Type of Sentence: {sentence_type}

    Ensure examples meets following conditions:
      	1. Examples do not frequently use dude, Yo, guys, folks.
      	2. Do not include any extra information in the with humor sentence that is not in the without humor sentence.  
      	3. difference between with humor and without humor sentence is subtle.
      	4. With humor and without humor example have the same length.

	With Humor: [sentence]
	Without Humor: [sentence]

	Return just the sentences, no quotation marks.
    '''
]