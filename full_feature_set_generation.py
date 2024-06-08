from datadreamer import DataDreamer
from datadreamer.llms import OpenAI
from datadreamer.steps import (
    DataFromAttributedPrompt,
    concat
)
from get_attribute import generate_attributes_for_sentences
from full_prompts import prompts
from full_process import split_examples
from tokens import gpt_api, hf_token

api = gpt_api
sentence_per_class = 100
num_of_features = len(prompts)
attributes = generate_attributes_for_sentences(num_of_features * sentence_per_class)

with DataDreamer("./output"):
    gpt_4 = OpenAI(model_name="gpt-4", api_key=api)

    probing_datasets = []

    for i, prompt in enumerate(prompts):
        dataset = (
            DataFromAttributedPrompt(
                "Generate Probing Sentences",
                args={
                    "llm": gpt_4,
                    "n": sentence_per_class,
                    'temperature': 1,
                    'top_p': 1,
                    "instruction": prompt,
                    "attributes": attributes[i*sentence_per_class:i*sentence_per_class+sentence_per_class]
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
    dataset = probing_dataset.map(lambda example, indices: split_examples(example, indices, sentence_per_class),
                                  with_indices=True, remove_columns=['generated sentences'])

    # Publish and share the synthetic dataset
    dataset.publish_to_hf_hub(
        "jjz5463/full_set_features_1.0",
        token= hf_token
    )