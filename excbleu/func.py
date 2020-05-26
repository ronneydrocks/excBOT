import requests
import json
import bleuBot
import excBot
import time
import hmac
import hashlib
import datetime
import config


########################################################################
# EXC CRIPTO
########################################################################
emailEXC = config.emailEXC
keyEXC = config.keyEXC
secretEXC = config.secretEXC
key_secretEXC = excBot.excBot(keyEXC, secretEXC, nonce=True)

saldoInicial_EXC = config.saldoInicial_EXC

feeEXC = config.feeEXC
funMinima_EXC_BLEU_BTC_USDT = config.funMinima_EXC_BLEU_BTC_USDT
funMinima_EXC_BLEU_ETH_USDT = config.funMinima_EXC_BLEU_ETH_USDT
########################################################################
# BLEUTRADE
########################################################################
emailBLEU = config.emailBLEU
keyBLEU = config.keyBLEU
secretBLEU = config.secretBLEU
key_secretBLEU = bleuBot.bleuBot(keyBLEU, secretBLEU, nonce=True)

saldoInicial_BLEU = config.saldoInicial_BLEU

feeBLEU = config.feeBLEU
funMinima_BLEU_EXC_BTC_USDT = config.funMinima_BLEU_EXC_BTC_USDT
funMinima_BLEU_EXC_ETH_USDT = config.funMinima_BLEU_EXC_ETH_USDT
########################################################################
# GLOBAL
########################################################################
minima_ETH_BTC = config.minima_ETH_BTC
minima_ETH_USDT = config.minima_ETH_USDT
minima_LTC_USDT = config.minima_LTC_USDT
minima_LTC_BTC = config.minima_LTC_BTC
minima_BTC_USDT = config.minima_BTC_USDT
minima_DOGE_USDT = config.minima_DOGE_USDT
########################################################################
# FUNÇÕES
########################################################################
funCancelaTodasOrdens_EXC_BLEU = config.funCancelaTodasOrdens_EXC_BLEU
funAutoBalance_USDT = config.funAutoBalance_USDT         
funVendeMercadoAlta = config.funVendeMercadoAlta    

# funcVendaQuantidadeMinima = config.funcVendaQuantidadeMinima 
########################################################################
# ERRO
########################################################################
listaErro1 = config.listaErro1
listaErroMinima = config.listaErroMinima
########################################################################

########################################################################
# ETH
########################################################################
'''
url_vETH_BTC = config.urlGettickerEXC_ETH_BTC
r_vETH_BTC = requests.get(url_vETH_BTC)
j_vETH_BTC = json.loads(r_vETH_BTC.text)
vETH_BTC = j_vETH_BTC['result'][0]['Last']
'''
urlGetOrderBookEXC_BUY_ETH_BTC = config.urlGetOrderBookEXC_BUY_ETH_BTC
rEXC = requests.get(urlGetOrderBookEXC_BUY_ETH_BTC)
jEXC = json.loads(rEXC.text)
quantidade_comprandoEXC_ETH_BTC = jEXC['result']['buy'][0]['Quantity']
'''
urlGetOrderBookEXC_SELL_ETH_BTC = config.urlGetOrderBookEXC_SELL_ETH_BTC
rEXC = requests.get(urlGetOrderBookEXC_SELL_ETH_BTC)
jEXC = json.loads(rEXC.text)
quantidade_vendendoEXC_ETH_BTC = jEXC['result']['sell'][0]['Quantity']
'''
urlGettickerEXC = config.urlGettickerEXC_ETH_BTC
rEXC = requests.get(urlGettickerEXC)
jEXC = json.loads(rEXC.text)

# lastAtivoEXC_ETH_BTC = float(jEXC['result'][0]['Last'])
compraAtivoEXC_ETH_BTC = float(jEXC['result'][0]['Bid'])
# vendaAtivoEXC_ETH_BTC = float(jEXC['result'][0]['Ask'])

########################################################################

urlGetOrderBookEXC_BUY_ETH_USDT = config.urlGetOrderBookEXC_BUY_ETH_USDT
rEXC = requests.get(urlGetOrderBookEXC_BUY_ETH_USDT)
jEXC = json.loads(rEXC.text)
quantidade_comprandoEXC_ETH_USDT = jEXC['result']['buy'][0]['Quantity']
'''
urlGetOrderBookEXC_SELL_ETH_USDT = config.urlGetOrderBookEXC_SELL_ETH_USDT
rEXC = requests.get(urlGetOrderBookEXC_SELL_ETH_USDT)
jEXC = json.loads(rEXC.text)
quantidade_vendendoEXC_ETH_USDT = jEXC['result']['sell'][0]['Quantity']
'''
urlGettickerEXC = config.urlGettickerEXC_ETH_USDT
rEXC = requests.get(urlGettickerEXC)
jEXC = json.loads(rEXC.text)

# lastAtivoEXC_ETH_USDT = float(jEXC['result'][0]['Last'])
compraAtivoEXC_ETH_USDT = float(jEXC['result'][0]['Bid'])
# vendaAtivoEXC_ETH_USDT = float(jEXC['result'][0]['Ask'])

########################################################################
# LTC
########################################################################

urlGetOrderBookEXC_BUY_LTC_BTC = config.urlGetOrderBookEXC_BUY_LTC_BTC
rEXC = requests.get(urlGetOrderBookEXC_BUY_LTC_BTC)
jEXC = json.loads(rEXC.text)
quantidade_comprandoEXC_LTC_BTC = jEXC['result']['buy'][0]['Quantity']
'''
urlGetOrderBookEXC_SELL_LTC_BTC = config.urlGetOrderBookEXC_SELL_LTC_BTC
rEXC = requests.get(urlGetOrderBookEXC_SELL_LTC_BTC)
jEXC = json.loads(rEXC.text)
quantidade_vendendoEXC_LTC_BTC = jEXC['result']['sell'][0]['Quantity']
'''
urlGettickerEXC = config.urlGettickerEXC_LTC_BTC
rEXC = requests.get(urlGettickerEXC)
jEXC = json.loads(rEXC.text)

# lastAtivoEXC_LTC_BTC = float(jEXC['result'][0]['Last'])
compraAtivoEXC_LTC_BTC = float(jEXC['result'][0]['Bid'])
# vendaAtivoEXC_LTC_BTC = float(jEXC['result'][0]['Ask'])

########################################################################

urlGetOrderBookEXC_BUY_LTC_USDT = config.urlGetOrderBookEXC_BUY_LTC_USDT
rEXC = requests.get(urlGetOrderBookEXC_BUY_LTC_USDT)
jEXC = json.loads(rEXC.text)
quantidade_comprandoEXC_LTC_USDT = jEXC['result']['buy'][0]['Quantity']
'''
urlGetOrderBookEXC_SELL_LTC_USDT = config.urlGetOrderBookEXC_SELL_LTC_USDT
rEXC = requests.get(urlGetOrderBookEXC_SELL_LTC_USDT)
jEXC = json.loads(rEXC.text)
quantidade_vendendoEXC_LTC_USDT = jEXC['result']['sell'][0]['Quantity']
'''

urlGettickerEXC = config.urlGettickerEXC_LTC_USDT
rEXC = requests.get(urlGettickerEXC)
jEXC = json.loads(rEXC.text)

# lastAtivoEXC_LTC_USDT = float(jEXC['result'][0]['Last'])
compraAtivoEXC_LTC_USDT = float(jEXC['result'][0]['Bid'])
# vendaAtivoEXC_LTC_USDT = float(jEXC['result'][0]['Ask'])

########################################################################


########################################################################
# LINHA PADRÃO (50)
########################################################################


def linha50():
    print('=' * 50)
########################################################################

########################################################################
# SALDO: EXC
########################################################################


def saldo_EXC():
    # DATA/HORA
    dataEhora = datetime.datetime.now()
    dataEhora = dataEhora.strftime('%d/%m/%Y %H:%M')
    linha50()
    print(f'{dataEhora}')

    # TELEGRAM
    config.mensagem_telegram('=' * 50)

    #####################################
    # 1BTC/BRL
    urlBTC_BRL = config.urlBTC_BRL
    r = requests.get(urlBTC_BRL)
    j = json.loads(r.text)
    # print(j)
    BTC_BRL = j['bitcoin']['brl']
    # print(BTC_BRL)
    ######################################################################
    print('=' * 50)
    print('> EXC <')

    # Consulta informações Balances
    rBalances = key_secretEXC.get_balances()
    resposta_rBalances = rBalances['result']
    # print(resposta_rBalances)

    resposta_rBalances = str(resposta_rBalances)
    if resposta_rBalances == 'ERR_LOGIN_REQUIRED':
        print('Não configurado')

    else:
        # Quantidade de Ativos na EXC
        nATIVOS = len(rBalances['result'])
        # print(nATIVOS)

        c = 0
        somaEqBTC_EXC = 0

        print('Ativo / Saldo Total / Saldo Disponível / Saldo em BTC\n')
        while c < nATIVOS:
            ATIVO = rBalances['result'][c]['Asset']
            balanceATIVO = rBalances['result'][c]['Balance']
            eATIVO = rBalances['result'][c]['BtcEquivalent']
            dATIVO = rBalances['result'][c]['Available']
            print(f'Saldo: {balanceATIVO:.8f} / {dATIVO:.8f} {ATIVO} = {eATIVO:.8f} BTC')

            # SOMA SALDO EQUIVALENTE EM BTC
            somaEqBTC_EXC += eATIVO
            c += 1

        ######################################################################
        #####################################################
        ######### TEMP - ADICIONAR EQUIVALENTE USDT #########
        recebeSaldoUSDT_EXC = key_secretEXC.get_balance('USDT')
        saldoUSDT_EXC = recebeSaldoUSDT_EXC['result'][0]['Balance']
        saldoUSDT_EXC = float(saldoUSDT_EXC)
        # print(saldoUSDT_EXC)

        # 1BTC/USD
        recebePrecoBTC_USD = config.coinGecko_BTC_USD
        r = requests.get(recebePrecoBTC_USD)
        j = json.loads(r.text)
        # print(j)
        precoBTC_USD = j['bitcoin']['usd']
        precoBTC_USD = float(precoBTC_USD)
        # print(precoBTC_USD)

        transformaSaldo = saldoUSDT_EXC / precoBTC_USD
        # print(transformaSaldo)

        somaEqBTC_EXC = somaEqBTC_EXC + transformaSaldo

        #####################################################
        print('=' * 50)
        print(f'Saldo inicial na EXC: {saldoInicial_EXC:.8f} BTC')
        print(f'Saldo atual na EXC: {somaEqBTC_EXC:.8f} BTC')

        # TELEGRAM
        config.mensagem_telegram(f'Saldo inicial na EXC: {saldoInicial_EXC:.8f} BTC \nSaldo atual na EXC: {somaEqBTC_EXC:.8f} BTC')
        print('=' * 50)
    ########################################################################

########################################################################
# SALDO: BLEU
########################################################################


def saldo_BLEU():
    # DATA/HORA
    dataEhora = datetime.datetime.now()
    dataEhora = dataEhora.strftime('%d/%m/%Y %H:%M')
    linha50()
    print(f'{dataEhora}')

    # TELEGRAM
    config.mensagem_telegram('=' * 50)

    #####################################
    # 1BTC/BRL
    urlBTC_BRL = config.urlBTC_BRL
    r = requests.get(urlBTC_BRL)
    j = json.loads(r.text)
    # print(j)
    BTC_BRL = j['bitcoin']['brl']
    # print(BTC_BRL)
    ######################################################################
    print('=' * 50)
    print('> BLEU <')

    # Consulta informações Balances
    rBalances = key_secretBLEU.get_balances()
    resposta_rBalances = rBalances['result']
    # print(resposta_rBalances)

    resposta_rBalances = str(resposta_rBalances)
    if resposta_rBalances == 'ERR_LOGIN_REQUIRED':
        print('Não configurado')

    else:
        # Quantidade de Ativos na BLEU
        nATIVOS = len(rBalances['result'])
        # print(nATIVOS)

        c = 0
        somaEqBTC_BLEU = 0

        print('Ativo / Saldo Total / Saldo Disponível / Saldo em BTC\n')
        while c < nATIVOS:
            ATIVO = rBalances['result'][c]['Asset']
            balanceATIVO = rBalances['result'][c]['Balance']
            eATIVO = rBalances['result'][c]['BtcEquivalent']
            dATIVO = rBalances['result'][c]['Available']
            print(f'Saldo: {balanceATIVO:.8f} / {dATIVO:.8f} {ATIVO} = {eATIVO:.8f} BTC')

            # SOMA SALDO EQUIVALENTE EM BTC
            somaEqBTC_BLEU += eATIVO
            c += 1

        ######################################################################
        #####################################################
        ######### TEMP - ADICIONAR EQUIVALENTE USDT #########
        recebeSaldoUSDT_BLEU = key_secretBLEU.get_balance('USDT')
        saldoUSDT_BLEU = recebeSaldoUSDT_BLEU['result'][0]['Balance']
        saldoUSDT_BLEU = float(saldoUSDT_BLEU)
        # print(saldoUSDT_BLEU)

        # 1BTC/USD
        recebePrecoBTC_USD = config.coinGecko_BTC_USD
        r = requests.get(recebePrecoBTC_USD)
        j = json.loads(r.text)
        # print(j)
        precoBTC_USD = j['bitcoin']['usd']
        precoBTC_USD = float(precoBTC_USD)
        # print(precoBTC_USD)

        transformaSaldo = saldoUSDT_BLEU / precoBTC_USD
        # print(transformaSaldo)

        somaEqBTC_BLEU = somaEqBTC_BLEU + transformaSaldo

        #####################################################
        print('=' * 50)
        print(f'Saldo inicial na BLEU: {saldoInicial_BLEU:.8f} BTC')
        print(f'Saldo atual na BLEU: {somaEqBTC_BLEU:.8f} BTC')

        # TELEGRAM
        config.mensagem_telegram(f'Saldo inicial na BLEU: {saldoInicial_BLEU:.8f} BTC \nSaldo atual na BLEU: {somaEqBTC_BLEU:.8f} BTC')
        print('=' * 50)
########################################################################

########################################################################
#               FUNÇÃO: CANCELA ORDENS ABERTAS
########################################################################


def cancelaTodasOrdens_EXC_BLEU():
    if funCancelaTodasOrdens_EXC_BLEU == 1:
        print('\n>> ORDENS:')
        ########################################################################
        # EXC: Verifica ordens abertar
        ########################################################################
        getOpenOrder = key_secretEXC.get_open_orders()
        if not getOpenOrder['result']:
            print('EXC: SEM ORDENS ABERTAS')
        else:
            nOpenOrder = len(getOpenOrder['result'])
            c = 0
            while c < nOpenOrder:
                OrderID = getOpenOrder['result'][c]['OrderID']
                cancelaOrder = key_secretEXC.cancel(OrderID)
                c += 1

        time.sleep(0.5)
        
        ########################################################################
        # BLEU: Verifica ordens abertar
        ########################################################################
        getOpenOrder = key_secretBLEU.get_open_orders()
        if not getOpenOrder['result']:
            print('BLEU: SEM ORDENS ABERTAS')
        else:
            nOpenOrder = len(getOpenOrder['result'])
            c = 0
            while c < nOpenOrder:
                OrderID = getOpenOrder['result'][c]['OrderID']
                cancelaOrder = key_secretEXC.cancel(OrderID)
                c += 1

        time.sleep(0.5)        

    elif funCancelaTodasOrdens_EXC_BLEU == 0:
        print(f'>> CANCELA ORDENS: Função desativada!')

    else:
        print(f'Por favor, configure a função: CANCELA ORDENS\nOpções:\n1 = Ativado\n2 = Desativado')
    
########################################################################


def vendeMerdadoAlta():
    ##########################################################
    #               FUNÇÃO: VENDE NO MERCADO EM ALTA
    ##########################################################
    if funVendeMercadoAlta == 1:
        ##########################################################
        print('\n>> CHANGE 24H:')

        urlCoinGecko_ATIVO_Change24h = config.urlCoinGecko_ATIVO_Change24h
        r = requests.get(urlCoinGecko_ATIVO_Change24h)
        j = json.loads(r.text)
        print(j)

        time.sleep(0.5)        

    elif funVendeMercadoAlta == 0:
        print(f'>> VENDE NO MERCADO EM ALTA: Função desativada!')

    else:
        print(f'Por favor, configure a função: VENDE NO MERCADO EM ALTA\nOpções:\n1 = Ativado\n0 = Desativado')    

    
########################################################################



def transfer_BLEU_EXC(ATIVO_BLEU):
    linha50()

    # exchangeBLEU = 1
    # exchangeEXC = 2
    email_destino = config.emailEXC

    print(f'Transfere {ATIVO_BLEU} da BLEU para EXC.')

    recebeSaldoATIVO_BLEU = key_secretBLEU.get_balance(ATIVO_BLEU)
    # print(recebeSaldoATIVO_BLEU)

    saldoATIVO_BLEU = str(recebeSaldoATIVO_BLEU['result'][0]['Balance'])
    aSaldoATIVO_BLEU = str(recebeSaldoATIVO_BLEU['result'][0]['Available'])
    print(f'\nSaldo Total {ATIVO_BLEU}: {saldoATIVO_BLEU}\nSaldo Disponível {ATIVO_BLEU}: {aSaldoATIVO_BLEU}')

    print(f'\n>> TRANSFERE... {aSaldoATIVO_BLEU} {ATIVO_BLEU}')

    urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
        int(
            time.time())) + '&asset=' + ATIVO_BLEU + '&quantity=' + aSaldoATIVO_BLEU + '&exchangeto=2&' + 'accountto=' + email_destino

    # sign
    sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
    # Adding sign to header
    headers = {'apisign': sign}
    # Make request
    response = requests.get(url=urlDirecttransferBLEU, headers=headers)
    # print(urlDirecttransferBLEU)
    print(response.json())
########################################################################


def vendeMercadoNaAlta_f2():

    print('#' * 20)
    print('CHANGE 24h\n')
    datetime.time(1)

    # USD
    urlCoinGecko_BTC_Change24h = config.urlCoinGecko_BTC_Change24h
    r = requests.get(urlCoinGecko_BTC_Change24h)
    j = json.loads(r.text)
    BTC_usd_24h_change = j['bitcoin']['usd_24h_change']
    BTC_usd_price = j['bitcoin']['usd']
    print(f'BTC: ${BTC_usd_price:.2f} / Change: {BTC_usd_24h_change:.2f}')

    urlCoinGecko_ETH_Change24h = config.urlCoinGecko_ETH_Change24h
    r = requests.get(urlCoinGecko_ETH_Change24h)
    j = json.loads(r.text)
    ETH_usd_24h_change = j['ethereum']['usd_24h_change']
    ETH_usd_price = j['ethereum']['usd']
    print(f'ETH: ${ETH_usd_price:.2f} / Change:  {ETH_usd_24h_change:.2f}')

    urlCoinGecko_LTC_Change24h = config.urlCoinGecko_LTC_Change24h
    r = requests.get(urlCoinGecko_LTC_Change24h)
    j = json.loads(r.text)
    LTC_usd_24h_change = j['litecoin']['usd_24h_change']
    LTC_usd_price = j['litecoin']['usd']
    print(f'LTC: ${LTC_usd_price:.2f} / Change: {LTC_usd_24h_change:.2f}')

    print('---')

    # BTC
    urlCoinGecko_ETH_BTC_Change24h = config.urlCoinGecko_ETH_BTC_Change24h
    r = requests.get(urlCoinGecko_ETH_BTC_Change24h)
    j = json.loads(r.text)
    ETH_BTC_24h_change = j['ethereum']['btc_24h_change']
    ETH_BTC_price = j['ethereum']['btc']
    print(f'ETH: {ETH_BTC_price:.8f} / Change: {ETH_BTC_24h_change:.2f}')

    urlCoinGecko_LTC_BTC_Change24h = config.urlCoinGecko_LTC_BTC_Change24h
    r = requests.get(urlCoinGecko_LTC_BTC_Change24h)
    j = json.loads(r.text)
    LTC_BTC_24h_change = j['litecoin']['btc_24h_change']
    LTC_BTC_price = j['litecoin']['btc']
    print(f'LTC: {LTC_BTC_price:.8f} / Change: {LTC_BTC_24h_change:.2f}')

    #########################################################################
    print('#' * 20)
    porcentagemDesejada = config.porcentagemDesejada
    print(f'Porcentagem desejada: {porcentagemDesejada}%')
    print('#' * 20)
    #########################################################################
    porcentagemParaCompra = config.porcentagemParaCompra
    print(f'Porcentagem do preço: {porcentagemParaCompra}%')
    print('#' * 20)

    porcentagemEXC_BTC_USDT = porcentagemParaCompra / 100 * BTC_usd_price
    print(f'{porcentagemParaCompra}% de {BTC_usd_price} é ${porcentagemEXC_BTC_USDT:.2f}')

    porcentagemEXC_ETH_USDT = porcentagemParaCompra / 100 * ETH_usd_price
    print(f'{porcentagemParaCompra}% de {ETH_usd_price} é ${porcentagemEXC_ETH_USDT:.2f}')

    porcentagemEXC_LTC_USDT = porcentagemParaCompra / 100 * LTC_usd_price
    print(f'{porcentagemParaCompra}% de {LTC_usd_price} é ${porcentagemEXC_LTC_USDT:.2f}')

    print('---')

    porcentagemEXC_ETH_BTC = porcentagemParaCompra / 100 * ETH_BTC_price
    print(f'{porcentagemParaCompra}% de {ETH_BTC_price} é {porcentagemEXC_ETH_BTC:.8f} BTC')

    porcentagemEXC_LTC_BTC = porcentagemParaCompra / 100 * LTC_BTC_price
    print(f'{porcentagemParaCompra}% de {LTC_BTC_price} é {porcentagemEXC_LTC_BTC:.8f} BTC')

    #########################################################################
    print('#' * 20)

    dif_BTC_USDT = (BTC_usd_price - porcentagemEXC_BTC_USDT)
    print(f'BTC {BTC_usd_price:.8f} - {porcentagemParaCompra}% = {dif_BTC_USDT:.8f}')

    dif_ETH_USDT = (ETH_usd_price - porcentagemEXC_ETH_USDT)
    print(f'ETH {ETH_usd_price:.8f} - {porcentagemParaCompra}% = {dif_ETH_USDT:.8f}')

    dif_LTC_USDT = (LTC_usd_price - porcentagemEXC_LTC_USDT)
    print(f'LTC {LTC_usd_price:.8f} - {porcentagemParaCompra}% = {dif_LTC_USDT:.8f}')

    print('---')

    dif_ETH_BTC = (ETH_BTC_price - porcentagemEXC_ETH_BTC)
    print(f'ETH {ETH_BTC_price:.8f} - {porcentagemParaCompra}% = {dif_ETH_BTC:.8f}')

    dif_LTC_BTC = (LTC_BTC_price - porcentagemEXC_LTC_BTC)
    print(f'LTC {LTC_BTC_price:.8f} - {porcentagemParaCompra}% = {dif_LTC_BTC:.8f}')
    #########################################################################
    print('#' * 20)
    print('\nATIVO: ETH')

    print('\n>> PROCURANDO << Oportunidade em USD...\n')
    if ETH_usd_24h_change > porcentagemDesejada and compraAtivoEXC_ETH_USDT >= dif_ETH_USDT:

        print(f'Preço: {compraAtivoEXC_ETH_USDT} ETH_USDT - Quantidade: {quantidade_comprandoEXC_ETH_USDT} ETH')

        compraAtivoEXC_ETH_USDT_2 = compraAtivoEXC_ETH_USDT

        while compraAtivoEXC_ETH_USDT_2 >= dif_ETH_USDT:

            urlGettickerEXC = config.urlGettickerEXC_ETH_USDT
            r = requests.get(urlGettickerEXC)
            j = json.loads(r.text)
            compraAtivoEXC_ETH_USDT_2 = float(j['result'][0]['Bid'])

            print(f'\nETH_USDT: Vendendo na EXC... {quantidade_comprandoEXC_ETH_USDT} por {compraAtivoEXC_ETH_USDT_2:.8f}')
            faz_vendaEXC = key_secretEXC.sell_limit('ETH_USDT', compraAtivoEXC_ETH_USDT_2, quantidade_comprandoEXC_ETH_USDT)
            print(f'Resposta: \n{faz_vendaEXC}')

            respostaResult = faz_vendaEXC['result']

            if respostaResult == 'ERR_INSUFICIENT_BALANCE':
                print('>> ERRO << Saldo insuficiente')

                print(f'\nETH_USDT: Vendendo QUANTIDADE MÍNINA na EXC...{minima_ETH_USDT}\n')
                faz_vendaEXC = key_secretEXC.sell_limit('ETH_USDT', compraAtivoEXC_ETH_USDT_2, minima_ETH_USDT)
                print(f'Resposta: \n{faz_vendaEXC}')

            elif respostaResult == 'ERR_LOW_VOLUME':
                print('\n>> ERRO << Valor da ordem baixo.\nExecutando ação, VENDA MÍNIMA!')

                print(f'\nETH_USDT: Vendendo QUANTIDADE MÍNINA na EXC...{minima_ETH_USDT}\n')
                faz_vendaEXC = key_secretEXC.sell_limit('ETH_USDT', compraAtivoEXC_ETH_USDT_2, minima_ETH_USDT)
                print(f'Resposta: \n{faz_vendaEXC}')

    else:
        print('Aguarde, sem oportunidades\n')

    print('\n>> PROCURANDO << Oportunidade em BTC...\n')

    if ETH_BTC_24h_change > porcentagemDesejada and compraAtivoEXC_ETH_BTC >= dif_ETH_BTC:

        print(f'Preço: {compraAtivoEXC_ETH_BTC} ETH_BTC - Quantidade: {quantidade_comprandoEXC_ETH_BTC} ETH')

        compraAtivoEXC_ETH_BTC_2 = compraAtivoEXC_ETH_BTC
        while compraAtivoEXC_ETH_BTC_2 >= dif_ETH_BTC:

            urlGettickerEXC = config.urlGettickerEXC_ETH_BTC
            r = requests.get(urlGettickerEXC)
            j = json.loads(r.text)
            compraAtivoEXC_ETH_BTC_2 = float(j['result'][0]['Bid'])

            print(f'\nETH_BTC: Vendendo na EXC... {quantidade_comprandoEXC_ETH_BTC} por {compraAtivoEXC_ETH_BTC_2:.8f}')
            faz_vendaEXC = key_secretEXC.sell_limit('ETH_BTC', compraAtivoEXC_ETH_BTC_2, quantidade_comprandoEXC_ETH_BTC)
            print(f'Resposta: \n{faz_vendaEXC}')

            respostaResult = faz_vendaEXC['result']

            if respostaResult == 'ERR_INSUFICIENT_BALANCE':
                print('>> ERRO << Saldo insuficiente')

                print(f'\nETH_BTC: Vendendo QUANTIDADE MÍNINA na EXC...{minima_ETH_BTC}\n')
                faz_vendaEXC = key_secretEXC.sell_limit('ETH_BTC', compraAtivoEXC_ETH_BTC_2, minima_ETH_BTC)
                print(f'Resposta: \n{faz_vendaEXC}')

            elif respostaResult == 'ERR_LOW_VOLUME':
                print('\n>> ERRO << Valor da ordem baixo.\nExecutando ação, VENDA MÍNIMA!')

                print(f'\nETH_BTC: Vendendo QUANTIDADE MÍNINA na EXC...{minima_ETH_BTC}\n')
                faz_vendaEXC = key_secretEXC.sell_limit('ETH_BTC', compraAtivoEXC_ETH_BTC_2, minima_ETH_BTC)
                print(f'Resposta: \n{faz_vendaEXC}')



    else:
        print('Aguarde, sem oportunidades\n')

    #########################################################################
    #########################################################################
    print('#' * 20)
    print('\n>> ATIVO: LTC')

    print('\n>> PROCURANDO << Oportunidade em USD...\n')
    if LTC_usd_24h_change > porcentagemDesejada and compraAtivoEXC_LTC_USDT >= dif_LTC_USDT:

        print(f'Preço: {compraAtivoEXC_LTC_USDT} LTC_USDT - Quantidade: {quantidade_comprandoEXC_LTC_USDT} LTC')

        compraAtivoEXC_LTC_USDT_2 = compraAtivoEXC_LTC_USDT

        while compraAtivoEXC_LTC_USDT_2 >= dif_LTC_USDT:

            urlGettickerEXC = config.urlGettickerEXC_LTC_USDT
            r = requests.get(urlGettickerEXC)
            j = json.loads(r.text)
            compraAtivoEXC_LTC_USDT_2 = float(j['result'][0]['Bid'])

            print(f'\nLTC_USDT: Vendendo na EXC... {quantidade_comprandoEXC_LTC_USDT} por {compraAtivoEXC_LTC_USDT_2:.8f}')
            faz_vendaEXC = key_secretEXC.sell_limit('LTC_USDT', compraAtivoEXC_LTC_USDT_2, quantidade_comprandoEXC_LTC_USDT)
            print(f'Resposta: \n{faz_vendaEXC}')

            respostaResult = faz_vendaEXC['result']

            if respostaResult == 'ERR_INSUFICIENT_BALANCE':
                print('>> ERRO << Saldo insuficiente')

                print(f'\nLTC_USDT: Vendendo QUANTIDADE MÍNINA na EXC...{minima_LTC_USDT}\n')
                faz_vendaEXC = key_secretEXC.sell_limit('ETH_USDT', compraAtivoEXC_LTC_USDT_2, minima_LTC_USDT)
                print(f'Resposta: \n{faz_vendaEXC}')

            elif respostaResult == 'ERR_LOW_VOLUME':
                print('\n>> ERRO << Valor da ordem baixo.\nExecutando ação, VENDA MÍNIMA!')

                print(f'\nLTC_USDT: Vendendo QUANTIDADE MÍNINA na EXC...{minima_LTC_USDT}\n')
                faz_vendaEXC = key_secretEXC.sell_limit('LTC_USDT', compraAtivoEXC_LTC_USDT_2, minima_LTC_USDT)
                print(f'Resposta: \n{faz_vendaEXC}')


    else:
        print('Aguarde, sem oportunidades\n')

    print('\n>> PROCURANDO << Oportunidade em BTC...\n')
    if LTC_BTC_24h_change > porcentagemDesejada and compraAtivoEXC_LTC_BTC >= dif_LTC_BTC:

        print(f'Preço: {compraAtivoEXC_LTC_BTC} LTC_BTC - Quantidade: {quantidade_comprandoEXC_LTC_BTC} LTC')

        compraAtivoEXC_LTC_BTC_2 = compraAtivoEXC_LTC_BTC

        while compraAtivoEXC_LTC_BTC_2 >= dif_LTC_BTC:

            urlGettickerEXC = config.urlGettickerEXC_LTC_BTC
            r = requests.get(urlGettickerEXC)
            j = json.loads(r.text)
            compraAtivoEXC_LTC_BTC_2 = float(j['result'][0]['Bid'])

            print(f'\nLTC_BTC: Vendendo na EXC... {quantidade_comprandoEXC_LTC_BTC} por {compraAtivoEXC_LTC_BTC_2:.8f}')
            faz_vendaEXC = key_secretEXC.sell_limit('LTC_BTC', compraAtivoEXC_LTC_BTC_2, quantidade_comprandoEXC_LTC_BTC)
            print(f'Resposta: \n{faz_vendaEXC}')

            respostaResult = faz_vendaEXC['result']

            if respostaResult == 'ERR_INSUFICIENT_BALANCE':
                print('>> ERRO << Saldo insuficiente')

                print(f'\nLTC_BTC: Vendendo QUANTIDADE MÍNINA na EXC...{minima_LTC_BTC}\n')
                faz_vendaEXC = key_secretEXC.sell_limit('ETH_BTC', compraAtivoEXC_LTC_BTC_2, minima_LTC_BTC)
                print(f'Resposta: \n{faz_vendaEXC}')

            elif respostaResult == 'ERR_LOW_VOLUME':
                print('\n>> ERRO << Valor da ordem baixo.\nExecutando ação, VENDA MÍNIMA!')

                print(f'\nLTC_BTC: Vendendo QUANTIDADE MÍNINA na EXC...{minima_LTC_BTC}\n')
                faz_vendaEXC = key_secretEXC.sell_limit('LTC_BTC', compraAtivoEXC_LTC_BTC_2, minima_LTC_BTC)
                print(f'Resposta: \n{faz_vendaEXC}')


    else:
        print('Aguarde, sem oportunidades\n')

    #########################################################################
    print('#' * 20)

    return

########################################################################


def vendaPrecoMercado():
    ########################################################################
    # ETH_USDT
    ########################################################################

    print(f'\nPreço: {compraAtivoEXC_ETH_USDT} ETH_USDT - Quantidade: {quantidade_comprandoEXC_ETH_USDT} ETH\n')
    print('\nETH_USDT: Vendendo na EXC...\n')
    faz_vendaEXC = key_secretEXC.sell_limit('ETH_USDT', compraAtivoEXC_ETH_USDT, quantidade_comprandoEXC_ETH_USDT)
    print(f'Resposta: \n{faz_vendaEXC}')

    respostaResult = faz_vendaEXC['result']

    if respostaResult == 'ERR_INSUFICIENT_BALANCE':
        print('>> ERRO << Saldo insuficiente')

        print(f'\nETH_USDT: Vendendo QUANTIDADE MÍNINA na EXC...{minima_ETH_USDT}\n')
        faz_vendaEXC = key_secretEXC.sell_limit('ETH_USDT', compraAtivoEXC_ETH_USDT, minima_ETH_USDT)
        print(f'Resposta: \n{faz_vendaEXC}')

    elif respostaResult == 'ERR_LOW_VOLUME':
        print('\n>> ERRO << Valor da ordem baixo.\nExecutando ação, VENDA MÍNIMA!')

        print(f'\nETH_USDT: Vendendo QUANTIDADE MÍNINA na EXC...{minima_ETH_USDT}\n')
        faz_vendaEXC = key_secretEXC.sell_limit('ETH_USDT', compraAtivoEXC_ETH_USDT, minima_ETH_USDT)
        print(f'Resposta: \n{faz_vendaEXC}')

    ########################################################################
    ########################################################################

    ########################################################################
    # ETH_BTC
    ########################################################################

    print(f'\nPreço: {compraAtivoEXC_ETH_BTC} ETH_BTC - Quantidade: {quantidade_comprandoEXC_ETH_BTC} ETH\n')
    print('\nETH_BTC: Vendendo na EXC...\n')
    faz_vendaEXC = key_secretEXC.sell_limit('ETH_BTC', compraAtivoEXC_ETH_BTC, quantidade_comprandoEXC_ETH_BTC)
    print(f'Resposta: \n{faz_vendaEXC}')

    respostaResult = faz_vendaEXC['result']

    if respostaResult == 'ERR_INSUFICIENT_BALANCE':
        print('>> ERRO << Saldo insuficiente')

        print(f'\nETH_BTC: Vendendo QUANTIDADE MÍNINA na EXC...{minima_ETH_BTC}\n')
        faz_vendaEXC = key_secretEXC.sell_limit('ETH_BTC', compraAtivoEXC_ETH_BTC, minima_ETH_BTC)
        print(f'Resposta: \n{faz_vendaEXC}')

    elif respostaResult == 'ERR_LOW_VOLUME':
        print('\n>> ERRO << Valor da ordem baixo.\nExecutando ação, VENDA MÍNIMA!')

        print(f'\nETH_BTC: Vendendo QUANTIDADE MÍNINA na EXC...{minima_ETH_BTC}\n')
        faz_vendaEXC = key_secretEXC.sell_limit('ETH_BTC', compraAtivoEXC_ETH_BTC, minima_ETH_BTC)
        print(f'Resposta: \n{faz_vendaEXC}')

    ########################################################################
    ########################################################################

    linha50()
    print('\nATIVO: LTC')

    print(f'\nPreço: {compraAtivoEXC_LTC_USDT} LTC_USDT - Quantidade: {quantidade_comprandoEXC_LTC_USDT} LTC\n')
    print('\nLTC_USDT: Vendendo na EXC...\n')
    faz_vendaEXC = key_secretEXC.sell_limit('LTC_USDT', compraAtivoEXC_LTC_USDT, quantidade_comprandoEXC_LTC_USDT)
    print(f'Resposta: \n{faz_vendaEXC}')

    print(f'\nPreço: {compraAtivoEXC_LTC_BTC} LTC_BTC - Quantidade: {quantidade_comprandoEXC_LTC_BTC} LTC\n')
    print('\nLTC_BTC: Vendendo na EXC...\n')
    faz_vendaEXC = key_secretEXC.sell_limit('LTC_BTC', compraAtivoEXC_LTC_BTC, quantidade_comprandoEXC_LTC_BTC)
    print(f'Resposta: \n{faz_vendaEXC}')

    linha50()
    return

########################################################################


def vendaMinimaEXC_BTC_USDT():
    urlGettickerEXC = config.urlGettickerEXC_BTC_USDT
    rEXC = requests.get(urlGettickerEXC)
    jEXC = json.loads(rEXC.text)
    compraAtivoEXC_BTC_USDT = float(jEXC['result'][0]['Bid'])

    print('Vendendo na EXC...\n')
    faz_vendaMinimaEXC = key_secretEXC.sell_limit('BTC_USDT', compraAtivoEXC_BTC_USDT, minima_BTC_USDT)
    print(f'Resposta: \n{faz_vendaMinimaEXC}')
########################################################################


def vendaMinimaEXC_ETH_USDT():
    urlGettickerEXC = config.urlGettickerEXC_ETH_USDT
    rEXC = requests.get(urlGettickerEXC)
    jEXC = json.loads(rEXC.text)
    compraAtivoEXC_ETH_USDT = float(jEXC['result'][0]['Bid'])

    print('Vendendo na EXC...\n')
    faz_vendaMinimaEXC = key_secretEXC.sell_limit('ETH_USDT', compraAtivoEXC_ETH_USDT, minima_ETH_USDT)
    print(f'Resposta: \n{faz_vendaMinimaEXC}')
########################################################################


def vendaMinimaEXC_LTC_USDT():
    urlGettickerEXC = config.urlGettickerEXC_LTC_USDT
    rEXC = requests.get(urlGettickerEXC)
    jEXC = json.loads(rEXC.text)
    compraAtivoEXC_LTC_USDT = float(jEXC['result'][0]['Bid'])

    print('Vendendo na EXC...\n')
    faz_vendaMinimaEXC = key_secretEXC.sell_limit('LTC_USDT', compraAtivoEXC_LTC_USDT, minima_LTC_USDT)
    print(f'Resposta: \n{faz_vendaMinimaEXC}')
    
########################################################################


def vendaMinimaEXC_DOGE_USDT():
    urlGettickerEXC = config.urlGettickerEXC_DOGE_USDT
    rEXC = requests.get(urlGettickerEXC)
    jEXC = json.loads(rEXC.text)
    compraAtivoEXC_DOGE_USDT = float(jEXC['result'][0]['Bid'])

    print('Vendendo na EXC...\n')
    faz_vendaMinimaEXC = key_secretEXC.sell_limit('DOGE_USDT', compraAtivoEXC_DOGE_USDT, minima_DOGE_USDT)
    print(f'Resposta: \n{faz_vendaMinimaEXC}')
    
#########################################################################


def vendaMinimaEXC_ETH_BTC():
    urlGettickerEXC = config.urlGettickerEXC_ETH_BTC
    rEXC = requests.get(urlGettickerEXC)
    jEXC = json.loads(rEXC.text)
    compraAtivoEXC_ETH_BTC = float(jEXC['result'][0]['Bid'])

    print('Vendendo na EXC...\n')
    faz_vendaMinimaEXC = key_secretEXC.sell_limit('ETH_BTC', compraAtivoEXC_ETH_BTC, minima_ETH_BTC)
    print(f'Resposta: \n{faz_vendaMinimaEXC}')
    
########################################################################

########################################################################
# FUNÇÃO: AUTO BALANCE (USDT)
########################################################################


def autoBalance_USDT():

    if funAutoBalance_USDT == 1:
        print('---')
        print('\n>>> EQUILIBRANDO SALDO <<<')
    
        # Aguarda 2 segundos
        time.sleep(2)
    
        saldoUSDT_BLEU = key_secretBLEU.get_balance('USDT')
        saldoUSDT_BLEU = float(saldoUSDT_BLEU['result'][0]['Balance'])
        print(f'Saldo na BLEU: {saldoUSDT_BLEU:.8f} USDT')
    
        saldoUSDT_EXC = key_secretEXC.get_balance('USDT')
        saldoUSDT_EXC = float(saldoUSDT_EXC['result'][0]['Balance'])
        print(f'Saldo na EXC: {saldoUSDT_EXC:.8f} USDT')
    
        if saldoUSDT_BLEU > saldoUSDT_EXC:
            print('\n>> ATENÇÃO<< Transferindo da BLEU para EXC\n')
    
            # Aguarda 2 segundos
            time.sleep(2)
    
            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########
            equilibraSaldo = (saldoUSDT_EXC + saldoUSDT_BLEU) / 2
            equilibraSaldo = str(equilibraSaldo)
            print(f'Transferindo... {equilibraSaldo} USDT')
    
            urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
                int(
                    time.time())) + '&asset=USDT&quantity=' + equilibraSaldo + '&exchangeto=2&' + 'accountto=' + emailEXC
    
            # sign
            sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(),
                            hashlib.sha512).hexdigest()
            # Adding sign to header
            headers = {'apisign': sign}
            # Make request
            response = requests.get(url=urlDirecttransferBLEU, headers=headers)
            print(response.json())
    
            # Mostra saldo atualizado após transferência de equilíbrio
            print(f'Saldo atualizado na EXC: {saldoUSDT_EXC:.8f} USDT')
            print(f'Saldo atualizado na BLEU: {saldoUSDT_BLEU:.8f} USDT')
    
            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########
    
        elif saldoUSDT_BLEU < saldoUSDT_EXC:
            print('\n>> ATENÇÃO << Transferindo da EXC para BLEU\n')
    
            # Aguarda 2 segundos
            time.sleep(2)
    
            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########
    
            equilibraSaldo = (saldoUSDT_BLEU + saldoUSDT_EXC) / 2
            equilibraSaldo = str(equilibraSaldo)
            print(f'Transferindo... {equilibraSaldo} USDT')
    
            urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
                int(
                    time.time())) + '&asset=USDT&quantity=' + equilibraSaldo + '&exchangeto=1&' + 'accountto=' + emailBLEU
    
            # sign
            sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(),
                            hashlib.sha512).hexdigest()
            # Adding sign to header
            headers = {'apisign': sign}
            # Make request
            response = requests.get(url=urlDirecttransferEXC, headers=headers)
            print(response.json())
    
            # Mostra saldo atualizado após transferência de equilíbrio
            print(f'Saldo atualizado na EXC: {saldoUSDT_EXC:.8f} USDT')
            print(f'Saldo atualizado na BLEU: {saldoUSDT_BLEU:.8f} USDT')
    
            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########
    
        else:
            print('>> SEM TRANSFERÊNCIA << Saldos iguais, ')
    
        print('---')
    
    elif funAutoBalance_USDT == 0:
        print(f'>> AUTO BALANCE: Função desativada!')
    
    else:
        print(f'Por favor, configure a função: AUTO BALANCE\nOpções:\n1 = Ativado\n2 = Desativado')
########################################################################

########################################################################
# FUNÇÃO: MÍNIMA BLEU/EXC (BTC_USDT)
########################################################################


def minima_BLEU_EXC_BTC_USDT():

    dataEhora = datetime.datetime.now()
    dataEhora = dataEhora.strftime('%d/%m/%Y %H:%M')
    print(f'{dataEhora}')

    url_vBTC_USDT = config.urlGettickerEXC_BTC_USDT
    r_vBTC_USDT = requests.get(url_vBTC_USDT)
    j_vBTC_USDT = json.loads(r_vBTC_USDT.text)
    vBTC_USDT = j_vBTC_USDT['result'][0]['Last']

    urlGetOrderBookBLEU_BUY_BTC_USDT = config.urlGetOrderBookBLEU_BUY_BTC_USDT
    rBLEU = requests.get(urlGetOrderBookBLEU_BUY_BTC_USDT)
    jBLEU = json.loads(rBLEU.text)
    quantidade_comprandoBLEU = jBLEU['result']['buy'][0]['Quantity']

    urlGetOrderBookBLEU_SELL_BTC_USDT = config.urlGetOrderBookBLEU_SELL_BTC_USDT
    rBLEU = requests.get(urlGetOrderBookBLEU_SELL_BTC_USDT)
    jBLEU = json.loads(rBLEU.text)
    quantidade_vendendoBLEU = jBLEU['result']['sell'][0]['Quantity']

    urlGetOrderBookEXC_BUY_BTC_USDT = config.urlGetOrderBookEXC_BUY_BTC_USDT
    rEXC = requests.get(urlGetOrderBookEXC_BUY_BTC_USDT)
    jEXC = json.loads(rEXC.text)
    quantidade_comprandoEXC = jEXC['result']['buy'][0]['Quantity']

    urlGetOrderBookEXC_SELL_BTC_USDT = config.urlGetOrderBookEXC_SELL_BTC_USDT
    rEXC = requests.get(urlGetOrderBookEXC_SELL_BTC_USDT)
    jEXC = json.loads(rEXC.text)
    quantidade_vendendoEXC = jEXC['result']['sell'][0]['Quantity']

    urlGettickerEXC = config.urlGettickerEXC_BTC_USDT
    rEXC = requests.get(urlGettickerEXC)
    jEXC = json.loads(rEXC.text)

    lastAtivoEXC = float(jEXC['result'][0]['Last'])
    compraAtivoEXC = float(jEXC['result'][0]['Bid'])
    vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    urlGettickerBLEU = config.urlGettickerBLEU_BTC_USDT
    rBLEU = requests.get(urlGettickerBLEU)
    jBLEU = json.loads(rBLEU.text)

    lastAtivoBLEU = float(jBLEU['result'][0]['Last'])
    compraAtivoBLEU = float(jBLEU['result'][0]['Bid'])
    vendaAtivoBLEU = float(jBLEU['result'][0]['Ask'])
    
    ############################## MINIMA ########################################
    if funMinima_BLEU_EXC_BTC_USDT == 1:
        ################################################################
        # COMPRA QUANTIDADE MÍNIMA                                     #
        # Faz COMPRA MÍNIMA na BLEU: MOEDA_MERCADO, PREÇO, QUANTIDADE  #
        ################################################################
        print(' >>> FAZENDO COMPRA MÍNIMA <<<\n')

        # calcula fee
        pagafee = (feeBLEU / 100) * minima_BTC_USDT
        print(f'Fee: {pagafee:.8f}')

        faz_compra = key_secretBLEU.buy_limit('BTC_USDT', vendaAtivoBLEU, minima_BTC_USDT)
        print(f'(1)Comprando... {minima_BTC_USDT:.8f} BTC')
        print(faz_compra)

        # Mensagem Telegram
        config.mensagem_telegram('>>> FAZENDO COMPRA MÍNIMA <<<')
        config.mensagem_telegram(
            f'>> VALORES: \nCompra: {vendaAtivoBLEU:.8f} \nVenda: {compraAtivoEXC:.8f} \nQuantidade: {minima_BTC_USDT:.8f}\n')
        config.mensagem_telegram(
            f'>> AÇÃO:\nComprando na BLEU... {minima_BTC_USDT:.8f}\n{faz_compra}\n')

        ############################
        # aqui tinha log txt
        ############################

        # Recebe resposta da ação COMPRA
        respostaFazCompra = faz_compra['result']
        if respostaFazCompra == listaErroMinima[0]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        elif respostaFazCompra == listaErroMinima[1]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        elif respostaFazCompra == listaErroMinima[2]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        elif respostaFazCompra == listaErroMinima[3]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        else:
            print('Sem erros na compra, continua...\n')

        ######################################
        # TRANSFERÊNCIA QUANTIDADE MINIMA    #
        # Faz TRANSFERÊNCIA da BLEU para EXC #
        ######################################
        print(f'\nTransferindo... {minima_BTC_USDT:.8f} BTC')
        mCOMPRA = str(minima_BTC_USDT)
        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
            int(
                time.time())) + '&asset=BTC&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC
        # sign
        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(),
                        hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
        print(response.json())

        # Aguarda 2 segundos antes de executar a venda
        time.sleep(2)

        # Mensagem Telegram
        config.mensagem_telegram('>> TRANSFERÊNCIA: BLEU para EXC')
        config.mensagem_telegram(
            f'>> AÇÃO:\nQuantidade: {minima_BTC_USDT:.8f}\n{response.json()}\n')

        ############################
        # aqui tinha log txt
        ############################

        ######################################################
        # VENDA QUANTIDADE MÍNIMA                            #
        # Faz VENDA na EXC: MOEDA_MERCADO, preço, quantidade #
        ######################################################
        print(f'\nVENDENDO... {minima_BTC_USDT:.8f} BTC')
        faz_vendaEXC = key_secretEXC.sell_limit('BTC_USDT', compraAtivoEXC, minima_BTC_USDT)
        print(faz_vendaEXC)

        # Mensagem Telegram
        config.mensagem_telegram('>>> VENDA QUANTIDADE MÍNIMA <<<')
        config.mensagem_telegram(
            f'>> AÇÃO:\nQuantidade: {minima_BTC_USDT:.8f}\n{faz_vendaEXC}\n')

        ############################
        # aqui tinha log txt
        ############################

        ############################
        # MINIMO ORDENS LOG WEB
        log = open('logs/BTC_USDT.txt', 'a')
        log.write(
            f'{dataEhora}, BTC_USDT, {vendaAtivoBLEU:.8f}, {compraAtivoEXC:.8f}, {minima_BTC_USDT:.8f}, 0, 0, 0\n')
        log.close()
        ############################

    elif funMinima_BLEU_EXC_BTC_USDT == 0:
        print(f'>> COMPRA MÍNIMA: Função desativada!')

    else:
        print(f'Por favor, configure a função: COMPRA MÍNIMA\nOpções:\n1 = Ativado\n2 = Desativado')
########################################################################

########################################################################
# FUNÇÃO: MÍNIMA BLEU/EXC (ETH_USDT)
########################################################################


def minima_BLEU_EXC_ETH_USDT():
    dataEhora = datetime.datetime.now()
    dataEhora = dataEhora.strftime('%d/%m/%Y %H:%M')
    print(f'{dataEhora}')

    url_vETH_USDT = config.urlGettickerEXC_ETH_USDT
    r_vETH_USDT = requests.get(url_vETH_USDT)
    j_vETH_USDT = json.loads(r_vETH_USDT.text)
    vETH_USDT = j_vETH_USDT['result'][0]['Last']

    urlGetOrderBookBLEU_BUY_ETH_USDT = config.urlGetOrderBookBLEU_BUY_ETH_USDT
    rBLEU = requests.get(urlGetOrderBookBLEU_BUY_ETH_USDT)
    jBLEU = json.loads(rBLEU.text)
    quantidade_comprandoBLEU = jBLEU['result']['buy'][0]['Quantity']

    urlGetOrderBookBLEU_SELL_ETH_USDT = config.urlGetOrderBookBLEU_SELL_ETH_USDT
    rBLEU = requests.get(urlGetOrderBookBLEU_SELL_ETH_USDT)
    jBLEU = json.loads(rBLEU.text)
    quantidade_vendendoBLEU = jBLEU['result']['sell'][0]['Quantity']

    urlGetOrderBookEXC_BUY_ETH_USDT = config.urlGetOrderBookEXC_BUY_ETH_USDT
    rEXC = requests.get(urlGetOrderBookEXC_BUY_ETH_USDT)
    jEXC = json.loads(rEXC.text)
    quantidade_comprandoEXC = jEXC['result']['buy'][0]['Quantity']

    urlGetOrderBookEXC_SELL_ETH_USDT = config.urlGetOrderBookEXC_SELL_ETH_USDT
    rEXC = requests.get(urlGetOrderBookEXC_SELL_ETH_USDT)
    jEXC = json.loads(rEXC.text)
    quantidade_vendendoEXC = jEXC['result']['sell'][0]['Quantity']

    urlGettickerEXC = config.urlGettickerEXC_ETH_USDT
    rEXC = requests.get(urlGettickerEXC)
    jEXC = json.loads(rEXC.text)

    lastAtivoEXC = float(jEXC['result'][0]['Last'])
    compraAtivoEXC = float(jEXC['result'][0]['Bid'])
    vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    urlGettickerBLEU = config.urlGettickerBLEU_ETH_USDT
    rBLEU = requests.get(urlGettickerBLEU)
    jBLEU = json.loads(rBLEU.text)

    lastAtivoBLEU = float(jBLEU['result'][0]['Last'])
    compraAtivoBLEU = float(jBLEU['result'][0]['Bid'])
    vendaAtivoBLEU = float(jBLEU['result'][0]['Ask'])

    ############################## MINIMA ########################################
    if funMinima_BLEU_EXC_ETH_USDT == 1:
        ################################################################
        # COMPRA QUANTIDADE MÍNIMA                                     #
        # Faz COMPRA MÍNIMA na BLEU: MOEDA_MERCADO, PREÇO, QUANTIDADE  #
        ################################################################
        print(' >>> FAZENDO COMPRA MÍNIMA <<<\n')

        # calcula fee
        pagafee = (feeBLEU / 100) * minima_ETH_USDT
        print(f'Fee: {pagafee:.8f}')

        faz_compra = key_secretBLEU.buy_limit('ETH_USDT', vendaAtivoBLEU, minima_ETH_USDT)
        print(f'(1)Comprando... {minima_ETH_USDT:.8f} ETH')
        print(faz_compra)

        # Mensagem Telegram
        config.mensagem_telegram('>>> FAZENDO COMPRA MÍNIMA <<<')
        config.mensagem_telegram(
            f'>> VALORES: \nCompra: {vendaAtivoBLEU:.8f} \nVenda: {compraAtivoEXC:.8f} \nQuantidade: {minima_ETH_USDT:.8f}\n')
        config.mensagem_telegram(
            f'>> AÇÃO:\nComprando na BLEU... {minima_ETH_USDT:.8f}\n{faz_compra}\n')

        ############################
        # aqui tinha log txt
        ############################

        # Recebe resposta da ação COMPRA
        respostaFazCompra = faz_compra['result']
        if respostaFazCompra == listaErroMinima[0]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        elif respostaFazCompra == listaErroMinima[1]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        elif respostaFazCompra == listaErroMinima[2]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        elif respostaFazCompra == listaErroMinima[3]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        else:
            print('Sem erros na compra, continua...\n')

        ######################################
        # TRANSFERÊNCIA QUANTIDADE MINIMA    #
        # Faz TRANSFERÊNCIA da BLEU para EXC #
        ######################################
        print(f'\nTransferindo... {minima_ETH_USDT:.8f} ETH')
        mCOMPRA = str(minima_ETH_USDT)
        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
            int(
                time.time())) + '&asset=ETH&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC
        # sign
        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(),
                        hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
        print(response.json())

        # Aguarda 2 segundos antes de executar a venda
        time.sleep(2)

        # Mensagem Telegram
        config.mensagem_telegram('>> TRANSFERÊNCIA: BLEU para EXC')
        config.mensagem_telegram(
            f'>> AÇÃO:\nQuantidade: {minima_ETH_USDT:.8f}\n{response.json()}\n')

        ############################
        # aqui tinha log txt
        ############################

        ######################################################
        # VENDA QUANTIDADE MÍNIMA                            #
        # Faz VENDA na EXC: MOEDA_MERCADO, preço, quantidade #
        ######################################################
        print(f'\nVENDENDO... {minima_ETH_USDT:.8f} ETH')
        faz_vendaEXC = key_secretEXC.sell_limit('ETH_USDT', compraAtivoEXC, minima_ETH_USDT)
        print(faz_vendaEXC)

        # Mensagem Telegram
        config.mensagem_telegram('>>> VENDA QUANTIDADE MÍNIMA <<<')
        config.mensagem_telegram(
            f'>> AÇÃO:\nQuantidade: {minima_ETH_USDT:.8f}\n{faz_vendaEXC}\n')

        ############################
        # aqui tinha log txt
        ############################

        ############################
        # MINIMO ORDENS LOG WEB
        log = open('logs/ETH_USDT.txt', 'a')
        log.write(
            f'{dataEhora}, ETH_USDT, {vendaAtivoBLEU:.8f}, {compraAtivoEXC:.8f}, {minima_ETH_USDT:.8f}, 0, 0, 0\n')
        log.close()
        ############################

    elif funMinima_BLEU_EXC_ETH_USDT == 0:
        print(f'>> COMPRA MÍNIMA: Função desativada!')

    else:
        print(f'Por favor, configure a função: COMPRA MÍNIMA\nOpções:\n1 = Ativado\n2 = Desativado')
########################################################################

########################################################################
# FUNÇÃO: MÍNIMA EXC/BLEU (BTC_USDT)
########################################################################


def minima_EXC_BLEU_BTC_USDT():

    dataEhora = datetime.datetime.now()
    dataEhora = dataEhora.strftime('%d/%m/%Y %H:%M')
    print(f'{dataEhora}')

    url_vBTC_USDT = config.urlGettickerEXC_BTC_USDT
    r_vBTC_USDT = requests.get(url_vBTC_USDT)
    j_vBTC_USDT = json.loads(r_vBTC_USDT.text)
    vBTC_USDT = j_vBTC_USDT['result'][0]['Last']

    urlGetOrderBookBLEU_BUY_BTC_USDT = config.urlGetOrderBookBLEU_BUY_BTC_USDT
    rBLEU = requests.get(urlGetOrderBookBLEU_BUY_BTC_USDT)
    jBLEU = json.loads(rBLEU.text)
    quantidade_comprandoBLEU = jBLEU['result']['buy'][0]['Quantity']

    urlGetOrderBookBLEU_SELL_BTC_USDT = config.urlGetOrderBookBLEU_SELL_BTC_USDT
    rBLEU = requests.get(urlGetOrderBookBLEU_SELL_BTC_USDT)
    jBLEU = json.loads(rBLEU.text)
    quantidade_vendendoBLEU = jBLEU['result']['sell'][0]['Quantity']

    urlGetOrderBookEXC_BUY_BTC_USDT = config.urlGetOrderBookEXC_BUY_BTC_USDT
    rEXC = requests.get(urlGetOrderBookEXC_BUY_BTC_USDT)
    jEXC = json.loads(rEXC.text)
    quantidade_comprandoEXC = jEXC['result']['buy'][0]['Quantity']

    urlGetOrderBookEXC_SELL_BTC_USDT = config.urlGetOrderBookEXC_SELL_BTC_USDT
    rEXC = requests.get(urlGetOrderBookEXC_SELL_BTC_USDT)
    jEXC = json.loads(rEXC.text)
    quantidade_vendendoEXC = jEXC['result']['sell'][0]['Quantity']

    urlGettickerEXC = config.urlGettickerEXC_BTC_USDT
    rEXC = requests.get(urlGettickerEXC)
    jEXC = json.loads(rEXC.text)

    lastAtivoEXC = float(jEXC['result'][0]['Last'])
    compraAtivoEXC = float(jEXC['result'][0]['Bid'])
    vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    urlGettickerBLEU = config.urlGettickerBLEU_BTC_USDT
    rBLEU = requests.get(urlGettickerBLEU)
    jBLEU = json.loads(rBLEU.text)

    lastAtivoBLEU = float(jBLEU['result'][0]['Last'])
    compraAtivoBLEU = float(jBLEU['result'][0]['Bid'])
    vendaAtivoBLEU = float(jBLEU['result'][0]['Ask'])

    if funMinima_EXC_BLEU_BTC_USDT == 1:
        ################################################################
        # COMPRA QUANTIDADE MÍNIMA                                     #
        # Faz COMPRA MÍNIMA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE   #
        ################################################################
        print(' >>> FAZENDO COMPRA MÍNIMA <<<\n')

        # calcula fee
        pagafee = (feeBLEU / 100) * minima_BTC_USDT
        print(f'Fee: {pagafee:.8f}')

        faz_compra = key_secretEXC.buy_limit('BTC_USDT', vendaAtivoEXC, minima_BTC_USDT)
        print(f'COMPRANDO... {minima_BTC_USDT:.8f} BTC')
        print(faz_compra)

        # Mensagem Telegram
        config.mensagem_telegram('>>> FAZENDO COMPRA MÍNIMA <<<')
        config.mensagem_telegram(
            f'>> VALORES: \nCompra: {vendaAtivoEXC:.8f} \nVenda: {compraAtivoBLEU:.8f} \nQuantidade: {minima_BTC_USDT:.8f}\n')
        config.mensagem_telegram(
            f'>> AÇÃO:\nComprando na EXC... {minima_BTC_USDT:.8f}\n{faz_compra}\n')

        ############################
        # aqui tinha log txt
        ############################

        # Recebe resposta da ação COMPRA
        respostaFazCompra = faz_compra['result']
        if respostaFazCompra == listaErroMinima[0]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        elif respostaFazCompra == listaErroMinima[1]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        elif respostaFazCompra == listaErroMinima[2]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        elif respostaFazCompra == listaErroMinima[3]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        else:
            print('Sem erros na compra, continua...')

        ######################################
        # TRANSFERÊNCIA QUANTIDADE MINIMA    #
        # Faz TRANSFERÊNCIA da EXC para BLEU #
        ######################################
        print(f'TRANSFERINDO... {minima_BTC_USDT:.8f} BTC')
        mCOMPRA = str(minima_BTC_USDT)
        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
            int(
                time.time())) + '&asset=BTC&quantity=' + mCOMPRA + '&exchangeto=1&' + 'accountto=' + emailBLEU

        # sign
        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(),
                        hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferEXC, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

        # Mensagem Telegram
        config.mensagem_telegram('>> TRANSFERÊNCIA: EXC para BLEU')
        config.mensagem_telegram(
            f'>> AÇÃO:\nQuantidade: {minima_BTC_USDT:.8f}\n{response.json()}\n')

        ############################
        # aqui tinha log txt
        ############################

        ######################################################
        # VENDA QUANTIDADE MÍNIMA                            #
        # Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade #
        ######################################################
        print(f'VENDENDO... {minima_BTC_USDT:.8f} BTC')
        faz_vendaBLEU = key_secretBLEU.sell_limit('BTC_USDT', compraAtivoBLEU,
                                                  minima_BTC_USDT)
        print(faz_vendaBLEU)

        # Mensagem Telegram
        config.mensagem_telegram('>>> VENDA QUANTIDADE MÍNIMA <<<')
        config.mensagem_telegram(
            f'>> AÇÃO:\nQuantidade: {minima_BTC_USDT:.8f}\n{faz_vendaBLEU}\n')

        ############################
        # aqui tinha log txt
        ############################

        ############################
        # MINIMO ORDENS LOG WEB
        log = open('logs/BTC_USDT.txt', 'a')
        log.write(f'{dataEhora}, BTC_USDT, {vendaAtivoEXC:.8f}, {compraAtivoBLEU:.8f}, {minima_BTC_USDT:.8f}, 0, 0, 0\n')
        log.close()
        ############################

    elif funMinima_EXC_BLEU_BTC_USDT == 0:
        print(f'>> COMPRA MÍNIMA: Função desativada!')

    else:
        print(f'Por favor, configure a função: COMPRA MÍNIMA\nOpções:\n1 = Ativado\n2 = Desativado')

    ############################## MINIMA ########################################
########################################################################

########################################################################
# FUNÇÃO: MÍNIMA EXC/BLEU (ETH_USDT)
########################################################################


def minima_EXC_BLEU_ETH_USDT():

    dataEhora = datetime.datetime.now()
    dataEhora = dataEhora.strftime('%d/%m/%Y %H:%M')
    print(f'{dataEhora}')

    url_vETH_USDT = config.urlGettickerEXC_ETH_USDT
    r_vETH_USDT = requests.get(url_vETH_USDT)
    j_vETH_USDT = json.loads(r_vETH_USDT.text)
    vETH_USDT = j_vETH_USDT['result'][0]['Last']

    urlGetOrderBookBLEU_BUY_ETH_USDT = config.urlGetOrderBookBLEU_BUY_ETH_USDT
    rBLEU = requests.get(urlGetOrderBookBLEU_BUY_ETH_USDT)
    jBLEU = json.loads(rBLEU.text)
    quantidade_comprandoBLEU = jBLEU['result']['buy'][0]['Quantity']

    urlGetOrderBookBLEU_SELL_ETH_USDT = config.urlGetOrderBookBLEU_SELL_ETH_USDT
    rBLEU = requests.get(urlGetOrderBookBLEU_SELL_ETH_USDT)
    jBLEU = json.loads(rBLEU.text)
    quantidade_vendendoBLEU = jBLEU['result']['sell'][0]['Quantity']

    urlGetOrderBookEXC_BUY_ETH_USDT = config.urlGetOrderBookEXC_BUY_ETH_USDT
    rEXC = requests.get(urlGetOrderBookEXC_BUY_ETH_USDT)
    jEXC = json.loads(rEXC.text)
    quantidade_comprandoEXC = jEXC['result']['buy'][0]['Quantity']

    urlGetOrderBookEXC_SELL_ETH_USDT = config.urlGetOrderBookEXC_SELL_ETH_USDT
    rEXC = requests.get(urlGetOrderBookEXC_SELL_ETH_USDT)
    jEXC = json.loads(rEXC.text)
    quantidade_vendendoEXC = jEXC['result']['sell'][0]['Quantity']

    urlGettickerEXC = config.urlGettickerEXC_ETH_USDT
    rEXC = requests.get(urlGettickerEXC)
    jEXC = json.loads(rEXC.text)

    lastAtivoEXC = float(jEXC['result'][0]['Last'])
    compraAtivoEXC = float(jEXC['result'][0]['Bid'])
    vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    urlGettickerBLEU = config.urlGettickerBLEU_ETH_USDT
    rBLEU = requests.get(urlGettickerBLEU)
    jBLEU = json.loads(rBLEU.text)

    lastAtivoBLEU = float(jBLEU['result'][0]['Last'])
    compraAtivoBLEU = float(jBLEU['result'][0]['Bid'])
    vendaAtivoBLEU = float(jBLEU['result'][0]['Ask'])

    if funMinima_EXC_BLEU_ETH_USDT == 1:
        ################################################################
        # COMPRA QUANTIDADE MÍNIMA                                     #
        # Faz COMPRA MÍNIMA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE   #
        ################################################################
        print(' >>> FAZENDO COMPRA MÍNIMA <<<\n')

        # calcula fee
        pagafee = (feeBLEU / 100) * minima_ETH_USDT
        print(f'Fee: {pagafee:.8f}')

        faz_compra = key_secretEXC.buy_limit('ETH_USDT', vendaAtivoEXC, minima_ETH_USDT)
        print(f'COMPRANDO... {minima_ETH_USDT:.8f} ETH')
        print(faz_compra)

        # Mensagem Telegram
        config.mensagem_telegram('>>> FAZENDO COMPRA MÍNIMA <<<')
        config.mensagem_telegram(
            f'>> VALORES: \nCompra: {vendaAtivoEXC:.8f} \nVenda: {compraAtivoBLEU:.8f} \nQuantidade: {minima_ETH_USDT:.8f}\n')
        config.mensagem_telegram(
            f'>> AÇÃO:\nComprando na EXC... {minima_ETH_USDT:.8f}\n{faz_compra}\n')

        ############################
        # aqui tinha log txt
        ############################

        # Recebe resposta da ação COMPRA
        respostaFazCompra = faz_compra['result']
        if respostaFazCompra == listaErroMinima[0]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        elif respostaFazCompra == listaErroMinima[1]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        elif respostaFazCompra == listaErroMinima[2]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        elif respostaFazCompra == listaErroMinima[3]:
            print('>> ERRO << Reiniciando verificação!')
            # break
        else:
            print('Sem erros na compra, continua...')

        ######################################
        # TRANSFERÊNCIA QUANTIDADE MINIMA    #
        # Faz TRANSFERÊNCIA da EXC para BLEU #
        ######################################
        print(f'TRANSFERINDO... {minima_ETH_USDT:.8f} ETH')
        mCOMPRA = str(minima_ETH_USDT)
        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
            int(
                time.time())) + '&asset=ETH&quantity=' + mCOMPRA + '&exchangeto=1&' + 'accountto=' + emailBLEU

        # sign
        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(),
                        hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferEXC, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

        # Mensagem Telegram
        config.mensagem_telegram('>> TRANSFERÊNCIA: EXC para BLEU')
        config.mensagem_telegram(
            f'>> AÇÃO:\nQuantidade: {minima_ETH_USDT:.8f}\n{response.json()}\n')

        ############################
        # aqui tinha log txt
        ############################

        ######################################################
        # VENDA QUANTIDADE MÍNIMA                            #
        # Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade #
        ######################################################
        print(f'VENDENDO... {minima_ETH_USDT:.8f} ETH')
        faz_vendaBLEU = key_secretBLEU.sell_limit('ETH_USDT', compraAtivoBLEU,
                                                  minima_ETH_USDT)
        print(faz_vendaBLEU)

        # Mensagem Telegram
        config.mensagem_telegram('>>> VENDA QUANTIDADE MÍNIMA <<<')
        config.mensagem_telegram(
            f'>> AÇÃO:\nQuantidade: {minima_ETH_USDT:.8f}\n{faz_vendaBLEU}\n')

        ############################
        # aqui tinha log txt
        ############################

        ############################
        # MINIMO ORDENS LOG WEB
        log = open('logs/ETH_USDT.txt', 'a')
        log.write(f'{dataEhora}, ETH_USDT, {vendaAtivoEXC:.8f}, {compraAtivoBLEU:.8f}, {minima_ETH_USDT:.8f}, 0, 0, 0\n')
        log.close()
        ############################

    elif funMinima_EXC_BLEU_ETH_USDT == 0:
        print(f'>> COMPRA MÍNIMA: Função desativada!')

    else:
        print(f'Por favor, configure a função: COMPRA MÍNIMA\nOpções:\n1 = Ativado\n2 = Desativado')

    ############################## MINIMA ########################################
########################################################################

########################################################################

########################################################################
