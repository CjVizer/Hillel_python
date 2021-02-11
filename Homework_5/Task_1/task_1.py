from string import punctuation

"""
Из текстового файла удалить все слова, содержащие от трех до пяти символов,
но при этом из каждой строки должно быть удалено только четное количество таких слов.
"""

with open('poem.txt', 'r', encoding='utf-8') as file_original:  # Opening the original file
    with open('poem_converted.txt', 'w', encoding='utf-8') as file_converted:  # Create a converted file
        for line in file_original:
            words = []  # List of words by specified criteria (3 <= word length < 5)
            line = line.strip('\n')  # Trim the \n at the end of the line

            for word in line.split():  # Separate words by spaces and iterate over them in a loop
                word = word.strip(punctuation)  # Trimming punctuation marks from each word
                if 3 <= len(word) < 5:  # Checking if the word matches our condition
                    words.append(word)  # And we add this word to the list

            if len(words) % 2:  # If the number of words in the list is odd
                words.pop()  # Remove the last word from the list

            for word in words:
                # Remove unnecessary words and spaces, then combine everything into one line
                line = ' '.join(line.replace(word, '', 1).split())

            file_converted.write(line + '\n')  # Let's write the result to a new file
