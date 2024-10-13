import csv
import glob

def read_ner_data(file_path):
    """
    Reads a NER tagged text file and returns a list of sentences,
    where each sentence is represented as a list of (word, tag) tuples.
    """
    sentences = []  # Will store the list of sentences
    current_sentence = []  # Temporarily stores the current sentence being processed

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Remove leading and trailing whitespace
            if line:  # If the line is not empty, it contains a word and a tag
                word, tag = line.split()
                current_sentence.append((word, tag))
            else:  # If the line is empty, we've reached the end of a sentence
                if current_sentence:  # If the current sentence contains words, add it to the sentences list
                    sentences.append(current_sentence)
                    current_sentence = []  # Reset the current sentence to start accumulating the next one

        # Add the last sentence if the file doesn't end with a newline
        if current_sentence:
            sentences.append(current_sentence)

    return sentences

def save_sentences_to_csv(sentences, csv_file_path):
    """
    Saves sentences and their tags to a CSV file.
    Each row will contain a full sentence and the corresponding tags as a tuple.

    Parameters:
    - sentences: A list of sentences, where each sentence is a list of (word, tag) tuples.
    - csv_file_path: The path to the CSV file where the data will be saved.
    """
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Sentence", "Tags"])  # Writing the header with new column names

        for sentence in sentences:
            sentence_text = " ".join(word for word, _ in sentence)  # Constructing the sentence text
            tags = tuple((word, tag) for word, tag in sentence)  # Constructing the tuple of (word, tag)
            writer.writerow([sentence_text, str(tags)])  # Converting tuple to string for CSV compatibility

# New part for iterating over .txt files
directory_path = './'  # Directory containing the txt files
txt_files = glob.glob(f'{directory_path}*.txt')  # Finds all txt files in the directory

for file_path in txt_files:
    sentences = read_ner_data(file_path)  # Read the NER data from each file
    csv_file_path = file_path.replace('.txt', '.csv')  # Replace .txt extension with .csv for the output file
    save_sentences_to_csv(sentences, "../csv/"+csv_file_path)  # Save to CSV for each file
    print(f"Data has been saved to {csv_file_path}")

