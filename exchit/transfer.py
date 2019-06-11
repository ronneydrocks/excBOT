import config
import excBot
import hitBOT
import time
import hmac
import requests
import hashlib


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

print('=' * 40)
print('excBOT v0.1.1\nFerramenta de Transferenência')
print('=' * 40)

acao = 0
while acao != 99:
    print('''    Escolha uma opção:

    EXC/HIT
    [1] DOGE
    [2] SMART
    [3] WAVES
    
    HIT/EXC
    [1] DOGE
    [2] SMART
    [3] WAVES
    
    [99] Sair''')

    acao = int(input('\nO que deseja fazer?: '))

    if acao == 1:
        print('DOGE')

        quantidade_transferirEXCHIT = float(input('\nQual a quantidade para transferir: '))

        #################
        # AÇÃO: TRANSFERE EXC para HIT
        print(f'TRANSFERINDO... {quantidade_transferirEXCHIT} DOGE')
        wCOMPRA = str(quantidade_transferirEXCHIT)
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

    elif acao == 2:
        print('Mostrar Mercado Smartcash')

    elif acao == 3:
        print('Mostrar verifica mercado')

    elif acao == 99:
        print('Sair do Programa')

    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    time.sleep(2)

print('Fim do programa!')

