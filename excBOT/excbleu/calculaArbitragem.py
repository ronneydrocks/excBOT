import config
import requests
import json


print('\n<< CALCULADORA DE ARBITRAGEM >>\n\n>> MERCADO: BTC_USDT')

print('\n--------------------\n')

print('>> VALORES:')

precoCompra = input('Digite o preço de compra: ')
precoCompra = float(precoCompra)
print(f'Compra: {precoCompra}\n')

precoVenda = float(input('Digite o preço de Venda: '))
precoVenda = float(precoVenda)
print(f'Venda: {precoVenda}\n')

quantidade = float(input('Digite a quantidade: '))  # Quantidade em Bitcoin tem q transformar para USDT
quantidade = float(quantidade)
print(f'Quantidade: {quantidade:.8f} BTC\n')

fee = 0.25
print(f'Fee taker/maker: {fee}')

urlPrecoBitcoin = config.coinGecko_BTC_USD
r = requests.get(urlPrecoBitcoin)
j = json.loads(r.text)
precoBitcoin = j['bitcoin']['usd']

print(f'Preço do Bitcoin: ${precoBitcoin}\n')

print('\n--------------------\n')
print('>> SPREAD:')
spreadUSDT = precoVenda - precoCompra
print(f'Spread: {spreadUSDT} USDT')

spreadPorcentagem = (precoVenda - precoCompra) / precoCompra * 100
print(f'Spread: {spreadPorcentagem:.2f}%')

spreadBTC = spreadUSDT / precoBitcoin
print(f'Spread {spreadBTC:.8f} BTC')

print('\n--------------------\n')
print('>> COMPRA:')
feeCompra = (fee / 100) * quantidade
feeCompra = feeCompra * precoVenda

precoCompraFee = (quantidade * precoBitcoin) + feeCompra
print(f'Valor Total: {precoCompraFee:.8f} USDT')
totalReceberCompra = precoCompraFee - feeCompra
print(f'Valor Receber: {totalReceberCompra:.8f} USDT')

print(f'Fee: {feeCompra:.8f} USDT')

print('\n--------------------\n')

print('>> VENDA:')
feeVenda = (fee / 100) * quantidade
feeVenda = feeVenda * precoCompra

precoVendaFee = (quantidade * precoBitcoin) + feeVenda
print(f'Valor Total: {precoVendaFee:.8f} USDT')
totalReceberVenda = precoVendaFee - feeVenda
print(f'Valor Receber: {totalReceberVenda:.8f} USDT')

print(f'Fee: {feeVenda:.8f} USDT')

print('\n--------------------\n')

print('>> RESUMO: ')

print(f'Comprando: {precoCompra} USDT')
print(f'Vendendo: {precoVenda} USDT')
print(f'Quantidade: {quantidade:.8f} BTC')
quantidadeUSDT = quantidade * precoBitcoin
print(f'Quantidade: {quantidadeUSDT:.8f} USDT')

print('\n--------------------\n')

print('>> ARBITRAGEM')

# arbitragem
arbitragem = (quantidade * precoVenda) - (quantidade * precoCompra)
arbitragem = arbitragem - (feeCompra + feeVenda)
print(f'Arbitragem: {arbitragem:.8f} USDT')
feeTotal = feeCompra + feeVenda
print(f'Fee Total: {feeTotal:.8f} USDT')
