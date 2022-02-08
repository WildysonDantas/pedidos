import unittest
import compra

class PedidoTeste(unittest.TestCase):
    #Responsavel por verificar se o pedido tem o frete gratis
    def test_frete_gratis_sim(self):
        pedido = compra
        self.assertTrue(pedido.frete_gratis(100))

     #Responsavel por verificar se o pedido tem o frete gratis
    def test_frete_gratis_nao(self):
        pedido = compra
        self.assertFalse(pedido.frete_gratis(69))

    #Responsavel por verificar o desconto
    def test_aplicar_desconto(self):
        pedido = compra
        self.assertEqual(pedido.aplicar_desconto(50,10), 40)

    #Responsavel por verificar a taxa de entrega 5km
    def test_taxa_de_entrega_5km(self):
        pedido = compra
        self.assertEqual(pedido.taxa_de_entrega(5), 0)
    
    #Responsavel por verificar a taxa de entrega 10 km
    def test_taxa_de_entrega_10km(self):
        pedido = compra
        self.assertEqual(pedido.taxa_de_entrega(10), 5)

    #Responsavel por verificar a taxa de entrega 15 km
    def test_taxa_de_entrega_15km(self):
        pedido = compra
        self.assertEqual(pedido.taxa_de_entrega(15), 10)
    
    #Responsavel por verificar a taxa de entrega 20 km
    def test_taxa_de_entrega_20km(self):
        pedido = compra
        self.assertEqual(pedido.taxa_de_entrega(20), 15)

    #Responsavel por verificar o tipo de pagamento REAL
    def test_tipo_pagamento_real(self):
        pedido = compra
        self.assertEqual(pedido.tipo_pagamento(1), 'REAL')
    
    #Responsavel por verificar o tipo de pagamento PIX
    def test_tipo_pagamento_pix(self):
        pedido = compra
        self.assertEqual(pedido.tipo_pagamento(2), 'PIX')
    
    #Responsavel por verificar o tipo de pagamento CARTAO
    def test_tipo_pagamento_cartao(self):
        pedido = compra
        self.assertEqual(pedido.tipo_pagamento(3), 'CARTÃO')

     #Responsavel por verificar o tipo de pagamento CARTEIRA DITAL
    def test_tipo_pagamento_carteira_digital(self):
        pedido = compra
        self.assertEqual(pedido.tipo_pagamento(4), 'CARTEIRA DIGITAL')

    #Responsavel por verificar a quantidade de produtos
    def test_qtd_produtos(self):
        pedido = compra
        produtos=[]
        produtos.append(['café 200 GM', 1, 1.84])
        produtos.append(['leite 100 GM', 2, 2.84])
        produtos.append(['arroz 1KG', 3, 4])
        self.assertEqual(pedido.qtd_produtos(produtos), 6)
    
    #Responsavel por verificar o subtotal de produtos
    def test_subtotal(self):
        pedido = compra
        produtos=[]
        produtos.append(['café 200 GM', 1, 3])
        produtos.append(['leite 100 GM', 2, 3])
        produtos.append(['arroz 1KG', 3, 4])
        self.assertEqual(pedido.subtotal(produtos), 21)
    
    #Responsavel por verificar o total de produto unitario
    def test_total_produto(self):
        pedido = compra
        produto=['café 200 GM', 5, 3.80]
        self.assertEqual(pedido.total_produto(produto), 19)

    #Responsavel por verificar o total do pedido com desconto e 8 km
    def test_total_pedido_com_desconto(self):
        pedido = compra
        produtos=[]
        produtos.append(['café 200 GM', 1, 3])
        produtos.append(['leite 100 GM', 2, 3])
        produtos.append(['arroz 1KG', 3, 4])
        self.assertEqual(pedido.total_pedido(produtos, 3, 8), 23)
    
    #Responsavel por verificar o total do pedido sem desconto e 8 km
    def test_total_pedido_sem_desconto(self):
        pedido = compra
        produtos=[]
        produtos.append(['café 200 GM', 1, 3])
        produtos.append(['leite 100 GM', 2, 3])
        produtos.append(['arroz 1KG', 3, 4])
        self.assertEqual(pedido.total_pedido(produtos, 0, 8), 26)
    
    #Responsavel por verificar o total do pedido sem desconto e 3 km
    def test_total_pedido_sem_desconto_3km(self):
        pedido = compra
        produtos=[]
        produtos.append(['café 200 GM', 1, 3])
        produtos.append(['leite 100 GM', 2, 3])
        produtos.append(['arroz 1KG', 3, 4])
        self.assertEqual(pedido.total_pedido(produtos, 0, 3), 21)
   


if __name__ == "__main__":
    unittest.main(verbosity=2) 