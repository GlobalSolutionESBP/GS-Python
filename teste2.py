def verifica_num(msg, msg_erro,):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)

    while len(num)!= 11:
        print(msg_erro)
        num = input(msg)


    return int(num)


usuarios = ['Ana', 'Josué', 'Joaquim']
cpf_usuarios = [12345678909, 11987654321, 10101010101]

CPF = verifica_num("Digite seu CPF sem acentuação: ", "Você precisa digitar seu CPF completo")

while CPF not in cpf_usuarios:
    CPF = verifica_num("Digite seu CPF sem acentuação: ", "Você precisa digitar seu CPF completo")

if CPF == cpf_usuarios:
    print(f"Relatório do paciente ")