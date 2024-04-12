prompts = [
    """                                  
    Here are some examples of real life formal sentences compare to its informal counterpart:
    (1) Formal: Two reasons I favor this performing group is their ability to write their own songs and play their own music.
        Informal: a) they right their own songs b) they ACTUALLY play their own music!
    (2) Formal: They are simply interested in expressing themselves, and creating a lively tune.
        Informal: They just want to express what they like and making a banging tune :)
    (3) Formal: I did not really discuss it with my parents before, but I did mention it once. They did not respond, and did not seem to care.
        Informal: I never told my parents before but mentioned it once and they said nothing and didn't care.
    (4) Formal: Thank you for the thought, but I would not desire to have a funeral party in my honor.
        Informal: I would not want a funeral party thrown for me Thanks anyway!!!
    (5) Formal: Maybe you will be able to use these next year.
        Informal: Maybe u can use these for next year.
        
    Now, generate a formal sentence and an informal sentence with the following attributes:
                              1. Topic: {topic}
                              2. Length: {length}
                              3. Point of view: {point_of_view}
                              4. Tense: {tense}
                              5. Voice: {voice}
                              6. Type of Sentence: {sentence_type}
    Return just the sentence, no quotation marks.
    """,
    """
    Here are some examples of real life complex sentences compare to its simple counterpart:
    (1) Complex: Description Pack rats are prevalent in the deserts and highlands of western United States and northern Mexico.
        Simple: Description: Pack rats are normally seen in the deserts and highlands of western United States and northern Mexico
    (2) Complex: Since then, documentation of saffron's use over the span of 4,000 years in the treatment of some 90 illnesses has been uncovered.
        Simple: Since then documentation of saffron's use over 4,000 years in the treatment of around 90 illnesses has been found.
    (3) Complex: Oregano is an indispensable ingredient in Greek cuisine.
        Simple:Oregano is a not replaceable part in Greek cuisine.
    (4) Complex: He also completed two collections of short stories entitled The Ribbajack & Other Curious Yarns and Seven Strange and Ghostly Tales.
        Simple: He also finished two sets of short stories called The Ribbajack & Other Curious Yarns and Seven Strange and Ghostly Tales.
    (5) Complex: He was considered by many to be a saint.
        Simple: Many think, that he was a saint.
    
    Now, generate a complex sentence and a simple sentence with the following attributes:
                          1. Topic: {topic}
                          2. Length: {length}
                          3. Point of view: {point_of_view}
                          4. Tense: {tense}
                          5. Voice: {voice}
                          6. Type of Sentence: {sentence_type}
    Return just the sentence, no quotation marks.
    """,
    """
    Here are some examples of real life sentence that use contraction compare to its without contraction counterpart:
    (1) With contraction: Here, two points on a sphere are called antipodal if they're in exactly opposite directions from the sphere's center.
        Without contraction: Here, two points on a sphere are called antipodal if they are in exactly opposite directions from the sphere's center.
    (2) With contraction: A hobby is a regular activity that's done for enjoyment, typically during one's leisure time
        Without contraction: A hobby is a regular activity that is done for enjoyment, typically during one's leisure time
    (3) With contraction: The government of Greenland doesn't have control of Greenland's military or foreign affairs
        Without contraction: The government of Greenland does not have control of Greenland's military or foreign affairs
    (4) With contraction: The 'existence' referred to needn't be 'real', but exist only in a universe of discourse.
        Without contraction: The 'existence' referred to need not be 'real', but exist only in a universe of discourse.
    (5) With contraction: Government bonds are usually denominated in the country's own currency, in which case the government can't be forced to default, although it may choose to do so.
        Without contraction: Government bonds are usually denominated in the country's own currency, in which case the government cannot be forced to default, although it may choose to do so.
    
    Now, generate a sentence with contraction and a sentence without contraction with the following attributes:
                          1. Topic: {topic}
                          2. Length: {length}
                          3. Point of view: {point_of_view}
                          4. Tense: {tense}
                          5. Voice: {voice}
                          6. Type of Sentence: {sentence_type}
    Return just the sentence, no quotation marks.
    """,
    """
    Here are some examples of real life sentences that use number substitution compare to its no number substitution counterpart:
    (1) With number substitution: No it's part of the game since b4 2007
        Without number substitution: No it's part of the game since before 2007
    (2) With number substitution: I also hope my 2 little puppies live 4ever
        Without number substitution: I also hope my 2 little puppies live forever
    (3) With number substitution: I may actually attend session 2 2day
        Without number substitution: I may actually attend session 2 today
    (4) With number substitution: H0w did y0u beat that ark lv10 ?!! It's s0 hard !
        Without number substitution: How did you beat that ark lv10 ?!! It's so hard !
    (5) With number substitution: THAT WA5 VERY IMPRE55IVE!
        Without number substitution: THAT WAS VERY IMPRESSIVE!
    
    Now, generate a sentence with number substitution and a sentence without number substitution with the following attributes:
                          1. Topic: {topic}
                          2. Length: {length}
                          3. Point of view: {point_of_view}
                          4. Tense: {tense}
                          5. Voice: {voice}
                          6. Type of Sentence: {sentence_type}
    Not every word need to have substitution, also only use substitution where human would likely do. Return just the sentence, no quotation marks.
    """
]