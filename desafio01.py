descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = int(input("Preço: "))
cupom = str(input("Cupom: ")).strip().upper()
total = 0

if cupom == "DESCONTO10":
  total = preco-(preco * descontos["DESCONTO10"])
  
elif cupom == "DESCONTO20":
  total = preco-(preco * descontos["DESCONTO20"])
else:
  total= preco

print(total)

  