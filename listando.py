from time import sleep #TEMPO



#            --------------------------FUNÇÕES DE TEMPO-------------------------
def tempo_de_apresentação():
       sleep(1.0)
        
#  ------------------------------------------FUNÇÕES DE SEPARAÇÃO---------------------------
def linha():
    print('_____'*10)
    
def traço():
    print('---'*20)


#------------------------------------------LISTA PARA RECEBER OS ITENS PEDIDOS------------

pedido = []

#Tuplas #variaveis composta
lanche = ('\t\thamburguer','\t\tpastel','\t\tpizza','\t\tbatata') #TUPLAS SÃO COM ()
bebidas = ('Suco','Coca','Água','Cerveja') #TUPLA PARA BEBIDA
sobremesa = ('pudim','Bolo','pão de mel')#TUPLAS DE SOBREMESA


#--------------------------------------------------------- APRESENTAÇÃO --------------


print('\t\tBEM - VINDO AO GOOD BURGUER')
tempo_de_apresentação()
print('\t\tA CASA DO HAMBURGUER')
tempo_de_apresentação()
print('\t\tPOSSO ANOTAR O SEU PEDIDO?')



#--------------------------------#MONTANDO O PEDIDO-----------------------------------
tempo_de_apresentação()


#------------------------------------FUNÇÕES DE CONFERENCIA--------------


def conferir():
    if pergunta == 'Não':
        certo_um = input('Qual o pedido correto?')
        certo_um.append(lanche[lanche_um])
#PEDIR A QUANTIDADE DE LANCHES
def pessoas():
     quantidade_de_lanches = int(input('São para quntas pessoas?'))
        
        

#------------------------------------MOSTRANDO CARDAPIO DE LANCHES------------------------------
for num, c in enumerate(lanche):
    print(f'{num} - {c}')
    
 #------- ESCOLHENDO A COMIDA  -----------
try:
        linha()
        lanche_um=int(input('\t\tQual lanche vc quer: \n'))
        pedido.append(lanche[lanche_um])
        linha()

except (NameError,ValueError):
    print('OCORREU UM ERRO NO DADO COLOCADO \n POR FAVOR EFETUE A AÇÃO NOVAMENTE')
except KeyboardInterrupt:
    print('NENHUM DADO FOI ENCONTRADO')


#------- PREÇOS DE CADA LANCHE -----------
if lanche_um == 0:
        print(f'\t\t{lanche_um} -- R$15,00 ')
        if  lanche_um == 1:
            print(f'\t\t{lanche_um} -- R$19,00')
            if lanche_um == 2:
                print(f'\t\t{lanche_um} -- R$14,50')
else:
        print(f'\t\t{lanche_um}-- R$ 13,00')

#----------------------------------------------MOSTRANDO CARDAPIO DE BEBIDAS------------------



#----- MOSTRANDO A LISTA DE BEBIDAS ----------
linha()
for num,b  in enumerate(bebidas):
    print(f'{num} - {b}')  
#------- ESCOLHENDO A BEBIDAS -----------
try:
    linha()
    bebida_um=int(input('Qual bebida?'))
    pedido.append(bebidas[bebida_um])
    linha()

except (NameError,ValueError):
    print('OCORREU UM ERRO NO DADO COLOCADO \n POR FAVOR EFETUE A AÇÃO NOVAMENTE')
    
#------- PREÇOS DE CADA BEBIDAS-----------
if lanche_um == 0:
    print(f'{bebida_um} -- R$15,00 ')
    if  lanche_um == 1:
        print(f'{bebida_um} -- R$19,00')
        if lanche_um == 2:
            print(f'{bebida_um} -- R$14,50')
else:
    print(f'{bebida_um}-- R$ 13,00')
# -----------MOSTRANDO SOBREMESA--------------

linha()
for num,m in enumerate(sobremesa):
    print(f'{num}-{m}')
    
    
#------- ESCOLHENDO A BEBIDAS -----------
try:
    sobre = int(input('Qual sobremesa?'))
    pedido.append(sobremesa[sobre])
    linha()

except NameError:
    print('O DADO NÃO FOI ENCONTRADO')
except ValueError:
    print('COLOQUE SÓ NÚMEROS ')
    
#------- PREÇOS DE CADA BEBIDAS-----------
if lanche_um == 0:
    print(f'{sobre} -- R$15,00 ')
    if  lanche_um == 1:
        print(f'{sobre} -- R$19,00')
        if lanche_um == 2:
            print(f'{sobre} -- R$14,50')
else:
    print(f'{lanche_um}-- R$ 13,00')
    
    

#------------------------CONFERIR SE ESTA CERTO ---------------------




pergunta = input('O pedido confere?')
if pergunta == 'Sim':
    print('Beleza')
else:
    conferir()

#----------------------------------#CONDIÇÃO DE PEDIDO--------------------------------------

#---------------  COLOCAÇÃO DE DADOS ----------
cliente = []  #lista dos dados da clientes
nome_cliente = input('----------- > NOME COMPLETO : \n')
cliente.append(nome_cliente)
numero_celular = int(input('----------- >TEL: \n'))
cliente.append(numero_celular)


# ----- ENDEREÇO ----


cep_cliente = input('----------- >CEP: \n')
cliente.append(cep_cliente)
bairro_cliente = input('----------- >BAIRRO: \n')
cliente.append(bairro_cliente)
numero_cliente = int(input('----------- >NÚMERO: \n'))
cliente.append(numero_cliente)


#-------- COLOCANDO OS DADOS NA LISTA-----



#----- MOSTRANDO DADOS-----
for dados in cliente:
    print(f'{dados}')
#------- CONFERENCIA DE DADOS DO CLIENTE --------
conf_dados = input('\t\t OS DADOS BATEM?')
while conf_dados == 'Sim':
    
#-----MOSTRANDO FORMA DE PAGAMENTO ----
    pagamento_escolha = input('QUAL A FORMA DE PAGAMENTO?')
else:
    print('Encerramento inconclusivo')
#--------------- FINALIZANDO O PEDIDO-----------
#----------------------------------#NOTA DA LISTA DO PEDIDO-------------------------------------




print('\t--------------NOTA DE PEDIDO ---------')
traço()
for num,p in enumerate(pedido):
    print(f'\t{num}-{p}')
