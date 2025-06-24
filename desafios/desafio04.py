def ordenar_pacientes(pacientes):
    lista = []
    for i, p in enumerate(pacientes):
        nome, idade, status = map(str.strip, p.split(','))
        idade = int(idade)
        prioridade = 0 if status.lower() == "urgente" else 1
        lista.append((prioridade, -idade, i, nome))
    lista.sort()
    return [nome for _, _, _, nome in lista]

n = int(input("Quantos pacientes serão cadastrados? "))
entradas = []
for i in range(n):
    entrada = input(f"Paciente {i+1} - Digite nome, idade e status separados por vírgula: ")
    entradas.append(entrada)

ordem = ordenar_pacientes(entradas)
print("\nOrdem de Atendimento:", ", ".join(ordem))

