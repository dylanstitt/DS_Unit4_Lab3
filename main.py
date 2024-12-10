# Dylan Stitt
# Unit 4 Lab 3
# Reverse a File

from Stack import ArrayStack
from string import ascii_lowercase, ascii_uppercase

def clean(content):
    content = content.split(' ')
    newContent = ""
    for word in content:
        newWord = ""
        for char in word:
            if char in ascii_lowercase+ascii_uppercase+' '+'\n':
                newWord += char
        newContent += newWord + ' '
    return newContent

def getContent(filename):
    with open(filename, 'r') as file:
        return clean(file.read())

def main():
    stack = ArrayStack()
    content = getContent('earnest.txt').split(' ')

    for i in content:
        stack.push(i)

    new = ''
    for i in range(len(stack)):
        new += stack.pop() + ' '

    with open('output.txt', 'w') as file:
        file.write(new)

if __name__ == '__main__':
    main()