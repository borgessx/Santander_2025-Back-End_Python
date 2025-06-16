email = str(input())

if " " in email:
    print("E-mail inválido")
elif email[0] == "@" or email[-1] == "@":
    print("E-mail inválido")
elif "@" in email and ("gmail.com" in email or "outlook.com" in email):
    print("E-mail válido")
else:
    print("E-mail inválido")




