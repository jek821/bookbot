def open_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    text = file_contents.lower()
    text = ''.join(filter(str.isalpha, text))  # Only keep alphabetic characters
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def print_char_report(char_count):
    for char, count in char_count.items():
        print(f"The \'{char}\' was found {count} times.")

def main():
    file_contents = open_file("books/frankenstein.txt")
    print(get_word_count(file_contents))
    print(count_characters(file_contents))
    print_char_report(count_characters(file_contents))


main()