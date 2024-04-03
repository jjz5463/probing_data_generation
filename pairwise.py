def pair_examples(batch, indices):
    # Initialize containers for the new batch data
    positive_sentences = []
    negative_sentences = []
    features = []
    attributes = []

    # Iterate over the indices of each example in the batch
    for idx in indices:
        # Calculate the position within the batch to determine if it's positive or negative
        pos_in_batch = idx % 200  # Use modulo to find position within current batch of 200

        if pos_in_batch < 100:
            # If the position is less than 100, it's a positive example
            positive_sentences.append(batch['generated sentences'][pos_in_batch])
            features.append(batch['feature'][pos_in_batch])
            attributes.append(batch['attributes'][pos_in_batch])
        else:
            # Otherwise, it's a negative example
            negative_index = pos_in_batch - 100  # Match to corresponding positive example
            negative_sentences.append(batch['generated sentences'][pos_in_batch])

    # Return structured pairs
    return {
        'positive': positive_sentences,
        'negative': negative_sentences,
        'feature': features,
        'attributes': attributes
    }

