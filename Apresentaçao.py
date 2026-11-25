from Dados import listar_todos
from Negocios import cadastrar_produto, realizar_venda


def menu():
    while True:
        print("\n--- MERCADINHO DEV ---")
        print("1. Cadastrar produto (entrada)")
        print("2. Vender produto (Saída)")
        print("3. Ver estoque")
        print("4. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço unitário: "))
            qtd = int(input("Quantidade: "))

            sucesso, mensagem = cadastrar_produto(nome, preco, qtd)
            print(mensagem)

        elif opcao == "2":
            nome = input("Nome do produto para vender: ")
            qtd = int(input("Quantidade desejada: "))

            sucesso, mensagem = realizar_venda(nome, qtd)
            print(mensagem)

        elif opcao == "3":
            lista = listar_todos()
            print("\n--- RELATÓRIO DE ESTOQUE ---")
            for item in lista:
                print(f"produto: {item['nome']} | R$ {item['preco']:.2f} | qtd {item['qtd']}")

        elif opcao == "4":
            print("A fechar o sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()