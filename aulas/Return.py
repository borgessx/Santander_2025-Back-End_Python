"""
🤔 Por que usar o return?
Quando você cria uma função, ela é como uma máquina que faz algo.

Mas se você quiser pegar o resultado do que essa função fez e usar em outro lugar, você precisa do return.

Sem o return, a função faz o trabalho e joga o resultado fora. Com o return, ela entrega o resultado de volta pra quem chamou.
"""

#📦 Imagina isso:

def caixa():
    return "Um presente"

#Se você chamar só caixa(), você recebe "Um presente".

#Agora, se não tivesse return, seria como uma caixa vazia, que não entrega nada.

##Vamos ver o que acontece sem e com return:

#Sem return:

def diga_ola():
    print("Olá!")

resultado = diga_ola()
print(resultado)
"""
Saída:

None
🧠 Aqui, o Python imprime "Olá!" dentro da função, mas como não tem return, a variável resultado recebe None, que significa "nada".
"""

#Com return:

def diga_ola():
    return "Olá!"

resultado = diga_ola()
print(resultado)
"""
Saída:

Olá!
🎯 Agora sim, a função retornou "Olá!", e esse valor foi guardado em resultado.
"""

"""
📌 Quando usar return:
Você usa return quando quer que sua função:

Calcule algo e te devolva o resultado.

Seja usada em outras partes do código.

Evite repetir código, facilitando manutenção.
"""

#✅ Exemplo prático:

def calcular_desconto(preco, porcentagem):
    desconto = preco * (porcentagem / 100)
    return preco - desconto

valor_final = calcular_desconto(100, 20)
print(f"O valor com desconto é: R${valor_final}")
#🧠 Aqui a função calcula o desconto e retorna o valor final com desconto. Sem return, a gente não conseguiria usar esse resultado depois.

