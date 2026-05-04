# Desenvolver um aplicativo que leia um CPF e após a sua validação exiba na tela:
#   CPF válido! ou
#   CPF inválido!


from validate_docbr import CPF

cpf = input("Digite o CPF (com ou sem pontos): ")

validador = CPF()

if validador.validate(cpf):
    print("CPF válido")
else:
    print("CPF inválido")