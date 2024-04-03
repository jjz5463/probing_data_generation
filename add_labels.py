from datadreamer import DataDreamer

with DataDreamer("./output"):
    def classify_feature(index):
        """Classify the feature based on the index."""
        if 0 <= index < 100:
            return 'formal'
        elif 100 <= index < 200:
            return 'informal'
        elif 200 <= index < 300:
            return 'complex'
        elif 300 <= index < 400:
            return 'simple'
        elif 400 <= index < 500:
            return 'with contraction'
        elif 500 <= index < 600:
            return 'without contraction'
        elif 600 <= index < 700:
            return 'with number substitution'
        elif 700 <= index < 800:
            return 'without number substitution'
        else:
            return 'unknown'  # For any index not within specified ranges

    # Define a function to use with map that incorporates the enumeration
    def add_feature(example, idx):
        example['feature'] = classify_feature(idx)
        return example