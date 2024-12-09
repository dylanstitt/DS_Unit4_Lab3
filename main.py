# Dylan Stitt
# Unit 4 Lab 3
# [NAME]

from Stack import ArrayStack

def getContent(filename):
    with open(filename, 'r') as file:
        return file.read().split(' ')

def main():
    stack = ArrayStack()
    content = getContent('test.txt')

    for word in content:
        stack.push(word)

    for i in range(len(stack)):
        print(stack.pop(), end=' ')


if __name__ == '__main__':
    main()
