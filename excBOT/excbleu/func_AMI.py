import excBot
import bleuBot
import requests
import json
import config
import datetime
import time

#####################################
# EXC CRIPTO
emailEXC = config.emailEXC
keyEXC = config.keyEXC
secretEXC = config.secretEXC
key_secretEXC = excBot.excBot(keyEXC, secretEXC, nonce=True)
#####################################
# BLEUTRADE
emailBLEU = config.emailBLEU
keyBLEU = config.keyBLEU
secretBLEU = config.secretBLEU
key_secretBLEU = bleuBot.bleuBot(keyBLEU, secretBLEU, nonce=True)
#####################################


def func_ami(ativo, mercado):

    # SALDO INICIAL EM BTC
    saldoInicial_EXC = config.saldoInicial_EXC
    saldoInicial_BLEU = config.saldoInicial_BLEU
    #####################################

    urlGettickerEXC_ATIVO_mercado = 'urlGettickerEXC_' + ativo + '_' + mercado

    if urlGettickerEXC_ATIVO_mercado == 'urlGettickerEXC_BTC_USDT':
        urlGettickerEXC_BTC_USDT = config.urlGettickerEXC_BTC_USDT
        rEXC = requests.get(urlGettickerEXC_BTC_USDT)
        jEXC = json.loads(rEXC.text)

        compraAtivoEXC = float(jEXC['result'][0]['Bid'])
        vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    elif urlGettickerEXC_ATIVO_mercado == 'urlGettickerEXC_ETH_USDT':
        urlGettickerEXC_ETH_USDT = config.urlGettickerEXC_ETH_USDT
        rEXC = requests.get(urlGettickerEXC_ETH_USDT)
        jEXC = json.loads(rEXC.text)

        compraAtivoEXC = float(jEXC['result'][0]['Bid'])
        vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    elif urlGettickerEXC_ATIVO_mercado == 'urlGettickerEXC_LTC_USDT':
        urlGettickerEXC_LTC_USDT = config.urlGettickerEXC_LTC_USDT
        rEXC = requests.get(urlGettickerEXC_LTC_USDT)
        jEXC = json.loads(rEXC.text)

        compraAtivoEXC = float(jEXC['result'][0]['Bid'])
        vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    elif urlGettickerEXC_ATIVO_mercado == 'urlGettickerEXC_DOGE_USDT':
        urlGettickerEXC_DOGE_USDT = config.urlGettickerEXC_DOGE_USDT
        rEXC = requests.get(urlGettickerEXC_DOGE_USDT)
        jEXC = json.loads(rEXC.text)

        compraAtivoEXC = float(jEXC['result'][0]['Bid'])
        vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    elif urlGettickerEXC_ATIVO_mercado == 'urlGettickerEXC_ETH_BTC':
        urlGettickerEXC_ETH_BTC = config.urlGettickerEXC_ETH_BTC
        rEXC = requests.get(urlGettickerEXC_ETH_BTC)
        jEXC = json.loads(rEXC.text)

        compraAtivoEXC = float(jEXC['result'][0]['Bid'])
        vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    elif urlGettickerEXC_ATIVO_mercado == 'urlGettickerEXC_LTC_BTC':
        urlGettickerEXC_LTC_BTC = config.urlGettickerEXC_LTC_BTC
        rEXC = requests.get(urlGettickerEXC_LTC_BTC)
        jEXC = json.loads(rEXC.text)

        compraAtivoEXC = float(jEXC['result'][0]['Bid'])
        vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    elif urlGettickerEXC_ATIVO_mercado == 'urlGettickerEXC_DOGE_BTC':
        urlGettickerEXC_DOGE_BTC = config.urlGettickerEXC_DOGE_BTC
        rEXC = requests.get(urlGettickerEXC_DOGE_BTC)
        jEXC = json.loads(rEXC.text)

        compraAtivoEXC = float(jEXC['result'][0]['Bid'])
        vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    elif urlGettickerEXC_ATIVO_mercado == 'urlGettickerEXC_BTC_CBRL':
        urlGettickerEXC_BTC_CBRL = config.urlGettickerEXC_BTC_CBRL
        rEXC = requests.get(urlGettickerEXC_BTC_CBRL)
        jEXC = json.loads(rEXC.text)

        compraAtivoEXC = float(jEXC['result'][0]['Bid'])
        vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    elif urlGettickerEXC_ATIVO_mercado == 'urlGettickerEXC_USDT_CBRL':
        urlGettickerEXC_USDT_CBRL = config.urlGettickerEXC_USDT_CBRL
        rEXC = requests.get(urlGettickerEXC_USDT_CBRL)
        jEXC = json.loads(rEXC.text)

        compraAtivoEXC = float(jEXC['result'][0]['Bid'])
        vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

    #####################################
    # DATA/HORA
    dataEhora = datetime.datetime.now()
    dataEhora = dataEhora.strftime('%d/%m/%Y %H:%M')
    print('=' * 20)
    print(f'{dataEhora}')
    print('=' * 20)
    ######################################################################
    #                       CONFIG                                       #
    ######################################################################

    # ATIVO = input('Digite Ativo: ').upper()
    # mercado = input('Digite Mercado: ').upper()

    ATIVO = ativo
    mercado = mercado

    ativoMercado = ATIVO + '_' + mercado

    # ATIVO = 'BTC'
    # ativoMercado = 'BTC_USDT'
    porcentagemUso = 100
    rangeInicial = ''
    porcentagemSpread = ''

    # rangeFinal = 11500
    # porcentagemSpread = 0.35

    minima_ATIVO_mercado = 'minima_' + ATIVO + '_' + mercado

    minima_BTC_USDT = config.minima_BTC_USDT
    minima_ETH_USDT = config.minima_ETH_USDT
    minima_LTC_USDT = config.minima_LTC_USDT
    minima_DOGE_USDT = config.minima_DOGE_USDT

    minima_ETH_BTC = config.minima_ETH_BTC
    minima_LTC_BTC = config.minima_LTC_BTC
    minima_DOGE_BTC = config.minima_DOGE_BTC

    minima_BTC_CBRL = config.minima_BTC_CBRL
    minima_USDT_CBRL = config.minima_USDT_CBRL

    if minima_ATIVO_mercado == 'minima_BTC_USDT':
        print(f'Valor mínimo: {minima_BTC_USDT}')
        minima_ATIVO_mercado = minima_BTC_USDT

    elif minima_ATIVO_mercado == 'minima_ETH_USDT':
        print(f'Valor mínimo: {minima_ETH_USDT}')
        minima_ATIVO_mercado = minima_ETH_USDT

    elif minima_ATIVO_mercado == 'minima_LTC_USDT':
        print(f'Valor mínimo: {minima_LTC_USDT}')
        minima_ATIVO_mercado = minima_LTC_USDT

    elif minima_ATIVO_mercado == 'minima_DOGE_USDT':
        print(f'Valor mínimo: {minima_DOGE_USDT}')
        minima_ATIVO_mercado = minima_DOGE_USDT

    elif minima_ATIVO_mercado == 'minima_ETH_BTC':
        print(f'Valor mínimo: {minima_ETH_BTC}')
        minima_ATIVO_mercado = minima_ETH_BTC

    elif minima_ATIVO_mercado == 'minima_LTC_BTC':
        print(f'Valor mínimo: {minima_LTC_BTC}')
        minima_ATIVO_mercado = minima_LTC_BTC

    elif minima_ATIVO_mercado == 'minima_DOGE_BTC':
        print(f'Valor mínimo: {minima_DOGE_BTC}')
        minima_ATIVO_mercado = minima_DOGE_BTC

    elif minima_ATIVO_mercado == 'minima_BTC_CBRL':
        print(f'Valor mínimo: {minima_BTC_CBRL}')
        minima_ATIVO_mercado = minima_BTC_CBRL

    elif minima_ATIVO_mercado == 'minima_USDT_CBRL':
        print(f'Valor mínimo: {minima_USDT_CBRL}')
        minima_ATIVO_mercado = minima_USDT_CBRL

    ######################################################################
    print('\n>> excBOT - CRIAR ORDENS AMI <<')
    print('-' * 50)
    print('>> AÇÃO\n\nO que deseja fazer: COMPRA / VENDA')
    acaoCV = input('Digite aqui: ').upper()

    if acaoCV == 'COMPRA':
        print('')
        ######################################################################
        #                       COMPRA                                       #
        ######################################################################
        print('=' * 50)
        print('\n>> COMPRA\n')
        print('ATENÇÃO: Digite apenas números!!!\n')
        print('>> VALOR FINAL: Até qual preço deseja para ...')
        rangeFinal = input('Digite aqui: ')
        rangeFinal = float(rangeFinal)

        print('\nSPREAD em % (Ex: 0.25)')
        porcentagemSpread = input('Digite aqui: ')
        porcentagemSpread = float(porcentagemSpread)
        print('=' * 50)
        ######################################################################
        print('=' * 50)
        print('\n> EXC <')
        print('=' * 50)
        # print('\n>> SALDO DISPONÍVEL:')

        # ATIVO = str(input('Qual ATIVO: '))
        ATIVO = ATIVO
        aBalance = key_secretEXC.get_balance(ATIVO)
        # print(aBalance)

        # assetATIVO = aBalance['result'][0]['Asset']
        saldoDisponivelATIVO = aBalance['result'][0]['Available']
        # print(f'{assetATIVO}: {saldoDisponivelATIVO:.8f}')
        ##########################################################
        # print('\n>> SALDO PARA AMI:')
        # print('Porcentagem do saldo que deseja usar?\nOpções: 100, 50 e 25\n')
        ##########################################################
        if porcentagemUso == 100:
            saldoDisponivelATIVO = saldoDisponivelATIVO
            # print(f'Saldo disponível: {saldoDisponivelATIVO} {assetATIVO}')
            # print(f'Saldo usado: {porcentagemUso}%\n')

            # ORDEM MÍNIMA
            q1 = saldoDisponivelATIVO / minima_ATIVO_mercado
            q1 = int(q1)
            print(f'Valor ordem mínima: {minima_ATIVO_mercado:.8f}')
            print(f'Quantidade de ordens Mínimas: {q1}')

            # INTERVALOS ORDENS EM % ORDENS
            spreadRange = compraAtivoEXC * (porcentagemSpread / 100)
            print(f'SPREAD de {porcentagemSpread}% em USDT: {spreadRange}\n')

            somasv = spreadRange + compraAtivoEXC
            # print(f'Range inicial: {somasv}')

            time.sleep(1)

            # CRIAR ORDENS
            print('>> CRIAR ORDENS:')

            ativoMercado = ativoMercado
            rateOrdem = compraAtivoEXC + (spreadRange * 2)
            # rateOrdem = compraAtivoEXC - (spreadRange * 3)
            quantidadeOrdem = minima_ATIVO_mercado

            rangeFinal = rangeFinal

            while rateOrdem > rangeFinal:
                rateOrdem = rateOrdem - spreadRange
                rateAMI = rateOrdem - (spreadRange * 1)
                # rateAMI = rateOrdem - (spreadRange * 2)
                print(f'Comprar por: {rateAMI:.8f} / Vender por: {rateOrdem:.8f} / Quantidade: {quantidadeOrdem:.8f}')

                criaOrdem = key_secretEXC.buy_limitami(ativoMercado, rateAMI, rateOrdem, quantidadeOrdem)
                print(f'Resposta: {criaOrdem}\n')

                time.sleep(1)

        ##########################################################
        elif porcentagemUso == 50:
            saldoDisponivelATIVO = saldoDisponivelATIVO / 2
            porcentagemUso = saldoDisponivelATIVO / 2
            print(f'{saldoDisponivelATIVO}')
            print(f'Usar {porcentagemUso}% do saldo')
        ##########################################################
        elif porcentagemUso == 25:
            saldoDisponivelATIVO = saldoDisponivelATIVO / 4
            porcentagemUso = saldoDisponivelATIVO / 4
            print(f'{saldoDisponivelATIVO}')
            print(f'Usar {porcentagemUso}% do saldo')
        ##########################################################
        else:
            print('ATENÇÃO: Digite 100, 50 ou 25')
        ##########################################################

    elif acaoCV == 'VENDA':
        print('')
        ######################################################################
        #                       VENDA                                        #
        ######################################################################
        print('-' * 50)
        print('\n>> VENDA\n')
        print('ATENÇÃO: Digite apenas números!!!\n')
        print('>> VALOR FINAL: Até qual preço deseja para ...')
        rangeFinal = input('Digite aqui: ')
        rangeFinal = float(rangeFinal)

        print('\nSPREAD em % (Ex: 0.25)')
        porcentagemSpread = input('Digite aqui: ')
        porcentagemSpread = float(porcentagemSpread)
        print('=' * 50)
        ######################################################################
        print('=' * 50)
        print('> EXC <')
        print('=' * 50)
        # print('\n>> SALDO DISPONÍVEL: ')

        # ATIVO = str(input('Qual ATIVO: '))
        ATIVO = ATIVO
        aBalance = key_secretEXC.get_balance(ATIVO)
        # print(aBalance)
        # assetATIVO = aBalance['result'][0]['Asset']
        #saldoDisponivelATIVO = aBalance['result'][0]['Available']
        saldoDisponivelATIVO = 0
        # print(f'{assetATIVO}: {saldoDisponivelATIVO:.8f}')
        ##########################################################
        # print('\n>> SALDO PARA AMI:')
        # print('Porcentagem do saldo que deseja usar?\nOpções: 100, 50 e 25\n')
        ##########################################################
        if porcentagemUso == 100:
            # saldoDisponivelATIVO = saldoDisponivelATIVO
            # print(f'Saldo disponível: {saldoDisponivelATIVO} {assetATIVO}')
            # print(f'Saldo usado: {porcentagemUso}%\n')

            # ORDEM MÍNIMA
            #q1 = saldoDisponivelATIVO / minima_ATIVO_mercado
            #q1 = int(q1)
            #print(f'Valor ordem mínima: {minima_ATIVO_mercado}')
            #print(f'Quantidade de ordens Mínimas: {q1}')

            # INTERVALOS EM % ORDENS
            spreadRange = vendaAtivoEXC * (porcentagemSpread / 100)
            print(f'\nSPREAD de {porcentagemSpread}% em {ATIVO}: {spreadRange}\n')

            somasv = spreadRange + vendaAtivoEXC
            # print(f'Range inicial: {somasv}')

            time.sleep(1)

            # CRIAR ORDENS
            print('>> CRIAR ORDENS:\n')

            ativoMercado = ativoMercado
            print(f'>>>>> {ativoMercado}')

            rateOrdem = vendaAtivoEXC - (spreadRange * 3)
            quantidadeOrdem = minima_ATIVO_mercado

            rangeFinal = rangeFinal

            while rateOrdem < rangeFinal:
                rateOrdem = rateOrdem + spreadRange
                rateAMI = rateOrdem + (spreadRange * 2)
                print(f'Vender por: {rateAMI:.8f} / Comprar por: {rateOrdem:.8f} / Quantidade: {quantidadeOrdem:.8f}')

                criaOrdem = key_secretEXC.sell_limitami(ativoMercado, rateAMI, rateOrdem, quantidadeOrdem)
                print(f'Resposta: {criaOrdem}\n')
                print(f'>>>>> {ativoMercado}')


                time.sleep(1)

        ##########################################################
        elif porcentagemUso == 50:
            saldoDisponivelATIVO = saldoDisponivelATIVO / 2
            porcentagemUso = saldoDisponivelATIVO / 2
            print(f'{saldoDisponivelATIVO}')
            print(f'Usar {porcentagemUso}% do saldo')
        ##########################################################
        elif porcentagemUso == 25:
            saldoDisponivelATIVO = saldoDisponivelATIVO / 4
            porcentagemUso = saldoDisponivelATIVO / 4
            print(f'{saldoDisponivelATIVO}')
            print(f'Usar {porcentagemUso}% do saldo')
        ##########################################################
        else:
            print('ATENÇÃO: Digite 100, 50 ou 25')
        ##########################################################

    else:
        print('\n>> ATENÇÃO <<\nPor favor, digite: COMPRA ou VENDA.\n')
