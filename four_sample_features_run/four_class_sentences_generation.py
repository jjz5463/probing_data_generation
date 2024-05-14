from datadreamer import DataDreamer
from datadreamer.llms import OpenAI
from datadreamer.steps import (
    DataFromAttributedPrompt,
    concat
)
from ..get_attribute import generate_attributes_for_sentences
from prompts import prompts
from process import split_examples
from ..tokens import gpt_api, hf_token

api = gpt_api
sentence_per_class = 100
attributes = generate_attributes_for_sentences(sentence_per_class)

with DataDreamer("../output"):
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
    dataset = probing_dataset.map(lambda example, indices: split_examples(example, indices, sentence_per_class),
                                  with_indices=True, remove_columns=['generated sentences'])

    # Publish and share the synthetic dataset
    dataset.publish_to_hf_hub(
        "jjz5463/probing_dataset_9.0",
        token= hf_token
        #add your token to huggingface
    )

    #dataset.export_to_csv('data.csv')