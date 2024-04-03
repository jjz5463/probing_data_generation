from datadreamer import DataDreamer
from datadreamer.llms import OpenAI
from datadreamer.steps import (
    DataFromAttributedPrompt,
    concat
)
from get_attribute import generate_attributes_for_sentences
from add_labels import add_feature

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
attributes = generate_attributes_for_sentences

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
                    "attributes": attributes[i*100:i*100+100]
                },
                outputs={"generations": "generated sentences"},
            )
            .select_columns(["generated sentences"])
            .shuffle()
        )
        probing_datasets.append(dataset)

    probing_dataset = concat(*probing_datasets, name='concat-probing-dataset')
    dataset = probing_dataset.map(add_feature, with_indices=True)

    # Publish and share the synthetic dataset
    dataset.publish_to_hf_hub(
        "jjz5463/probing_dataset_2.0",
        #add your token to huggingface
    )
