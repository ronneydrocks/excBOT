import requests
import bleuBot
import excBot


########################################################################
#                           EXC CRIPTO - CONFIG
########################################################################
emailEXC = '_EDITAR_AQUI_'                                        
keyEXC = '_EDITAR_AQUI_'                           
secretEXC = '_EDITAR_AQUI_' 
key_secretEXC = excBot.excBot(keyEXC, secretEXC, nonce=True)

feeEXC = 0.25

funMinima_EXC_BLEU_BTC_USDT = 1     # FUNÇÃO: MÍNIMA EXC/BLEU (BTC_USDT)
funMinima_EXC_BLEU_ETH_USDT = 1     # FUNÇÃO: MÍNIMA EXC/BLEU (ETH_USDT)

saldoInicial_EXC = 0.00000000   # SALDO INICIAL EM BTC
########################################################################
#           BLEUTRADE - CONFIG
########################################################################
emailBLEU = '_EDITAR_AQUI_'                                    
keyBLEU = '_EDITAR_AQUI_'                        
secretBLEU = '_EDITAR_AQUI_'  
key_secretBLEU = bleuBot.bleuBot(keyBLEU, secretBLEU, nonce=True)

feeBLEU = 0.25

funMinima_BLEU_EXC_BTC_USDT = 1     # FUNÇÃO: MÍNIMA BLEU/EXC (BTC_USDT)
funMinima_BLEU_EXC_ETH_USDT = 1     # FUNÇÃO: MÍNIMA BLEU/EXC (ETH_USDT)

saldoInicial_BLEU = 0.00000000  # SALDO INICIAL EM BTC
########################################################################
#           TELEGRAM - CONFIG
########################################################################
bot_id_telegram = '_EDITAR_AQUI_'
chat_id = '_EDITAR_AQUI_'
########################################################################
#           GLOBAL - CONFIG
########################################################################
tempoVerificacao = 0.2  # Tempo para NOVA verificação em segundos

# SPREAD BTC
spread_ETH_BTC = 0.00012720
spread_LTC_BTC = 0.00006000
spread_DOGE_BTC = 0.000000009
# MÍNIMA BTC
minima_ETH_BTC = 0.01000000
minima_LTC_BTC = 0.10000000
minima_DOGE_BTC = 500.00000000

# SPREAD USDT
spread_BTC_USDT = 60.00000000
spread_ETH_USDT = 1.40000000
spread_LTC_USDT = 0.50000000
# MÍNIMA USDT
minima_BTC_USDT = 0.00102000
minima_ETH_USDT = 0.06500000
minima_LTC_USDT = 0.10000000
minima_DOGE_USDT = 1000.00000000

# SPREAD cBRL
spread_BTC_CBRL = 500.00000000
spread_USDT_CBRL = 10.00000000
# MÍNIMA cBRL
minima_BTC_CBRL = 0.00022000
minima_USDT_CBRL = 3.50000000

########################################################################
# FUNÇÕES: Habilitado 1 / Desabilitado 0
########################################################################

funCancelaTodasOrdens_EXC_BLEU = 1  # FUNÇÃO CANCELA TODAS AS ORDENS ABERTAS
funAutoBalance_USDT = 1             # FUNÇÃO: AUTO BALANCE (USDT)

funVendeMercadoAlta = 0             # FUNÇÃO VMA (Venda no Mercado em Alta)
# funcVendePrecoMercado = 0           # FUNÇÃO VPM (Venda a Preço de Mercado)
transferBE = 0                      # FUNÇÃO TransferBE (Transfere BLEU para EXC)
# funcVendaQuantidadeMinima = 0       # FUNÇÃO VQM (Venda Quantidade Mínima)

########################################################################
# Config FUNÇÃO VPM
########################################################################
porcentagemDesejada = 2             # Quantos porcento de alta
porcentagemParaCompra = 0.5         # Quantos porcento abaixo do valor médio global
########################################################################
# ERRO
########################################################################
listaErro1 = 'ERR_LOW_VOLUME', 'ERR_INVALID_AMOUNT', 'ERR_LOGIN_REQUIRED'
listaErroMinima = 'ERR_LOW_VOLUME', 'ERR_INVALID_AMOUNT', 'ERR_LOGIN_REQUIRED', 'ERR_INSUFICIENT_BALANCE'
########################################################################

########################################################################
# EXC CRIPTO - LINKS
########################################################################
# ETH_BTC
urlGettickerEXC_ETH_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=ETH_BTC'
urlGetOrderBookEXC_BUY_ETH_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=ETH_BTC&type=BUY'
urlGetOrderBookEXC_SELL_ETH_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=ETH_BTC&type=SELL'
# LTC_BTC
urlGettickerEXC_LTC_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=LTC_BTC'
urlGetOrderBookEXC_BUY_LTC_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=LTC_BTC&type=BUY'
urlGetOrderBookEXC_SELL_LTC_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=LTC_BTC&type=SELL'
# DOGE_BTC
urlGettickerEXC_DOGE_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=DOGE_BTC'
urlGetOrderBookEXC_BUY_DOGE_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DOGE_BTC&type=BUY'
urlGetOrderBookEXC_SELL_DOGE_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DOGE_BTC&type=SELL'
########################################################################
# BTC_USDT
urlGettickerEXC_BTC_USDT = 'https://trade.exccripto.com/api/v3/public/getticker?market=BTC_USDT'
urlGetOrderBookEXC_BUY_BTC_USDT = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=BTC_USDT&type=BUY'
urlGetOrderBookEXC_SELL_BTC_USDT = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=BTC_USDT&type=SELL'
# ETH_ETH
urlGettickerEXC_ETH_USDT = 'https://trade.exccripto.com/api/v3/public/getticker?market=ETH_USDT'
urlGetOrderBookEXC_BUY_ETH_USDT = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=ETH_USDT&type=BUY'
urlGetOrderBookEXC_SELL_ETH_USDT = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=ETH_USDT&type=SELL'
# LTC_USDT
urlGettickerEXC_LTC_USDT = 'https://trade.exccripto.com/api/v3/public/getticker?market=LTC_USDT'
urlGetOrderBookEXC_BUY_LTC_USDT = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=LTC_USDT&type=BUY'
urlGetOrderBookEXC_SELL_LTC_USDT = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=LTC_USDT&type=SELL'
# DOGE_USDT
urlGettickerEXC_DOGE_USDT = 'https://trade.exccripto.com/api/v3/public/getticker?market=DOGE_USDT'
urlGetOrderBookEXC_BUY_DOGE_USDT = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DOGE_USDT&type=BUY'
urlGetOrderBookEXC_SELL_DOGE_USDT = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DOGE_USDT&type=SELL'
########################################################################
# BTC_CBRL
urlGettickerEXC_BTC_CBRL = 'https://trade.exccripto.com/api/v3/public/getticker?market=BTC_CBRL'
urlGetOrderBookEXC_BUY_BTC_CBRL = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=BTC_CBRL&type=BUY'
urlGetOrderBookEXC_SELL_BTC_CBRL = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=BTC_CBRL&type=SELL'
# USDT_CBRL
urlGettickerEXC_USDT_CBRL = 'https://trade.exccripto.com/api/v3/public/getticker?market=USDT_CBRL'
urlGetOrderBookEXC_BUY_USDT_CBRL = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=USDT_CBRL&type=BUY'
urlGetOrderBookEXC_SELL_USDT_CBRL = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=USDT_CBRL&type=SELL'
########################################################################
# BLEUTRADE - LINKS
########################################################################
# ETH_BTC
urlGettickerBLEU_ETH_BTC = 'https://bleutrade.com/api/v3/public/getticker?market=ETH_BTC'
urlGetOrderBookBLEU_BUY_ETH_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=ETH_BTC&type=BUY'
urlGetOrderBookBLEU_SELL_ETH_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=ETH_BTC&type=SELL'
# LTC_BTC
urlGettickerBLEU_LTC_BTC = 'https://bleutrade.com/api/v3/public/getticker?market=LTC_BTC'
urlGetOrderBookBLEU_BUY_LTC_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=LTC_BTC&type=BUY'
urlGetOrderBookBLEU_SELL_LTC_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=LTC_BTC&type=SELL'
########################################################################
# BTC_USDT
urlGettickerBLEU_BTC_USDT = 'https://bleutrade.com/api/v3/public/getticker?market=BTC_USDT'
urlGetOrderBookBLEU_BUY_BTC_USDT = 'https://bleutrade.com/api/v3/public/getorderbook?market=BTC_USDT&type=BUY'
urlGetOrderBookBLEU_SELL_BTC_USDT = 'https://bleutrade.com/api/v3/public/getorderbook?market=BTC_USDT&type=SELL'
# ETH_USDT
urlGettickerBLEU_ETH_USDT = 'https://bleutrade.com/api/v3/public/getticker?market=ETH_USDT'
urlGetOrderBookBLEU_BUY_ETH_USDT = 'https://bleutrade.com/api/v3/public/getorderbook?market=ETH_USDT&type=BUY'
urlGetOrderBookBLEU_SELL_ETH_USDT = 'https://bleutrade.com/api/v3/public/getorderbook?market=ETH_USDT&type=SELL'
# LTC_USDT
urlGettickerBLEU_LTC_USDT = 'https://bleutrade.com/api/v3/public/getticker?market=LTC_USDT'
urlGetOrderBookBLEU_BUY_LTC_USDT = 'https://bleutrade.com/api/v3/public/getorderbook?market=LTC_USDT&type=BUY'
urlGetOrderBookBLEU_SELL_LTC_USDT = 'https://bleutrade.com/api/v3/public/getorderbook?market=LTC_USDT&type=SELL'
########################################################################
# CoinGecko
########################################################################
urlBTC_BRL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl'
coinGecko_BTC_USD = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
# USD
urlCoinGecko_BTC_Change24h = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true'
urlCoinGecko_ETH_Change24h = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&include_24hr_change=true'
urlCoinGecko_LTC_Change24h = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd&include_24hr_change=true'
# BTC
urlCoinGecko_ETH_BTC_Change24h = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=btc&include_24hr_change=true'
urlCoinGecko_LTC_BTC_Change24h = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=btc&include_24hr_change=true'


########################################################################
# TELEGRAM LOG BOT
########################################################################


def mensagem_telegram(acao):
    urlTelegramAPI = 'https://api.telegram.org/bot' + bot_id_telegram + '/sendMessage?chat_id=' + chat_id + '&text=' + acao
    requests.get(urlTelegramAPI).json()
########################################################################
