import pandas as pd
import ast
from decompose import decompose

# Load the CSV files
train_df = pd.read_csv('csv/train_ncbi_gold.csv') # The train dataset
dev_df = pd.read_csv('csv/dev_ncbi.csv') # The dataset we want to filter

print("Train", train_df.shape)
print("Dev", dev_df.shape)

# Extract entities from train_df, excluding 'O' entities
def extract_entities(df):
    train_entities = []
    train_tag_words = []
    for tags in df['Tags']:
        for word, entity in ast.literal_eval(tags):
            if entity != 'O':
                train_entities.append((word, entity))
                train_tag_words.append(word)
    return train_entities, train_tag_words

train_entities, train_tag_words = extract_entities(train_df)

# Function to check if a sentence contains any of the train entities
def contains_train_entity(tags):
    for word, entity in ast.literal_eval(tags):
        if entity != 'O':
            if (word, entity) not in train_entities :
                return False
    return True

# Filter dev_df to include only rows where the entity is found in train_entities
filtered_dev_df = dev_df[dev_df['Tags'].apply(contains_train_entity)]

print(len(filtered_dev_df))
filename = "filtered_dev_bc5_onncbi.csv"

filtered_dev_df.to_csv(filename, index=False)

decompose(filename)
