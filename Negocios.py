from Dados import *

def cadastrar_produto(nome, preco, quantidade):

    if preco < 0:
        return False, "Erro: preço inválido."


    produto_existente = buscar_produto(nome)

    if produto_existente:
        produto_existente['qtd'] +=quantidade
        return True, "Estoque atualizado com sucesso!"

    novo_produto = {
        "nome": nome,
        "preo": preco,
        "qtd": quantidade
        }

    salvar_produto(novo_produto)
    return True, "Produto cadastrado com sucesso!"

def realizar_venda(nome, qtd_desejada):
    produto = buscar_produto(nome)

    if not produto:
        return False, "Erro: produto não encontrado."

    produto['qtd'] = produto['qtd'] - qtd_desejada

    valor_total = produto['preco'] * qtd_desejada

    return True, f"Venda realizada! Total: R$ {valor_total: .2f}"