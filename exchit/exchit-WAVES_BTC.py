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

addressWavesEXC = config.addressWavesEXC

urlGettickerEXC_WAVES_BTC = config.urlGettickerEXC_WAVES_BTC
urlGetOrderBookEXC_market_WAVES_BTC = config.urlGetOrderBookEXC_market_WAVES_BTC

feeWAVES_EXC = config.feeWAVES_EXC

################################################
#           HITBTC - CONFIG                    #
################################################

# HitBTC configurações

public_key = config.public_keyHIT
secret = config.secretHIT
client = hitBOT.Client("https://api.hitbtc.com", public_key, secret)

addressWavesHIT = config.addressWavesHIT

urlGettickerHIT_WAVES_BTC = config.urlGettickerHIT_WAVES_BTC
urlGetOrderBookHIT_BUY_WAVES_BTC = config.urlGetOrderBookHIT_BUY_WAVES_BTC
tempoWavesBlockchain = config.tempoWavesBlockchain

WAVES_btc = client.get_symbol('WAVESBTC')
addressWaves = client.get_address('WAVES')     # obter endereço WAVES para depósito

feeWAVES_HIT = config.feeWAVES_HIT

################################################
#           GLOBAL - CONFIG                    #
################################################

diferencaSatoshi_WAVES_BTC = config.diferencaSatoshi_WAVES_BTC
minimaCompra_WAVES_BTC = config.minimaCompra_WAVES_BTC
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

            print('Exchange: ExcCripto (WAVES/BTC)\n')
            requisicaoExc = requests.get(urlGettickerEXC_WAVES_BTC)
            dicionarioExc = json.loads(requisicaoExc.text)

            rEXC = requests.get(urlGetOrderBookEXC_market_WAVES_BTC)
            jEXC = json.loads(rEXC.text)
            quantidade_vendendoEXC = jEXC['result']['sell'][0]['Quantity']
            quantidade_comprandoEXC = jEXC['result']['buy'][0]['Quantity']

            compraWavesEXC = float(dicionarioExc['result'][0]['Bid'])
            print(f'Compra: {compraWavesEXC:.8f} / Quantidade: {quantidade_comprandoEXC}')

            vendaWavesEXC = float(dicionarioExc['result'][0]['Ask'])
            print(f'Venda: {vendaWavesEXC:.8f} / Quantidade: {quantidade_vendendoEXC}')

            print('-' * 10)

            print('Exchange: HitBTC (WAVES/BTC)\n')

            requisicaoHIT = requests.get(urlGettickerHIT_WAVES_BTC)
            dicionarioHIT = json.loads(requisicaoHIT.text)

            rHIT = requests.get(urlGetOrderBookHIT_BUY_WAVES_BTC)
            jHIT = json.loads(rHIT.text)

            compraWavesHIT = float(dicionarioHIT['bid'][0]['price'])
            quantidade_comprandoHIT = jHIT['bid'][0]['size']
            print(f'Compra: {compraWavesHIT:.9f} / Quantidade: {quantidade_comprandoHIT}')

            vendaWavesHIT = float(dicionarioHIT['ask'][0]['price'])
            quantidade_vendendoHIT = jHIT['ask'][0]['size']
            print(f'Venda: {vendaWavesHIT:.9f} / Quantidade: {quantidade_vendendoHIT}')

            print('-' * 10, '\n')

            # ADICIONANDO FEE
            quantidade_comprandoEXC = float(quantidade_comprandoEXC) + float(feeWAVES_HIT)
            quantidade_vendendoEXC = float(quantidade_vendendoEXC) + float(feeWAVES_EXC)
            quantidade_comprandoHIT = float(quantidade_comprandoHIT) + float(feeWAVES_EXC)
            quantidade_vendendoHIT = float(quantidade_vendendoHIT) + float(feeWAVES_HIT)

            ########################################################################
            # PRINCIPAL
            print('\nVerificando: COMPRAR na EXC, para VENDER na HIT')
            if vendaWavesEXC < compraWavesHIT and compraWavesHIT - vendaWavesEXC > diferencaSatoshi_WAVES_BTC:
                print(f'>>> OPORTUNIDADE <<< VENDA na EXC mais barata que COMPRA na HIT e diferença acima de: {diferencaSatoshi_WAVES_BTC:.8f} satoshi')

                ###################################################
                #                  COMPRA na EXC:                 #
                ###################################################
                if float(quantidade_vendendoEXC) < float(quantidade_comprandoHIT) > minimaCompra_WAVES_BTC:
                    print(f'\nCOMPRANDO NA EXC... {quantidade_vendendoEXC}')

                    # AÇÃO: COMPRA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE
                    faz_compraEXC = key_secretEXC.buy_limit('WAVES_BTC', vendaWavesHIT, quantidade_vendendoEXC)
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
                    print(f'TRANSFERINDO... {quantidade_vendendoEXC} WAVES')
                    wCOMPRA = str(quantidade_vendendoEXC)
                    urlWithdrawEXC = 'https://trade.exccripto.com/api/v3/private/withdraw?apikey=' + keyEXC + '&nonce=' + str(
                        int(time.time())) + '&asset=WAVES&quantity=' + wCOMPRA + '&address=' + addressWavesHIT
                    # print(urlWithdrawEXC)  # PRINT url completa transferencia

                    # sign
                    sign = hmac.new(secretEXC.encode(), urlWithdrawEXC.encode(), hashlib.sha512).hexdigest()
                    # Adding sign to header
                    headers = {'apisign': sign}
                    # Make request
                    response = requests.get(url=urlWithdrawEXC, headers=headers)
                    # print(response.json())

                    # TEMPO TRANSFERENCIA WAVES: 6 minutos = 360 segundos + 20s extra
                    print('\n>> AGUARDANDO CONFIRMAÇÕES<< \n')
                    for contagem in range(380, -1, -1):
                        time.sleep(1)
                        print(contagem, end='.')

                    ##############
                    # AÇÃO: TRANSFERE CONTA PRINCIPAL PARA TRADING
                    # Obter saldo WAVES em trading
                    WAVES_balance = 0.0
                    balances = client.get_trading_balance()
                    for balance in balances:
                        if balance['currency'] == 'WAVES':
                            WAVES_balance = float(balance['available'])

                    print('Saldo Conta Trading: %s' % WAVES_balance)

                    # Obter saldo WAVES em Conta Principal
                    WAVES_balance = 0.0
                    balances = client.get_account_balance()
                    for balance in balances:
                        if balance['currency'] == 'WAVES':
                            WAVES_balance = float(balance['available'])

                    print('Saldo Conta Principal: %s' % WAVES_balance)

                    # TRANSFERE de CONTA PRINCIPAL para CONTA TRADING
                    print('\nTRANSFERINDO...PRINCIPAL/TRANDING')
                    client.transfer('WAVES', WAVES_balance, True)
                    print(f'Saldo Atualizado(Conta Principal): {WAVES_balance}')

                    time.sleep(2)  # espere até que a transferência seja concluída

                    # TIRA FEE
                    quantidade_vendendoEXC = float(quantidade_vendendoEXC) - float(feeWAVES_EXC)

                    # AÇÃO: VENDE na HIT
                    print(f'\nVENDENDO na HIT... {quantidade_vendendoEXC}')
                    session = requests.session()
                    session.auth = (public_key, secret)
                    orderData = {'symbol': 'wavesbtc', 'side': 'sell', 'quantity': quantidade_vendendoEXC, 'price': vendaWavesHIT}
                    r = session.post('https://api.hitbtc.com/api/2/order', data=orderData)
                    print(r.json())
                    print('Ordem de VENDA criada na HIT')

                elif float(quantidade_vendendoEXC) > float(quantidade_comprandoHIT) > minimaCompra_WAVES_BTC:
                    print(f'\nCOMPRANDO NA EXC... {quantidade_comprandoHIT}')

                    # AÇÃO: COMPRA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE
                    faz_compraEXC = key_secretEXC.buy_limit('WAVES_BTC', vendaWavesHIT, quantidade_comprandoHIT)
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
                    print(f'TRANSFERINDO... {quantidade_comprandoHIT} WAVES')
                    wCOMPRA = str(quantidade_comprandoHIT)
                    urlWithdrawEXC = 'https://trade.exccripto.com/api/v3/private/withdraw?apikey=' + keyEXC + '&nonce=' + str(int(time.time())) + '&asset=WAVES&quantity=' + wCOMPRA + '&address=' + addressWavesHIT
                    # print(urlWithdrawEXC)      # PRINT url completa transferencia

                    # sign
                    sign = hmac.new(secretEXC.encode(), urlWithdrawEXC.encode(), hashlib.sha512).hexdigest()
                    # Adding sign to header
                    headers = {'apisign': sign}
                    # Make request
                    response = requests.get(url=urlWithdrawEXC, headers=headers)
                    # print(response.json())

                    # TEMPO TRANSFERENCIA WAVES: 10 CONFIRMAÇÕES = 750 segundos
                    print('\n>> AGUARDANDO CONFIRMAÇÕES <<\n')
                    for contagem in range(750, -1, -1):
                        time.sleep(1)
                        print(contagem, end='.')

                    ##############
                    # AÇÃO: TRANSFERE CONTA PRINCIPAL PARA TRADING
                    # Obter saldo WAVES em trading
                    WAVES_balance = 0.0
                    balances = client.get_trading_balance()
                    for balance in balances:
                        if balance['currency'] == 'WAVES':
                            WAVES_balance = float(balance['available'])

                    print('Saldo Conta Trading: %s' % WAVES_balance)

                    # Obter saldo WAVES em Conta Principal
                    WAVES_balance = 0.0
                    balances = client.get_account_balance()
                    for balance in balances:
                        if balance['currency'] == 'WAVES':
                            WAVES_balance = float(balance['available'])

                    print('Saldo Conta Principal: %s' % WAVES_balance)

                    # TRANSFERE de CONTA PRINCIPAL para CONTA TRADING
                    print('\nTRANSFERINDO...PRINCIPAL/TRANDING')
                    client.transfer('WAVES', WAVES_balance, True)
                    print(f'Saldo Atualizado(Conta Principal): {WAVES_balance}')

                    time.sleep(2)  # espere até que a transferência seja concluída

                    # TIRA FEE
                    quantidade_comprandoHIT = float(quantidade_comprandoHIT) - float(feeWAVES_EXC)

                    # AÇÃO: VENDE na HIT
                    print(f'\nVENDENDO na HIT... {quantidade_comprandoHIT}')
                    session = requests.session()
                    session.auth = (public_key, secret)
                    orderData = {'symbol': 'wavesbtc', 'side': 'sell', 'quantity': quantidade_comprandoHIT, 'price': vendaWavesHIT}
                    r = session.post('https://api.hitbtc.com/api/2/order', data=orderData)
                    print(r.json())
                    print('Ordem de VENDA criada na HIT')

            # PRINCIPAL
            elif vendaWavesEXC < compraWavesHIT and compraWavesHIT - vendaWavesEXC < diferencaSatoshi_WAVES_BTC:
                print(f'\n>> AGUARDE << Venda na EXC está mais barata que compra na HIT, mas diferença abaixo de {diferencaSatoshi_WAVES_BTC:.8f} satoshi')

            # PRINCIPAL
            elif vendaWavesEXC > compraWavesHIT:
                print('\n>> AGUARDE << Sem oportunidades.')

            # PRINCIPAL
            else:
                print('\n>> AGUARDE << Valores iguais!!!')

            print('-' * 10)

            ########################################################################
            # PRINCIPAL
            print('\nVerificando: COMPRAR na HIT, para VENDER na EXC')
            if vendaWavesHIT < compraWavesEXC and compraWavesEXC - vendaWavesHIT > diferencaSatoshi_WAVES_BTC:
                print(f'>>> OPORTUNIDADE <<< VENDA na HIT mais barata que COMPRA na EXC e diferença acima de: {diferencaSatoshi_WAVES_BTC:.8f} satoshi')

                ###################################################
                #                  COMPRA na HIT:                 #
                ###################################################
                if float(quantidade_vendendoHIT) < float(quantidade_comprandoEXC) > minimaCompra_WAVES_BTC:
                    print(f'\nCOMPRANDO NA HIT... {quantidade_vendendoHIT}')

                    # AÇÃO: COMPRA
                    # ORDEM DE COMPRA NA HIT
                    session = requests.session()
                    session.auth = (public_key, secret)
                    orderData = {'symbol': 'wavesbtc', 'side': 'buy', 'quantity': quantidade_vendendoHIT, 'price': vendaWavesHIT}
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
                        # Obter saldo WAVES em trading
                        WAVES_ContaTrading = 0.0
                        balances = client.get_trading_balance()
                        for balance in balances:
                            if balance['currency'] == 'WAVES':
                                WAVES_ContaTrading = float(balance['available'])

                        # print(f'Saldo Conta Trading {WAVES_ContaTrading}')

                        # Obter saldo WAVES em Conta Principal
                        WAVES_ContaPrincipal = 0.0
                        balances = client.get_account_balance()
                        for balance in balances:
                            if balance['currency'] == 'WAVES':
                                WAVES_ContaPrincipal = float(balance['available'])

                        # print(f'Saldo Conta Principal {WAVES_ContaPrincipal}')

                        # TRANSFERE de CONTA TRADING para CONTA PRINCIPAL
                        print('\n>> TRANSFERINDO...TRANDING/PRINCIPAL <<')
                        client.transfer2('WAVES', WAVES_ContaTrading, 'exchangeToBank')

                        time.sleep(2)

                        # FAZ WITHDRAW PARA EXC
                        print(f'\nWITHDRAW PARA EXC... {quantidade_vendendoHIT}')
                        client = hitBOT.Client("https://api.hitbtc.com", public_key, secret)
                        faz_withdraw = hitBOT.Client.withdraw(client, 'WAVES', quantidade_vendendoHIT, addressWavesEXC)
                        print(faz_withdraw)

                        # TEMPO TRANSFERENCIA WAVES: 3 CONFIRMAÇÕES = 300 segundos
                        print('\n>> AGUARDANDO CONFIRMAÇÕES <<\n')
                        for contagem in range(300, -1, -1):
                            time.sleep(1)
                            print(contagem, end='.')

                        # TIRA FEE
                        quantidade_vendendoHIT = float(quantidade_vendendoHIT) - float(feeWAVES_HIT)

                        # AÇÃO: VENDE
                        print(f'\nVENDENDO NA EXC... {quantidade_vendendoHIT}')
                        # Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade
                        faz_vendaEXC = key_secretEXC.sell_limit('WAVES_BTC', vendaWavesHIT, quantidade_vendendoHIT)
                        print(faz_vendaEXC)

                elif float(quantidade_vendendoHIT) > float(quantidade_comprandoEXC) > minimaCompra_WAVES_BTC:
                    print(f'\nCOMPRANDO NA HIT... {quantidade_comprandoEXC}')

                    # AÇÃO: COMPRA
                    # ORDEM DE COMPRA NA HIT
                    session = requests.session()
                    session.auth = (public_key, secret)
                    orderData = {'symbol': 'wavesbtc', 'side': 'buy', 'quantity': quantidade_comprandoEXC, 'price': vendaWavesHIT}
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
                        # Obter saldo WAVES em trading
                        WAVES_ContaTrading = 0.0
                        balances = client.get_trading_balance()
                        for balance in balances:
                            if balance['currency'] == 'WAVES':
                                WAVES_ContaTrading = float(balance['available'])

                        # Obter saldo WAVES em Conta Principal
                        WAVES_ContaPrincipal = 0.0
                        balances = client.get_account_balance()
                        for balance in balances:
                            if balance['currency'] == 'WAVES':
                                WAVES_ContaPrincipal = float(balance['available'])

                        # TRANSFERE de CONTA TRADING para CONTA PRINCIPAL
                        print('\n>> TRANSFERINDO...TRANDING/PRINCIPAL <<')
                        client.transfer2('WAVES', WAVES_ContaTrading, 'exchangeToBank')

                        time.sleep(2)

                        # FAZ WITHDRAW PARA EXC
                        print(f'\nWITHDRAW PARA EXC... {quantidade_comprandoEXC}')
                        client = hitBOT.Client("https://api.hitbtc.com", public_key, secret)
                        faz_withdraw = hitBOT.Client.withdraw(client, 'WAVES', quantidade_comprandoEXC, addressWavesEXC)
                        print(faz_withdraw)

                        # TEMPO TRANSFERENCIA WAVES: 3 minutos = 180 segundos + 20s entras
                        print('\n>> AGUARDANDO CONFIRMAÇÕES <<\n')
                        for contagem in range(200, -1, -1):
                            time.sleep(1)
                            print(contagem, end='.')

                        # TIRA FEE
                        quantidade_comprandoEXC = float(quantidade_comprandoEXC) - float(feeWAVES_HIT)

                        # AÇÃO: VENDE
                        print(f'\nVENDENDO NA EXC... {quantidade_comprandoEXC}')
                        # Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade
                        faz_vendaEXC = key_secretEXC.sell_limit('WAVES_BTC', vendaWavesHIT, quantidade_comprandoEXC)
                        print(faz_vendaEXC)

            # PRINCIPAL
            elif vendaWavesHIT < compraWavesEXC and compraWavesEXC - vendaWavesHIT < diferencaSatoshi_WAVES_BTC:
                print(f'\n>> AGUARDE << - Venda na HIT está mais barata que compra na EXC, mas diferença abaixo de {diferencaSatoshi_WAVES_BTC:.8f} satoshi')

            # PRINCIPAL
            elif vendaWavesHIT > compraWavesEXC:
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
