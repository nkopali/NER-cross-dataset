import pandas as pd
from ast import literal_eval

# Function to extract total sentences, tokens, annotated entities (B/I), and unique entities
def extract_ner_statistics(file_path):
    df = pd.read_csv(file_path)
    total_sentences = len(df)
    
    total_tokens = 0
    total_entities = 0
    unique_entities = set()

    for index, row in df.iterrows():
        tokens_tags = literal_eval(row['Tags'])
        total_tokens += len(tokens_tags)
        
        # Counting entities and unique entities
        for token, tag in tokens_tags:
            if tag.startswith('B') or tag.startswith('I'):
                total_entities += 1
                unique_entities.add(token)

    result = {
        'Total Sentences': total_sentences,
        'Total Tokens': total_tokens,
        'Total Entities (B/I)': total_entities,
        'Unique Entities size ': len(unique_entities),
        'Unique Entities': unique_entities,
    }
    
    return result

def compare_entity_intersection(entities_set1, entities_set2):
    intersection = entities_set1.intersection(entities_set2)
    return len(intersection), intersection

bc5_train_ner_stats = extract_ner_statistics("csv/train_bc5_gold.csv")
# print("BC5 Train ",bc5_train_ner_stats)

ncbi_train_ner_stats = extract_ner_statistics("csv/train_ncbi_gold.csv")
# print("NCBI Train ",ncbi_train_ner_stats)
print()
print("train")

intersection_count, intersecting_entities = compare_entity_intersection(
    bc5_train_ner_stats['Unique Entities'], 
    ncbi_train_ner_stats['Unique Entities']
)

bc5_unique_entities = bc5_train_ner_stats['Unique Entities'].difference(ncbi_train_ner_stats['Unique Entities'])
ncbi_unique_entities =  ncbi_train_ner_stats['Unique Entities'].difference(bc5_train_ner_stats['Unique Entities'])

print(f"Number of intersecting entities: {len(intersecting_entities)}")
print(f"Number of unique entities in BC5: {len(bc5_unique_entities)}")
print(f"Number of unique entities in NCBI: {len(ncbi_unique_entities)}")
print()

print("test")
bc5_test_ner_stats = extract_ner_statistics("csv/test_bc5_gold.csv")
# print("BC5 Test ", bc5_test_ner_stats)

ncbi_test_ner_stats = extract_ner_statistics("csv/test_ncbi_gold.csv")
# print("NCBI Test ",ncbi_test_ner_stats)
print()

intersection_count, intersecting_entities = compare_entity_intersection(
    bc5_test_ner_stats['Unique Entities'], 
    ncbi_test_ner_stats['Unique Entities']
)

bc5_unique_entities = bc5_test_ner_stats['Unique Entities'].difference(ncbi_test_ner_stats['Unique Entities'])
ncbi_unique_entities =  ncbi_test_ner_stats['Unique Entities'].difference(bc5_test_ner_stats['Unique Entities'])

print(f"Number of intersecting entities: {len(intersecting_entities)}")
print(f"Number of unique entities in BC5: {len(bc5_unique_entities)}")
print(f"Number of unique entities in NCBI: {len(ncbi_unique_entities)}")

print()
print("dev")
dev_bc5_ner_stats = extract_ner_statistics("csv/dev_BC5.csv")
# print("BC5 Dev ",dev_bc5_ner_stats)

dev_ncbi_ner_stats = extract_ner_statistics("csv/dev_NCBI.csv")
# print("NCBI Dev ",dev_ncbi_ner_stats)

intersection_count, intersecting_entities = compare_entity_intersection(
    dev_bc5_ner_stats['Unique Entities'], 
    dev_ncbi_ner_stats['Unique Entities']
)

bc5_unique_entities = dev_bc5_ner_stats['Unique Entities'].difference(dev_ncbi_ner_stats['Unique Entities'])
ncbi_unique_entities =  dev_ncbi_ner_stats['Unique Entities'].difference(dev_bc5_ner_stats['Unique Entities'])

print(f"Number of intersecting entities: {len(intersecting_entities)}")
print(f"Number of unique entities in BC5: {len(bc5_unique_entities)}")
print(f"Number of unique entities in NCBI: {len(ncbi_unique_entities)}")

