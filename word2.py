# Path to the file containing words to filter
deactivated_words_path = r"C:\Users\Lou13\Desktop\deactivated_words.txt"

# Path to the input word list file
input_word_list_path = r"C:\Users\Lou13\Desktop\cleaned_corpus_word_list2.txt"

# Path to save the filtered word list
output_filtered_word_list_path = r"C:\Users\Lou13\Desktop\filtered_corpus_word_list2.txt"

# Load deactivated words
with open(deactivated_words_path, 'r', encoding='utf-8') as deactivated_file:
    deactivated_words = set(line.strip().lower() for line in deactivated_file.readlines())

# Read the input word list
with open(input_word_list_path, 'r', encoding='utf-8') as input_file:
    words = [line.strip() for line in input_file.readlines()]

# Filter out the words that are in the deactivated word list
filtered_words = [word for word in words if word.lower() not in deactivated_words]

# Write the filtered words to the output file
with open(output_filtered_word_list_path, 'w', encoding='utf-8') as output_file:
    for word in filtered_words:
        output_file.write(word + '\n')

print("Filtered word list saved to filtered_corpus_word_list.txt.")
