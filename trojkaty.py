a=int(input("a = ile cm?"))
b=int(input("b = ile cm?"))
c=int(input("c = ile cm?"))

if (a+b<=c or a+c<=b or b+c<=a):
    print("Nie da sie z takiego gówna zrobić trójkąta.")
else:
    print("Złóżmy z tego trójkąt...")

    if (a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a):
        print("Trojkat jest pitagorejski.")
    else:
        print("Trójkąt nie jest pitagorejski")

    if a < b:
        temp = a
        a = b
        b = temp
    if a < c:
        temp = a
        a = c
        c = temp
    if b < c:
        temp = b
        b = c
        c =temp

#    print("{},{},{}" .format(a,b,c))

        if (c/b == 3/4 and b/a == 4/5):
            print("Trójkąt egipski!")
        else:
            print("Trójkąt nie egipski :<")
    
