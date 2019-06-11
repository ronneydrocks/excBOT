import requests
import json


#########################################
# VOLUME BTC
#########################################
getMarketSummaries = 'https://trade.exccripto.com/api/v3/public/getmarketsummaries?basemarket=BTC'
r = requests.get(getMarketSummaries)
j = json.loads(r.text)
# print(j)
#########################################
print('=' * 40)
#########################################
# Quantidade de Ativos na EXC
baseAsset = j['result'][0]['BaseAsset']
baseAssetName = j['result'][0]['BaseAssetName']
nATIVOS = len(j['result'])
print(f'\nMercado {baseAssetName}: {nATIVOS} Ativos\n')

c = 0
somaEqBTC_EXC = 0

while c < nATIVOS:
    marketName = j['result'][c]['MarketName']
    volume = j['result'][c]['Volume']
    marketAsset = j['result'][c]['MarketAsset']
    baseAsset = j['result'][c]['BaseAsset']
    baseVolume = j['result'][c]['BaseVolume']

    # SOMA SALDO EQUIVALENTE EM BTC
    somaEqBTC_EXC += baseVolume
    c += 1

    print(f'{marketName} \nVolume em {marketAsset}: {volume} \nVolume em {baseAsset}: {baseVolume}\n')

print(f'\nSoma volume em {baseAsset}: {somaEqBTC_EXC:.8f}\n')
print('=' * 40)

#########################################
# VOLUME DOGE
#########################################
getMarketSummaries = 'https://trade.exccripto.com/api/v3/public/getmarketsummaries?basemarket=DOGE'
r = requests.get(getMarketSummaries)
j = json.loads(r.text)
# print(j)
#########################################
print('=' * 40)
#########################################
# Quantidade de Ativos na EXC
baseAsset = j['result'][0]['BaseAsset']
baseAssetName = j['result'][0]['BaseAssetName']
nATIVOS = len(j['result'])
print(f'\nMercado {baseAssetName}: {nATIVOS} Ativos\n')

c = 0
somaEqBTC_EXC = 0

while c < nATIVOS:
    marketName = j['result'][c]['MarketName']
    volume = j['result'][c]['Volume']
    marketAsset = j['result'][c]['MarketAsset']
    baseAsset = j['result'][c]['BaseAsset']
    baseVolume = j['result'][c]['BaseVolume']

    # SOMA SALDO EQUIVALENTE EM BTC
    somaEqBTC_EXC += baseVolume
    c += 1

    print(f'{marketName} \nVolume em {marketAsset}: {volume} \nVolume em {baseAsset}: {baseVolume}\n')

print(f'\nSoma volume em {baseAsset}: {somaEqBTC_EXC:.8f}\n')
print('=' * 40)

#########################################
# VOLUME USDT
#########################################
getMarketSummaries = 'https://trade.exccripto.com/api/v3/public/getmarketsummaries?basemarket=USDT'
r = requests.get(getMarketSummaries)
j = json.loads(r.text)
# print(j)
#########################################
print('=' * 40)
#########################################
# Quantidade de Ativos na EXC
baseAsset = j['result'][0]['BaseAsset']
baseAssetName = j['result'][0]['BaseAssetName']
nATIVOS = len(j['result'])
print(f'\nMercado {baseAssetName}: {nATIVOS} Ativo\n')

c = 0
somaEqBTC_EXC = 0

while c < nATIVOS:
    marketName = j['result'][c]['MarketName']
    volume = j['result'][c]['Volume']
    marketAsset = j['result'][c]['MarketAsset']
    baseAsset = j['result'][c]['BaseAsset']
    baseVolume = j['result'][c]['BaseVolume']

    # SOMA SALDO EQUIVALENTE EM BTC
    somaEqBTC_EXC += baseVolume
    c += 1

    print(f'{marketName} \nVolume em {marketAsset}: {volume} \nVolume em {baseAsset}: {baseVolume}\n')

print(f'\nSoma volume em {baseAsset}: {somaEqBTC_EXC:.8f}\n')
print('=' * 40)

