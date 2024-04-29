prompts = [
    """                                  
    Here are some real-life examples of formal sentences compare to their less formal counterparts:
    (1) Formal: Three attractive women walk by and express their sympathy for him.
        Less formal: three beautiful girls walk by and feel really bad for him.
    (2) Formal: He wrote a song for us all to keep dreaming with.
        Less formal: He just gave us a song to keep dreaming with and alot of us do.
    (3) Formal: I did not really discuss it with my parents before, but I did mention it once. They did not respond, and did not seem to care.
        Less formal: I never told my parents before but mentioned it once and they said nothing and didn't care.
    (4) Formal: Hopefully, Taylor Hicks will be voted off soon, since his only unique characteristic is his gray hair.
        Less formal: taylor hicks will hopefully be voted out soon since he's just riding his lame gray hair.
    (5) Formal: Subsequently you will travel to the beach after achieving a high.
        Less formal: So when you get your high, you'll head out to the beach !)
    (6) Formal: I can not believe that you never heard of him, he rapped with 50Cent and a lot of other people.
        Less formal: ?He rapped with 50cent and alot of other people, I can't believe you don't know who he is?!!

    Now, generate a pair of formal and less formal sentences simulating real-life examples with the following attributes:
          1. Topic: {topic}
          2. Length: {length}
          3. Point of view: {point_of_view}
          4. Tense: {tense}
          5. Type of Sentence: {sentence_type}

    Ensure examples meets following conditions:
          1. examples do not frequently use dude, Yo, guys, folks. 
          2. Do not include any extra information in the formal sentence that is not in the less formal sentence.  
          3. difference between formal and less formal sentence is subtle.
          4. formal and less formal example have the same length.

    Formal: [sentence]
    Less formal: [sentence]

    Return just the sentences, no quotation marks.
    """,
    """
    Here are some real-life examples of complex sentences compare to their less complex counterparts:
    (1) Complex: A road number is often assigned to a stretch of public roadway.	
        Less Complex: A road number is often given a stretch of public roadway.
    (2) Complex: They had extensive maritime trade contacts with the Roman empire.
        Less Complex: They had many trade relationships with the Roman empire.
    (3) Complex: After gathering a list of names from fans and conducting an online poll, the feature was named ECW X-Stream on October 31, 2007.
        Less Complex: After making a list of names from fans and taking an online poll, the feature was named ECW X-Stream on October 31, 2007.	
    (4) Complex: On July 17 2006, the Keck-10m II telescope and its Laser guide star Adaptive Optics (AO) system indicated a bilobated shape for Hektor.
        Less Complex: On July 17 2006, the Keck-10m II telescope, and its Laser guide star Adaptive Optics system indicated a bilobated shape for Hektor.
    (5) Complex: Wilson settled in the district in late 1836 with his wife and family.
        Less Complex: Wilson made a home in the district in late 1836 with his wife and family.
    (6) Complex: Cognition is the scientific term for "the process of thought".
        Less Complex: Cognition is a term used in science for "the process of thought".

    Now, generate a pair of complex and less complex sentences simulating real-life examples with the following attributes:
          1. Topic: {topic}
          2. Length: {length}
          3. Point of view: {point_of_view}
          4. Tense: {tense}
          5. Type of Sentence: {sentence_type}

    Ensure examples meets following conditions:
          1. the complex sentence and the less complex sentence carry the exact same amount of information
          2. the difference between a complex and a less complex sentence is very subtle
          3. complex and less complex example have the same length

    Complex: [sentence]
    Less Complex: [sentence]

    Return just the sentences, no quotation marks.
    """,
    """
    Here are some real-life examples of sentence that use contraction compare to their without contraction counterparta:
    (1) With contraction: Here, two points on a sphere are called antipodal if they're in exactly opposite directions from the sphere's center.
        Without contraction: Here, two points on a sphere are called antipodal if they are in exactly opposite directions from the sphere's center.
    (2) With contraction: A hobby is a regular activity that's done for enjoyment, typically during one's leisure time
        Without contraction: A hobby is a regular activity that is done for enjoyment, typically during one's leisure time
    (3) With contraction: The government of Greenland doesn't have control of Greenland's military or foreign affairs
        Without contraction: The government of Greenland does not have control of Greenland's military or foreign affairs
    (4) With contraction: A men's basketball tournament was first held at the 1904 Olympics as a demonstration; it's been held at every Summer Olympics since 1936.
        Without contraction: A men's basketball tournament was first held at the 1904 Olympics as a demonstration; it has been held at every Summer Olympics since 1936.
    (5) With contraction: For example, in seven-card stud this is two downcards and one upcard, in Texas hold 'em it's two downcards, and in five-card draw it's five cards.
        Without contraction: For example, in seven-card stud this is two downcards and one upcard, in Texas hold 'em it is two downcards, and in five-card draw it is five cards.
    (6) With contraction: All of its isotopes are radioactive; it's extremely rare, with only about 500-600 grams naturally occurring in Earth's crust at any given time, and one of only two such elements that are followed in the periodic table by elements with stable forms, a distinction shared with technetium.
        Without contraction: All of its isotopes are radioactive; it is extremely rare, with only about 500-600 grams naturally occurring in Earth's crust at any given time, and one of only two such elements that are followed in the periodic table by elements with stable forms, a distinction shared with technetium.

    Now, generate a pair of `with contraction` and `without contraction` sentences simulating real-life examples with the following attributes:
          1. Topic: {topic}
          2. Length: {length}
          3. Point of view: {point_of_view}
          4. Tense: {tense}
          5. Type of Sentence: {sentence_type}

    With contraction: [sentence]
    Without contraction: [sentence]

    Return just the sentences, no quotation marks.
    """,
    """
    Here are some real-life sentences that use number substitution in words (eg. before -> b4, wait -> w8) compare to their no number substitution counterpart:
    (1) With number substitution: There are 46^8 passwords possible, but you start with words, then you do words with numbers or symbols around them, then you do words with l33t substitutions, then you do words with l33t substitutions and symbols around them. It's probably only feasible if you've got the hash of the password, because attempting that many logins would probably take forever.
        Without number substitution: There are 46^8 passwords possible, but you start with words, then you do words with numbers or symbols around them, then you do words with leet substitutions, then you do words with leet substitutions and symbols around them. It's probably only feasible if you've got the hash of the password, because attempting that many logins would probably take forever.
    (2) With number substitution: 2MORROW WILL BE THE BEST DAY OF UR LIFE.HOWEVER IF U DONT POST THIS COMMENT TO ATLEAST 3 VIDEOS U WILL DIE IN 2 DAYS.NOW UV STARTED READIN THIS SO DONT STOP NOW!THIS IS SOOO SCARY.SEND THIS TO ATLEAST 5 VIDEOS IN 143 MINUTES WHEN UR DONE PRESS F6 AND UR CRUSSHES NAMEWILL APPEAR ON THE SCREEN IN BIG LETTERS THIS IS SOO SCARY CUZ IT ACTUALLY WORKS!!!!!!!!
        Without number substitution: TOMORROW WILL BE THE BEST DAY OF UR LIFE.HOWEVER IF U DONT POST THIS COMMENT TO ATLEAST 3 VIDEOS U WILL DIE IN 2 DAYS.NOW UV STARTED READIN THIS SO DONT STOP NOW!THIS IS SOOO SCARY.SEND THIS TO ATLEAST 5 VIDEOS IN 143 MINUTES WHEN UR DONE PRESS F6 AND UR CRUSSHES NAMEWILL APPEAR ON THE SCREEN IN BIG LETTERS THIS IS SOO SCARY CUZ IT ACTUALLY WORKS!!!!!!!!
    (3) With number substitution: Tapped on the shoulder by the baton, sorry, ur not cool, ur not smart, and this is actually code that u smell like bad cheese! Now every1 knows! Post this on 10 other uni subreddits, or ur gonna get tapped on the shoulder by a baton when u graduate!
        Without number substitution: Tapped on the shoulder by the baton, sorry, ur not cool, ur not smart, and this is actually code that u smell like bad cheese! Now everyone knows! Post this on 10 other uni subreddits, or ur gonna get tapped on the shoulder by a baton when u graduate!
    (4) With number substitution: i wish i cud enter i only 12 and i h8 it if it always 16 or 18 to enter a compotion
        Without number substitution: i wish i cud enter i only 12 and i hate it if it always 16 or 18 to enter a compotion
    (5) With number substitution: cool, so what? There's 2 different pics with 3 full mules, you're such a h8r lol
        Without number substitution: cool, so what? There's 2 different pics with 3 full mules, you're such a hater lol
    (6) With number substitution: W0w de devil is nao leakin from roadblacks but srsly the real number is 600+16 (still does nothing)
        Without number substitution: Wow de devil is nao leakin from roadblacks but srsly the real number is 600+16 (still does nothing)

    Now, generate a pair of `with number substitution` and `without number substitution` sentences simulating real-life sentences with the following attributes:
          1. Topic: {topic}
          2. Length: {length}
          3. Point of view: {point_of_view}
          4. Tense: {tense}
          5. Type of Sentence: {sentence_type}

    Ensure examples meets following conditions:
          1. with number substitution sentence contain only 1 word with number substitution
          2. number substitution involves replacing words or parts of words with numerical digits
          3. only make transformations that naturally and frequently occur in slang use, such as changing "before" to "b4" or "forever" to "4ever"
          4. do no use other types of substitution, such as 'you' -> 'u', 'second' -> '2nd', 'never' -> 'nvr'
          5. besides number substitution, two sentences should be exactly the same

    With number substitution: [sentence]
    Without number substitution: [sentence]

    Return just the sentences, no quotation marks.
    """
]

# 1. complex sentence incorporate one or more of the following characteristics: parenthetical elements, subordinate clauses, complex vocabulary, or intricate syntax choices.