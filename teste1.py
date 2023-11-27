def verifica_num(msg, msg_erro,):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)

    while len(num)!= 11:
        print(msg_erro)
        num = input(msg)


    return int(num)

def encontrar_registro_por_cpf(dados, cpf_usuario):
    for paciente in dados:
        if paciente.get("cpf") == cpf_usuario:
            print("Registro Encontrado:")
            print(f"Nome: {paciente['nome']}")
            print(f"Idade: {paciente['idade']}")
            print(f"Condição de Saúde: {paciente['condicao']}")
            print(f"Data da Última Consulta: {paciente['data_consulta']}")
            return
    print("Registro não encontrado para o CPF informado.")

nome = input("Digite seu nome completo: ")
CPF  = verifica_num("Digite seu CPF: ", "Você precisa digirar os 11 números do seu CPF!")

#simulação
dados_saúde = [
    {'nome': "Paciente A", "idade": 24, 'condição': 'Colesterol alto', 'data_consulta': "20/10/2023", 'cpf':{'123.456.789.01'}}, 
    {'nome': "Paciente A", "idade": 36, 'condição': 'Diabetes', 'data_consulta': "12/10/2023", 'cpf':{'109.876.543.21'}}
]

def encontrar_registro_por_cpf(dados, cpf_usuario):
    for paciente in dados:
        if paciente.get("cpf") == cpf_usuario:
            print("Registro Encontrado:")
            print(f"Nome: {paciente['nome']}")
            print(f"Idade: {paciente['idade']}")
            print(f"Condição de Saúde: {paciente['condicao']}")
            print(f"Data da Última Consulta: {paciente['data_consulta']}")
            return
    print("Registro não encontrado para o CPF informado.")