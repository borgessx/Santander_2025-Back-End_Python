#Dicionários aninhados

contatos = {
    "prod": {"nome": "guilherme", "telefone": "9865-9999"},
    "couro": {"nome": "joão", "telefone": "689048-5454"},
    "pao": {"nome": "gabriel", "telefone": "8504-8459"}
}
#para acessar
print(contatos["couro"]["nome"])

#usando for
for chave in contatos:
    print(chave, contatos[chave])
print("-------------------")
for chave, valor in contatos.items():
    print(chave,valor)