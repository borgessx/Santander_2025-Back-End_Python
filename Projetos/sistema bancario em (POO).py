import textwrap


class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


class Conta:
    def __init__(self, agencia, numero_conta, usuario, saldo=0, limite=500):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = saldo
        self.limite = limite
        self.extrato = ""
        self.numero_saques = 0


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(conta, valor):
    if valor > 0:
        conta.saldo += valor
        conta.extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")


def sacar(conta, valor, limite_saques=3):
    excedeu_saldo = valor > conta.saldo
    excedeu_limite = valor > conta.limite
    excedeu_saques = conta.numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        conta.saldo -= valor
        conta.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        conta.numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")


def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta.extrato else conta.extrato)
    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return None

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)

    print("=== Usuário criado com sucesso! ===")
    return novo_usuario


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return Conta(agencia, numero_conta, usuario)

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    return None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
Agência:\t{conta.agencia}
C/C:\t\t{conta.numero_conta}
Titular:\t{conta.usuario.nome}
"""
        print("=" * 100)
        print(textwrap.dedent(linha))


def selecionar_conta(contas):
    if not contas:
        print("\n@@@ Não há contas cadastradas. @@@")
        return None

    numero = int(input("Informe o número da conta: "))
    for conta in contas:
        if conta.numero_conta == numero:
            return conta

    print("\n@@@ Conta não encontrada. @@@")
    return None


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            conta = selecionar_conta(contas)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                depositar(conta, valor)

        elif opcao == "s":
            conta = selecionar_conta(contas)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                sacar(conta, valor, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            conta = selecionar_conta(contas)
            if conta:
                exibir_extrato(conta)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Encerrando o programa...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
