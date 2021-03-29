name = input("Vad heter filen? ")
openfile = open(name, 'r')
for rad in openfile:
    print(rad, end="")
openfile.close()












