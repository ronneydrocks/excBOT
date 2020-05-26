import excBot
import bleuBot
import requests
import json
import config
import datetime
import func


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

print('Ativo / Saldo Total / Saldo Disponível / Saldo em BTC\n')
while c < nATIVOS:
    ATIVO = rBalances['result'][c]['Asset']
    balanceATIVO = rBalances['result'][c]['Balance']
    eATIVO = rBalances['result'][c]['BtcEquivalent']

    print(f'{ATIVO} {balanceATIVO:.8f} = {eATIVO:.8f} BTC')

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

print(f'\nSaldo inicial na EXC: {saldoInicial_EXC:.8f} BTC')
print(f'Saldo atual na EXC: {somaEqBTC_EXC:.8f} BTC')

# TELEGRAM
config.mensagem_telegram(f'Saldo inicial na EXC: {saldoInicial_EXC:.8f} BTC \nSaldo atual na EXC: {somaEqBTC_EXC:.8f} BTC')

######################################################################
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

print('Ativo / Saldo Total / Saldo Disponível / Saldo em BTC\n')
while c < nATIVOS:

    ATIVO = rBalances['result'][c]['Asset']
    balanceATIVO = rBalances['result'][c]['Balance']
    eATIVO = rBalances['result'][c]['BtcEquivalent']
    print(f'{ATIVO} {balanceATIVO:.8f} = {eATIVO:.8f} BTC')

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

print(f'\nSaldo inicial na BLEU: {saldoInicial_BLEU:.8f} BTC')
print(f'Saldo atual na BLEU: {somaEqBTC_BLEU:.8f} BTC\n')

# TELEGRAM
config.mensagem_telegram(f'Saldo inicial na BLEU: {saldoInicial_BLEU:.8f} BTC \nSaldo atual na BLEU: {somaEqBTC_BLEU:.8f} BTC')

######################################################################
#   SOMA SALDOS
######################################################################
print('=' * 40)
saldoInicial = (saldoInicial_EXC) + (saldoInicial_BLEU)
somaEqBTC = (somaEqBTC_EXC) + (somaEqBTC_BLEU)

######################################################################
# profit
######################################################################
if saldoInicial < somaEqBTC:
    # PROFIT VARIAÇÃO PERCENTUAL
    profit_BTC_p = (somaEqBTC - saldoInicial) / saldoInicial * 100
    profit_BTC = somaEqBTC - saldoInicial

    print(f'Profit: {profit_BTC:.8f} BTC ({profit_BTC_p:.2f} %)\n')
else:
    # PROFIT VARIAÇÃO PERCENTUAL
    profit_BTC_p = (saldoInicial - somaEqBTC) / somaEqBTC * 100
    profit_BTC = saldoInicial - somaEqBTC

    print(f'Negativo: -{profit_BTC:.8f} BTC (-{profit_BTC_p:.2f} %)\n')

######################################################################
#   SALDO EM BRL
######################################################################

saldoAtual_BRL = somaEqBTC * BTC_BRL

######################################################################
######################################################################
if somaEqBTC > saldoInicial:
    lucro = somaEqBTC - saldoInicial
    lucroBRL = BTC_BRL * lucro
    print(f'Saldo Atual: {somaEqBTC:.8f} BTC (R$ {saldoAtual_BRL:.2f})')
    print(f'>> Lucro: {lucro:.8f} BTC (R$ {lucroBRL:.2f}) <<')

    # TELEGRAM
    config.mensagem_telegram(f'Saldo Atual: {somaEqBTC:.8f} \n>> Lucro BTC: {lucro:.8f} (R$ {lucroBRL:.2f}) <<')

    # GRAVA LOG WEB (saldo.txt)
    log = open('logs/saldo.txt', 'a')
    log.write(f'{dataEhora}, {saldoInicial:.8f}, {somaEqBTC:.8f}, {profit_BTC_p:.2f}, {saldoAtual_BRL:.2f}\n')
    log.close()

elif somaEqBTC < saldoInicial:
    preju = saldoInicial - somaEqBTC
    prejuBRL = BTC_BRL * preju
    print(f'Saldo Atual: {somaEqBTC:.8f}')
    print(f'>> Negativo em BTC: -{preju:.8f} (R$ -{prejuBRL:.2f}) <<')

    # TELEGRAM
    config.mensagem_telegram(f'Saldo Atual: {somaEqBTC:.8f} \n>> Negativo em BTC: -{preju:.8f} (R$ -{prejuBRL:.2f}) <<')

    # GRAVA LOG WEB (saldo.txt)
    log = open('logs/saldo.txt', 'a')
    log.write(f'{dataEhora}, {saldoInicial:.8f}, {somaEqBTC:.8f}, -{preju:.8f}, -{prejuBRL:.2f}\n')
    log.close()

print('=' * 40)

######################################################################
funVendeMercadoAlta = config.funVendeMercadoAlta
funcVendePrecoMercado = config.funcVendePrecoMercado
transferBE = config.transferBE
######################################################################
func.linhaTitulo1()
######################################################################
if funVendeMercadoAlta == 1:
    print('\nFUNÇÃO VMA (Venda no Mercado em Alta)\n')
    func.vendaMercadoNaAlta()
else:
    print('>> SEM AÇÃO << FUNÇÃO VMA (Venda no Mercado em Alta)')
######################################################################
if funcVendePrecoMercado == 1:
    print('\nFUNÇÃO VPM (Venda a Preço de Mercado)\n')
    func.vendaPrecoMercado()
else:
    print('>> SEM AÇÃO << FUNÇÃO VPM (Venda a Preço de Mercado)')
######################################################################
if transferBE == 1:
    print('\nFUNÇÃO TransferBE (Transfere BLEU para EXC)\n')
    func.transfer_BLEU_EXC('ETH')
    func.transfer_BLEU_EXC('LTC')
else:
    print('>> SEM AÇÃO << FUNÇÃO TransferBE (Transfere BLEU para EXC)')
######################################################################
func.linhaTitulo1()
######################################################################