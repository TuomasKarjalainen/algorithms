def fibonacci():
    
    print()
    alkio = int(input("Syötä alkioiden määrä: "))

    # Kaksi ensimmäistä alkiota
    a1, a2 = 0, 1
    count = 0

    # Alkion tarkistus
    if alkio <= 0:
        print("Syötä ainostaan positiivisiä lukuja.")
    elif alkio == 1:
        print("Tylsää, syötit vain yhden alkion.")
        print(a1)
    else:
        print()
        print("Tulostetaan fibonacci lukujono: ")
        while count < alkio:
            print(a1)
            nth = a1 + a2
            a1 = a2
            a2 = nth
            count += 1

    vastaus = input("Haluatko kokeilla vielä uudestaan? k/e ")

    if vastaus == 'k':
        fibonacci()

    elif vastaus == 'e':
        print()
        print("Asia kunnossa, näkemiin!")
        print()
        

fibonacci()       
            