"""Para que o programa funcionone corretamente é necessário digitar a frase
sem espaços e sem acentuações"""

from stack import Stack

def main():
    mainStack = Stack()
    copyStack = Stack()
    analyzeStack = Stack()

    phrase = input("Digite uma frase: ")

    for i in range(len(phrase)):
        mainStack.push(phrase[i])
        copyStack.push(phrase[i])

    for i in range(len(copyStack.getStack())):
        analyzeStack.push(copyStack.pop())

    if mainStack.getStack() == analyzeStack.getStack():
        print("A frase é um palíndromo")
        print(f"Frase digitada: {mainStack.getStack()}")
        print(f"Frase invertida: {analyzeStack.getStack()}")
    else:
        print("A frase não é um palindromo")
        print(f"Frase digitada: {mainStack.getStack()}")
        print(f"Frase invertida: {analyzeStack.getStack()}")

main()