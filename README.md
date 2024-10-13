# Project Overview

This repository contains Python scripts for performing data preprocessing, analysis, and evaluation on biomedical Named Entity Recognition (NER) datasets. We used two models for NER tasks, namely BioBERT and KebioLM, and instructions for each model can be found within their respective folders. The scripts focus on tasks such as filtering datasets, generating LaTeX tables, part-of-speech tagging, and comparing evaluation results. Below is an overview of each file in this repository.

## Files Description

### 1. `eval_compare.py`
- **Purpose**: Compares gold-standard and predicted NER tags to identify differences in the filtered datasets, which are then stored in a CSV file.

### 2. `analysis_merged.py`
- **Purpose**: Merges, processes, and analyzes the validation datasets to compare gold and predicted tags, identifying false positives, false negatives, and overlapping entities. The processed data, including error types and consecutive tag sequences, is saved as a csv. To display a specific dataset, start by first executing the `eval_compare.py` script on it.

### 3. `filtered_csv.py`
- **Purpose**: Filters entities in the validation dataset based on the entities found in the training dataset. The script saves the filtered data as a csv file and processes it further using the `decompose.py` python script.

### 4. `latex_error_table.py`
- **Purpose**: Generates a LaTeX table from a CSV file, displaying sentences, gold-standard labels, and predicted labels for error analysis. The table is formatted using the `tabulate` library and is ready for LaTeX integration. To display a specific dataset, start by first executing the `analysis_merged.py` script on it.

### 5. `pos_tagging.py`
- **Purpose**: Applies part-of-speech (POS) tagging to sentences in a dataset using the Stanza NLP libraries. The tagged data is saved to a new CSV file for further analysis. To display a specific dataset, start by first executing the `analysis_merged.py` script on it.

### 6. `pos_tagging_freq.py`
- **Purpose**: Calculates the frequency of POS tag patterns and saves the results as a LaTeX table. This provides insights into common patterns within the dataset, aiding in error analysis and reporting. To display the frequencies, start by first executing the `pos_tagging.py` script on the dataset you wish to analyse.

### 7. `basic_stats.py`
- **Purpose**: Computes basic statistics about the datasets, such as the number of sentences, tokens, entities, and unique entities.

### 8. `decompose.py`
- **Purpose**: Converts CSV data into a TSV format suitable for training or evaluation in both NER models.

---

Ensure that all dependencies, such as `pandas`, `ast`, `tabulate` and `stanza` are installed before running these scripts.
