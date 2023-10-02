'''
O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

# Declara dicionário com código contendo dicionário com nome, preço e quantidade dos produtos
produtos = {
    100: {"nome": "Cachorro Quente", "preco": 1.20, "quantidade": 0},
    101: {"nome": "Bauru Simples", "preco": 1.30, "quantidade": 0},
    102: {"nome": "Bauru com ovo", "preco": 1.50, "quantidade": 0},
    103: {"nome": "Hamburguer", "preco": 1.20, "quantidade": 0},
    104: {"nome": "Cheeseburguer", "preco": 1.30, "quantidade": 0},
    105: {"nome": "Refrigerante", "preco": 1.00, "quantidade": 0}
}

# Mostra o cardápio
print(
    "Produto         Codigo  Preço"
    "\n-------------------------------"
    "\nCachorro Quente 100     R$ 1.20"
    "\nBauru Simples   101     R$ 1.30"
    "\nBauru com ovo   102     R$ 1.50"
    "\nHamburguer      103     R$ 1.20"
    "\nCheeseburguer   104     R$ 1.30"
    "\nRefrigerante    105     R$ 1.00\n"
)

# Coleta código do produto, confere se é valido ou finalizando
while True:
    codigo = int(input("Insira o código do produto (Ou 0 para finalizar): "))
    if codigo == 0:
        break
    if codigo not in produtos:
        print("Código inválido")
        continue
    
    # Coleta quantia do produto e insere no dicionário
    qtd = int(input("Insira a quantidade do produto: "))
    produtos[codigo]["quantidade"] += qtd

# Mostra o resultado
print(
    "\nFechamento do pedido"
    "\nCodigo  -  Quantidade  -  Preço unidade  -  Preço total"
)

# Declara variável para armazenar o total
total = 0

# Verifica se produto foi comprado, atualiza preço total e mostra o resultado
for codigo, produto in produtos.items():
    if produto["quantidade"] > 0:
        preco_total = produto["preco"] * produto["quantidade"]
        print(
            f"{codigo}\t-\t{produto['quantidade']}\t-  R$ {produto['preco']:.2f}\t-"
            f"\tR$ {preco_total:.2f}"
        )
        total += preco_total

# Mostra o resultado total
print(f"Total do pedido: R$ {total:.2f}")