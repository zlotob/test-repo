import random as rand

gracz_wynik = 0
cpu_wynik = 0
cont = 't'

gracz = ''
cpu = ''
cpu_str = ''

while cont is not 'n':
    gracz = str(input("(k)amień, (p)apier czy (n)ożyce?\n"))
    cpu = rand.randint(1,3)

    if cpu is 1:
        cpu = 'k'
        cpu_str = 'kamień'
    elif cpu is 2:
        cpu = 'p'
        cpu_str = 'papier'
    elif cpu is 3:
        cpu = 'n'
        cpu_str = 'nożyce'

    

    print("Komputer wybrał {} - ".format(cpu_str), end="")

    if gracz is 'k' or gracz is 'K':
        if cpu is 'k':
            print("remis")
        elif cpu is 'n':
            print("wygrałeś!")
            gracz_wynik +=1
        elif cpu is 'p':
            print("przegrałeś.")
            cpu_wynik +=1
        
    elif gracz is 'p' or gracz is 'P':
        if cpu is 'p':
            print("remis")
        elif cpu is 'k':
            print("wygrałeś!")
            gracz_wynik +=1
        elif cpu is 'n':
            print("przegrałeś.")
            cpu_wynik +=1
    
    elif gracz is 'n' or gracz is 'N':
        if cpu is 'n':
            print("remis")
        elif cpu is 'p':
            print("wygrałeś!")
            gracz_wynik +=1
        elif cpu is 'k':
            print("przegrałeś.")
            cpu_wynik +=1

    else:
        print("ale Ty nie wybrałeś nic! Spróbuj ponownie.")

    print("\nWynik: {}-{} dla gracza.\n".format(gracz_wynik, cpu_wynik))

    cont = str(input("Jeszcze raz? (t/n)"))
