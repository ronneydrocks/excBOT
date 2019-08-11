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
# SALDO INICIAL EM BTC
saldoInicial_EXC = config.saldoInicial_EXC
saldoInicial_BLEU = config.saldoInicial_BLEU
#####################################
# VALOR ORDEM MÍNIMA
minimaCompra_BTC_USDT = config.minimaCompra_BTC_USDT
#####################################
# print('\nMERCADO EXC: BTC_USDT')
urlGettickerEXC = config.urlGettickerEXC_BTC_USDT
requisicaoEXC = requests.get(urlGettickerEXC)
dicionarioEXC = json.loads(requisicaoEXC.text)

lastAtivoEXC = float(dicionarioEXC['result'][0]['Last'])
# print(f'Última: {lastAtivoEXC:.8f}')
compraAtivoEXC = float(dicionarioEXC['result'][0]['Bid'])
vendaAtivoEXC = float(dicionarioEXC['result'][0]['Ask'])
#####################################
# DATA/HORA
dataEhora = datetime.datetime.now()
dataEhora = dataEhora.strftime('%d/%m/%Y %H:%M')
print('=' * 20)
print(f'{dataEhora}')
print('=' * 20)
#####################################
# TELEGRAM
# config.mensagem_telegram('=' * 40)
#####################################
# LOG
log = open('logs/saldo.txt', 'a')
log.write('#' * 40)
log.write(f'\nData/Hora: {dataEhora}\n')

######################################################################

######################################################################
#                       CONFIG                                       #
######################################################################
ATIVO = 'BTC'
ativoMercado = 'BTC_USDT'
porcentagemUso = 100
rangeInicial = ''
porcentagemSpread = ''

# rangeFinal = 11500
# porcentagemSpread = 0.35

######################################################################

print('\n>> excBOT - CRIAR ORDENS AMI <<')
print('-' * 40)
print('>> AÇÃO\n\nO que deseja fazer: COMPRA / VENDA')
acaoCV = input('Digite aqui: ')


if acaoCV == 'COMPRA':
    print('')
    ######################################################################
    #                       COMPRA                                       #
    ######################################################################

    print('-' * 40)

    print('\n>> COMPRA\n')
    print('ATENÇÃO: Digite apenas números!!!\n')
    print('>> VALOR FINAL: Até qual preço deseja comprar (Ex: 10000.0)')
    rangeFinal = input('Digite aqui: ')
    rangeFinal = float(rangeFinal)

    print('\nSPREAD em % (Ex: 0.25)')
    porcentagemSpread = input('Digite aqui: ')
    porcentagemSpread = float(porcentagemSpread)
    print('=' * 20)

    ######################################################################

    print('=' * 40)
    # EXC
    print('\n> EXC <')

    # Consulta informações Balances
    rBalances = key_secretEXC.get_balances()
    # print(rBalances)

    # Quantidade de Ativos na EXC
    nATIVOS = len(rBalances['result'])
    print(f'Quantidade de Ativos: {nATIVOS}')

    c = 0
    somaEqBTC_EXC = 0

    while c < nATIVOS:
        ATIVO = rBalances['result'][c]['Asset']
        balanceATIVO = rBalances['result'][c]['Balance']
        eATIVO = rBalances['result'][c]['BtcEquivalent']
        print(f'{balanceATIVO:.8f} {ATIVO} = {eATIVO:.8f} BTC')

        # SOMA SALDO EQUIVALENTE EM BTC
        somaEqBTC_EXC += eATIVO
        c += 1

    ######################################################################

    print(f'\nSaldo inicial na EXC: {saldoInicial_EXC:.8f} BTC')
    print(f'Saldo atual na EXC: {somaEqBTC_EXC:.8f} BTC')

    # TELEGRAM
    # config.mensagem_telegram(f'
    # Saldo inicial na EXC: {saldoInicial_EXC:.8f} BTC \nSaldo atual na EXC: {somaEqBTC_EXC:.8f} BTC')

    # LOG
    log = open('logs/saldo.txt', 'a')
    log.write(f'Saldo inicial na EXC: {saldoInicial_EXC:.8f} BTC \nSaldo atual na EXC: {somaEqBTC_EXC:.8f} BTC\n')
    log.write('-' * 10)
    log.write('\n')
    log.close()

    ######################################################################

    print('=' * 40)
    print('\n>> SALDO DISPONÍVEL:')

    # ATIVO = str(input('Qual ATIVO: '))
    ATIVO = ATIVO
    aBalance = key_secretEXC.get_balance(ATIVO)

    time.sleep(1)

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
        q1 = saldoDisponivelATIVO / minimaCompra_BTC_USDT
        q1 = int(q1)
        print(f'Valor ordem mínima: {minimaCompra_BTC_USDT:.8f}')
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
        quantidadeOrdem = minimaCompra_BTC_USDT

        rangeFinal = rangeFinal

        while rateOrdem > rangeFinal:
            rateOrdem = rateOrdem - spreadRange
            rateAMI = rateOrdem - (spreadRange * 1)
            # rateAMI = rateOrdem - (spreadRange * 2)
            print(f'Comprar por: {rateAMI:.8f} / Vender por: {rateOrdem:.8f}')

            criaOrdem = key_secretEXC.buy_limitami('BTC_USDT', rateAMI, rateOrdem, quantidadeOrdem)
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

    print('-' * 40)

    print('\n>> VENDA\n')
    print('ATENÇÃO: Digite apenas números!!!\n')
    print('>> VALOR FINAL: Até qual preço deseja vender (Ex: 15000)')
    rangeFinal = input('Digite aqui: ')
    rangeFinal = float(rangeFinal)

    print('\nSPREAD em % (Ex: 0.25)')
    porcentagemSpread = input('Digite aqui: ')
    porcentagemSpread = float(porcentagemSpread)
    print('=' * 20)

    ######################################################################

    print('=' * 40)
    # EXC
    print('\n> EXC <')

    # Consulta informações Balances
    rBalances = key_secretEXC.get_balances()
    # print(rBalances)

    # Quantidade de Ativos na EXC
    nATIVOS = len(rBalances['result'])
    print(f'Quantidade de Ativos: {nATIVOS}')

    c = 0
    somaEqBTC_EXC = 0

    while c < nATIVOS:
        ATIVO = rBalances['result'][c]['Asset']
        balanceATIVO = rBalances['result'][c]['Balance']
        eATIVO = rBalances['result'][c]['BtcEquivalent']
        print(f'{balanceATIVO:.8f} {ATIVO} = {eATIVO:.8f} BTC')

        # SOMA SALDO EQUIVALENTE EM BTC
        somaEqBTC_EXC += eATIVO
        c += 1

    ######################################################################

    print(f'\nSaldo inicial na EXC: {saldoInicial_EXC:.8f} BTC')
    print(f'Saldo atual na EXC: {somaEqBTC_EXC:.8f} BTC')

    # TELEGRAM
    # config.mensagem_telegram(f'Saldo inicial na EXC: {saldoInicial_EXC:.8f} BTC \nSaldo atual na EXC: {somaEqBTC_EXC:.8f} BTC')

    # LOG
    log = open('logs/saldo.txt', 'a')
    log.write(f'Saldo inicial na EXC: {saldoInicial_EXC:.8f} BTC \nSaldo atual na EXC: {somaEqBTC_EXC:.8f} BTC\n')
    log.write('-' * 10)
    log.write('\n')
    log.close()

    ######################################################################

    print('=' * 40)
    print('\n>> SALDO DISPONÍVEL:')

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
        q1 = saldoDisponivelATIVO / minimaCompra_BTC_USDT
        q1 = int(q1)
        print(f'Valor ordem mínima: {minimaCompra_BTC_USDT}')
        print(f'Quantidade de ordens Mínimas: {q1}')

        # INTERVALOS EM % ORDENS
        spreadRange = vendaAtivoEXC * (porcentagemSpread / 100)
        print(f'SPREAD de {porcentagemSpread}% em USDT: {spreadRange}\n')

        somasv = spreadRange + vendaAtivoEXC
        # print(f'Range inicial: {somasv}')

        time.sleep(1)

        # CRIAR ORDENS
        print('>> CRIAR ORDENS:\n')

        ativoMercado = ativoMercado

        rateOrdem = vendaAtivoEXC - (spreadRange * 3)
        quantidadeOrdem = minimaCompra_BTC_USDT

        rangeFinal = rangeFinal

        while rateOrdem < rangeFinal:
            rateOrdem = rateOrdem + spreadRange
            rateAMI = rateOrdem + (spreadRange * 2)
            print(f'Vender por: {rateAMI:.8f} / Comprar por: {rateOrdem:.8f}')

            criaOrdem = key_secretEXC.sell_limitami('BTC_USDT', rateAMI, rateOrdem, quantidadeOrdem)
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


else:
    print('\n>> ATENÇÃO <<\nPor favor, digite: COMPRA ou VENDA.\n')




