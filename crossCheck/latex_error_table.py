import pandas as pd
from tabulate import tabulate

def generate_latex_table(file_path, indices):
    # Load the dataset from the provided file path
    data = pd.read_csv(file_path)

    table_data = []

    # Loop through each index and append rows for Model, Sentence, Gold, and Predicted
    for index in indices:
        row = data.iloc[index]
        table_data.extend([
            ["Dataset", row["Data"]],
            ["Sentence", row["Sentence"]],
            ["Gold", row["Gold"]],
            ["Predicted", row["Pred"]],
            []
        ])
    
    # Generate the LaTeX table using tabulate
    latex_table = tabulate(table_data, headers=["Column", "Value"], tablefmt="latex_longtable")
    latex_table = latex_table.replace("{ll}", "{l|p{12cm}}")

    return latex_table

file_path = 'processed_data/ncbitobc5LatexConsecutive.csv'
print(generate_latex_table(file_path, [1,2]))
