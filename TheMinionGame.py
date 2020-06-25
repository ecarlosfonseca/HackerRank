def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart = 0
    kevin = 0
    words = []

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            word = string[i:j]
            word_count = string[i+1:].count(word)
            if word not in words:
                if word[0] in vowels:
                    kevin += word_count + 1
                else:
                    stuart += word_count + 1
            words.append(word)
            print(word, kevin, stuart)
    if kevin > stuart:
        print('Kevin' + ' ', kevin)
    elif stuart > kevin:
        print('Stuart' + ' ', stuart)


if __name__ == '__main__':
    s = 'BANANANAAAS'
    minion_game(s)