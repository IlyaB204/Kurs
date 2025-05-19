with open('resourse_1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()
words_count = {}


for word in words:
    words_count[word] = words_count.get(word, 0) + 1

print(words_count)

sorted_words = sorted(words_count.items(), key=lambda item: (-item[1], item[0]))

with open('result_1.txt', 'w', encoding='utf-8') as result_file:
    for word, count in sorted_words:
        line = f"{word} {count}\n"
        result_file.write(line)
        print(f'Добавлена строка: {word} {count}')