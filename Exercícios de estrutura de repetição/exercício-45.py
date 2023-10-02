'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de 
cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
'''

# Declara variáveis para armazenar os valores necessários
aluno_com_maior_acerto = ""
aluno_com_menor_acerto = ""
maior_acerto = 0
media_da_turma = 0
numero_de_alunos = 0
gabarito = {}
alunos = {}

# Coleta o número de questões
numero_de_questoes = int(input("Digite o número de questões: "))
menor_acerto = numero_de_questoes

# Coleta as respostas corretas e insere no gabarito
for i in range(1, numero_de_questoes + 1):
    resposta_atual = input(f"Digite a resposta correta da questão '{i}': ").upper()
    gabarito[f"questao_{i}"] = resposta_atual

# Coleta as respostas dos alunos e calcula os acertos
while True:
    aluno = input("Digite o nome do aluno (ou 0 para sair): ")
    if aluno == "0":
        break
    numero_de_alunos += 1
    alunos[aluno] = {"acertos": 0}
    for i in range(1, numero_de_questoes + 1):
        resposta_atual = input(
            f"Digite a resposta que o aluno {aluno} deu para a questão {i}: "
        ).upper()
        alunos[aluno][f"questao_{i}"] = resposta_atual

# Calcula os acertos de cada aluno e a nota
for aluno, respostas in alunos.items():
    for questao, resposta in respostas.items():
        if questao == "acertos":
            continue
        if resposta == gabarito[questao]:
            alunos[aluno]["acertos"] += 1
    acertos = alunos[aluno]["acertos"]
    nota = 10 * acertos / numero_de_questoes
    print(
        f"O aluno {aluno} obteve {acertos} acertos dentre {numero_de_questoes}"
        f" questões e ficou com a nota {nota:.2f}"
    )

    # Atualiza o aluno com o maior acerto
    if acertos > maior_acerto:
        maior_acerto = acertos
        aluno_com_maior_acerto = aluno

    # Atualiza o aluno com o menor acerto
    if acertos < menor_acerto:
        menor_acerto = acertos
        aluno_com_menor_acerto = aluno

    media_da_turma += nota

# Calcula a média da turma
media_da_turma /= numero_de_alunos

# Imprime os resultados
print(
    f"O aluno com mais acertos é {aluno_com_maior_acerto}, "
    f"com {maior_acerto} acertos"
)
print(
    f"O aluno com menos acertos é {aluno_com_menor_acerto}, "
    f"com {menor_acerto} acertos"
)
print(f"A média da turma é {media_da_turma:.2f}")