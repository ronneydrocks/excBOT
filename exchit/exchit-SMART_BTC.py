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

addressSmartcashEXC = config.addressSmartcashEXC

urlGettickerEXC_SMART_BTC = config.urlGettickerEXC_SMART_BTC
urlGetOrderBookEXC_market_SMART_BTC = config.urlGetOrderBookEXC_market_SMART_BTC

feeSMART_EXC = config.feeSMART_EXC

################################################
#           HITBTC - CONFIG                    #
################################################

# HitBTC configurações

public_key = config.public_keyHIT
secret = config.secretHIT
client = hitBOT.Client("https://api.hitbtc.com", public_key, secret)

addressSmartcashHIT = config.addressSmartcashHIT

urlGettickerHIT_SMART_BTC = config.urlGettickerHIT_SMART_BTC
urlGetOrderBookHIT_BUY_SMART_BTC = config.urlGetOrderBookHIT_BUY_SMART_BTC
tempoSmartcashBlockchain = config.tempoSmartcashBlockchain

SMART_btc = client.get_symbol('SMARTBTC')
addressSmartcash = client.get_address('SMART')     # obter endereço SMART para depósito

feeSMART_HIT = config.feeSMART_HIT

################################################
#           GLOBAL - CONFIG                    #
################################################

diferencaSatoshi_SMART_BTC = config.diferencaSatoshi_SMART_BTC
minimaCompra_SMART_BTC = config.minimaCompra_SMART_BTC
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

            print('Exchange: ExcCripto (SMART/BTC)\n')
            requisicaoExc = requests.get(urlGettickerEXC_SMART_BTC)
            dicionarioExc = json.loads(requisicaoExc.text)

            rEXC = requests.get(urlGetOrderBookEXC_market_SMART_BTC)
            jEXC = json.loads(rEXC.text)
            quantidade_vendendoEXC = jEXC['result']['sell'][0]['Quantity']
            quantidade_comprandoEXC = jEXC['result']['buy'][0]['Quantity']

            compraSmartcashEXC = float(dicionarioExc['result'][0]['Bid'])
            print(f'Compra: {compraSmartcashEXC:.8f} / Quantidade: {quantidade_comprandoEXC}')

            vendaSmartcashEXC = float(dicionarioExc['result'][0]['Ask'])
            print(f'Venda: {vendaSmartcashEXC:.8f} / Quantidade: {quantidade_vendendoEXC}')

            print('-' * 10)

            print('Exchange: HitBTC (SMART/BTC)\n')

            requisicaoHIT = requests.get(urlGettickerHIT_SMART_BTC)
            dicionarioHIT = json.loads(requisicaoHIT.text)

            rHIT = requests.get(urlGetOrderBookHIT_BUY_SMART_BTC)
            jHIT = json.loads(rHIT.text)

            compraSmartcashHIT = float(dicionarioHIT['bid'][0]['price'])
            quantidade_comprandoHIT = jHIT['bid'][0]['size']
            print(f'Compra: {compraSmartcashHIT:.9f} / Quantidade: {quantidade_comprandoHIT}')

            vendaSmartcashHIT = float(dicionarioHIT['ask'][0]['price'])
            quantidade_vendendoHIT = jHIT['ask'][0]['size']
            print(f'Venda: {vendaSmartcashHIT:.9f} / Quantidade: {quantidade_vendendoHIT}')

            print('-' * 10, '\n')

            # ADICIONANDO FEE
            quantidade_comprandoEXC = float(quantidade_comprandoEXC) + float(feeSMART_HIT)
            quantidade_vendendoEXC = float(quantidade_vendendoEXC) + float(feeSMART_EXC)
            quantidade_comprandoHIT = float(quantidade_comprandoHIT) + float(feeSMART_EXC)
            quantidade_vendendoHIT = float(quantidade_vendendoHIT) + float(feeSMART_HIT)

            ########################################################################
            # PRINCIPAL
            print('\nVerificando: COMPRAR na EXC, para VENDER na HIT')
            if vendaSmartcashEXC < compraSmartcashHIT and compraSmartcashHIT - vendaSmartcashEXC > diferencaSatoshi_SMART_BTC:
                print(f'>>> OPORTUNIDADE <<< VENDA na EXC mais barata que COMPRA na HIT e diferença acima de: {diferencaSatoshi_SMART_BTC:.8f} satoshi')

                ###################################################
                #                  COMPRA na EXC:                 #
                ###################################################
                if float(quantidade_vendendoEXC) < float(quantidade_comprandoHIT) > minimaCompra_SMART_BTC:
                    print(f'\nCOMPRANDO NA EXC... {quantidade_vendendoEXC}')

                    # AÇÃO: COMPRA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE
                    faz_compraEXC = key_secretEXC.buy_limit('SMART_BTC', vendaSmartcashHIT, quantidade_vendendoEXC)
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
                    print(f'TRANSFERINDO... {quantidade_vendendoEXC} SMART')
                    wCOMPRA = str(quantidade_vendendoEXC)
                    urlWithdrawEXC = 'https://trade.exccripto.com/api/v3/private/withdraw?apikey=' + keyEXC + '&nonce=' + str(
                        int(time.time())) + '&asset=SMART&quantity=' + wCOMPRA + '&address=' + addressSmartcashHIT
                    # print(urlWithdrawEXC)  # PRINT url completa transferencia

                    # sign
                    sign = hmac.new(secretEXC.encode(), urlWithdrawEXC.encode(), hashlib.sha512).hexdigest()
                    # Adding sign to header
                    headers = {'apisign': sign}
                    # Make request
                    response = requests.get(url=urlWithdrawEXC, headers=headers)
                    # print(response.json())

                    # TEMPO TRANSFERENCIA SMART: 6 minutos = 360 segundos + 20s extra
                    print('\n>> AGUARDANDO CONFIRMAÇÕES<< \n')
                    for contagem in range(380, -1, -1):
                        time.sleep(1)
                        print(contagem, end='.')

                    ##############
                    # AÇÃO: TRANSFERE CONTA PRINCIPAL PARA TRADING
                    # Obter saldo SMART em trading
                    SMART_balance = 0.0
                    balances = client.get_trading_balance()
                    for balance in balances:
                        if balance['currency'] == 'SMART':
                            SMART_balance = float(balance['available'])

                    print('Saldo Conta Trading: %s' % SMART_balance)

                    # Obter saldo SMART em Conta Principal
                    SMART_balance = 0.0
                    balances = client.get_account_balance()
                    for balance in balances:
                        if balance['currency'] == 'SMART':
                            SMART_balance = float(balance['available'])

                    print('Saldo Conta Principal: %s' % SMART_balance)

                    # TRANSFERE de CONTA PRINCIPAL para CONTA TRADING
                    print('\nTRANSFERINDO...PRINCIPAL/TRANDING')
                    client.transfer('SMART', SMART_balance, True)
                    print(f'Saldo Atualizado(Conta Principal): {SMART_balance}')

                    time.sleep(2)  # espere até que a transferência seja concluída

                    # TIRA FEE
                    quantidade_vendendoEXC = float(quantidade_vendendoEXC) - float(feeSMART_EXC)

                    # AÇÃO: VENDE na HIT
                    print(f'\nVENDENDO na HIT... {quantidade_vendendoEXC}')
                    session = requests.session()
                    session.auth = (public_key, secret)
                    orderData = {'symbol': 'smartbtc', 'side': 'sell', 'quantity': quantidade_vendendoEXC, 'price': vendaSmartcashHIT}
                    r = session.post('https://api.hitbtc.com/api/2/order', data=orderData)
                    print(r.json())
                    print('Ordem de VENDA criada na HIT')

                elif float(quantidade_vendendoEXC) > float(quantidade_comprandoHIT) > minimaCompra_SMART_BTC:
                    print(f'\nCOMPRANDO NA EXC... {quantidade_comprandoHIT}')

                    # AÇÃO: COMPRA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE
                    faz_compraEXC = key_secretEXC.buy_limit('SMART_BTC', vendaSmartcashHIT, quantidade_comprandoHIT)
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
                    print(f'TRANSFERINDO... {quantidade_comprandoHIT} SMART')
                    wCOMPRA = str(quantidade_comprandoHIT)
                    urlWithdrawEXC = 'https://trade.exccripto.com/api/v3/private/withdraw?apikey=' + keyEXC + '&nonce=' + str(int(time.time())) + '&asset=SMART&quantity=' + wCOMPRA + '&address=' + addressSmartcashHIT
                    # print(urlWithdrawEXC)      # PRINT url completa transferencia

                    # sign
                    sign = hmac.new(secretEXC.encode(), urlWithdrawEXC.encode(), hashlib.sha512).hexdigest()
                    # Adding sign to header
                    headers = {'apisign': sign}
                    # Make request
                    response = requests.get(url=urlWithdrawEXC, headers=headers)
                    # print(response.json())

                    # TEMPO TRANSFERENCIA SMART: 10 CONFIRMAÇÕES = 750 segundos
                    print('\n>> AGUARDANDO CONFIRMAÇÕES <<\n')
                    for contagem in range(750, -1, -1):
                        time.sleep(1)
                        print(contagem, end='.')

                    ##############
                    # AÇÃO: TRANSFERE CONTA PRINCIPAL PARA TRADING
                    # Obter saldo SMART em trading
                    SMART_balance = 0.0
                    balances = client.get_trading_balance()
                    for balance in balances:
                        if balance['currency'] == 'SMART':
                            SMART_balance = float(balance['available'])

                    print('Saldo Conta Trading: %s' % SMART_balance)

                    # Obter saldo SMART em Conta Principal
                    SMART_balance = 0.0
                    balances = client.get_account_balance()
                    for balance in balances:
                        if balance['currency'] == 'SMART':
                            SMART_balance = float(balance['available'])

                    print('Saldo Conta Principal: %s' % SMART_balance)

                    # TRANSFERE de CONTA PRINCIPAL para CONTA TRADING
                    print('\nTRANSFERINDO...PRINCIPAL/TRANDING')
                    client.transfer('SMART', SMART_balance, True)
                    print(f'Saldo Atualizado(Conta Principal): {SMART_balance}')

                    time.sleep(2)  # espere até que a transferência seja concluída

                    # TIRA FEE
                    quantidade_comprandoHIT = float(quantidade_comprandoHIT) - float(feeSMART_EXC)

                    # AÇÃO: VENDE na HIT
                    print(f'\nVENDENDO na HIT... {quantidade_comprandoHIT}')
                    session = requests.session()
                    session.auth = (public_key, secret)
                    orderData = {'symbol': 'smartbtc', 'side': 'sell', 'quantity': quantidade_comprandoHIT, 'price': vendaSmartcashHIT}
                    r = session.post('https://api.hitbtc.com/api/2/order', data=orderData)
                    print(r.json())
                    print('Ordem de VENDA criada na HIT')

            # PRINCIPAL
            elif vendaSmartcashEXC < compraSmartcashHIT and compraSmartcashHIT - vendaSmartcashEXC < diferencaSatoshi_SMART_BTC:
                print(f'\n>> AGUARDE << Venda na EXC está mais barata que compra na HIT, mas diferença abaixo de {diferencaSatoshi_SMART_BTC:.8f} satoshi')

            # PRINCIPAL
            elif vendaSmartcashEXC > compraSmartcashHIT:
                print('\n>> AGUARDE << Sem oportunidades.')

            # PRINCIPAL
            else:
                print('\n>> AGUARDE << Valores iguais!!!')

            print('-' * 10)

            ########################################################################
            # PRINCIPAL
            print('\nVerificando: COMPRAR na HIT, para VENDER na EXC')
            if vendaSmartcashHIT < compraSmartcashEXC and compraSmartcashEXC - vendaSmartcashHIT > diferencaSatoshi_SMART_BTC:
                print(f'>>> OPORTUNIDADE <<< VENDA na HIT mais barata que COMPRA na EXC e diferença acima de: {diferencaSatoshi_SMART_BTC:.8f} satoshi')

                ###################################################
                #                  COMPRA na HIT:                 #
                ###################################################
                if float(quantidade_vendendoHIT) < float(quantidade_comprandoEXC) > minimaCompra_SMART_BTC:
                    print(f'\nCOMPRANDO NA HIT... {quantidade_vendendoHIT}')

                    # AÇÃO: COMPRA
                    # ORDEM DE COMPRA NA HIT
                    session = requests.session()
                    session.auth = (public_key, secret)
                    orderData = {'symbol': 'smartbtc', 'side': 'buy', 'quantity': quantidade_vendendoHIT, 'price': vendaSmartcashHIT}
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
                        # Obter saldo SMART em trading
                        SMART_ContaTrading = 0.0
                        balances = client.get_trading_balance()
                        for balance in balances:
                            if balance['currency'] == 'SMART':
                                SMART_ContaTrading = float(balance['available'])

                        # print(f'Saldo Conta Trading {SMART_ContaTrading}')

                        # Obter saldo SMART em Conta Principal
                        SMART_ContaPrincipal = 0.0
                        balances = client.get_account_balance()
                        for balance in balances:
                            if balance['currency'] == 'SMART':
                                SMART_ContaPrincipal = float(balance['available'])

                        # print(f'Saldo Conta Principal {SMART_ContaPrincipal}')

                        # TRANSFERE de CONTA TRADING para CONTA PRINCIPAL
                        print('\n>> TRANSFERINDO...TRANDING/PRINCIPAL <<')
                        client.transfer2('SMART', SMART_ContaTrading, 'exchangeToBank')

                        time.sleep(2)

                        # FAZ WITHDRAW PARA EXC
                        print(f'\nWITHDRAW PARA EXC... {quantidade_vendendoHIT}')
                        client = hitBOT.Client("https://api.hitbtc.com", public_key, secret)
                        faz_withdraw = hitBOT.Client.withdraw(client, 'SMART', quantidade_vendendoHIT, addressSmartcashEXC)
                        print(faz_withdraw)

                        # TEMPO TRANSFERENCIA SMART: 3 CONFIRMAÇÕES = 300 segundos
                        print('\n>> AGUARDANDO CONFIRMAÇÕES <<\n')
                        for contagem in range(300, -1, -1):
                            time.sleep(1)
                            print(contagem, end='.')

                        # TIRA FEE
                        quantidade_vendendoHIT = float(quantidade_vendendoHIT) - float(feeSMART_HIT)

                        # AÇÃO: VENDE
                        print(f'\nVENDENDO NA EXC... {quantidade_vendendoHIT}')
                        # Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade
                        faz_vendaEXC = key_secretEXC.sell_limit('SMART_BTC', vendaSmartcashHIT, quantidade_vendendoHIT)
                        print(faz_vendaEXC)

                elif float(quantidade_vendendoHIT) > float(quantidade_comprandoEXC) > minimaCompra_SMART_BTC:
                    print(f'\nCOMPRANDO NA HIT... {quantidade_comprandoEXC}')

                    # AÇÃO: COMPRA
                    # ORDEM DE COMPRA NA HIT
                    session = requests.session()
                    session.auth = (public_key, secret)
                    orderData = {'symbol': 'smartbtc', 'side': 'buy', 'quantity': quantidade_comprandoEXC, 'price': vendaSmartcashHIT}
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
                        # Obter saldo SMART em trading
                        SMART_ContaTrading = 0.0
                        balances = client.get_trading_balance()
                        for balance in balances:
                            if balance['currency'] == 'SMART':
                                SMART_ContaTrading = float(balance['available'])

                        # Obter saldo SMART em Conta Principal
                        SMART_ContaPrincipal = 0.0
                        balances = client.get_account_balance()
                        for balance in balances:
                            if balance['currency'] == 'SMART':
                                SMART_ContaPrincipal = float(balance['available'])

                        # TRANSFERE de CONTA TRADING para CONTA PRINCIPAL
                        print('\n>> TRANSFERINDO...TRANDING/PRINCIPAL <<')
                        client.transfer2('SMART', SMART_ContaTrading, 'exchangeToBank')

                        time.sleep(2)

                        # FAZ WITHDRAW PARA EXC
                        print(f'\nWITHDRAW PARA EXC... {quantidade_comprandoEXC}')
                        client = hitBOT.Client("https://api.hitbtc.com", public_key, secret)
                        faz_withdraw = hitBOT.Client.withdraw(client, 'SMART', quantidade_comprandoEXC, addressSmartcashEXC)
                        print(faz_withdraw)

                        # TEMPO TRANSFERENCIA SMART: 3 minutos = 180 segundos + 20s entras
                        print('\n>> AGUARDANDO CONFIRMAÇÕES <<\n')
                        for contagem in range(200, -1, -1):
                            time.sleep(1)
                            print(contagem, end='.')

                        # TIRA FEE
                        quantidade_comprandoEXC = float(quantidade_comprandoEXC) - float(feeSMART_HIT)

                        # AÇÃO: VENDE
                        print(f'\nVENDENDO NA EXC... {quantidade_comprandoEXC}')
                        # Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade
                        faz_vendaEXC = key_secretEXC.sell_limit('SMART_BTC', vendaSmartcashHIT, quantidade_comprandoEXC)
                        print(faz_vendaEXC)

            # PRINCIPAL
            elif vendaSmartcashHIT < compraSmartcashEXC and compraSmartcashEXC - vendaSmartcashHIT < diferencaSatoshi_SMART_BTC:
                print(f'\n>> AGUARDE << - Venda na HIT está mais barata que compra na EXC, mas diferença abaixo de {diferencaSatoshi_SMART_BTC:.8f} satoshi')

            # PRINCIPAL
            elif vendaSmartcashHIT > compraSmartcashEXC:
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
