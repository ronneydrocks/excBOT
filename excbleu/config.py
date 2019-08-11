import requests
import bleuBot
import excBot


################################################
#           EXC CRIPTO - CONFIG                #
################################################
emailEXC = '__EDITAR_AQUI__'                                 # EDITAR
keyEXC = '__EDITAR_AQUI__'                           # EDITAR
secretEXC = '__EDITAR_AQUI__'                # EDITAR
key_secretEXC = excBot.excBot(keyEXC, secretEXC, nonce=True)
################################################
#           BLEUTRADE - CONFIG                 #
################################################
emailBLEU = '__EDITAR_AQUI__'                                    # EDITAR
keyBLEU = '__EDITAR_AQUI__'                        # EDITAR
secretBLEU = '__EDITAR_AQUI__'             # EDITAR
key_secretBLEU = bleuBot.bleuBot(keyBLEU, secretBLEU, nonce=True)
################################################
#           TELEGRAM - CONFIG                  #
################################################
bot_id_telegram = '__EDITAR_AQUI__'
chat_id = '__EDITAR_AQUI__'
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

################ BTC ################
# SPREAD BTC
spread_ETH_BTC = 0.00012720       # EDITAR (opcional)
spread_LTC_BTC = 0.00006000       # EDITAR (opcional)
spread_DCR_BTC = 0.00001000       # EDITAR (opcional)
spread_SMART_BTC = 0.00000001     # EDITAR (opcional)
spread_USDT_BTC = 0.00001000      # EDITAR (opcional)
spread_DOGE_BTC = 0.000000009     # EDITAR (opcional)
spread_WAVES_BTC = 0.00001000     # EDITAR (opcional)
spread_BC_BTC = 0.000000009       # EDITAR (opcional)
# COMPRA MÍNIMA BTC
minimaCompra_ETH_BTC = 0.00600000           # EDITAR (opcional)
minimaCompra_LTC_BTC = 0.01500000           # EDITAR (opcional)
minimaCompra_DCR_BTC = 0.10000000           # EDITAR (opcional)
minimaCompra_SMART_BTC = 200.00000000       # EDITAR (opcional)
minimaCompra_USDT_BTC = 1.00000000          # EDITAR (opcional)
minimaCompra_DOGE_BTC = 500.00000000        # EDITAR (opcional)
minimaCompra_WAVES_BTC = 1.00000000         # EDITAR (opcional)
minimaCompra_BC_BTC = 5000.00000000         # EDITAR (opcional)

################ DOGE ################
# SPREAD DOGE
spread_DCR_DOGE = 100.00000000    # EDITAR (opcional)
spread_ETH_DOGE = 100.00000000    # EDITAR (opcional)
spread_LTC_DOGE = 100.00000000    # EDITAR (opcional)
spread_SMART_DOGE = 0.10000000    # EDITAR (opcional)
# COMPRA MÍNIMA DOGE
minimaCompra_DCR_DOGE = 0.01000000          # EDITAR (opcional)
minimaCompra_ETH_DOGE = 0.01000000          # EDITAR (opcional)
minimaCompra_LTC_DOGE = 0.01000000          # EDITAR (opcional)
minimaCompra_SMART_DOGE = 200.00000000       # EDITAR (opcional)

################ USDT ################
# SPREAD USDT
spread_BTC_USDT = 60.00000000    # EDITAR (opcional)
spread_ETH_USDT = 1.40000000    # EDITAR (opcional)
spread_LTC_USDT = 0.50000000    # EDITAR (opcional)
# COMPRA MÍNIMA USDT
minimaCompra_BTC_USDT = 0.00025000         # EDITAR (opcional)
minimaCompra_ETH_USDT = 0.0100000         # EDITAR (opcional)
minimaCompra_LTC_USDT = 0.0100000         # EDITAR (opcional)

##################################################################
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

# DCR_BTC
urlGettickerEXC_DCR_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=DCR_BTC'

urlGetOrderBookEXC_BUY_DCR_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DCR_BTC&type=BUY'
urlGetOrderBookEXC_SELL_DCR_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DCR_BTC&type=SELL'

# SMART_BTC
urlGettickerEXC_SMART_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=SMART_BTC'

urlGetOrderBookEXC_BUY_SMART_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=SMART_BTC&type=BUY'
urlGetOrderBookEXC_SELL_SMART_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=SMART_BTC&type=SELL'

# USDT_BTC
urlGettickerEXC_USDT_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=USDT_BTC'

urlGetOrderBookEXC_BUY_USDT_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=USDT_BTC&type=BUY'
urlGetOrderBookEXC_SELL_USDT_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=USDT_BTC&type=SELL'

# DOGE_BTC
urlGettickerEXC_DOGE_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=DOGE_BTC'

urlGetOrderBookEXC_BUY_DOGE_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DOGE_BTC&type=BUY'
urlGetOrderBookEXC_SELL_DOGE_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DOGE_BTC&type=SELL'

# ZCR_BTC
urlGettickerEXC_ZCR_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=ZCR_BTC'

urlGetOrderBookEXC_BUY_ZCR_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=ZCR_BTC&type=BUY'
urlGetOrderBookEXC_SELL_ZCR_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=ZCR_BTC&type=SELL'

# WAVES_BTC
urlGettickerEXC_WAVES_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=WAVES_BTC'

urlGetOrderBookEXC_BUY_WAVES_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=WAVES_BTC&type=BUY'
urlGetOrderBookEXC_SELL_WAVES_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=WAVES_BTC&type=SELL'

# BC_BTC
urlGettickerEXC_BC_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=BC_BTC'

urlGetOrderBookEXC_BUY_BC_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=BC_BTC&type=BUY'
urlGetOrderBookEXC_SELL_BC_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=BC_BTC&type=SELL'


############ DOGE ###########

# DCR_DOGE
urlGettickerEXC_DCR_DOGE = 'https://trade.exccripto.com/api/v3/public/getticker?market=DCR_DOGE'

urlGetOrderBookEXC_BUY_DCR_DOGE = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DCR_DOGE&type=BUY'
urlGetOrderBookEXC_SELL_DCR_DOGE = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DCR_DOGE&type=SELL'

# ETH_DOGE
urlGettickerEXC_ETH_DOGE = 'https://trade.exccripto.com/api/v3/public/getticker?market=ETH_DOGE'

urlGetOrderBookEXC_BUY_ETH_DOGE = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=ETH_DOGE&type=BUY'
urlGetOrderBookEXC_SELL_ETH_DOGE = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=ETH_DOGE&type=SELL'

# LTC_DOGE
urlGettickerEXC_LTC_DOGE = 'https://trade.exccripto.com/api/v3/public/getticker?market=LTC_DOGE'

urlGetOrderBookEXC_BUY_LTC_DOGE = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=LTC_DOGE&type=BUY'
urlGetOrderBookEXC_SELL_LTC_DOGE = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=LTC_DOGE&type=SELL'

# SMART_DOGE
urlGettickerEXC_SMART_DOGE = 'https://trade.exccripto.com/api/v3/public/getticker?market=SMART_DOGE'

urlGetOrderBookEXC_BUY_SMART_DOGE = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=SMART_DOGE&type=BUY'
urlGetOrderBookEXC_SELL_SMART_DOGE = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=SMART_DOGE&type=SELL'

############ USDT ###########

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

# ETH_USDT
urlGettickerBLEU_ETH_USDT = 'https://bleutrade.com/api/v3/public/getticker?market=ETH_USDT'

urlGetOrderBookBLEU_BUY_ETH_USDT = 'https://bleutrade.com/api/v3/public/getorderbook?market=ETH_USDT&type=BUY'
urlGetOrderBookBLEU_SELL_ETH_USDT = 'https://bleutrade.com/api/v3/public/getorderbook?market=ETH_USDT&type=SELL'

# LTC_USDT
urlGettickerBLEU_LTC_USDT = 'https://bleutrade.com/api/v3/public/getticker?market=LTC_USDT'

urlGetOrderBookBLEU_BUY_LTC_USDT = 'https://bleutrade.com/api/v3/public/getorderbook?market=LTC_USDT&type=BUY'
urlGetOrderBookBLEU_SELL_LTC_USDT = 'https://bleutrade.com/api/v3/public/getorderbook?market=LTC_USDT&type=SELL'

################################################
#           COTAÇÃO BRL - CoinGecko            #
################################################
urlBTC_BRL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl'
coinGecko_BTC_USD = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

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
