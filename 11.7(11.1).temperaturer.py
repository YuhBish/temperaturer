name = input("Vad heter filen? ")
f = open(name, 'r')
for rad in f:
    print(rad, end="")
f.close()