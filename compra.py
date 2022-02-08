#Frete Gratis
def frete_gratis(valor):
    if valor < 70:
        return False
    return True

#Aplicar Desconto
def aplicar_desconto(valor, desconto):
    return valor - desconto

#Taxa de Entrega
def taxa_de_entrega(distancia):

    if distancia <= 5:
        return 0
    elif distancia > 5 and distancia <= 10:
        return 5
    elif distancia > 10 and distancia <= 15:
        return 10
    
    return 15

#Tipo de Pagamento
def tipo_pagamento(pgto):

    if pgto == 1:
        return 'REAL'
    elif pgto == 2:
        return 'PIX'
    elif pgto == 3:
        return 'CARTÃO'
    
    return "CARTEIRA DIGITAL"

#quantidade de produtos
def qtd_produtos(produtos):
    qtd = 0
    for p in produtos:
        qtd += p[1]
        
    return qtd

#subtotal de produtos
def subtotal(produtos):
    total = 0
    for p in produtos:
        total += p[1] * p[2]
        
    return total

#total do produto
def total_produto(produto):
    
    return produto[1] * produto[2]
        

#total do pedido
def total_pedido(produtos, desconto, distancia):
    total = subtotal(produtos) 
    total = aplicar_desconto(total, desconto)
    if(frete_gratis(total) == False):
        taxa = taxa_de_entrega(distancia)
        total += taxa
    return total
