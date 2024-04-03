from datadreamer import DataDreamer
from datadreamer.llms import OpenAI
from datadreamer.steps import (
    DataFromAttributedPrompt,
    concat
)
from get_attribute import generate_attributes_for_sentences
from add_labels import add_feature
from pairwise import pair_examples

prompts = [
    """
    Please generate an extremely formal sentence with the following attributes:
                                  1. Topic: {topic}
                                  2. Length: {length}
                                  3. Point of view: {point_of_view}
                                  4. Tense: {tense}
                                  5. Voice: {voice}
                                  6. Type of Sentence: {sentence_type}
                                  Return just the sentence, no quotation marks.
    """,
    """
    Generate a sentence using extremely informal language with the following attributes:
                                  1. Topic: {topic}
                                  2. Length: {length}
                                  3. Point of view: {point_of_view}
                                  4. Tense: {tense}
                                  5. Voice: {voice}
                                  6. Type of Sentence: {sentence_type}
                                  Return just the sentence, no quotation marks.
    """,
    """
    Please generate a extremely complex sentence with the following attributes:
                              1. Topic: {topic}
                              2. Length: {length}
                              3. Point of view: {point_of_view}
                              4. Tense: {tense}
                              5. Voice: {voice}
                              6. Type of Sentence: {sentence_type}
                              Return just the sentence, no quotation marks.
    """,
    """
    Generate a very simple sentence with the following attributes:
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
attributes = generate_attributes_for_sentences(100)

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
                    "attributes": attributes
                },
                outputs={
                    "attributes": "attributes",
                    "generations": "generated sentences"
                },
            )
            .select_columns(["generated sentences", "attributes"])
        )
        probing_datasets.append(dataset)

    probing_dataset = concat(*probing_datasets, name='concat-probing-dataset')
    dataset = probing_dataset.map(add_feature, with_indices=True)
    paired_dataset = dataset.map(pair_examples,
                                 batched=True,
                                 batch_size=200,
                                 with_indices=True,
                                 remove_columns=['generated sentences'])

    # Publish and share the synthetic dataset
    paired_dataset.publish_to_hf_hub(
        "jjz5463/probing_dataset_4.0",
        #add your token to huggingface
    )

    paired_dataset.export_to_csv('data.csv')