a = 0
for i in range(1,11):
    a = a + i
    print("{},".format(a), end=" ")

print("")

b = 1
for i in range(0,10):
    print(b**3, end=" ")
    b = b + 1

print("")

end = 3
for i in range (1,3):
    for j in range (1,end):
        print(j*"#")
    end = end + 1

print("")

str_names = input ("Podaj imiona oddzielone przecinkiem\n")
names = str_names.replace(" ","").split(",")
#print(names)

for name in names:
    print("Siema {}" .format(name.title()), end=" ")
    print("")
