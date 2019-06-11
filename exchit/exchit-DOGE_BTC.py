import requests
import json
import excBot
import time
import hmac
import hashlib
import datetime
import hitBOT
import config


################################################
#           EXC CRIPTO - CONFIG                #
################################################
emailEXC = config.emailEXC
keyEXC = config.keyEXC
secretEXC = config.secretEXC
key_secretEXC = excBot.excBot(keyEXC, secretEXC, nonce=True)

addressDogecoinEXC = config.addressDogecoinEXC

urlGettickerEXC_DOGE_BTC = config.urlGettickerEXC_DOGE_BTC
urlGetOrderBookEXC_market_DOGE_BTC = config.urlGetOrderBookEXC_market_DOGE_BTC

feeDOGE_EXC = config.feeDOGE_EXC

################################################
#           HITBTC - CONFIG                    #
################################################

# HitBTC configurações

public_key = config.public_keyHIT
secret = config.secretHIT
client = hitBOT.Client("https://api.hitbtc.com", public_key, secret)

addressDogecoinHIT = config.addressDogecoinHIT

urlGettickerHIT_DOGE_BTC = config.urlGettickerHIT_DOGE_BTC
urlGetOrderBookHIT_BUY_DOGE_BTC = config.urlGetOrderBookHIT_BUY_DOGE_BTC
tempoDogecoinBlockchain = config.tempoDogecoinBlockchain

DOGE_btc = client.get_symbol('DOGEBTC')
addressDogecoin = client.get_address('DOGE')     # obter endereço DOGE para depósito

feeDOGE_HIT = config.feeDOGE_HIT

################################################
#           GLOBAL - CONFIG                    #
################################################

diferencaSatoshi_DOGE_BTC = config.diferencaSatoshi_DOGE_BTC
minimaCompra_DOGE_BTC = config.minimaCompra_DOGE_BTC
tempoVerificacao = config.tempoVerificacao

########################################################################
print('=' * 40)
while True:
    try:
        contador = 0
        while contador <= 1000000:
            contador += 1
            print(f'\nVerificação: {contador}')
            print(datetime.datetime.now())

            for contagem in range(10, -1, -1):
                time.sleep(tempoVerificacao)
                print('.', end=' ')

            ########################################################################
            print('\n')
            print('-x-' * 20)
            ########################################################################

            print('-' * 10)

            print('Exchange: ExcCripto (DOGE/BTC)\n')
            requisicaoExc = requests.get(urlGettickerEXC_DOGE_BTC)
            dicionarioExc = json.loads(requisicaoExc.text)

            rEXC = requests.get(urlGetOrderBookEXC_market_DOGE_BTC)
            jEXC = json.loads(rEXC.text)
            quantidade_vendendoEXC = jEXC['result']['sell'][0]['Quantity']
            quantidade_comprandoEXC = jEXC['result']['buy'][0]['Quantity']

            compraDogecoinEXC = float(dicionarioExc['result'][0]['Bid'])
            print(f'Compra: {compraDogecoinEXC:.8f} / Quantidade: {quantidade_comprandoEXC}')

            vendaDogecoinEXC = float(dicionarioExc['result'][0]['Ask'])
            print(f'Venda: {vendaDogecoinEXC:.8f} / Quantidade: {quantidade_vendendoEXC}')

            print('-' * 10)

            print('Exchange: HitBTC (DOGE/BTC)\n')

            requisicaoHIT = requests.get(urlGettickerHIT_DOGE_BTC)
            dicionarioHIT = json.loads(requisicaoHIT.text)

            rHIT = requests.get(urlGetOrderBookHIT_BUY_DOGE_BTC)
            jHIT = json.loads(rHIT.text)

            compraDogecoinHIT = float(dicionarioHIT['bid'][0]['price'])
            quantidade_comprandoHIT = jHIT['bid'][0]['size']
            print(f'Compra: {compraDogecoinHIT:.9f} / Quantidade: {quantidade_comprandoHIT}')

            vendaDogecoinHIT = float(dicionarioHIT['ask'][0]['price'])
            quantidade_vendendoHIT = jHIT['ask'][0]['size']
            print(f'Venda: {vendaDogecoinHIT:.9f} / Quantidade: {quantidade_vendendoHIT}')

            print('-' * 10, '\n')

            # ADICIONANDO FEE
            quantidade_comprandoEXC = float(quantidade_comprandoEXC) + float(feeDOGE_HIT)
            quantidade_vendendoEXC = float(quantidade_vendendoEXC) + float(feeDOGE_EXC)
            quantidade_comprandoHIT = float(quantidade_comprandoHIT) + float(feeDOGE_EXC)
            quantidade_vendendoHIT = float(quantidade_vendendoHIT) + float(feeDOGE_HIT)

            ########################################################################
            # PRINCIPAL
            print('\nVerificando: COMPRAR na EXC, para VENDER na HIT')
            if vendaDogecoinEXC < compraDogecoinHIT and compraDogecoinHIT - vendaDogecoinEXC > diferencaSatoshi_DOGE_BTC:
                print(f'>>> OPORTUNIDADE <<< VENDA na EXC mais barata que COMPRA na HIT e diferença acima de: {diferencaSatoshi_DOGE_BTC:.10f} satoshi')

                ###################################################
                #                  COMPRA na EXC:                 #
                ###################################################
                if float(quantidade_vendendoEXC) < float(quantidade_comprandoHIT) > minimaCompra_DOGE_BTC:
                    print(f'\nCOMPRANDO NA EXC... {quantidade_vendendoEXC}')

                    # AÇÃO: COMPRA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE
                    faz_compraEXC = key_secretEXC.buy_limit('DOGE_BTC', vendaDogecoinHIT, quantidade_vendendoEXC)
                    print(faz_compraEXC)
                    # print(faz_compraEXC['result'])

                    #################
                    # SALDO INSUFICIENTE EXC
                    # recebe mensagem do saldo
                    respostaFazCompraEXC = faz_compraEXC['result']
                    for item in respostaFazCompraEXC:
                        if respostaFazCompraEXC == 'ERR_INSUFICIENT_BALANCE':
                            print('\nATENÇÃO >> SALDO INSUFICIENTE << ')
                            break

                    #################
                    # AÇÃO: TRANSFERE EXC para HIT
                    print(f'TRANSFERINDO... {quantidade_vendendoEXC} DOGE')
                    wCOMPRA = str(quantidade_vendendoEXC)
                    urlWithdrawEXC = 'https://trade.exccripto.com/api/v3/private/withdraw?apikey=' + keyEXC + '&nonce=' + str(
                        int(time.time())) + '&asset=DOGE&quantity=' + wCOMPRA + '&address=' + addressDogecoinHIT
                    # print(urlWithdrawEXC)  # PRINT url completa transferencia

                    # sign
                    sign = hmac.new(secretEXC.encode(), urlWithdrawEXC.encode(), hashlib.sha512).hexdigest()
                    # Adding sign to header
                    headers = {'apisign': sign}
                    # Make request
                    response = requests.get(url=urlWithdrawEXC, headers=headers)
                    # print(response.json())

                    # TEMPO TRANSFERENCIA DOGE: 6 minutos = 360 segundos + 20s extra
                    print('\n>> AGUARDANDO CONFIRMAÇÕES<< \n')
                    for contagem in range(380, -1, -1):
                        time.sleep(1)
                        print(contagem, end='.')

                    ##############
                    # AÇÃO: TRANSFERE CONTA PRINCIPAL PARA TRADING
                    # Obter saldo DOGE em trading
                    DOGE_balance = 0.0
                    balances = client.get_trading_balance()
                    for balance in balances:
                        if balance['currency'] == 'DOGE':
                            DOGE_balance = float(balance['available'])

                    print('Saldo Conta Trading: %s' % DOGE_balance)

                    # Obter saldo DOGE em Conta Principal
                    DOGE_balance = 0.0
                    balances = client.get_account_balance()
                    for balance in balances:
                        if balance['currency'] == 'DOGE':
                            DOGE_balance = float(balance['available'])

                    print('Saldo Conta Principal: %s' % DOGE_balance)

                    # TRANSFERE de CONTA PRINCIPAL para CONTA TRADING
                    print('\nTRANSFERINDO...PRINCIPAL/TRANDING')
                    client.transfer('DOGE', DOGE_balance, True)
                    print(f'Saldo Atualizado(Conta Principal): {DOGE_balance}')

                    time.sleep(2)  # espere até que a transferência seja concluída

                    # TIRA FEE
                    quantidade_vendendoEXC = float(quantidade_vendendoEXC) - float(feeDOGE_EXC)

                    # AÇÃO: VENDE na HIT
                    print(f'\nVENDENDO na HIT... {quantidade_vendendoEXC}')
                    session = requests.session()
                    session.auth = (public_key, secret)
                    orderData = {'symbol': 'dogebtc', 'side': 'sell', 'quantity': quantidade_vendendoEXC, 'price': vendaDogecoinHIT}
                    r = session.post('https://api.hitbtc.com/api/2/order', data=orderData)
                    print(r.json())
                    print('Ordem de VENDA criada na HIT')

                elif float(quantidade_vendendoEXC) > float(quantidade_comprandoHIT) > minimaCompra_DOGE_BTC:
                    print(f'\nCOMPRANDO NA EXC... {quantidade_comprandoHIT}')

                    # AÇÃO: COMPRA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE
                    faz_compraEXC = key_secretEXC.buy_limit('DOGE_BTC', vendaDogecoinHIT, quantidade_comprandoHIT)
                    print(faz_compraEXC)
                    # print(faz_compraEXC['result'])

                    #################
                    # SALDO INSUFICIENTE EXC
                    # recebe mensagem do saldo
                    respostaFazCompraEXC = faz_compraEXC['result']
                    for item in respostaFazCompraEXC:
                        if respostaFazCompraEXC == 'ERR_INSUFICIENT_BALANCE':
                            print('\nATENÇÃO >> SALDO INSUFICIENTE << ')
                            break
                    #################

                    # AÇÃO: TRANSFERE EXC para HIT
                    print(f'TRANSFERINDO... {quantidade_comprandoHIT} DOGE')
                    wCOMPRA = str(quantidade_comprandoHIT)
                    urlWithdrawEXC = 'https://trade.exccripto.com/api/v3/private/withdraw?apikey=' + keyEXC + '&nonce=' + str(int(time.time())) + '&asset=DOGE&quantity=' + wCOMPRA + '&address=' + addressDogecoinHIT
                    # print(urlWithdrawEXC)      # PRINT url completa transferencia

                    # sign
                    sign = hmac.new(secretEXC.encode(), urlWithdrawEXC.encode(), hashlib.sha512).hexdigest()
                    # Adding sign to header
                    headers = {'apisign': sign}
                    # Make request
                    response = requests.get(url=urlWithdrawEXC, headers=headers)
                    # print(response.json())

                    # TEMPO TRANSFERENCIA DOGE: 10 CONFIRMAÇÕES = 750 segundos
                    print('\n>> AGUARDANDO CONFIRMAÇÕES <<\n')
                    for contagem in range(750, -1, -1):
                        time.sleep(1)
                        print(contagem, end='.')

                    ##############
                    # AÇÃO: TRANSFERE CONTA PRINCIPAL PARA TRADING
                    # Obter saldo DOGE em trading
                    DOGE_balance = 0.0
                    balances = client.get_trading_balance()
                    for balance in balances:
                        if balance['currency'] == 'DOGE':
                            DOGE_balance = float(balance['available'])

                    print('Saldo Conta Trading: %s' % DOGE_balance)

                    # Obter saldo DOGE em Conta Principal
                    DOGE_balance = 0.0
                    balances = client.get_account_balance()
                    for balance in balances:
                        if balance['currency'] == 'DOGE':
                            DOGE_balance = float(balance['available'])

                    print('Saldo Conta Principal: %s' % DOGE_balance)

                    # TRANSFERE de CONTA PRINCIPAL para CONTA TRADING
                    print('\nTRANSFERINDO...PRINCIPAL/TRANDING')
                    client.transfer('DOGE', DOGE_balance, True)
                    print(f'Saldo Atualizado(Conta Principal): {DOGE_balance}')

                    time.sleep(2)  # espere até que a transferência seja concluída

                    # TIRA FEE
                    quantidade_comprandoHIT = float(quantidade_comprandoHIT) - float(feeDOGE_EXC)

                    # AÇÃO: VENDE na HIT
                    print(f'\nVENDENDO na HIT... {quantidade_comprandoHIT}')
                    session = requests.session()
                    session.auth = (public_key, secret)
                    orderData = {'symbol': 'dogebtc', 'side': 'sell', 'quantity': quantidade_comprandoHIT, 'price': vendaDogecoinHIT}
                    r = session.post('https://api.hitbtc.com/api/2/order', data=orderData)
                    print(r.json())
                    print('Ordem de VENDA criada na HIT')

            # PRINCIPAL
            elif vendaDogecoinEXC < compraDogecoinHIT and compraDogecoinHIT - vendaDogecoinEXC < diferencaSatoshi_DOGE_BTC:
                print(f'\n>> AGUARDE << Venda na EXC está mais barata que compra na HIT, mas diferença abaixo de {diferencaSatoshi_DOGE_BTC:.10f} satoshi')

            # PRINCIPAL
            elif vendaDogecoinEXC > compraDogecoinHIT:
                print('\n>> AGUARDE << Sem oportunidades.')

            # PRINCIPAL
            else:
                print('\n>> AGUARDE << Valores iguais!!!')

            print('-' * 10)

            ########################################################################
            # PRINCIPAL
            print('\nVerificando: COMPRAR na HIT, para VENDER na EXC')
            if vendaDogecoinHIT < compraDogecoinEXC and compraDogecoinEXC - vendaDogecoinHIT > diferencaSatoshi_DOGE_BTC:
                print(f'>>> OPORTUNIDADE <<< VENDA na HIT mais barata que COMPRA na EXC e diferença acima de: {diferencaSatoshi_DOGE_BTC:.10f} satoshi')

                ###################################################
                #                  COMPRA na HIT:                 #
                ###################################################
                if float(quantidade_vendendoHIT) < float(quantidade_comprandoEXC) > minimaCompra_DOGE_BTC:
                    print(f'\nCOMPRANDO NA HIT... {quantidade_vendendoHIT}')

                    # AÇÃO: COMPRA
                    # ORDEM DE COMPRA NA HIT
                    session = requests.session()
                    session.auth = (public_key, secret)
                    orderData = {'symbol': 'dogebtc', 'side': 'buy', 'quantity': quantidade_vendendoHIT, 'price': vendaDogecoinHIT}
                    r = session.post('https://api.hitbtc.com/api/2/order', data=orderData)
                    print(r.json())
                    # print('ORDEM DE COMPRA CRIADA')

                    time.sleep(2)

                    #################
                    # SALDO INSUFICIENTE HIT
                    # recebe mensagem do saldo
                    jHIT = json.loads(r.text)
                    # respostaFazCompraHIT = jHIT['error']['message']

                    try:
                        respostaFazCompraHIT = jHIT['status']
                    except KeyError:
                        respostaFazCompraHIT = jHIT['error']['message']

                    # if respostaFazCompraHIT == 'Insufficient funds':
                    #     print('\nATENÇÃO >> SALDO INSUFICIENTE <<< ')

                    for item in respostaFazCompraHIT:
                        if respostaFazCompraHIT == 'Insufficient funds':
                            print('\nATENÇÃO >> SALDO INSUFICIENTE < ')
                            break

                    else:
                        #################
                        # AÇÃO: TRANSFERE
                        # transferir conta tranding para conta principal
                        ##############
                        # Obter saldo DOGE em trading
                        DOGE_ContaTrading = 0.0
                        balances = client.get_trading_balance()
                        for balance in balances:
                            if balance['currency'] == 'DOGE':
                                DOGE_ContaTrading = float(balance['available'])

                        # print(f'Saldo Conta Trading {DOGE_ContaTrading}')

                        # Obter saldo DOGE em Conta Principal
                        DOGE_ContaPrincipal = 0.0
                        balances = client.get_account_balance()
                        for balance in balances:
                            if balance['currency'] == 'DOGE':
                                DOGE_ContaPrincipal = float(balance['available'])

                        # print(f'Saldo Conta Principal {DOGE_ContaPrincipal}')

                        # TRANSFERE de CONTA TRADING para CONTA PRINCIPAL
                        print('\n>> TRANSFERINDO...TRANDING/PRINCIPAL <<')
                        client.transfer2('DOGE', DOGE_ContaTrading, 'exchangeToBank')

                        time.sleep(2)

                        # FAZ WITHDRAW PARA EXC
                        print(f'\nWITHDRAW PARA EXC... {quantidade_vendendoHIT}')
                        client = hitBOT.Client("https://api.hitbtc.com", public_key, secret)
                        faz_withdraw = hitBOT.Client.withdraw(client, 'DOGE', quantidade_vendendoHIT, addressDogecoinEXC)
                        print(faz_withdraw)

                        # TEMPO TRANSFERENCIA DOGE: 3 CONFIRMAÇÕES = 300 segundos
                        print('\n>> AGUARDANDO CONFIRMAÇÕES <<\n')
                        for contagem in range(300, -1, -1):
                            time.sleep(1)
                            print(contagem, end='.')

                        # TIRA FEE
                        quantidade_vendendoHIT = float(quantidade_vendendoHIT) - float(feeDOGE_HIT)

                        # AÇÃO: VENDE
                        print(f'\nVENDENDO NA EXC... {quantidade_vendendoHIT}')
                        # Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade
                        faz_vendaEXC = key_secretEXC.sell_limit('DOGE_BTC', vendaDogecoinHIT, quantidade_vendendoHIT)
                        print(faz_vendaEXC)

                elif float(quantidade_vendendoHIT) > float(quantidade_comprandoEXC) > minimaCompra_DOGE_BTC:
                    print(f'\nCOMPRANDO NA HIT... {quantidade_comprandoEXC}')

                    # AÇÃO: COMPRA
                    # ORDEM DE COMPRA NA HIT
                    session = requests.session()
                    session.auth = (public_key, secret)
                    orderData = {'symbol': 'dogebtc', 'side': 'buy', 'quantity': quantidade_comprandoEXC, 'price': vendaDogecoinHIT}
                    r = session.post('https://api.hitbtc.com/api/2/order', data=orderData)
                    print(r.json())

                    time.sleep(2)

                    #################
                    # SALDO INSUFICIENTE HIT
                    # recebe mensagem do saldo
                    jHIT = json.loads(r.text)
                    # respostaFazCompraHIT = jHIT['error']['message']

                    try:
                        respostaFazCompraHIT = jHIT['status']
                    except KeyError:
                        respostaFazCompraHIT = jHIT['error']['message']

                    # if respostaFazCompraHIT == 'Insufficient funds':
                    #     print('\nATENÇÃO >>> SALDO INSUFICIENTE << ')

                    for item in respostaFazCompraHIT:
                        if respostaFazCompraHIT == 'Insufficient funds':
                            print('\nATENÇÃO >> SALDO INSUFICIENTE < ')
                            break

                    else:
                        #################
                        # AÇÃO: TRANSFERE
                        # transferir conta tranding para conta principal
                        ##############
                        # Obter saldo DOGE em trading
                        DOGE_ContaTrading = 0.0
                        balances = client.get_trading_balance()
                        for balance in balances:
                            if balance['currency'] == 'DOGE':
                                DOGE_ContaTrading = float(balance['available'])

                        # Obter saldo DOGE em Conta Principal
                        DOGE_ContaPrincipal = 0.0
                        balances = client.get_account_balance()
                        for balance in balances:
                            if balance['currency'] == 'DOGE':
                                DOGE_ContaPrincipal = float(balance['available'])

                        # TRANSFERE de CONTA TRADING para CONTA PRINCIPAL
                        print('\n>> TRANSFERINDO...TRANDING/PRINCIPAL <<')
                        client.transfer2('DOGE', DOGE_ContaTrading, 'exchangeToBank')

                        time.sleep(2)

                        # FAZ WITHDRAW PARA EXC
                        print(f'\nWITHDRAW PARA EXC... {quantidade_comprandoEXC}')
                        client = hitBOT.Client("https://api.hitbtc.com", public_key, secret)
                        faz_withdraw = hitBOT.Client.withdraw(client, 'DOGE', quantidade_comprandoEXC, addressDogecoinEXC)
                        print(faz_withdraw)

                        # TEMPO TRANSFERENCIA DOGE: 3 minutos = 180 segundos + 20s entras
                        print('\n>> AGUARDANDO CONFIRMAÇÕES <<\n')
                        for contagem in range(200, -1, -1):
                            time.sleep(1)
                            print(contagem, end='.')

                        # TIRA FEE
                        quantidade_comprandoEXC = float(quantidade_comprandoEXC) - float(feeDOGE_HIT)

                        # AÇÃO: VENDE
                        print(f'\nVENDENDO NA EXC... {quantidade_comprandoEXC}')
                        # Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade
                        faz_vendaEXC = key_secretEXC.sell_limit('DOGE_BTC', vendaDogecoinHIT, quantidade_comprandoEXC)
                        print(faz_vendaEXC)

            # PRINCIPAL
            elif vendaDogecoinHIT < compraDogecoinEXC and compraDogecoinEXC - vendaDogecoinHIT < diferencaSatoshi_DOGE_BTC:
                print(f'\n>> AGUARDE << - Venda na HIT está mais barata que compra na EXC, mas diferença abaixo de {diferencaSatoshi_DOGE_BTC:.10f} satoshi')

            # PRINCIPAL
            elif vendaDogecoinHIT > compraDogecoinEXC:
                print('\n>> AGUARDE << Sem oportunidades.')

            # PRINCIPAL
            else:
                print('\n>> AGUARDE << Valores iguais!!!')

            ########################################################################
            print('=' * 40)
            print('-x-' * 20)
            ########################################################################

    except Exception as e:
            print(f'Tipo de erro: {e}')
