import itertools
import random
import pprint
from datasets import load_dataset


def load_topics_from_hf():
    dataset = load_dataset("jjz5463/topics_common_crawl_large_1.0")
    topics = dataset['train']['Topics']
    return topics


topics = load_topics_from_hf()
length = ['10-15 words', '15-20 words', '20-25 words', '25-30 words']
point_of_view = ['first-person', 'second-person', 'third-person']
tense = ['past', 'present', 'future']
#voice = ['active voice', 'passive voice']
type_of_sentence = ['Declarative', 'Semicolon Structure (compound)', 'Question', 'Exclamation']


def generate_attributes_for_sentences(n):
  r = random.Random(42)
  all_attribute_combinations = list(itertools.product(length, point_of_view, tense, type_of_sentence))
  attributes = []
  for t in topics[:n]:
    sample = random.choice(all_attribute_combinations)
    attributes.append({
      "topic": t,
      "length": sample[0],
      "point_of_view": sample[1],
      "tense": sample[2],
      #"voice": sample[3],
      "sentence_type": sample[3],
    })
  return attributes

#pprint.pprint(generate_attributes_for_sentences(6))

# Now you can pass: `"attributes": generate_attributes_for_sentences(100)` directly in the `DataFromAttributedPrompt` step