#http://learnpythonthehardway.org/book/ex36.html

def start():
    print ("Ez egy vacak es unalmas jatek, de legalabb az eletre nevel.")
    print ("Szoval: ahelyett, hogy ezzel jatszol, ertelmesebb dolgokat is tehetsz, peldaul:")
    print ("(K)eresel egy masik jatekot vagy (M)esz a dolgodra. Melyiket valasztod?")

    choice = input("> ")

    if choice == "K":
            print ("Jo dontes! Sok sikert a kereseshez, bar nem lesz nehez ennel szinvonalasabbat talalni!")
    elif choice == "M":
            print ("Jo dontes, ugyis munkabol fogsz megelni, nem jatekbol...")
    else:
        print("Ezt nem ertem. K vagy M betut kellett volna beirnod - hat mi a nehez ebben...?")


start()