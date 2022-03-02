import random
from timeit import default_timer as timer

# Alkuun pientä käyttöliittymän tynkää, jotta ohjelmaa voi testata eriluvuilla ja määrällä

print()
alkio = []
alkiomin=int(input("Aseta alkioden ala-raja: "))
alkiomax=int(input("Aseta alkioden ylä-raja: "))
alkiot=int(input("Aseta alkioiden määrä: "))
print()
print("Min:", alkiomin)
print("Max:", alkiomax)
print("Määrä:", alkiot)
for a in range(alkiot):
  alkio.append(random.randint(alkiomin, alkiomax))
print("Alkuperäinen lista:", alkio)

def partition(alkio, alku, loppu):
    pivot = alku
    for i in range(alku+1, loppu+1):
        if alkio[i] <= alkio[alku]:
            pivot +=1
            alkio[i], alkio[pivot] = alkio[pivot], alkio[i]
    alkio[pivot], alkio[alku] = alkio[alku], alkio[pivot]
    return pivot

def quicksort(alkio, alku = 0, loppu = None):
    if loppu is None:
        loppu = len(alkio) -1
    def _quicksort(alkio, alku, loppu):
        if alku >= loppu:
            return
        pivot = partition(alkio, alku, loppu)
        _quicksort(alkio, alku, pivot-1)
        _quicksort(alkio, pivot+1, loppu)
    return _quicksort(alkio, alku, loppu)

# Ajan aloitus ennen funktion kutsua ja lopetus funktion jälkeen
start = timer()
quicksort(alkio)
stop = timer()
print("Quicksorted:", alkio)
print()
print("Listan järjestämiseen kului aikaa", stop - start, "sekuntia.")
print()
print("Quicksort on nopeampi kuin bubblesort")