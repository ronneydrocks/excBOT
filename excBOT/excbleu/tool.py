import config
import excBot
import time
import hmac
import requests
import hashlib
import func
import func_AMI


################################################
#           EXC CRIPTO - CONFIG                #
################################################
emailEXC = config.emailEXC
keyEXC = config.keyEXC
secretEXC = config.secretEXC
key_secretEXC = excBot.excBot(keyEXC, secretEXC, nonce=True)
##############################################################################
print('=' * 65)
print('''
    ######## ##     ##  ######  ########   #######  ######## 
    ##        ##   ##  ##    ## ##     ## ##     ##    ##    
    ##         ## ##   ##       ##     ## ##     ##    ##    
    ######      ###    ##       ########  ##     ##    ##    
    ##         ## ##   ##       ##     ## ##     ##    ##    
    ##        ##   ##  ##    ## ##     ## ##     ##    ##    
    ######## ##     ##  ######  ########   #######     ##  
                                           Versão - 0.1.6    
''')
print('=' * 65)

acao = 'None'
while acao:



    print('''Escolha uma opção:   
     
    >> EXCHANGE: EXC CRIPTO
    
    [0] SALDO
    [1] TRANSFERÊNCIA (EXC/BLEU)
    [2] CANCELAR ORDENS (TODAS) 
    [3] MOSTRAR ORDENS (TODAS)
    [4] AMI (1x) 
    [5] AMI 2 (Nx) 
    [6] ORDEM VENDA (1x)
    [7] ORDEM COMPRA (1x)
    
    [EXIT] Sair ''')

    print('=' * 50)

    acao = str(input('\nDigite o número do que deseja fazer: ')).upper()

    if acao == 'EXIT':
        print('>> SAIR')
        break

    ativo = str(input('Qual ativo: ')).upper()
    mercado = str(input('Qual mercado: ')).upper()
    ativo_mercado = ativo + '_' + mercado

######################################################################

    if acao == '0':
        func.saldo_EXC()
        time.sleep(2)
        func.saldo_BLEU()

    elif acao == '1':
        print('=' * 50)
        print('>> TRANSFERÊNCIA')

        # Consulta informações Balances
        rBalances = key_secretEXC.get_balances()
        # print(rBalances)

        # Quantidade de Ativos na EXC
        nATIVOS = len(rBalances['result'])
        # print(nATIVOS)

        c = 0
        somaEqBTC_EXC = 0
        while c < nATIVOS:
            ATIVO = rBalances['result'][c]['Asset']
            balancType = rBalances['result'][c]['Balance']
            Type = rBalances['result'][c]['BtcEquivalent']
            Price = rBalances['result'][c]['Available']
            print(f'Saldo: {Price:.8f} / {balancType:.8f} {ATIVO} = {Type:.8f} BTC')

            # SOMA SALDO EQUIVALENTE EM BTC
            somaEqBTC_EXC += Type
            c += 1

        print(f'Saldo atual na EXC: {somaEqBTC_EXC:.8f} BTC')
        quantidade_transferir = input('\nQuantidade transferir: ')
        email_destino = input('Email destino na BLEU: ')

        ################################################
        # TRANSFERENCIA
        ################################################

        print(f'Transferindo... {quantidade_transferir} {ativo}')
        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
            int(
                time.time())) + '&asset=' + ativo + '&quantity=' + quantidade_transferir + '&exchangeto=1&' + 'accountto=' + email_destino

        # sign
        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferEXC, headers=headers)
        # print(urlDirecttransferEXC)
        print(response.json())

        print('=' * 50)

######################################################################

    elif acao == '2':
        print('=' * 50)
        print('>> CANCELAR ORDENS')

        ordemAberta = key_secretEXC.get_open_orders()
        resposta_ordemAberta = ordemAberta['result']

        resposta_ordemAberta = str(resposta_ordemAberta)
        if resposta_ordemAberta == 'None':
            print('>> SEM ORDENS ABERTAS')
            # break

        else:
            # Quantidade de ordens abertas
            nOrdemAberta = len(ordemAberta['result'])
            # print(f'Total de ordens abertas: {nOrdemAberta}')

            ordensAM = ordemAberta['result']
            print(f'>> {ativo_mercado}\n')

            c = 0
            while c < nOrdemAberta:
                ATIVO = ordemAberta['result'][c]['Exchange']
                Type = ordemAberta['result'][c]['Type']
                Price = ordemAberta['result'][c]['Price']
                Status = ordemAberta['result'][c]['Status']
                OrderID = ordemAberta['result'][c]['OrderID']

                if ATIVO == ativo_mercado:
                    print(f'Ordem: {Status} Tipo: {Type} Valor: {Price:.8f}\n')

                    # cancela ordem
                    cancelaOrder = key_secretEXC.cancel(OrderID)
                    print(f'Resultado:\n{cancelaOrder}')

                    # Pausa em segundos
                    time.sleep(0.2)

                c += 1

            print('=' * 50)

######################################################################
    
    elif acao == '3':
        print('=' * 50)
        print('\n>> MOSTRAR ORDENS\n')

        ordemAberta = key_secretEXC.get_open_orders()
        resposta_ordemAberta = ordemAberta['result']

        resposta_ordemAberta = str(resposta_ordemAberta)
        if resposta_ordemAberta == 'None':
            print('>> SEM ORDENS ABERTAS')
            # break
        else:
            # Quantidade de ordens abertas
            nOrdemAberta = len(ordemAberta['result'])
            # print(f'Total de ordens abertas: {nOrdemAberta}')

            # executar acao
            ativo_mercado = ativo + '_' + mercado
            ordensAM = ordemAberta['result']
            print(f'>> {ativo_mercado}\n')

            c = 0
            while c < nOrdemAberta:
                OrderID = ordemAberta['result'][c]['OrderID']
                ATIVO = ordemAberta['result'][c]['Exchange']
                Type = ordemAberta['result'][c]['Type']
                Quantity = ordemAberta['result'][c]['Quantity']
                Price = ordemAberta['result'][c]['Price']
                Status = ordemAberta['result'][c]['Status']
                Created = ordemAberta['result'][c]['Created']

                if ATIVO == ativo_mercado:
                    # print(f'Ordem: {Status} Tipo: {Type} Valor: {Price:.8f} Quantidade: {Quantity}\n')
                    if Status == 'OPEN':
                        if Type == 'BUY':
                            print('=' * 50)
                            print('>> ORDEM: BUY')
                            print(f'ID: {OrderID}\nData: {Created}\nOrdem: {Status} \nTipo: {Type} \nValor: {Price:.8f} \nQuantidade: {Quantity}\n')
                        elif Type == 'SELL':
                            print('=' * 50)
                            print('>> ORDEM: SELL')
                            print(f'ID: {OrderID}\nData: {Created}\nOrdem: {Status} \nTipo: {Type} \nValor: {Price:.8f} \nQuantidade: {Quantity}\n')
                        else:
                            print('>> ERRO: Tipo de ordem não é BUY ou SELL')
                    else:
                        print('>> ERRO: Status não é OPEN')
                c += 1
            print('=' * 50)
        
######################################################################
    
    elif acao == '4':
        print('=' * 50)
        print('>> AMI')
        print('\nDigite: COMPRA / VENDA\n\nO que deseja fazer?')
        acaoAMI = input('Digite aqui: ').upper()
        market = ativo + '_' + mercado
        rate = 0
        amirate = 0
        quantity = 0

        if acaoAMI == 'COMPRA':
            print('>> CRIA ORDEM AMI DE COMPRA\n')
            rate = input('Qual o preço? ')
            amirate = input('Qual o preço AMI? ')
            quantity = input('Qual a quantidade? ')

            compraAMI = key_secretEXC.buy_limitami(market, rate, amirate, quantity)
            print(f'Resposta: {compraAMI}\n')

        elif acaoAMI == 'VENDA':
            print('>> CRIA ORDEM AMI DE VENDA\n')
            rate = input('Qual o preço? ')
            amirate = input('Qual o preço AMI? ')
            quantity = input('Qual a quantidade? ')

            vendaAMI = key_secretEXC.sell_limitami(market, rate, amirate, quantity)
            print(f'Resposta: {vendaAMI}\n')

        else:
            print('Por favor, digite a palavra correta.')

######################################################################
    
    elif acao == '7':
        print('=' * 50)
        print('>> ORDEM COMPRA: EXC')

        precoCompra = input('Digite o preço: ')
        quantidadeCompra = input('Digite a quantidade: ')

        faz_compraEXC = key_secretEXC.buy_limit(ativo_mercado, precoCompra, quantidadeCompra)
        print(faz_compraEXC)
        # print(faz_compraEXC['result'])

######################################################################
    
    elif acao == '6':
        print('=' * 50)
        print('>> ORDEM VENDA: EXC')

        precoVenda = input('Digite o preço: ')
        quantidadeVenda = input('Digite a quantidade: ')

        faz_vendaEXC = key_secretEXC.sell_limit(ativo_mercado, precoVenda, quantidadeVenda)
        print(faz_vendaEXC)
        # print(faz_vendaEXC['result'])

######################################################################
    
    elif acao == '5':
        print('=' * 50)
        print('>> ORDEM AMI 2: EXC')

        func_AMI.func_ami(ativo, mercado)

######################################################################
    
    elif not acao:
        print('>> SAIR')
        break

######################################################################
    
    else:
        print('>> ATENÇÃO: Opção inválida. Tente novamente!')
    print('=' * 50)
    time.sleep(2)

print('\nFim do programa!\n')

