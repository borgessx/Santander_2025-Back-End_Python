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
