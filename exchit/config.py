import excBot
import hitBOT

################################################
#           HITBTC - CONFIG                    #
################################################
public_keyHIT = "SUA_AQUI"           # EDITAR
secretHIT = "SUA_AQUI"            # EDITAR

addressSmartcashHIT = 'SUA_AQUI'  # EDITAR
addressDogecoinHIT = 'SUA_AQUI'    # EDITAR
addressWavesHIT = 'SUA_AQUI'    # EDITAR

client = hitBOT.Client("https://api.hitbtc.com", public_keyHIT, secretHIT)

################################################
#           CONFIG PESSOAL                     #
################################################

# Diferênça entre os valores em BTC
diferencaSatoshi_SMART_BTC = 0.00000001     	# EDITAR (opcional)
diferencaSatoshi_DOGE_BTC = 0.0000000010     	# EDITAR (opcional)
diferencaSatoshi_WAVES_BTC = 0.00001000     	# EDITAR (opcional)

# Mínina BTC
minimaCompra_SMART_BTC = 100.00000000		# EDITAR (opcional)
minimaCompra_DOGE_BTC = 200.00000000		# EDITAR (opcional)
minimaCompra_WAVES_BTC = 1.00000000		    # EDITAR (opcional)

################################################
#           EXC CRIPTO - CONFIG                #
################################################
emailEXC = 'SUA_AQUI'       # EDITAR
keyEXC = 'SUA_AQUI'                     # EDITAR
secretEXC = 'SUA_AQUI'          # EDITAR

addressSmartcashEXC = 'SUA_AQUI'      # EDITAR
addressDogecoinEXC = 'SUA_AQUI'       # EDITAR
addressWavesEXC = 'SUA_AQUI'          # EDITAR

key_secretEXC = excBot.excBot(keyEXC, secretEXC, nonce=True)

################################################
#           EXC CRIPTO - LINKS                 #
################################################

# SMART_BTC
urlGettickerEXC_SMART_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=SMART_BTC'
urlGetOrderBookEXC_market_SMART_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=SMART_BTC'
urlGetOrderBookEXC_BUY_SMART_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=SMART_BTC&type=BUY'
urlGetOrderBookEXC_SELL_SMART_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=SMART_BTC&type=SELL'

# DOGE_BTC
urlGettickerEXC_DOGE_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=DOGE_BTC'
urlGetOrderBookEXC_market_DOGE_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DOGE_BTC'
urlGetOrderBookEXC_BUY_DOGE_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DOGE_BTC&type=BUY'
urlGetOrderBookEXC_SELL_DOGE_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=DOGE_BTC&type=SELL'

# WAVES_BTC
urlGettickerEXC_WAVES_BTC = 'https://trade.exccripto.com/api/v3/public/getticker?market=WAVES_BTC'
urlGetOrderBookEXC_market_WAVES_BTC = 'https://trade.exccripto.com/api/v3/public/getorderbook?market=WAVES_BTC'

################################################
#           HITBTC - LINKS                     #
################################################

# SMART

urlGettickerHIT_SMART_BTC = 'https://api.hitbtc.com/api/2/public/orderbook/SMARTBTC'
urlGetOrderBookHIT_BUY_SMART_BTC = 'https://api.hitbtc.com/api/2/public/orderbook/SMARTBTC'
# urlGetOrderBookBuyHIT = 'https://api.hitbtc.com/api/2/public/orderbook/SMARTBTC'
# urlGettickerHIT = 'https://api.hitbtc.com/api/2/public/orderbook/SMARTBTC'

# DOGE
urlGettickerHIT_DOGE_BTC = 'https://api.hitbtc.com/api/2/public/orderbook/DOGEBTC'
urlGetOrderBookHIT_BUY_DOGE_BTC = 'https://api.hitbtc.com/api/2/public/orderbook/DOGEBTC'

# WAVES
urlGettickerHIT_WAVES_BTC = 'https://api.hitbtc.com/api/2/public/orderbook/WAVESBTC'
urlGetOrderBookHIT_BUY_WAVES_BTC = 'https://api.hitbtc.com/api/2/public/orderbook/WAVESBTC'

################################################
#           GLOBAL - CONFIG                    #
################################################

# Tempo para NOVA verificação em segundos
tempoVerificacao = 1.5  # segundos * 10s

# Confirmações Blockchain
tempoSmartcashBlockchain = 750  # segundos
tempoDogecoinBlockchain = 380  # segundos
tempoWavesBlockchain = 750  # segundos

# Taxas de saque SMART
feeSMART_EXC = 0.1
feeSMART_HIT = 0.4

# Taxas de saque DOGE
feeDOGE_EXC = 1
feeDOGE_HIT = 2

# Taxas de saque WAVES
feeWAVES_EXC = 0.1
feeWAVES_HIT = 0.4

################################################

