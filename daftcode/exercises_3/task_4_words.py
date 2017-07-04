def get_words_from_line(line):
    data = set()
    first = line.split('/')[-1]
    second = first.split('.')[0]
    word_start = 0
    word_end = 0
    checker = True

    for seq in range(len(second)):
        if second[seq].isalpha():
            if checker:
                checker = False
                word_start = seq
                # print('Word start: {}'.format(word_start))
        else:
            if not checker:
                checker = True
                word_end = seq
                # print('Word end: {}'.format(word_end))
                if word_start != word_end:
                    data.add(second[word_start:word_end])
    if not checker:
        data.add(second[word_start:])
    return data

def get_words(in_file_name):
    words = set()
    save_words = set()
    print('Creating list of words...')
    with open(in_file_name, 'r') as f:
        for line in f:
            save_words = get_words_from_line(line)
            words |= save_words
    words = list(words)
    print('Sorting words...')
    words.sort()
    print('Words sorted!')
    return words

with open('words_result.txt', 'w') as f:
    words = get_words('html.lst')
    f.writelines(w+'\n' for w in words)
    print("Your file is ready!")