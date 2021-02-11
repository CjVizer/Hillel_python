from string import punctuation

"""
Из текстового файла удалить все слова, содержащие от трех до пяти символов,
но при этом из каждой строки должно быть удалено только четное количество таких слов."""

with open('poem.txt', 'r', encoding='utf-8') as file_original:
    for _ in range(10):
        words = []
        file_line = file_original.readline().strip('\n')
        print(file_line)
        for word in file_line.split():
            word = word.strip(punctuation)
            if 3 <= len(word) < 5:
                words.append(word)
        # print(words)

        if len(words) % 2:
            words.pop()

        for word in words:
            # print(word)
            file_line = ' '.join(file_line.replace(word, '').split())

        print(file_line)
