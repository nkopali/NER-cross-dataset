# Project Overview

This repository contains Python scripts for performing data preprocessing, analysis, and evaluation on biomedical Named Entity Recognition (NER) datasets. We used two models for NER tasks, namely BioBERT and KebioLM, and instructions for each model can be found within their respective folders. The scripts focus on tasks such as filtering datasets, generating LaTeX tables, part-of-speech tagging, and comparing evaluation results. Below is an overview of each file in this repository.

## File Descriptions

### 1. Datasets

The `datasets` folder contains all datasets required for this project. Ensure you place the necessary data files here before running any models.

On biobert that would be `biobert/datasets` and for kebiolm `kebiolm/ner`.

Ensure you run `biobert/named-entity-recognition/preprocess.sh` before you start training your model.

### 2. BioBERT

To use BioBERT for NER tasks, first install the required version of `transformers`:

```bash
pip install transformers==3.0.0
```

Then, run the following command to train and evaluate the model using the NCBI-disease dataset. You can follow the same steps for any other dataset:

```bash
python run_ner.py --data_dir ../datasets/NCBI-disease --labels ../datasets/NCBI-disease/labels.txt --model_name_or_path dmis-lab/biobert-base-cased-v1.1 --output_dir output/NCBI-disease --max_seq_length 128 --num_train_epochs 5 --per_device_train_batch_size 32 --save_steps 1000 --seed 1 --do_train --do_eval --do_predict --overwrite_output_dir
```

### 3. KeBioLM

For KeBioLM, first download the pre-trained model from [this link](https://drive.google.com/file/d/1kMbTsc9rPpBc-6ezEHjMbQLljW3SUWG9/edit) and place it in the `kebiolm/ner/model` directory.

To use KebioLM first install the required version of `transformers` and `PyTorch`, and ensure you have Python 3.7 installed:

```bash
pip install transformers==3.4.0
pip install pytorch==1.7.0
```

Use the following command to train and evaluate KeBioLM on the NCBI-disease dataset. You can follow the same steps for any other dataset:

```bash
python run_ner.py --data_dir ./NCBI-disease --model_name_or_path ./model --output_dir ./output/NCBI-disease --num_train_epochs 5 --seed 1 --do_train --do_eval --do_predict --overwrite_output_dir --gradient_accumulation_steps 2 --learning_rate 3e-5 --warmup_steps 1710 --save_steps 1000 --max_seq_length 512 --per_device_train_batch_size 8 --eval_accumulation_steps 1 --load_best_model_at_end --metric_for_best_model f1
```

### 4. Python scripts in crossCheck folder

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

Ensure that all dependencies, such as `pandas`, `ast`, `tabulate` and `stanza` are installed before running these scripts.
