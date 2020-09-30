'''
Faça um
programa que para uma determinada quantidade de tempo a cada fatia de tempo sejam
produzidos aleatoriamente de 1 a 20 eventos descritos na tabela acima.

Conforme são
gerados os eventos estes devem ser mostrados na tela e inseridos na estrutura que vai
solucionar este problema (dica: resolva este problema com uma combinação de filas e filas
com prioridades).

Concluída esta etapa cada evento será extraído da estrutura para ser
executado (isto vai ser simulado, não precisa ser implementado). Conforme vai sendo
extraído exibe-se uma mensagem na tela que o determinado evento está sendo executado.
A cada fatia de tempo todos os eventos são tratados deixando a estrutura vazia.
'''
from random import randint, randrange
from time import sleep
from queue import Queues

processamentoGrafico = ["Colisão", "Atualização de tela", "Partículas"]
logica = ["Lógica do jogo", "Inteligência Artificial", "Simulação Física"]
entradaDeDados = ["Teclado", "Mouse", "Internet"]

listOfEvents = [processamentoGrafico, logica, entradaDeDados]
queueOfEvents = Queues()
queueOfGrafics = Queues()
queueOfLogics = Queues()
queueOfDatas = Queues()

def organizeEvents(event):
    if event in processamentoGrafico:
        queueOfGrafics.enterData(event)
        #print(f"Processamento gráfico: {queueOfGrafics}")
    elif event in logica:
        queueOfLogics.enterData(event)
        #print(f"Lógica: {queueOfLogics}")
    else:
        queueOfDatas.enterData(event)
        #print(f"Entrada de dados: {queueOfDatas}")

def organizeQueueOfGrafics(queue):
    highPriority = Queues()
    mediumPriority = Queues()
    lowPriority = Queues()

    organizedQueue = Queues()

    for event in queue:
        if event == "Colisão":
            highPriority.enterData(event)
            
        elif event == "Atualização de tela":
            mediumPriority.enterData(event)
            
        else:
            lowPriority.enterData(event)
            
    
    for event in range(highPriority.lenQueue()):
        organizedQueue.enterData(highPriority.remove())

    for event in range(mediumPriority.lenQueue()):
        organizedQueue.enterData(mediumPriority.remove())

    for event in range(lowPriority.lenQueue()):
        organizedQueue.enterData(lowPriority.remove())

    return organizedQueue.getQueue()

def organizeQueueOfLogics(queue):
    highPriority = Queues()
    mediumPriority = Queues()
    lowPriority = Queues()

    organizedQueue = Queues()

    for event in queue:
        if event == "Lógica do jogo":
            highPriority.enterData(event)
            
        elif event == "Inteligência Artificial":
            mediumPriority.enterData(event)
            
        else:
            lowPriority.enterData(event)
            
    
    for event in range(highPriority.lenQueue()):
        organizedQueue.enterData(highPriority.remove())

    for event in range(mediumPriority.lenQueue()):
        organizedQueue.enterData(mediumPriority.remove())

    for event in range(lowPriority.lenQueue()):
        organizedQueue.enterData(lowPriority.remove())

    return organizedQueue.getQueue()

def organizeQueueOfDatas(queue):
    highPriority = Queues()
    mediumPriority = Queues()
    lowPriority = Queues()

    organizedQueue = Queues()

    for event in queue:
        if event == "Teclado":
            highPriority.enterData(event)
            
        elif event == "Mouse":
            mediumPriority.enterData(event)
            
        else:
            lowPriority.enterData(event)
            
    
    for event in range(highPriority.lenQueue()):
        organizedQueue.enterData(highPriority.remove())

    for event in range(mediumPriority.lenQueue()):
        organizedQueue.enterData(mediumPriority.remove())

    for event in range(lowPriority.lenQueue()):
        organizedQueue.enterData(lowPriority.remove())

    return organizedQueue.getQueue()

timeOfRunning = int(input("Informe a quantidade de tempo (s): "))

for i in range(timeOfRunning):
    for j in range(randint(0, 20)):
        event = listOfEvents[randrange(3)][randrange(3)]
        organizeEvents(event)
        print(event)
    sleep(1)

finalQueueOfGrafics = organizeQueueOfGrafics(queueOfGrafics.getQueue())
finalQueueOfLogics = organizeQueueOfLogics(queueOfLogics.getQueue())
finalQueueOfDatas = organizeQueueOfDatas(queueOfDatas.getQueue())

for i in range(len(finalQueueOfGrafics)):
    event = finalQueueOfGrafics.pop(0)
    queueOfEvents.enterData(event)

for i in range(len(finalQueueOfLogics)):
    event = finalQueueOfLogics.pop(0)
    queueOfEvents.enterData(event)

for i in range(len(finalQueueOfDatas)):
    event = finalQueueOfDatas.pop(0)
    queueOfEvents.enterData(event)

print("---" * 10)

for i in range(queueOfEvents.lenQueue()):
    event = queueOfEvents.remove()
    print(f"{event} está em execução")
    print("---" * 10)
    sleep(0.5)

print("FIM DA EXECUÇÃO")