from stack import Stack
from queue import Queues

def optionA():
    mainStack = Stack()
    invertedStack = Stack()

    print("Insira cinco valores")
    for i in range(5):
        value = input(f"Insira o valor {i+1}: ")
        mainStack.push(value)

    print(f"Valores digitados: {mainStack.getStack()}")

    for i in range(5):
        invertedStack.push(mainStack.pop())

    print(f"Valores invertidos usando uma pilha adicional: {invertedStack.getStack()}")
    print("FIM DO PROGRAMA")

def opctionB():
    mainStack = Stack()
    mainQueue = Queues()

    print("Insira cinco valores")

    for i in range(5):
        value = input(f"Insira o valor {i + 1}: ")
        mainStack.push(value)

    print(f"Pilha ordenada: {mainStack.getStack()}")

    for i in range(len(mainStack.getStack())):
        mainQueue.enterData(mainStack.pop())

    for i in range(len(mainQueue.getQueue())):
        mainStack.push(mainQueue.remove())

    print(f"Valores invertidos usando uma fila adicional: {mainStack.getStack()}")
    print("FIM DO PROGRAMA")

def main():
    option = input("Escolha a opção para inverter a pilha\n"
                   "Digite 'A' para inverter com pilhas adcionais\n"
                   "Digite 'B' para inverter com filas adcionais\n"
                   "Insira o comando aqui: ")

    if option == 'A' or option == 'a':
        optionA()
    elif option == 'B' or option == 'b':
        opctionB()
    else:
        print("Escolha um comando válido")
        main()

main()