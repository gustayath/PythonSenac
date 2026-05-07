#Utilização de funções
def myfunc1():
    x = "Honda"
    def myfunc2():
        x = "Yamaha"
        print(x)
    myfunc2()
    print(x)
myfunc1()

