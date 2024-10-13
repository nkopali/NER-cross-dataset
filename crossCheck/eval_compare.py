import pandas as pd
import ast

gold_df = pd.read_csv('processed_data/filtered_dev_bc5_onncbi.csv') # The ground truth
pred_df1 = pd.read_csv('processed_data/ncbitobc5-filtered-newdev.csv') # Predictions

diff_tags = []

for index, gold_row  in gold_df.iterrows():
    gold_tags = ast.literal_eval(gold_row['Tags'])
    pred_tags = ast.literal_eval(pred_df1.iloc[index]['Tags'])
    
    # Check if there's any tag different between gold and pred
    has_difference = False

    for g_tag, p_tag in zip(gold_tags, pred_tags):
        if g_tag != p_tag:
            has_difference = True
            diff_tags.append({
                'Sentence': gold_row['Sentence'] ,
                'Gold': g_tag,
                'Pred': p_tag,
                # 'word' : g_tag[0]
            })
            # break


diff_tags_df = pd.DataFrame(diff_tags)

diff_tags_df.to_csv('diff_tags_new_ncbitobc5.csv', index=False)


