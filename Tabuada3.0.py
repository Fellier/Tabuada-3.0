while True:
    num2 = 0
    num = int(input("Digite o numero que você deseja saber a tabuada: "))
    if num < 0:
        print("Programa finalizado")
        break
    while num2 < 10:
        num2 += 1
        print('{} x {} = {}'.format(num, num2, num*num2))
