# Desenvolver um aplicativo que leia um CPF e após a sua validação exiba na tela:
#   CPF válido! ou
#   CPF inválido!

cpf = int(input("Digite o CPF sem pontos e hífens: "))

if cpf > 99999999999 or cpf < 10000000000:
    print("CPF inválido!")
else:
    print("CPF válido!")


