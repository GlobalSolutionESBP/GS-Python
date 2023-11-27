def cadastrar_paciente(pacientes):
    nome = input("Digite o nome do paciente: ")
    CPF = input("Digite o CPF: ")
    while not CPF.isnumeric():
        print("Você deve digitar um número!")
        CPF = input("Digite o CPF: ")
    CPF = int(CPF)

    genero = input("Digite o genero: ")

    idade = input('Digite a idade: ')
    while not idade.isnumeric():
        print("Você deve digitar um número!")
        idade = int(input('Digite a idade: '))
    idade = int(idade)

    altura = input("Digite a altura do paciente(cm): ")
    while not altura.isnumeric():
        print("Você deve digitar um número!")
        altura = input("Digite a altura do paciente(cm): ")
    altura = int(altura)

    peso = (input("Digite o peso do paciente (kg): "))
    while not peso.isnumeric():
        print("VocÊ deve digitar um número!")
        peso = (input("Digite o peso do paciente (kg): "))
    peso = float(peso)

    condicao = input("Digite a condição do paciente: ")

    paciente = (f'nome: {nome}, CPF: {CPF}, idade: {idade}, gênero: {genero}, altura: {altura}, peso: {peso}, '
                f'condição: {condicao}.')


    print(paciente)
    print('Paciente cadastrado com sucesso!\n')
    return paciente

'''paciente01 = cadastro()'''
def calcular_imc(paciente):
    imc = paciente["peso"] / (paciente["altura"] ** 2)
    return imc

def avaliar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def visualizar_prontuario(pacientes):
    for i, paciente in enumerate(pacientes, 1):
        imc = calcular_imc(paciente)
        status_imc = avaliar_imc(imc)
        print(f"\nProntuário do Paciente {i}:")
        print(f"Nome: {paciente['nome']}")
        print(f"Idade: {paciente['idade']}")
        print(f"IMC: {imc:.2f} - {status_imc}\n")


def simular_visualizacao_prontuario():
    pacientes_simulacao = [
        {"nome": "Maria", "idade": 22, "altura": 1.60, "peso": 60}
    ]
    print("Simulação - Visualizar prontuário:\n")
    visualizar_prontuario(pacientes_simulacao)


def main():
    while True:
        print("1. Cadastrar paciente")
        print("2. Visualizar prontuário")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente(pacientes)
        elif opcao == "2":
            if not pacientes:
                print("Nenhum paciente cadastrado ainda. Cadastre um paciente primeiro.")
            else:
                simular_visualizacao_prontuario()
        elif opcao == "3":
            print("Saindo do prontuário eletrônico.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

pacientes = ['Maria']
teste = print(main())
