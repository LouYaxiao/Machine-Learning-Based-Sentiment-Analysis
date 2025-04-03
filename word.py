# Path to the input file
input_file_path = r"C:\Users\Lou13\Desktop\cleaned_corpus2.txt"

# Path to the output file
output_file_path = r"C:\Users\Lou13\Desktop\cleaned_corpus_word_list2.txt"

# Read the content of the file and split it word by word
with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Split the text into words
words = text.split()

# Write each word to a new line in the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for word in words:
        output_file.write(word + '\n')

print("File processed and saved as cleaned_corpus_word_list2.txt.")
