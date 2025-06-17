"""
Um bloco de código identificado por um nome e pode receberuma lista de parâmetros.
Conhecido como: "Identificador"

def = função

def nome_da_função():
    print("Olá Mundo")      <código da função

def nome_da_função_2(argumento):
    print(f"Seja bem vindo {argumento}!")

def nome_da_função_3(argumento="Gabriel"):
    print(f"Seja bem vindo {argumento}!")

# como executar a função
nome_da_função()
nome_da_função_2()
nome_da_função_3()

°Quando digita algum argumento e não declara um valor, vai dar errado.
    Exemplo na nome_da_função_2     < não declaro nenhum argumento, então vai declara quando chamar a funçã.
    Veja:

nome_da_função_2(argumento="João")

°Também pode alterar o argumento:

nome_da_função_3(argumento="Lucas")


"""

def nome_da_função():
    print("Olá Mundo")

def nome_da_função_2(argumento):
    print(f"Seja bem vindo {argumento}!")

def nome_da_função_3(argumento="Gabriel"):
    print(f"Seja bem vindo {argumento}!")

nome_da_função_2(argumento="Gabriel")

# argumentos nomeados

def salva_carro(marca,modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# declarar argumentos
salva_carro("Hyundai","Ix35",2016,"ABC-1234")

# para não desorganizar, caso ocorrar uma mudança de ordem na função. ->Afirmar argumentos.
salva_carro(marca="Fiat",ano=1998,modelo="Uno",placa="ACF-8968")

# em forma de dicionário
salva_carro(**{"marca":"Honda","modelo":"civic","ano":2017,"placa":"SUF-0983"})


"""
>>> Args e Kwargs >>>
Quando esses são definidos (*args(tupla) e **kwargs(dicionário)), o método recebe os valores como tupla e dicionário respectivamente.
* = tupla & ** = dicionário
"""


# retorno >>>>>>>>>>>>>>>>>>>>>>>
def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)

#argumentos >>>>>>>>>>>>>>>>
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

# parametros por posição >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

# objetos de priemira classe >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20

#
