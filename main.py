# Dylan Stitt
# Unit 4 Lab 3
# Reverse a File

from Stack import ArrayStack
from string import ascii_lowercase, ascii_uppercase

def clean(content):
    newContent = []
    for line in content:
        newLine = []
        for word in line.split(' '):
            newWord = ""
            for char in word:
                if char in ascii_lowercase+ascii_uppercase:
                    newWord += char
            newLine.append(newWord)
        newContent.append(' '.join(newLine))
    return newContent

def getContent(filename):
    with open(filename, 'r') as file:
        return clean(file.read().splitlines())


def main():
    stack = ArrayStack()
    content = getContent('earnest.txt')

    for line in content:
        if len(line) > 1:
            stack.push(line)

    new = ""
    for i in range(len(stack)):
        new += stack.pop() + ' '
    with open('output.txt', 'w') as file:
        file.write(new)


if __name__ == '__main__':
    main()