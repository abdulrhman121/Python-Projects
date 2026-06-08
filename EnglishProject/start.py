import re


def normalize(text):
    text = re.sub(r"[أإآ]", "ا", text)
    text = re.sub(r"[ى]", "ي", text)
    text = re.sub(r"[ة]", "ه", text)
    return text


def start():
    print(
        """==================================
Welcome to Learn English with PYTHON
==================================
>>> Write 'n' for unknowing the answer, 'q' for quit the program, 'r' for rest words file<<<\n"""
    )


def read(words_count):
    with open(
        r"C:\Users\abdul\Desktop\Projects\Python\EnglishProject\Words.txt",
        encoding="utf-8",
    ) as f:
        lines = []
        for i, line in enumerate(f):
            if i == words_count:
                break
            lines.append(line.strip())
        return lines


def correct_file(word):
    with open(
        r"C:\Users\abdul\Desktop\Projects\Python\EnglishProject\CorrectWords.txt",
        "a",
        encoding="utf-8",
    ) as cf:
        cf.write(word + "\n")


def remove_word(word):
    with open(
        r"C:\Users\abdul\Desktop\Projects\Python\EnglishProject\Words.txt",
        encoding="utf-8",
    ) as f:
        lines = f.readlines()
    with open(
        r"C:\Users\abdul\Desktop\Projects\Python\EnglishProject\Words.txt",
        "w",
        encoding="utf-8",
    ) as f:
        for line in lines:
            if not line.startswith(word.split()[0]):
                f.write(line)


def rest_word():
    with open(
        r"C:\Users\abdul\Desktop\Projects\Python\EnglishProject\Words2.txt",
        encoding="utf-8",
    ) as f:
        lines = f.readlines()
    with open(
        r"C:\Users\abdul\Desktop\Projects\Python\EnglishProject\Words.txt",
        "w",
        encoding="utf-8",
    ) as f:
        for line in lines:
            f.write(line)
    with open(
        r"C:\Users\abdul\Desktop\Projects\Python\EnglishProject\CorrectWords.txt",
        "w",
        encoding="utf-8",
    ) as f:
        pass
    print("Done Rest!")
