def hanoi(n, a, b, c):
    if n <= 0:
        pass
    else:
        for h in hanoi(n-1, a, c, b):
            yield h
        yield (a, c)
        for h in hanoi(n-1, c, b, a):
            yield h

def tower(n, a, b, c):
    if n <= 0:
        return
    tower(n-1, a, c, b)
    print(a, b)
    tower(n-1, c, b, a)

hanoi(3, 1, 3, 2)
tower(3, 1, 3, 2)

print()
n = int(input("Kuinka monta kiekkoa laitetaan? "))


def hanoi2(n, start, end, middle):
    if n==1:
        print("Move %i from tower %s to tower %s" %(n, start, end))
    else:
        hanoi2(n-1, start, middle, end)
        print("Move %i from tower %s to tower %s" %(n, start, end))
        hanoi2(n-1, middle, end, start)
print()
hanoi2(n, "A", "B", "C")

        
