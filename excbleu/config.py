import requests
import bleuBot
import excBot


################################################
#           EXC CRIPTO - CONFIG                #
################################################
emailEXC = 'EDITAR_AQUI'                                        # EDITAR
keyEXC = 'EDITAR_AQUI'                           # EDITAR
secretEXC = 'EDITAR_AQUI'                # EDITAR
key_secretEXC = excBot.excBot(keyEXC, secretEXC, nonce=True)
################################################
#           BLEUTRADE - CONFIG                 #
################################################
emailBLEU = 'EDITAR_AQUI'                                    # EDITAR
keyBLEU = 'EDITAR_AQUI'                        # EDITAR
secretBLEU = 'EDITAR_AQUI'             # EDITAR
key_secretBLEU = bleuBot.bleuBot(keyBLEU, secretBLEU, nonce=True)
################################################
#           TELEGRAM - CONFIG                  #
################################################
bot_id_telegram = 'EDITAR_AQUI'
chat_id = 'EDITAR_AQUI'
################################################
#           COTAÇÃO BRL - CoinGecko            #
################################################
urlBTC_BRL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl'
################################################
#           SALDO INICIAL EM BTC               #
################################################
saldoInicial_EXC = 0.00000000                                       # EDITAR
saldoInicial_BLEU = 0.00000000                                      # EDITAR
################################################
#           GLOBAL - PESSOAL                   #
################################################

######### DIFERÊNÇA BTC 09/04/2019 ########

# Diferênça entre os valores em BTC
diferencaSatoshi_DCR_BTC = 0.00001000       # EDITAR (opcional)
diferencaSatoshi_ETH_BTC = 0.00001000       # EDITAR (opcional)
diferencaSatoshi_LTC_BTC = 0.00001000       # EDITAR (opcional)
diferencaSatoshi_SMART_BTC = 0.00000002     # EDITAR (opcional)
diferencaSatoshi_USDT_BTC = 0.00001000      # EDITAR (opcional)
diferencaSatoshi_DOGE_BTC = 0.000000009     # EDITAR (opcional)
diferencaSatoshi_WAVES_BTC = 0.00001000     # EDITAR (opcional)
diferencaSatoshi_BC_BTC = 0.000000009       # EDITAR (opcional)

# Mínina BTC
minimaCompra_DCR_BTC = 0.02200000           # EDITAR (opcional)
minimaCompra_ETH_BTC = 0.00500000           # EDITAR (opcional)
minimaCompra_LTC_BTC = 0.00800000           # EDITAR (opcional)
minimaCompra_SMART_BTC = 100.00000000       # EDITAR (opcional)
minimaCompra_USDT_BTC = 0.43000000          # EDITAR (opcional)
minimaCompra_DOGE_BTC = 200.00000000        # EDITAR (opcional)
minimaCompra_WAVES_BTC = 0.50000000         # EDITAR (opcional)
minimaCompra_BC_BTC = 1500.00000000         # EDITAR (opcional)

######### DIFERÊNÇA DOGE 09/04/2019 ########

# Diferênça entre os valores em DOGE
diferencaSatoshi_DCR_DOGE = 100.00000000    # EDITAR (opcional)
diferencaSatoshi_ETH_DOGE = 100.00000000    # EDITAR (opcional)
diferencaSatoshi_LTC_DOGE = 100.00000000    # EDITAR (opcional)
diferencaSatoshi_SMART_DOGE = 0.10000000    # EDITAR (opcional)
diferencaSatoshi_USDT_DOGE = 0.10000000     # EDITAR (opcional)

# Mínina DOGE
minimaCompra_DCR_DOGE = 0.00100000          # EDITAR (opcional)
minimaCompra_ETH_DOGE = 0.00010000          # EDITAR (opcional)
minimaCompra_LTC_DOGE = 0.00100000          # EDITAR (opcional)
minimaCompra_SMART_DOGE = 10.00000000       # EDITAR (opcional)
minimaCompra_USDT_DOGE = 0.30000000         # EDITAR (opcional)

######### DIFERÊNÇA USDT 31/05/2019 ########

# Diferênça entre os valores em USDT
diferencaSatoshi_BTC_USDT = 10.00000000    # EDITAR (opcional)

# Mínina USDT
minimaCompra_BTC_USDT = 0.00010000         # EDITAR (opcional)

################################################
#           EXC CRIPTO - LINKS                 #
################################################

# DCR_BTC
urlGettickerEXC_DCR_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=DCR_BTC'

urlGetOrderBookEXC_BUY_DCR_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DCR_BTC&type=BUY'
urlGetOrderBookEXC_SELL_DCR_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DCR_BTC&type=SELL'

# ETH_BTC
urlGettickerEXC_ETH_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=ETH_BTC'

urlGetOrderBookEXC_BUY_ETH_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=ETH_BTC&type=BUY'
urlGetOrderBookEXC_SELL_ETH_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=ETH_BTC&type=SELL'

# LTC_BTC
urlGettickerEXC_LTC_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=LTC_BTC'

urlGetOrderBookEXC_BUY_LTC_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=LTC_BTC&type=BUY'
urlGetOrderBookEXC_SELL_LTC_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=LTC_BTC&type=SELL'

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

# USDT_DOGE
urlGettickerEXC_USDT_DOGE = 'https://trade.exccripto.com/api/v3/public/getticker?market=USDT_DOGE'

urlGetOrderBookEXC_BUY_USDT_DOGE = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=USDT_DOGE&type=BUY'
urlGetOrderBookEXC_SELL_USDT_DOGE = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=USDT_DOGE&type=SELL'

# WAVES_DOGE
urlGettickerEXC_WAVES_DOGE = 'https://trade.exccripto.com/api/v3/public/getticker?market=WAVES_DOGE'

urlGetOrderBookEXC_BUY_WAVES_DOGE = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=WAVES_DOGE&type=BUY'
urlGetOrderBookEXC_SELL_WAVES_DOGE = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=WAVES_DOGE&type=SELL'


############ USDT ###########

# BTC_USDT
urlGettickerEXC_BTC_USDT = 'https://trade.exccripto.com/api/v3/public/getticker?market=BTC_USDT'

urlGetOrderBookEXC_BUY_BTC_USDT = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=BTC_USDT&type=BUY'
urlGetOrderBookEXC_SELL_BTC_USDT = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=BTC_USDT&type=SELL'

################################################
#           BLEUTRADE - LINKS                  #
################################################

# DCR_BTC
urlGettickerBLEU_DCR_BTC = 'https://bleutrade.com/api/v3/public/getticker?market=DCR_BTC'

urlGetOrderBookBLEU_BUY_DCR_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=DCR_BTC&type=BUY'
urlGetOrderBookBLEU_SELL_DCR_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=DCR_BTC&type=SELL'

# ETH_BTC
urlGettickerBLEU_ETH_BTC = 'https://bleutrade.com/api/v3/public/getticker?market=ETH_BTC'

urlGetOrderBookBLEU_BUY_ETH_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=ETH_BTC&type=BUY'
urlGetOrderBookBLEU_SELL_ETH_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=ETH_BTC&type=SELL'

# LTC_BTC
urlGettickerBLEU_LTC_BTC = 'https://bleutrade.com/api/v3/public/getticker?market=LTC_BTC'

urlGetOrderBookBLEU_BUY_LTC_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=LTC_BTC&type=BUY'
urlGetOrderBookBLEU_SELL_LTC_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=LTC_BTC&type=SELL'

# SMART_BTC
urlGettickerBLEU_SMART_BTC = 'https://bleutrade.com/api/v3/public/getticker?market=SMART_BTC'

urlGetOrderBookBLEU_BUY_SMART_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=SMART_BTC&type=BUY'
urlGetOrderBookBLEU_SELL_SMART_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=SMART_BTC&type=SELL'

# USDT_BTC
urlGettickerBLEU_USDT_BTC = 'https://bleutrade.com/api/v3/public/getticker?market=USDT_BTC'

urlGetOrderBookBLEU_BUY_USDT_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=USDT_BTC&type=BUY'
urlGetOrderBookBLEU_SELL_USDT_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=USDT_BTC&type=SELL'

# DOGE_BTC
urlGettickerBLEU_DOGE_BTC = 'https://bleutrade.com/api/v3/public/getticker?market=DOGE_BTC'

urlGetOrderBookBLEU_BUY_DOGE_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=DOGE_BTC&type=BUY'
urlGetOrderBookBLEU_SELL_DOGE_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=DOGE_BTC&type=SELL'

# WAVES_BTC
urlGettickerBLEU_WAVES_BTC = 'https://bleutrade.com/api/v3/public/getticker?market=WAVES_BTC'

urlGetOrderBookBLEU_BUY_WAVES_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=WAVES_BTC&type=BUY'
urlGetOrderBookBLEU_SELL_WAVES_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=WAVES_BTC&type=SELL'

# BC_BTC
urlGettickerBLEU_BC_BTC = 'https://bleutrade.com/api/v3/public/getticker?market=BC_BTC'

urlGetOrderBookBLEU_BUY_BC_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=BC_BTC&type=BUY'
urlGetOrderBookBLEU_SELL_BC_BTC = 'https://bleutrade.com/api/v3/public/getorderbook?market=BC_BTC&type=SELL'

############ DOGE ###########

# DCR_DOGE
urlGettickerBLEU_DCR_DOGE = 'https://bleutrade.com/api/v3/public/getticker?market=DCR_DOGE'

urlGetOrderBookBLEU_BUY_DCR_DOGE = 'https://bleutrade.com/api/v3/public/getorderbook?market=DCR_DOGE&type=BUY'
urlGetOrderBookBLEU_SELL_DCR_DOGE = 'https://bleutrade.com/api/v3/public/getorderbook?market=DCR_DOGE&type=SELL'

# ETH_DOGE
urlGettickerBLEU_ETH_DOGE = 'https://bleutrade.com/api/v3/public/getticker?market=ETH_DOGE'

urlGetOrderBookBLEU_BUY_ETH_DOGE = 'https://bleutrade.com/api/v3/public/getorderbook?market=ETH_DOGE&type=BUY'
urlGetOrderBookBLEU_SELL_ETH_DOGE = 'https://bleutrade.com/api/v3/public/getorderbook?market=ETH_DOGE&type=SELL'

# LTC_DOGE
urlGettickerBLEU_LTC_DOGE = 'https://bleutrade.com/api/v3/public/getticker?market=LTC_DOGE'

urlGetOrderBookBLEU_BUY_LTC_DOGE = 'https://bleutrade.com/api/v3/public/getorderbook?market=LTC_DOGE&type=BUY'
urlGetOrderBookBLEU_SELL_LTC_DOGE = 'https://bleutrade.com/api/v3/public/getorderbook?market=LTC_DOGE&type=SELL'

# SMART_DOGE
urlGettickerBLEU_SMART_DOGE = 'https://bleutrade.com/api/v3/public/getticker?market=SMART_DOGE'

urlGetOrderBookBLEU_BUY_SMART_DOGE = 'https://bleutrade.com/api/v3/public/getorderbook?market=SMART_DOGE&type=BUY'
urlGetOrderBookBLEU_SELL_SMART_DOGE = 'https://bleutrade.com/api/v3/public/getorderbook?market=SMART_DOGE&type=SELL'

# USDT_DOGE
urlGettickerBLEU_USDT_DOGE = 'https://bleutrade.com/api/v3/public/getticker?market=USDT_DOGE'

urlGetOrderBookBLEU_BUY_USDT_DOGE = 'https://bleutrade.com/api/v3/public/getorderbook?market=USDT_DOGE&type=BUY'
urlGetOrderBookBLEU_SELL_USDT_DOGE = 'https://bleutrade.com/api/v3/public/getorderbook?market=USDT_DOGE&type=SELL'

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
