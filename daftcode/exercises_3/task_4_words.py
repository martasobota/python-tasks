def get_words(in_file_name, out_file_name):
    words = set()
    with open(file_name, 'r') as f:
        for line in f:
            words_in_lines = get_words_from_line(line)
            words |= line_words

with open('words_result.txt', 'w') as f:
    words = get_words('html.lst')
    f.writelines(w+'\n' for w in words)