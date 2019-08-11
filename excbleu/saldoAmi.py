import excBot
import bleuBot
import requests
import json
import config
import datetime


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

# DATA/HORA
dataEhora = datetime.datetime.now()
dataEhora = dataEhora.strftime('%d/%m/%Y %H:%M')
print(f'{dataEhora}')

# TELEGRAM
config.mensagem_telegram('=' * 40)

# LOG
log = open('logs/saldo.txt', 'a')
log.write('#' * 40)
log.write(f'\nData/Hora: {dataEhora}\n')

#####################################

# 1BTC/BRL
urlBTC_BRL = config.urlBTC_BRL
r = requests.get(urlBTC_BRL)
j = json.loads(r.text)
# print(j)
BTC_BRL = j['bitcoin']['brl']
# print(BTC_BRL)

######################################################################

print('=' * 40)
# EXC
print('\n> EXC <')

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
config.mensagem_telegram(f'Saldo inicial na EXC: {saldoInicial_EXC:.8f} BTC \nSaldo atual na EXC: {somaEqBTC_EXC:.8f} BTC')

# LOG
log = open('logs/saldo.txt', 'a')
log.write(f'Saldo inicial na EXC: {saldoInicial_EXC:.8f} BTC \nSaldo atual na EXC: {somaEqBTC_EXC:.8f} BTC\n')
log.write('-' * 10)
log.write('\n')
log.close()

######################################################################
'''
print('=' * 40)
# BLEU
print('\n> BLEU <')

# Consulta informações Balances
rBalances = key_secretBLEU.get_balances()
# print(rBalances)

# Quantidade de Ativos na BLEU
nATIVOS = len(rBalances['result'])
# print(nATIVOS)

c = 0
somaEqBTC_BLEU = 0

while c < nATIVOS:
    ATIVO = rBalances['result'][c]['Asset']
    balanceATIVO = rBalances['result'][c]['Balance']
    eATIVO = rBalances['result'][c]['BtcEquivalent']
    print(f'{balanceATIVO:.8f} {ATIVO} = {eATIVO:.8f} BTC')

    # SOMA SALDO EQUIVALENTE EM BTC
    somaEqBTC_BLEU += eATIVO
    c += 1

######################################################################

print(f'\nSaldo inicial na BLEU: {saldoInicial_BLEU:.8f} BTC')
print(f'Saldo atual na BLEU: {somaEqBTC_BLEU:.8f} BTC\n')

# TELEGRAM
config.mensagem_telegram(f'Saldo inicial na BLEU: {saldoInicial_BLEU:.8f} BTC \nSaldo atual na BLEU: {somaEqBTC_BLEU:.8f} BTC')

# LOG
log = open('logs/saldo.txt', 'a')
log.write(f'Saldo inicial na BLEU: {saldoInicial_BLEU:.8f} BTC \nSaldo atual na BLEU: {somaEqBTC_BLEU:.8f} BTC\n')
log.write('-' * 10)
log.write('\n')
log.close()

######################################################################
print('=' * 40)
saldoInicial = (saldoInicial_EXC) + (saldoInicial_BLEU)
somaEqBTC = (somaEqBTC_EXC) + (somaEqBTC_BLEU)

if somaEqBTC > saldoInicial:
    lucro = somaEqBTC - saldoInicial
    lucroBRL = BTC_BRL * lucro
    print(f'Saldo Atual: {somaEqBTC:.8f}')
    print(f'>> Lucro BTC: {lucro:.8f} (R$ {lucroBRL:.2f}) <<')

    # TELEGRAM
    config.mensagem_telegram(f'Saldo Atual: {somaEqBTC:.8f} \n>> Lucro BTC: {lucro:.8f} (R$ {lucroBRL:.2f}) <<')

    # LOG
    log = open('logs/saldo.txt', 'a')
    log.write('=' * 40)
    log.write(f'\nSaldo Atual: {somaEqBTC:.8f} \n>> Lucro BTC: {lucro:.8f} (R$ {lucroBRL:.2f}) <<\n')
    log.write('=' * 40)
    log.write('\n')
    log.close()

elif somaEqBTC < saldoInicial:
    preju = saldoInicial - somaEqBTC
    prejuBRL = BTC_BRL * preju
    print(f'Saldo Atual: {somaEqBTC:.8f}')
    print(f'>> Negativo em BTC: {preju:.8f} (R$ {prejuBRL:.2f}) <<')

    # TELEGRAM
    config.mensagem_telegram(f'Saldo Atual: {somaEqBTC:.8f} \n>> Negativo em BTC: {preju:.8f} (R$ {prejuBRL:.2f}) <<')

    # LOG
    log = open('logs/saldo.txt', 'a')
    log.write('=' * 40)
    log.write(f'\nSaldo Atual: {somaEqBTC:.8f} \n>> Negativo em BTC: {preju:.8f} (R$ {prejuBRL:.2f}) <<\n')
    log.write('=' * 40)
    log.write('\n')
    log.close()

print('=' * 40)

######################################################################
'''
