#Notas utilizando if, elif, else
nota = float (input("Qual nota você tirou? "))
if nota < 7:
    print("C")
elif nota < 9:
    print("B")
elif nota < 11:
    print("A")
else:
    print("Nota inválida")