import random
from timeit import default_timer as timer 

print()
alkio = []
alkioala=int(input("Aseta alkioden ala-raja: "))
alkioyla=int(input("Aseta alkioden ylä-raja: "))
alkiot=int(input("Anna alkioiden määrä: "))
print()
print("Valitsit alarajaksi:", alkioala)
print("Valitsit ylä-rajaksi:", alkioyla)
print("Alkioiden määrä:", alkiot)

for a in range(alkiot):
    alkio.append(random.randint(alkioala, alkioyla))
print("Alkuperäinen lista:", alkio)

def bubbleSort(alkio):
    for passnum in range(len(alkio)-1,0,-1):
        for i in range(passnum):
            if alkio[i]>alkio[i+1]:
                temp = alkio[i]
                alkio[i] = alkio[i+1]
                alkio[i+1] = temp

start = timer()
bubbleSort(alkio)
end = timer()
print()
print("Bubblesorted:", alkio)
print()
print("Listan järjestämiseen kului aikaa", end - start, "sekuntia.")
print()