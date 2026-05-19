'''Alguns testes de Funções, Whiles e For'''

def my_function(frutas):
    for fruta in frutas:
        print(fruta)

frutas = ["Maçã", "Banana", "Uva", "Laranja"]
print(type(frutas))
my_function(frutas)



def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_function(1, 1, 2, 3, 5, 8, 13, 21))
print(my_function(17**3))
print(my_function(5 * 5))



def my_function(**myvar):
    print("Type:", type(myvar))

    print ("Name:", myvar["name"])
    print ("Age:", myvar["age"])
    print("City:", myvar["city"])



i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i é maior que 6")



fruits = ["Apple", "Banana", "Cherry"]
for x in fruits: 
    # print(x)
    if x == "Cherry":
        print(f"O valor de X é: {x}")
        break



for x in range(2, 24, 2):
    print(x)



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)



cars = ["Ford", "Volvo", "BMW"]
print(cars)
cars.append(input("Qual carro você deseja adcionar? "))
print(f"O carro que você adicionou foi: {cars}")


