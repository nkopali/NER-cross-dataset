import pandas as pd
import ast
from collections import Counter
from tabulate import tabulate

# Convert to DataFrame
df = pd.read_csv("processed_data/pos_tagged_new_ncbitobc5.csv")

def save_latex_table(col_name, filename):
    def extract_pos_pattern(pos_list_str):
        item_list = []
        for items in pos_list_str:
            # print(items)
            nested_list = ast.literal_eval(items)
            # item_list.append(nested_list[0])
            for tags in nested_list:
                item_list.append(' '.join([pos[1] for pos in tags]))
        return item_list


    df_pos_list = extract_pos_pattern(df[col_name])
    # print(df_pos_list)

    with open('test.txt', 'w') as f:
        f.write(df.to_string(index=False))
    # Count the frequency of each pattern
    pattern_counts = Counter(df_pos_list)

    pattern_counts_df = pd.DataFrame(pattern_counts.items(), columns=['POS_Pattern', 'Frequency'])

    # Sort the DataFrame by frequency
    pattern_counts_df = pattern_counts_df.sort_values(by='Frequency', ascending=False)

    latex_table = tabulate(pattern_counts_df, headers=['Pattern', 'Frequency'], tablefmt="latex_longtable", showindex=False, stralign='left')
    with open(filename, 'w') as f:
        f.write(latex_table)

    # Display the result
    print(pattern_counts_df)

# save_latex_table("stanza_FP","latex_table_dataMerged_FP.txt")
# save_latex_table("stanza_FN","latex_table_dataMerged_FN.txt")
# save_latex_table("stanza_Overlap","latex_table_dataMerged_Overlap.txt")
# save_latex_table("stanza_Tags","latex_table_dataMerged_Tags.txt")

# save_latex_table("Pred", "latex_newDev_freq.txt")
save_latex_table("stanza_Tags", "latex_newDev_Stanza2.txt")