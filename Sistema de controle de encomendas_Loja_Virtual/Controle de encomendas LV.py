# Lista de produtos no estoque, cada produto tem: (nome, categoria, preço, quantidade)
armazem = [
    ("Notebook", "Eletrônicos", 3500.00, 10, 0),
    ("Camiseta", "Vestuário", 50.00, 100, 0),
    ("Smartphone", "Eletrônicos", 2000.00, 15, 0),
    ("Calça Jeans", "Vestuário", 120.00, 50, 0)
]

# Carrinho de compras (lista de itens no carrinho)
carrinho = []

# Função para exibir o estoque de produtos
def exibir_estoque():
    print("\nEstoque atual:")
    for i, produtos in enumerate(armazem):
        print(f"{i + 1}. {produtos[0]} (Categoria: {produtos[1]}) -- Preço: R${produtos[2]:.2f} -- Quantidade: {produtos[3]} -- Reservado: {produtos[4]}")

# Função para adicionar item ao carrinho
def adicionar_ao_carrinho(sumario_produtos, quantidades):
    nome, categoria, preco, quantidade_estoque, reservado = armazem[sumario_produtos]

    quantidade_estoque_disponivel = quantidade_estoque - reservado

    if quantidades <= quantidade_estoque_disponivel:
        carrinho.append((nome, quantidades, preco * quantidades))

        for i, produtos in enumerate(armazem):
            nome_item_estoque, categoria, preco, quantidade_estoque, reservado = produtos
            if nome_item_estoque == nome:
                armazem[i] = (nome, categoria, preco, quantidade_estoque, reservado + quantidades)

        print(f"{quantidades}x {nome} adicionado(s) ao carrinho.")
    else:
        print(f"Estoque insuficiente! Apenas {quantidade_estoque_disponivel} produtos disponíveis.")

# Função para exibir o carrinho
def exibir_carrinho():
    if not carrinho:
        print("Carrinho está vazio.")
    else:
        print("\nCarrinho de compras:")
        total = 0
        for i, itens in enumerate(carrinho):
            nome, quantidade, preco_total = itens
            print(f"{i + 1}. {nome} - Quantidade: {quantidade} - Preço Total: R${preco_total:.2f}")
            total += preco_total
        print(f"Total do carrinho: R${total:.2f}")

# Função para finalizar a compra e atualizar o estoque
def finalizar_compra():
    if not carrinho:
        print("Seu carrinho está vazio. Adicione algum produto.")
        return

    preco_total_carrinho = 0.00

    for item in carrinho:
        nome_item, quantidade_comprada, preco_total_item = item

        preco_total_carrinho = preco_total_carrinho + preco_total_item

        for i, produtos in enumerate(armazem):
            nome, categoria, preco, quantidade_estoque, _ = produtos
            if nome == nome_item:
                armazem[i] = (nome, categoria, preco, quantidade_estoque - quantidade_comprada, 0)

    desconto = calcula_desconto(preco_total_carrinho)

    if desconto > 0:
        print(f"Você teve um desconto de R${desconto:.2f}")

    print(f"O valor total da sua compra foi de R${preco_total_carrinho - desconto:.2f}")
    
    print("Compra finalizada com sucesso! Estoque atualizado.")
    carrinho.clear()
# Fim função finalizar a compra

def calcula_desconto(preco_total_carrinho):
    if preco_total_carrinho > 15000:
        return preco_total_carrinho * 0.15
    elif preco_total_carrinho > 10000:
        return preco_total_carrinho * 0.10
    elif preco_total_carrinho > 5000:
        return preco_total_carrinho * 0.05
    else:
        return 0

def exibir_tipos_de_descontos():
    print("Acima de R$5.000,00 - 5% de desconto no valor do carrinho")
    print("Acima de R$10.000,00 - 10% de desconto no valor do carrinho")
    print("Acima de R$15.000,00 - 15% de desconto no valor do carrinho")

# Função para simular uma encomenda
def fazer_encomenda():
    exibir_estoque()
    num_produto = int(input("Escolha o número do produto que deseja comprar: ")) - 1
    quantidade = int(input("Digite a quantidade que deseja comprar: "))

   
    adicionar_ao_carrinho(num_produto, quantidade)

# Função principal para rodar o sistema
def sistema():
    while True:
        print("\nMenu:")
        print("1. Exibir estoque")
        print("2. Fazer encomenda")
        print("3. Exibir carrinho")
        print("4. Finalizar compra")
        print("5. Sistema de descontos")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_estoque()
        elif opcao == '2':
            fazer_encomenda()
        elif opcao == '3':
            exibir_carrinho()
        elif opcao == '4':
            finalizar_compra()
        elif opcao == '5':
            exibir_tipos_de_descontos()
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Inicia o sistema
sistema()