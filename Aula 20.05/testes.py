def tabuada():
    x = int (input("Digite um número: "))
    for y in range(1, 11):
      print(f"{x}x{y} = {x * y}")
tabuada()