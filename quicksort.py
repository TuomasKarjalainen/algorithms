import random
from timeit import default_timer as timer

print()
alkio = []
pieni = []
sama = []
isompi = []

alkioala=int(input("Aseta alkioden ala-raja: "))
alkioyla=int(input("Aseta alkioden ylä-raja: "))
alkiot=int(input("Aseta alkioiden määrä: "))
print()
print("Min:", alkioala)
print("Max:", alkioyla)
print("Määrä:", alkiot)
for a in range(alkiot):
  alkio.append(random.randint(alkioala, alkioyla))
print("Alkuperäinen lista:", alkio)

def quicksort(alkio):

  if len(alkio) > 1:
   # Sarana-alkioksi on valittu listan ensimmäinen luku
    pivot = alkio[0]
    for x in alkio:
        # Lisään listaan sarana-alkiota pienemmät luvut
      if x < pivot:
        pieni.append(x)
        # Lisään listaan yhtäsuuret luvut
      elif x == pivot:
        sama.append(x)
        # Lisään listaan sarana-alkiota suuremmat luvut
      elif x > pivot:
        isompi.append(x)
        # Järjestetään listat ja yhdistetään ne
    return quicksort(pieni) + sama + quicksort(isompi)
  
  # Ellei lista ole ykköstä isompi palautetaan se 
  else:
    return alkio

quicksort(alkio)
print("Quicksorted: ", pieni + sama + isompi)