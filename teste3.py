prontuarios = {}

def cadastrar_paciente():
    nome = input("Digite o nome do paciente: ")
    CPF = input("Digite seu CPF: ")
    while not CPF.isnumeric() and len(CPF)!= 11:
        print("Digite seu CPF corretamente!")
        CPF = input("Digite seu CPF: ")
    CPF = int(CPF)
    idade = input("Digite a idade do paciente: ")
    while not idade.isnumeric():
        print('Digite um número!')
        idade = input("Digite a idade do paciente: ")
    idade = int(idade)
    altura = input("Digite a altura (cm): ")
    while not altura.isnumeric():
        print('Digite um número!')
        altura = input("Digite a altura (cm): ")
    altura = int(altura)
    peso = input("digite o peso (kg): ")
    while not peso.isnumeric():
        print('Digite um número!')
        Peso = input("digite o peso (kg): ")
    peso = int(peso)
    sintomas = input("Digite os sintomas do paciente: ")


    # Cria um prontuário para o paciente
    prontuario = {"Nome": nome, "CPF": CPF, "Idade": idade, "Sintomas": sintomas, "altura": altura, "peso": peso}

    # Adiciona o prontuário ao dicionário
    prontuarios[nome] = prontuario

    print("Paciente cadastrado com sucesso!")
    return prontuarios

'''def calcular_imc(prontuarios):
   imc = prontuarios["peso"] / (prontuarios["altura"] ** 2)
    return imc
'''

'''def avaliar_imc(imc):
    if imc < 18:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade grau I"
    elif imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"
'''
def buscar_paciente():
    nome = input("Digite o nome do paciente a ser buscado: ")

    # Verifica se o paciente está no dicionário
    if nome in prontuarios:
        prontuario = prontuarios[nome]
        '''imc = calcular_imc(prontuarios[nome])'''
        '''status_imc = avaliar_imc(prontuarios[nome])'''
        print("Prontuário encontrado:")
        print("Nome:", prontuario["Nome"])
        print("Idade:", prontuario["Idade"])
        print("Altura:", prontuario["altura"], "cm")
        print("Peso:", prontuario["peso"],"kg")
        print("Sintomas:", prontuario["Sintomas"])
        '''print("imc:", imc, "Status IMC", status_imc)'''

    else:
        print("Paciente não encontrado.")


# Menu principal
while True:
    print("\n=== Prontuário Eletrônico ===")
    print("Teste Cadastrar um paciente antes de buscá-lo!")
    print("1. Cadastrar Paciente")
    print("2. Buscar Paciente")
    print("3. Sair")

    opcao = input("Escolha uma opção (1/2/3): ")

    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        buscar_paciente()
    elif opcao == "3":
        print("Saindo do Prontuário Eletrônico. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")