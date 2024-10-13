import pandas as pd
import stanza
import spacy
import ast

data = pd.read_csv('processed_data/ncbitobc5LatexConsecutive.csv')

df = pd.DataFrame(data)

stanza.download('en')
nlp_stanza = stanza.Pipeline('en')
nlp_spacy = spacy.load("en_core_web_sm")

def pos_tagging_stanza(tags):
    pos_tags = []
    for tag in tags:
        doc = nlp_stanza(tag)
        pos_tags.append([(word.text, word.upos) for sent in doc.sentences for word in sent.words])
    return pos_tags

# def pos_tagging_spacy(tags):
#     pos_tags = []
#     for tag in tags:
#         doc = nlp_spacy(tag)
#         pos_tags.append([(token.text, token.pos_) for token in doc])
#     return pos_tags

df['Tags'] = df['Tags'].apply(ast.literal_eval)
# df['Pred'] = df['Pred'].apply(ast.literal_eval)

# Apply POS tagging to the "Tags" column using Stanza
df['stanza_Tags'] = df['Tags'].apply(lambda tags: pos_tagging_stanza(tags))

# df['stanza_FP'] = df['FP'].apply(lambda tags: pos_tagging_stanza(ast.literal_eval(tags)))

# df['stanza_FN'] = df['FN'].apply(lambda tags: pos_tagging_stanza(ast.literal_eval(tags)))

# df['stanza_Overlap'] = df['Overlap'].apply(lambda tags: pos_tagging_stanza(ast.literal_eval(tags)))

# df['stanza_Pred'] = df['Pred'].apply(lambda tags: pos_tagging_stanza(tags))

# Apply POS tagging to the "Tags" column using SpaCy
# df['Tags_POS_SpaCy'] = df['Tags'].apply(lambda tags: pos_tagging_spacy(tags))

pd.set_option('display.max_columns', None)  # Ensure all columns are shown

# Display the resulting DataFrame
# print(df[['Tags', 'Tags_POS_Stanza', 'Tags_POS_SpaCy']])
df.to_csv("pos_tagged_new_ncbitobc52.csv", index=False)

