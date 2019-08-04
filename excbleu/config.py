import requests
import bleuBot
import excBot


################################################
#           EXC CRIPTO - CONFIG                #
################################################
emailEXC = '_EDITAR_AQUI_'                                        # EDITAR
keyEXC = '_EDITAR_AQUI_'                           # EDITAR
secretEXC = '_EDITAR_AQUI_'                # EDITAR
key_secretEXC = excBot.excBot(keyEXC, secretEXC, nonce=True)
################################################
#           BLEUTRADE - CONFIG                 #
################################################
emailBLEU = '_EDITAR_AQUI_'                                    # EDITAR
keyBLEU = '_EDITAR_AQUI_'                        # EDITAR
secretBLEU = '_EDITAR_AQUI_'             # EDITAR
key_secretBLEU = bleuBot.bleuBot(keyBLEU, secretBLEU, nonce=True)
################################################
#           TELEGRAM - CONFIG                  #
################################################
bot_id_telegram = '_EDITAR_AQUI_'
chat_id = '_EDITAR_AQUI_'
################################################
#           COTAÇÃO BRL - CoinGecko            #
################################################
urlBTC_BRL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl'
coinGecko_BTC_USD = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
################################################
#           SALDO INICIAL EM BTC               #
################################################
saldoInicial_EXC = 0.00000000                                       # EDITAR
saldoInicial_BLEU = 0.00000000                                      # EDITAR
################################################
#           GLOBAL - PESSOAL                   #
################################################

# CANCELA ORDEM - Habilitado 1 / Desabilitado 0
funCancelaOrdens = 0

# AUTO BALANCE - Habilitado 1 / Desabilitado 0
funAutoBalance = 1

# COMPRA MÍNIMA - Habilitado 1 / Desabilitado 0
funCompraMinima = 1

######### SPREAD BTC 16/07/2019 ########

# SPREAD BTC
spread_ETH_BTC = 0.00012720       # EDITAR (opcional)
spread_LTC_BTC = 0.00006000       # EDITAR (opcional)

# Mínina BTC
minimaCompra_ETH_BTC = 0.00550000           # EDITAR (opcional)
minimaCompra_LTC_BTC = 0.01200000           # EDITAR (opcional)

######### SPREAD USDT 16/07/2019 ########

# SPREAD USDT
spread_BTC_USDT = 60.00000000    # EDITAR (opcional)

# Mínina USDT
minimaCompra_BTC_USDT = 0.00020000         # EDITAR (opcional)

# FEE exchanges
feeEXC = 0.25
feeBLEU = 0.25

################################################
#           EXC CRIPTO - LINKS                 #
################################################

# ETH_BTC
urlGettickerEXC_ETH_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=ETH_BTC'

urlGetOrderBookEXC_BUY_ETH_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=ETH_BTC&type=BUY'
urlGetOrderBookEXC_SELL_ETH_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=ETH_BTC&type=SELL'

# LTC_BTC
urlGettickerEXC_LTC_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=LTC_BTC'

urlGetOrderBookEXC_BUY_LTC_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=LTC_BTC&type=BUY'
urlGetOrderBookEXC_SELL_LTC_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=LTC_BTC&type=SELL'

############ USDT ###########

# BTC_USDT
urlGettickerEXC_BTC_USDT = 'https://trade.exccripto.com/api/v3/public/getticker?market=BTC_USDT'

urlGetOrderBookEXC_BUY_BTC_USDT = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=BTC_USDT&type=BUY'
urlGetOrderBookEXC_SELL_BTC_USDT = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=BTC_USDT&type=SELL'

################################################
#           BLEUTRADE - LINKS                  #
################################################

# ETH_BTC
urlGettickerBLEU_ETH_BTC = 'https://bleutrade.com/api/v3/public/getticker?market=ETH_BTC'

urlGetOrderBookBLEU_BUY_ETH_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=ETH_BTC&type=BUY'
urlGetOrderBookBLEU_SELL_ETH_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=ETH_BTC&type=SELL'

# LTC_BTC
urlGettickerBLEU_LTC_BTC = 'https://bleutrade.com/api/v3/public/getticker?market=LTC_BTC'

urlGetOrderBookBLEU_BUY_LTC_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=LTC_BTC&type=BUY'
urlGetOrderBookBLEU_SELL_LTC_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=LTC_BTC&type=SELL'

############ USDT ###########

# BTC_USDT
urlGettickerBLEU_BTC_USDT = 'https://bleutrade.com/api/v3/public/getticker?market=BTC_USDT'

urlGetOrderBookBLEU_BUY_BTC_USDT = 'https://bleutrade.com/api/v3/public/getorderbook?market=BTC_USDT&type=BUY'
urlGetOrderBookBLEU_SELL_BTC_USDT = 'https://bleutrade.com/api/v3/public/getorderbook?market=BTC_USDT&type=SELL'

################################################
#           GLOBAL - CONFIG                    #
################################################

# Tempo para NOVA verificação em segundos
tempoVerificacao = 1  # segundos

########################################################################

# TELEGRAM LOG BOT
def mensagem_telegram(acao):
    urlTelegramAPI = 'https://api.telegram.org/bot' + bot_id_telegram + '/sendMessage?chat_id=' + chat_id + '&text=' + acao
    requests.get(urlTelegramAPI).json()

########################################################################
