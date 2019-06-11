import requests
import json
import bleuBot
import excBot
import time
import hmac
import hashlib
import datetime
import config


# BLEUTRADE
emailBLEU = config.emailBLEU
keyBLEU = config.keyBLEU
secretBLEU = config.secretBLEU

key_secretBLEU = bleuBot.bleuBot(keyBLEU, secretBLEU, nonce=True)

# EXC CRIPTO
emailEXC = config.emailEXC
keyEXC = config.keyEXC
secretEXC = config.secretEXC

key_secretEXC = excBot.excBot(keyEXC, secretEXC, nonce=True)

# diferença entre os preços em DOGE
diferencaSatoshi_ETH_DOGE = config.diferencaSatoshi_ETH_DOGE

# minina
minimaCompra_ETH_DOGE = config.minimaCompra_ETH_DOGE

# tempo de verificação em segundos
tempoVerificacao = config.tempoVerificacao

########################################################################

while True:
    try:
        contador = 0
        while contador <= 1000000:
            contador += 1
            print(f'\nVERIFICAÇÃO: {contador}')
            dataEhora = datetime.datetime.now()
            dataEhora = dataEhora.strftime('%d/%m/%Y %H:%M')
            print(f'{dataEhora}')

            for contagem in range(10, -1, -1):
                time.sleep(tempoVerificacao)
                print('', end='.')

            ############################
            # LOG
            log = open('logs/ETH_DOGE.txt', 'a')
            log.write('#' * 40)
            log.write(f'\nVerificação: {contador}\n')
            log.write(f'Data/Hora: {dataEhora}\n')
            log.write('-' * 10)
            log.write('\n')
            log.close()
            ############################

            ########################################################################
            print('\n')
            print('-x-' * 20)
            ########################################################################

            # print('\n >> QUANTIDADES << \n')

            urlGetOrderBookBLEU_BUY_ETH_DOGE = config.urlGetOrderBookBLEU_BUY_ETH_DOGE
            rBLEU = requests.get(urlGetOrderBookBLEU_BUY_ETH_DOGE)
            jBLEU = json.loads(rBLEU.text)
            quantidade_comprandoBLEU = jBLEU['result']['buy'][0]['Quantity']

            urlGetOrderBookBLEU_SELL_ETH_DOGE = config.urlGetOrderBookBLEU_SELL_ETH_DOGE
            rBLEU = requests.get(urlGetOrderBookBLEU_SELL_ETH_DOGE)
            jBLEU = json.loads(rBLEU.text)
            quantidade_vendendoBLEU = jBLEU['result']['sell'][0]['Quantity']

            urlGetOrderBookEXC_BUY_ETH_DOGE = config.urlGetOrderBookEXC_BUY_ETH_DOGE
            rEXC = requests.get(urlGetOrderBookEXC_BUY_ETH_DOGE)
            jEXC = json.loads(rEXC.text)
            quantidade_comprandoEXC = jEXC['result']['buy'][0]['Quantity']

            urlGetOrderBookEXC_SELL_ETH_DOGE = config.urlGetOrderBookEXC_SELL_ETH_DOGE
            rEXC = requests.get(urlGetOrderBookEXC_SELL_ETH_DOGE)
            jEXC = json.loads(rEXC.text)
            quantidade_vendendoEXC = jEXC['result']['sell'][0]['Quantity']

            # print('-' * 10)

            # print('\nMERCADO EXC: ETH_DOGE')
            urlGettickerEXC = config.urlGettickerEXC_ETH_DOGE
            requisicaoEXC = requests.get(urlGettickerEXC)
            dicionarioEXC = json.loads(requisicaoEXC.text)

            lastAtivoEXC = float(dicionarioEXC['result'][0]['Last'])
            # print(f'Última: {lastAtivoEXC:.8f}')
            compraAtivoEXC = float(dicionarioEXC['result'][0]['Bid'])
            vendaAtivoEXC = float(dicionarioEXC['result'][0]['Ask'])

            # print('-' * 10)

            # print('\nMERCADO BLEU: ETH_DOGE')
            urlGettickerBLEU = config.urlGettickerBLEU_ETH_DOGE
            requisicaoBLEU = requests.get(urlGettickerBLEU)
            dicionarioBLEU = json.loads(requisicaoBLEU.text)

            lastAtivoBLEU = float(dicionarioBLEU['result'][0]['Last'])
            # print(f'Última: {lastAtivoBLEU:.8f}')
            compraAtivoBLEU = float(dicionarioBLEU['result'][0]['Bid'])
            vendaAtivoBLEU = float(dicionarioBLEU['result'][0]['Ask'])

####################################################################################
# COMPRAR na BLEU, VENDER na EXC 1
####################################################################################

            print('=' * 40)
            print(f'\n<< VERIFICANDO >> COMPRAR na BLEU, para VENDER na EXC\n')
            print('MERCADO BLEU: ETH_DOGE')
            print(f'Compra: {compraAtivoBLEU:.8f} / Quantidade: {quantidade_comprandoBLEU:.8f}')
            print(f'Venda: {vendaAtivoBLEU:.8f} / Quantidade: {quantidade_vendendoBLEU:.8f}')

            time.sleep(2)

            if vendaAtivoBLEU < compraAtivoEXC and compraAtivoEXC - vendaAtivoBLEU > diferencaSatoshi_ETH_DOGE:
                ########################
                #     OPORTUNIDADE     #
                ########################
                print(f'\n>> OPORTUNIDADE << VENDA na BLEU mais barata que COMPRA na EXC e diferença acima de: {diferencaSatoshi_ETH_DOGE:.8f} satoshi\n')

                # VARIAÇÃO PERCENTUAL
                vPercentual = (compraAtivoEXC - vendaAtivoBLEU) / vendaAtivoBLEU * 100
                print(f'>> VALORES: \nComprar por: {vendaAtivoBLEU:.8f} \nVende por: {compraAtivoEXC:.8f} \nQuantidade de:{quantidade_vendendoBLEU:.8f}\n')
                print(f'>> LUCRO: {vPercentual:.2f}%\n')

                if float(quantidade_vendendoBLEU) < float(quantidade_comprandoEXC):

                    print(f'>> AÇÃO:\nComprando na BLEU... {quantidade_vendendoBLEU:.8f}')

##########################################################################################
# EDIT 1            # AÇÃO COMPRA - Faz COMPRA na BLEU: MOEDA_MERCADO, PREÇO, QUANTIDADE #
##########################################################################################

                    faz_compraBLEU = key_secretBLEU.buy_limit('ETH_DOGE', vendaAtivoBLEU, quantidade_vendendoBLEU)
                    # print(faz_compraBLEU['result'])
                    print(faz_compraBLEU)
                    respostaResult = faz_compraBLEU['result']

                    # Mensagem Telegram
                    config.mensagem_telegram('__' * 15)
                    config.mensagem_telegram('>> OPORTUNIDADE BLEU <<\nMercado: ETH_DOGE\n')
                    config.mensagem_telegram(f'>> VALORES: \nCompra: {vendaAtivoBLEU:.8f} \nVenda: {compraAtivoEXC:.8f} \nQuantidade: {quantidade_vendendoBLEU:.8f}\n')
                    config.mensagem_telegram(f'>> LUCRO: {vPercentual:.2f}%\n')
                    config.mensagem_telegram(f'>> AÇÃO:\nComprando na BLEU \nQuantidade: {quantidade_vendendoBLEU:.8f}\n{faz_compraBLEU}\n')

                    log = open('logs/ETH_DOGE.txt', 'a')
                    log.write(f'>> OPORTUNIDADE BLEU <<\nMercado: ETH_DOGE\n')
                    log.write(f'>> VALORES: \nCompra: {vendaAtivoBLEU:.8f} \nVenda: {compraAtivoEXC:.8f} \nQuantidade: {quantidade_vendendoBLEU:.8f}\n')
                    log.write(f'>> LUCRO: {vPercentual:.2f}%\n')
                    log.write('-' * 10)
                    log.write(f'>> AÇÃO:\nComprando na BLEU \nQuantidade: {quantidade_vendendoBLEU:.8f}\n{faz_compraBLEU}\n')
                    log.close()

                    for item in respostaResult:
                        if respostaResult == 'ERR_LOGIN_REQUIRED':
                            print('>> ERRO << Reiniciando verificação!')
                            break

                    # Recebe mensagem do saldo
                    respostaFazCompra = faz_compraBLEU['result']

                    # Verifica se o saldo é insuficiente e retorna uma mensagem
                    if respostaFazCompra == 'ERR_INSUFICIENT_BALANCE':
                        print('\nATENÇÃO >> SALDO INSUFICIENTE << \n')

                        ############################## MINIMA ########################################

                        ################################################################
                        # COMPRA QUANTIDADE MÍNIMA                                     #
                        # Faz COMPRA MÍNIMA na BLEU: MOEDA_MERCADO, PREÇO, QUANTIDADE  #
                        ################################################################
                        print(' >>> FAZENDO COMPRA MÍNIMA <<<\n')
                        faz_compra = key_secretBLEU.buy_limit('ETH_DOGE', vendaAtivoBLEU, minimaCompra_ETH_DOGE)
                        print(f'Comprando... {minimaCompra_ETH_DOGE:.8f} ETH')
                        print(faz_compra)

                        # Mensagem Telegram
                        config.mensagem_telegram('>>> FAZENDO COMPRA MÍNIMA <<<')
                        config.mensagem_telegram(f'>> VALORES: \nCompra: {vendaAtivoBLEU:.8f} \nVenda: {compraAtivoEXC:.8f} \nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n')
                        config.mensagem_telegram(f'>> AÇÃO:\nComprando na BLEU... {minimaCompra_ETH_DOGE:.8f}\n{faz_compra}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'>>> FAZENDO COMPRA MÍNIMA <<<\n')
                        log.write(f'>> VALORES: \nCompra: {vendaAtivoBLEU:.8f} \nVenda: {compraAtivoEXC:.8f} \nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n')
                        log.write('-' * 10)
                        log.write(f'>> AÇÃO:\nComprando na BLEU... {minimaCompra_ETH_DOGE:.8f}\n{faz_compra}\n')
                        log.close()

                        ######################################
                        # TRANSFERÊNCIA QUANTIDADE MINIMA    #
                        # Faz TRANSFERÊNCIA da BLEU para EXC #
                        ######################################
                        print(f'\nTransferindo... {minimaCompra_ETH_DOGE:.8f} ETH')
                        mCOMPRA = str(minimaCompra_ETH_DOGE)
                        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(int(time.time())) + '&asset=ETH&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC
                        # sign
                        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
                        # Adding sign to header
                        headers = {'apisign': sign}
                        # Make request
                        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
                        print(response.json())

                        # Aguarda 2 segundos antes de executar a venda
                        time.sleep(2)

                        # Mensagem Telegram
                        config.mensagem_telegram('>> TRANSFERÊNCIA: BLEU para EXC')
                        config.mensagem_telegram(f'>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{response.json()}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'>> TRANSFERÊNCIA: BLEU para EXC\n')
                        log.write('-' * 10)
                        log.write(f'\n>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{response.json()}\n')
                        log.close()

                        ######################################################
                        # VENDA QUANTIDADE MÍNIMA                            #
                        # Faz VENDA na EXC: MOEDA_MERCADO, preço, quantidade #
                        ######################################################
                        print(f'\nVENDENDO... {minimaCompra_ETH_DOGE:.8f} ETH')
                        faz_vendaEXC = key_secretEXC.sell_limit('ETH_DOGE', compraAtivoEXC, minimaCompra_ETH_DOGE)
                        print(faz_vendaEXC)

                        # Mensagem Telegram
                        config.mensagem_telegram('>>> VENDA QUANTIDADE MÍNIMA <<<')
                        config.mensagem_telegram(f'>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{faz_vendaEXC}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'>>> VENDA QUANTIDADE MÍNIMA <<<\n')
                        log.write('-' * 10)
                        log.write(f'\n>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{faz_vendaEXC}\n')
                        log.close()

                        ############################## MINIMA ########################################

                        ############################## EQUILIBRA SALDO ###############################

                        print('---')
                        print('\n>>> EQUILIBRANDO SALDO <<<')

                        # Aguarda 2 segundos
                        time.sleep(2)

                        saldoDOGE_BLEU = key_secretBLEU.get_balance('DOGE')
                        saldoDOGE_BLEU = float(saldoDOGE_BLEU['result'][0]['Balance'])
                        print(f'Saldo na BLEU: {saldoDOGE_BLEU:.8f} DOGE')

                        saldoDOGE_EXC = key_secretEXC.get_balance('DOGE')
                        saldoDOGE_EXC = float(saldoDOGE_EXC['result'][0]['Balance'])
                        print(f'Saldo na EXC: {saldoDOGE_EXC:.8f} DOGE')

                        if saldoDOGE_BLEU > saldoDOGE_EXC:
                            print('\n>> ATENÇÃO<< Transferindo da BLEU para EXC\n')

                            # Aguarda 2 segundos
                            time.sleep(2)

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########
                            equilibraSaldo = (saldoDOGE_EXC + saldoDOGE_BLEU) / 2
                            equilibraSaldo = str(equilibraSaldo)
                            print(f'Transferindo... {equilibraSaldo} DOGE')

                            urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
                                int(
                                    time.time())) + '&asset=DOGE&quantity=' + equilibraSaldo + '&exchangeto=2&' + 'accountto=' + emailEXC

                            # sign
                            sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
                            # Adding sign to header
                            headers = {'apisign': sign}
                            # Make request
                            response = requests.get(url=urlDirecttransferBLEU, headers=headers)
                            print(response.json())

                            # Mostra saldo atualizado após transferência de equilíbrio
                            print(f'Saldo atualizado na EXC: {saldoDOGE_EXC:.8f} DOGE')
                            print(f'Saldo atualizado na BLEU: {saldoDOGE_BLEU:.8f} DOGE')

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                        elif saldoDOGE_BLEU < saldoDOGE_EXC:
                            print('\n>> ATENÇÃO << Transferindo da EXC para BLEU\n')

                            # Aguarda 2 segundos
                            time.sleep(2)

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                            equilibraSaldo = (saldoDOGE_BLEU + saldoDOGE_EXC) / 2
                            equilibraSaldo = str(equilibraSaldo)
                            print(f'Transferindo... {equilibraSaldo} DOGE')

                            urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
                                int(
                                    time.time())) + '&asset=DOGE&quantity=' + equilibraSaldo + '&exchangeto=1&' + 'accountto=' + emailBLEU

                            # sign
                            sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
                            # Adding sign to header
                            headers = {'apisign': sign}
                            # Make request
                            response = requests.get(url=urlDirecttransferEXC, headers=headers)
                            print(response.json())

                            # Mostra saldo atualizado após transferência de equilíbrio
                            print(f'Saldo atualizado na EXC: {saldoDOGE_EXC:.8f} DOGE')
                            print(f'Saldo atualizado na BLEU: {saldoDOGE_BLEU:.8f} DOGE')

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                        else:
                            print('>> SEM TRANSFERÊNCIA << Saldos iguais, ')

                        print('---')
                        ############################## EQUILIBRA SALDO ###############################

                    else:
                        ##################################
                        # TRANSFERÊNCIA                  #
                        # Transferência da BLEU para EXC #
                        ##################################
                        print('\nTransferindo da BLEU para EXC...')
                        mCOMPRA = str(quantidade_vendendoBLEU)
                        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(int(time.time())) + '&asset=ETH&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC

                        # sign
                        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
                        # Adding sign to header
                        headers = {'apisign': sign}
                        # Make request
                        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
                        print(response.json())

                        # Aguarda 2 segundos
                        time.sleep(2)

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Transferência da BLEU para EXC \nQuantidade: {quantidade_vendendoBLEU:.8f}\n{response.json()}')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write('-' * 10)
                        log.write(f'\nTransferência da BLEU para EXC \nQuantidade: {quantidade_vendendoBLEU:.8f}\n{response.json()}\n')
                        log.write('-' * 10)
                        log.write('\n')
                        log.close()

                        ##############################################################
                        # VENDA - Faz VENDA na EXC: MOEDA_MERCADO, preço, quantidade #
                        ##############################################################
                        print('\nVendendo na EXC...')
                        faz_vendaEXC = key_secretEXC.sell_limit('ETH_DOGE', compraAtivoEXC, quantidade_vendendoBLEU)
                        print(faz_vendaEXC)

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Faz VENDA na EXC \nQuantidade: {quantidade_vendendoBLEU:.8f}\n{faz_vendaEXC}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'Faz VENDA na EXC \nQuantidade: {quantidade_vendendoBLEU:.8f}\n{faz_vendaEXC}\n')
                        log.write('-' * 10)
                        log.write('\n')
                        log.close()

####################################################################################
# EDIT 1 - FIM                                                                     #
####################################################################################
####################################################################################
# COMPRAR na BLEU, VENDER na EXC 2                                                 #
####################################################################################

                elif float(quantidade_vendendoBLEU) > float(quantidade_comprandoEXC):
                    print(f'Comprando na BLEU... {quantidade_comprandoEXC:.8f}')

##########################################################################################
# EDIT 2            # AÇÃO COMPRA - Faz COMPRA na BLEU: MOEDA_MERCADO, PREÇO, QUANTIDADE #
##########################################################################################

                    faz_compraBLEU = key_secretBLEU.buy_limit('ETH_DOGE', vendaAtivoBLEU, quantidade_comprandoEXC)
                    # print(faz_compra['result'])
                    print(faz_compraBLEU)
                    respostaResult = faz_compraBLEU['result']

                    # Mensagem Telegram
                    config.mensagem_telegram('__' * 15)
                    config.mensagem_telegram('>> OPORTUNIDADE BLEU <<\nMercado: ETH_DOGE\n')
                    config.mensagem_telegram(f'>> VALORES: \nCompra: {vendaAtivoBLEU:.8f} \nVenda: {compraAtivoEXC:.8f} \nQuantidade: {quantidade_comprandoEXC:.8f}\n')
                    config.mensagem_telegram(f'>> LUCRO: {vPercentual:.2f}%\n')
                    config.mensagem_telegram(f'>> AÇÃO:\nComprando na BLEU \nQuantidade: {quantidade_comprandoEXC:.8f}\n{faz_compraBLEU}\n')

                    log = open('logs/ETH_DOGE.txt', 'a')
                    log.write(f'>> OPORTUNIDADE BLEU <<\nMercado: ETH_DOGE\n')
                    log.write(f'>> VALORES: \nCompra: {vendaAtivoBLEU:.8f} \nVenda: {compraAtivoEXC:.8f} \nQuantidade: {quantidade_comprandoEXC:.8f}\n')
                    log.write(f'>> LUCRO: {vPercentual:.2f}%\n')
                    log.write('-' * 10)
                    log.write(f'\n>> AÇÃO:\nComprando na BLEU \nQuantidade: {quantidade_comprandoEXC:.8f}\n{faz_compraBLEU}\n')
                    log.close()

                    for item in respostaResult:
                        if respostaResult == 'ERR_LOGIN_REQUIRED':
                            print('>> ERRO << Reiniciando verificação!')
                            break

                    # Recebe mensagem do saldo
                    respostaFazCompra = faz_compraBLEU['result']

                    # Verifica se o saldo é insuficiente e retorna uma mensagem
                    if respostaFazCompra == 'ERR_INSUFICIENT_BALANCE':
                        print('\nATENÇÃO >> SALDO INSUFICIENTE << \n')

                        ############################## MINIMA ########################################

                        ################################################################
                        # COMPRA QUANTIDADE MÍNIMA                                     #
                        # Faz COMPRA MÍNIMA na BLEU: MOEDA_MERCADO, PREÇO, QUANTIDADE  #
                        ################################################################
                        print(' >>> FAZENDO COMPRA MÍNIMA <<<\n')
                        faz_compra = key_secretBLEU.buy_limit('ETH_DOGE', vendaAtivoBLEU, minimaCompra_ETH_DOGE)
                        print(f'Comprando... {minimaCompra_ETH_DOGE:.8f} ETH')
                        print(faz_compra)

                        # Mensagem Telegram
                        config.mensagem_telegram('>>> FAZENDO COMPRA MÍNIMA <<<')
                        config.mensagem_telegram(f'>> VALORES: \nCompra: {vendaAtivoBLEU:.8f} \nVenda: {compraAtivoEXC:.8f} \nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n')
                        config.mensagem_telegram(f'>> AÇÃO:\nComprando na BLEU... {minimaCompra_ETH_DOGE:.8f}\n{faz_compra}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'>>> FAZENDO COMPRA MÍNIMA <<< \n')
                        log.write(f'>> VALORES: \nCompra: {vendaAtivoBLEU:.8f} \nVenda: {compraAtivoEXC:.8f} \nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n')
                        log.write('-' * 10)
                        log.write('>> AÇÃO:\nComprando na BLEU... {minimaCompra_ETH_DOGE:.8f}\n{faz_compra}\n')
                        log.close()

                        ######################################
                        # TRANSFERÊNCIA QUANTIDADE MINIMA    #
                        # Faz TRANSFERÊNCIA da BLEU para EXC #
                        ######################################
                        print(f'Transferindo... {minimaCompra_ETH_DOGE:.8f} ETH')
                        mCOMPRA = str(minimaCompra_ETH_DOGE)
                        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
                            int(
                                time.time())) + '&asset=ETH&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC
                        # sign
                        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
                        # Adding sign to header
                        headers = {'apisign': sign}
                        # Make request
                        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
                        print(response.json())

                        # Aguarda 2 segundos antes de executar a venda
                        time.sleep(2)

                        # Mensagem Telegram
                        config.mensagem_telegram('>> TRANSFERÊNCIA: BLEU para EXC')
                        config.mensagem_telegram(f'>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{response.json()}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'>> TRANSFERÊNCIA: BLEU para EXC\n')
                        log.write('-' * 10)
                        log.write(f'\n>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{response.json()}\n')
                        log.close()

                        ######################################################
                        # VENDA QUANTIDADE MÍNIMA                            #
                        # Faz VENDA na EXC: MOEDA_MERCADO, preço, quantidade #
                        ######################################################
                        print(f'Vendendo... {minimaCompra_ETH_DOGE:.8f} ETH')
                        faz_vendaEXC = key_secretEXC.sell_limit('ETH_DOGE', compraAtivoEXC, minimaCompra_ETH_DOGE)
                        print(faz_vendaEXC)

                        # Mensagem Telegram
                        config.mensagem_telegram('>>> VENDA QUANTIDADE MÍNIMA <<<')
                        config.mensagem_telegram(f'>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{faz_vendaEXC}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'>>> VENDA QUANTIDADE MÍNIMA <<<\n')
                        log.write('-' * 10)
                        log.write(f'\n>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{faz_vendaEXC}\n')
                        log.close()

                        ############################## MINIMA ########################################

                        ############################## EQUILIBRA SALDO ###############################

                        print('---')
                        print('\n>>> EQUILIBRANDO SALDO <<<')

                        # Aguarda 2 segundos
                        time.sleep(2)

                        saldoDOGE_BLEU = key_secretBLEU.get_balance('DOGE')
                        saldoDOGE_BLEU = float(saldoDOGE_BLEU['result'][0]['Balance'])
                        print(f'Saldo na BLEU: {saldoDOGE_BLEU:.8f} DOGE')

                        saldoDOGE_EXC = key_secretEXC.get_balance('DOGE')
                        saldoDOGE_EXC = float(saldoDOGE_EXC['result'][0]['Balance'])
                        print(f'Saldo na EXC: {saldoDOGE_EXC:.8f} DOGE')

                        if saldoDOGE_BLEU > saldoDOGE_EXC:
                            print('\n>> ATENÇÃO<< Transferindo da BLEU para EXC\n')

                            # Aguarda 2 segundos
                            time.sleep(2)

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########
                            equilibraSaldo = (saldoDOGE_EXC + saldoDOGE_BLEU) / 2
                            equilibraSaldo = str(equilibraSaldo)
                            print(f'Transferindo... {equilibraSaldo} DOGE')

                            urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
                                int(
                                    time.time())) + '&asset=DOGE&quantity=' + equilibraSaldo + '&exchangeto=2&' + 'accountto=' + emailEXC

                            # sign
                            sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(),
                                            hashlib.sha512).hexdigest()
                            # Adding sign to header
                            headers = {'apisign': sign}
                            # Make request
                            response = requests.get(url=urlDirecttransferBLEU, headers=headers)
                            print(response.json())

                            # Mostra saldo atualizado após transferência de equilíbrio
                            print(f'Saldo atualizado na EXC: {saldoDOGE_EXC:.8f} DOGE')
                            print(f'Saldo atualizado na BLEU: {saldoDOGE_BLEU:.8f} DOGE')

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                        elif saldoDOGE_BLEU < saldoDOGE_EXC:
                            print('\n>> ATENÇÃO << Transferindo da EXC para BLEU\n')

                            # Aguarda 2 segundos
                            time.sleep(2)

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                            equilibraSaldo = (saldoDOGE_BLEU + saldoDOGE_EXC) / 2
                            equilibraSaldo = str(equilibraSaldo)
                            print(f'Transferindo... {equilibraSaldo} DOGE')

                            urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
                                int(
                                    time.time())) + '&asset=DOGE&quantity=' + equilibraSaldo + '&exchangeto=1&' + 'accountto=' + emailBLEU

                            # sign
                            sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(),
                                            hashlib.sha512).hexdigest()
                            # Adding sign to header
                            headers = {'apisign': sign}
                            # Make request
                            response = requests.get(url=urlDirecttransferEXC, headers=headers)
                            print(response.json())

                            # Mostra saldo atualizado após transferência de equilíbrio
                            print(f'Saldo atualizado na EXC: {saldoDOGE_EXC:.8f} DOGE')
                            print(f'Saldo atualizado na BLEU: {saldoDOGE_BLEU:.8f} DOGE')

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                        else:
                            print('>> SEM TRANSFERÊNCIA << Saldos iguais, ')

                        print('---')
                        ############################## EQUILIBRA SALDO ###############################

                    else:
                        ##################################
                        # TRANSFERÊNCIA                  #
                        # Transferência da BLEU para EXC #
                        ##################################
                        print('\nTransferindo da BLEU para EXC...')
                        mCOMPRA = str(quantidade_comprandoEXC)
                        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
                            int(
                                time.time())) + '&asset=ETH&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC

                        # sign
                        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
                        # Adding sign to header
                        headers = {'apisign': sign}
                        # Make request
                        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
                        print(response.json())

                        # Aguarda 2 segundos
                        time.sleep(2)

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Transferência da BLEU para EXC \nQuantidade: {quantidade_comprandoEXC:.8f}\n{response.json()}')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write('-' * 10)
                        log.write(f'\nTransferência da BLEU para EXC \nQuantidade: {quantidade_comprandoEXC:.8f}\n{response.json()}\n')
                        log.write('-' * 10)
                        log.write('\n')
                        log.close()

                        ##############################################################
                        # VENDA - Faz VENDA na EXC: MOEDA_MERCADO, preço, quantidade #
                        ##############################################################
                        print('\nVendendo na EXC...')
                        faz_vendaEXC = key_secretEXC.sell_limit('ETH_DOGE', compraAtivoEXC, quantidade_comprandoEXC)
                        print(faz_vendaEXC)

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Faz VENDA na EXC \nQuantidade: {quantidade_comprandoEXC:.8f}\n{faz_vendaEXC}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'Faz VENDA na EXC \nQuantidade: {quantidade_comprandoEXC:.8f}\n{faz_vendaEXC}\n')
                        log.write('-' * 10)
                        log.write('\n')
                        log.close()

####################################################################################
# EDIT 2 - FIM                                                                     #
####################################################################################

            elif vendaAtivoBLEU < compraAtivoEXC and compraAtivoEXC - vendaAtivoBLEU < diferencaSatoshi_ETH_DOGE:
                print(f'\n>> AGUARDE << VENDA na BLEU mais barata que COMPRA na EXC, mas diferença abaixo de: {diferencaSatoshi_ETH_DOGE:.8f} satoshi\n')

            elif vendaAtivoBLEU > compraAtivoEXC:
                print('\n>> AGUARDE <<  Sem oportunidades.\n')

            else:
                print('\n>> AGUARDE <<  Valores igual!!!\n')

####################################################################################
# COMPRAR na EXC, VENDER na BLEU 1
####################################################################################
            print('-' * 40)
            print('\n<< VERIFICANDO >> COMPRAR na EXC, VENDER na BLEU\n')
            print('MERCADO EXC: ETH_DOGE')
            print(f'Compra: {compraAtivoEXC:.8f} / Quantidade: {quantidade_comprandoEXC:.8f}')
            print(f'Venda: {vendaAtivoEXC:.8f} / Quantidade: {quantidade_vendendoEXC:.8f}')

            time.sleep(2)

            if vendaAtivoEXC < compraAtivoBLEU and compraAtivoBLEU - vendaAtivoEXC > diferencaSatoshi_ETH_DOGE:
                ########################
                #     OPORTUNIDADE     #
                ########################
                print(f'\n>> OPORTUNIDADE << VENDA na EXC mais barata que COMPRA na BLEU e diferença acima de: {diferencaSatoshi_ETH_DOGE:.8f} satoshi\n')

                # VARIAÇÃO PERCENTUAL
                vPercentual = (compraAtivoBLEU - vendaAtivoEXC) / vendaAtivoEXC * 100
                print(f'>> VALORES: \nComprar por: {vendaAtivoEXC:.8f} \nVende por: {compraAtivoBLEU:.8f} \nQuantidade de: {quantidade_vendendoEXC:.8f}\n')
                print(f'>> LUCRO: {vPercentual:.2f}%\n')

                if float(quantidade_vendendoEXC) < float(quantidade_comprandoBLEU):
                    print(f'>> AÇÃO:\nComprando na EXC... {quantidade_vendendoEXC:.8f}')

####################################################################################
# EDIT 1            # COMPRA - Faz COMPRA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE #
####################################################################################
                    faz_compraEXC = key_secretEXC.buy_limit('ETH_DOGE', vendaAtivoBLEU, quantidade_vendendoEXC)
                    # print(faz_compra['result'])
                    print(faz_compraEXC)
                    respostaResult = faz_compraEXC['result']

                    # Mensagem Telegram
                    config.mensagem_telegram('__' * 15)
                    config.mensagem_telegram(f'>> OPORTUNIDADE EXC <<\nMercado: ETH_DOGE\n')
                    config.mensagem_telegram(f'>> VALORES: \nCompra: {vendaAtivoEXC:.8f} \nVenda: {compraAtivoBLEU:.8f} \nQuantidade: {quantidade_vendendoEXC:.8f}\n')
                    config.mensagem_telegram(f'>> LUCRO: {vPercentual:.2f}%\n')
                    config.mensagem_telegram(f'>> AÇÃO:\nComprando na EXC \nQuantidade: {quantidade_vendendoEXC:.8f}\n{faz_compraEXC}\n')

                    log = open('logs/ETH_DOGE.txt', 'a')
                    log.write(f'>> OPORTUNIDADE EXC <<\nMercado: ETH_DOGE\n')
                    log.write(f'>> VALORES: \nCompra: {vendaAtivoEXC:.8f} \nVenda: {compraAtivoBLEU:.8f} \nQuantidade: {quantidade_vendendoEXC:.8f}\n')
                    log.write(f'>> LUCRO: {vPercentual:.2f}%\n')
                    log.write('-' * 10)
                    log.write(f'\n>> AÇÃO:\nComprando na EXC \nQuantidade: {quantidade_vendendoEXC:.8f}\n{faz_compraEXC}\n')
                    log.close()

                    for item in respostaResult:
                        if respostaResult == 'ERR_LOGIN_REQUIRED':
                            print('>> ERRO << Reiniciando verificação!')
                            break

                    # recebe mensagem do saldo
                    respostaFazCompraEXC = faz_compraEXC['result']

                    # Verifica se o saldo é insuficiente e retorna uma mensagem
                    if respostaFazCompraEXC == 'ERR_INSUFICIENT_BALANCE':
                        print('\nATENÇÃO >> SALDO INSUFICIENTE << ')

                        ############################## MINIMA ########################################

                        ################################################################
                        # COMPRA QUANTIDADE MÍNIMA                                     #
                        # Faz COMPRA MÍNIMA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE   #
                        ################################################################
                        print(' >>> FAZENDO COMPRA MÍNIMA <<<\n')
                        faz_compra = key_secretEXC.buy_limit('ETH_DOGE', vendaAtivoEXC, minimaCompra_ETH_DOGE)
                        print(f'COMPRANDO... {minimaCompra_ETH_DOGE:.8f} ETH')
                        print(faz_compra)

                        # Mensagem Telegram
                        config.mensagem_telegram('>>> FAZENDO COMPRA MÍNIMA <<<')
                        config.mensagem_telegram(f'>> VALORES: \nCompra: {vendaAtivoEXC:.8f} \nVenda: {compraAtivoBLEU:.8f} \nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n')
                        config.mensagem_telegram(f'>> AÇÃO:\nComprando na EXC... {minimaCompra_ETH_DOGE:.8f}\n{faz_compra}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'>>> FAZENDO COMPRA MÍNIMA <<<\n')
                        log.write(f'>> VALORES: \nCompra: {vendaAtivoEXC:.8f} \nVenda: {compraAtivoBLEU:.8f} \nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n')
                        log.write('-' * 10)
                        log.write(f'\n>> AÇÃO:\nComprando na EXC... {minimaCompra_ETH_DOGE:.8f}\n{faz_compraEXC}\n')
                        log.close()

                        ######################################
                        # TRANSFERÊNCIA QUANTIDADE MINIMA    #
                        # Faz TRANSFERÊNCIA da EXC para BLEU #
                        ######################################
                        print(f'TRANSFERINDO... {minimaCompra_ETH_DOGE:.8f} ETH')
                        mCOMPRA = str(minimaCompra_ETH_DOGE)
                        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
                            int(
                                time.time())) + '&asset=ETH&quantity=' + mCOMPRA + '&exchangeto=1&' + 'accountto=' + emailBLEU

                        # sign
                        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
                        # Adding sign to header
                        headers = {'apisign': sign}
                        # Make request
                        response = requests.get(url=urlDirecttransferEXC, headers=headers)
                        print(response.json())

                        # Aguarda 2 segundos
                        time.sleep(2)

                        # Mensagem Telegram
                        config.mensagem_telegram('>> TRANSFERÊNCIA: EXC para BLEU')
                        config.mensagem_telegram(f'>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{response.json()}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'>> TRANSFERÊNCIA: EXC para BLEU\n')
                        log.write('-' * 10)
                        log.write(f'\n>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{response.json()}\n')
                        log.close()

                        ######################################################
                        # VENDA QUANTIDADE MÍNIMA                            #
                        # Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade #
                        ######################################################
                        print(f'VENDENDO... {minimaCompra_ETH_DOGE:.8f} ETH')
                        faz_vendaBLEU = key_secretBLEU.sell_limit('ETH_DOGE', compraAtivoBLEU, minimaCompra_ETH_DOGE)
                        print(faz_vendaBLEU)

                        # Mensagem Telegram
                        config.mensagem_telegram('>>> VENDA QUANTIDADE MÍNIMA <<<')
                        config.mensagem_telegram(f'>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{faz_vendaBLEU}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'>>> VENDA QUANTIDADE MÍNIMA <<<\n')
                        log.write('-' * 10)
                        log.write(f'\n>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{faz_vendaBLEU}\n')
                        log.close()

                        ############################## MINIMA ########################################

                        ############################## EQUILIBRA SALDO ###############################

                        print('---')
                        print(' >>> EQUILIBRANDO SALDO <<<')

                        # Aguarda 2 segundos
                        time.sleep(2)

                        saldoDOGE_BLEU = key_secretBLEU.get_balance('DOGE')
                        saldoDOGE_BLEU = float(saldoDOGE_BLEU['result'][0]['Balance'])
                        print(f'Saldo na BLEU: {saldoDOGE_BLEU:.8f} DOGE')

                        saldoDOGE_EXC = key_secretEXC.get_balance('DOGE')
                        saldoDOGE_EXC = float(saldoDOGE_EXC['result'][0]['Balance'])
                        print(f'Saldo na EXC: {saldoDOGE_EXC:.8f} DOGE')

                        if saldoDOGE_BLEU > saldoDOGE_EXC:
                            print('\n>> ATENÇÃO << Transferindo de BLEU para EXC\n')

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                            equilibraSaldo = (saldoDOGE_EXC + saldoDOGE_BLEU) / 2
                            equilibraSaldo = str(equilibraSaldo)
                            print(f'Transferindo... {equilibraSaldo} DOGE')

                            urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
                                int(
                                    time.time())) + '&asset=DOGE&quantity=' + equilibraSaldo + '&exchangeto=2&' + 'accountto=' + emailEXC

                            # sign
                            sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(),
                                            hashlib.sha512).hexdigest()
                            # Adding sign to header
                            headers = {'apisign': sign}
                            # Make request
                            response = requests.get(url=urlDirecttransferBLEU, headers=headers)
                            print(response.json())

                            # Mostra saldo atualizado após transferência de equilíbrio
                            print(f'Saldo atualizado na EXC: {saldoDOGE_EXC:.8f} DOGE')
                            print(f'Saldo atualizado na BLEU: {saldoDOGE_BLEU:.8f} DOGE')

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                        elif saldoDOGE_BLEU < saldoDOGE_EXC:
                            print('\n>> ATENÇÃO << Transferindo de EXC para BLEU\n')

                            # Aguarda 2 segundos
                            time.sleep(2)

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                            equilibraSaldo = (saldoDOGE_BLEU + saldoDOGE_EXC) / 2
                            equilibraSaldo = str(equilibraSaldo)
                            print(f'Transferindo: {equilibraSaldo} DOGE')

                            urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
                                int(
                                    time.time())) + '&asset=DOGE&quantity=' + equilibraSaldo + '&exchangeto=1&' + 'accountto=' + emailBLEU

                            # sign
                            sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(),
                                            hashlib.sha512).hexdigest()
                            # Adding sign to header
                            headers = {'apisign': sign}
                            # Make request
                            response = requests.get(url=urlDirecttransferEXC, headers=headers)
                            print(response.json())

                            # Mostra saldo atualizado após transferência de equilíbrio
                            print(f'Saldo atualizado na EXC: {saldoDOGE_EXC:.8f} DOGE')
                            print(f'Saldo atualizado na BLEU: {saldoDOGE_BLEU:.8f} DOGE')

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                        else:
                            print('>> SEM TRANSFERÊNCIA << Saldos iguais')

                        print('---')

                        ############################## EQUILIBRA SALDO ###############################

                    else:
                        ##################################
                        # TRANSFERENCIA                  #
                        # Transferência da EXC para BLEU #
                        ##################################
                        print(f'\nTransferindo... {quantidade_vendendoEXC:.8f}')
                        mCOMPRA2 = str(quantidade_vendendoEXC)
                        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
                            int(
                                time.time())) + '&asset=ETH&quantity=' + mCOMPRA2 + '&exchangeto=1&' + 'accountto=' + emailBLEU

                        # sign
                        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
                        # Adding sign to header
                        headers = {'apisign': sign}
                        # Make request
                        response = requests.get(url=urlDirecttransferEXC, headers=headers)
                        print(response.json())

                        # Aguarda 2 segundos
                        time.sleep(2)

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Transferência da EXC para BLEU \nQuantidade: {quantidade_vendendoEXC:.8f}\n{response.json()}')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write('-' * 10)
                        log.write(f'\nTransferência da EXC para BLEU \nQuantidade: {quantidade_vendendoEXC:.8f}\n{response.json()}\n')
                        log.write('-' * 10)
                        log.write('\n')
                        log.close()

                        ###############################################################
                        # VENDA - Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade #
                        ###############################################################
                        print(f'\nVendendo... {quantidade_vendendoEXC:.8f}')
                        faz_vendaBLEU = key_secretBLEU.sell_limit('ETH_DOGE', compraAtivoEXC, quantidade_vendendoEXC)
                        print(faz_vendaBLEU)

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Faz VENDA na BLEU \nQuantidade: {quantidade_vendendoEXC:.8f}\n{faz_vendaBLEU}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'Faz VENDA na BLEU \nQuantidade: {quantidade_vendendoEXC:.8f}\n{faz_vendaBLEU}\n')
                        log.write('-' * 10)
                        log.write('\n')
                        log.close()

####################################################################################
# EDIT 1 - FIM                                                                     #
####################################################################################
####################################################################################
# COMPRAR na EXC, VENDER na BLEU 2
####################################################################################

                elif float(quantidade_vendendoEXC) > float(quantidade_comprandoBLEU):
                    print(f'>> OPORTUNIDADE << Comprando na EXC... {quantidade_comprandoBLEU:.8f}')

####################################################################################
# EDIT 2            # COMPRA - Faz COMPRA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE #
####################################################################################
                    print(f'\nComprando... {quantidade_comprandoBLEU:.8f}')
                    faz_compraEXC = key_secretEXC.buy_limit('ETH_DOGE', vendaAtivoBLEU, quantidade_comprandoBLEU)
                    # print(faz_compra['result'])
                    print(faz_compraEXC)
                    respostaResult = faz_compraEXC['result']

                    # Mensagem Telegram
                    config.mensagem_telegram('__' * 15)
                    config.mensagem_telegram('>> OPORTUNIDADE EXC <<\nMercado: ETH_DOGE\n')
                    config.mensagem_telegram(f'>> VALORES: \nCompra: {vendaAtivoEXC:.8f} \nVenda: {compraAtivoBLEU:.8f} \nQuantidade: {quantidade_comprandoBLEU:.8f}\n')
                    config.mensagem_telegram(f'>> LUCRO: {vPercentual:.2f}%\n')
                    config.mensagem_telegram(f'>> AÇÃO:\nComprando na EXC \nQuantidade: {quantidade_comprandoBLEU:.8f}\n{faz_compraEXC}\n')

                    log = open('logs/ETH_DOGE.txt', 'a')
                    log.write(f'>> OPORTUNIDADE EXC <<\nMercado: ETH_DOGE\n')
                    log.write(f'>> VALORES: \nCompra: {vendaAtivoEXC:.8f} \nVenda: {compraAtivoBLEU:.8f} \nQuantidade: {quantidade_comprandoBLEU:.8f}\n')
                    log.write('-' * 10)
                    log.write(f'\n>> AÇÃO:\nComprando na EXC \nQuantidade: {quantidade_vendendoEXC:.8f}\n{faz_compraEXC}\n')
                    log.close()

                    for item in respostaResult:
                        if respostaResult == 'ERR_LOGIN_REQUIRED':
                            print('>> ERRO << Reiniciando verificação!')
                            break

                    # recebe mensagem do saldo
                    respostaFazCompraEXC = faz_compraEXC['result']

                    # Verifica se o saldo é insuficiente e retorna uma mensagem
                    if respostaFazCompraEXC == 'ERR_INSUFICIENT_BALANCE':
                        print('\nATENÇÃO >> SALDO INSUFICIENTE << ')

                        ############################## MINIMA ########################################

                        ################################################################
                        # COMPRA QUANTIDADE MÍNIMA                                     #
                        # Faz COMPRA MÍNIMA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE   #
                        ################################################################
                        print(' >>> FAZENDO COMPRA MÍNIMA <<<\n')
                        faz_compra = key_secretEXC.buy_limit('ETH_DOGE', vendaAtivoEXC, minimaCompra_ETH_DOGE)
                        print(f'COMPRANDO... {minimaCompra_ETH_DOGE:.8f} ETH')
                        print(faz_compra)

                        # Mensagem Telegram
                        config.mensagem_telegram('>>> FAZENDO COMPRA MÍNIMA <<<')
                        config.mensagem_telegram(f'>> VALORES: \nCompra: {vendaAtivoEXC:.8f} \nVenda: {compraAtivoBLEU:.8f} \nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n')
                        config.mensagem_telegram(f'>> AÇÃO:\nComprando na EXC... {minimaCompra_ETH_DOGE:.8f}\n{faz_compra}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'>>> FAZENDO COMPRA MÍNIMA <<<\n')
                        log.write(f'>> VALORES: \nCompra: {vendaAtivoEXC:.8f} \nVenda: {compraAtivoBLEU:.8f} \nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n')
                        log.write('-' * 10)
                        log.write(f'\n>> AÇÃO:\nComprando na EXC... {minimaCompra_ETH_DOGE:.8f}\n{faz_compra}\n')
                        log.close()

                        ######################################
                        # TRANSFERÊNCIA QUANTIDADE MINIMA    #
                        # Faz TRANSFERÊNCIA da EXC para BLEU #
                        ######################################
                        print(f'TRANSFERINDO... {minimaCompra_ETH_DOGE:.8f} ETH')
                        mCOMPRA = str(minimaCompra_ETH_DOGE)
                        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
                            int(
                                time.time())) + '&asset=ETH&quantity=' + mCOMPRA + '&exchangeto=1&' + 'accountto=' + emailBLEU

                        # sign
                        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
                        # Adding sign to header
                        headers = {'apisign': sign}
                        # Make request
                        response = requests.get(url=urlDirecttransferEXC, headers=headers)
                        print(response.json())

                        # Aguarda 2 segundos
                        time.sleep(2)

                        # Mensagem Telegram
                        config.mensagem_telegram('>> TRANSFERÊNCIA: EXC para BLEU')
                        config.mensagem_telegram(f'>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{response.json()}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'>> TRANSFERÊNCIA: EXC para BLEU\n')
                        log.write('-' * 10)
                        log.write(f'\n>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{response.json()}\n')
                        log.close()

                        ######################################################
                        # VENDA QUANTIDADE MÍNIMA                            #
                        # Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade #
                        ######################################################
                        print(f'VENDENDO... {minimaCompra_ETH_DOGE:.8f} ETH')
                        faz_vendaBLEU = key_secretBLEU.sell_limit('ETH_DOGE', compraAtivoBLEU, minimaCompra_ETH_DOGE)
                        print(faz_vendaBLEU)

                        # Mensagem Telegram
                        config.mensagem_telegram('>>> VENDA QUANTIDADE MÍNIMA <<<')
                        config.mensagem_telegram(f'>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{faz_vendaBLEU}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'>>> VENDA QUANTIDADE MÍNIMA <<<\n')
                        log.write('-' * 10)
                        log.write(f'\n>> AÇÃO:\nQuantidade: {minimaCompra_ETH_DOGE:.8f}\n{faz_vendaBLEU}\n')
                        log.close()

                        ############################## MINIMA ########################################

                        ############################## EQUILIBRA SALDO ###############################

                        print('---')
                        print(' >>> EQUILIBRANDO SALDO <<<')

                        # Aguarda 2 segundos
                        time.sleep(2)

                        saldoDOGE_BLEU = key_secretBLEU.get_balance('DOGE')
                        saldoDOGE_BLEU = float(saldoDOGE_BLEU['result'][0]['Balance'])
                        print(f'Saldo na BLEU: {saldoDOGE_BLEU:.8f} DOGE')

                        saldoDOGE_EXC = key_secretEXC.get_balance('DOGE')
                        saldoDOGE_EXC = float(saldoDOGE_EXC['result'][0]['Balance'])
                        print(f'Saldo na EXC: {saldoDOGE_EXC:.8f} DOGE')

                        if saldoDOGE_BLEU > saldoDOGE_EXC:
                            print('\n>> ATENÇÃO << Transferindo de BLEU para EXC\n')

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                            equilibraSaldo = (saldoDOGE_EXC + saldoDOGE_BLEU) / 2
                            equilibraSaldo = str(equilibraSaldo)
                            print(f'Transferindo... {equilibraSaldo} DOGE')

                            urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
                                int(
                                    time.time())) + '&asset=DOGE&quantity=' + equilibraSaldo + '&exchangeto=2&' + 'accountto=' + emailEXC

                            # sign
                            sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(),
                                            hashlib.sha512).hexdigest()
                            # Adding sign to header
                            headers = {'apisign': sign}
                            # Make request
                            response = requests.get(url=urlDirecttransferBLEU, headers=headers)
                            print(response.json())

                            # Mostra saldo atualizado após transferência de equilíbrio
                            print(f'Saldo atualizado na EXC: {saldoDOGE_EXC:.8f} DOGE')
                            print(f'Saldo atualizado na BLEU: {saldoDOGE_BLEU:.8f} DOGE')

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                        elif saldoDOGE_BLEU < saldoDOGE_EXC:
                            print('\n>> ATENÇÃO << Transferindo de EXC para BLEU\n')

                            # Aguarda 2 segundos
                            time.sleep(2)

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                            equilibraSaldo = (saldoDOGE_BLEU + saldoDOGE_EXC) / 2
                            equilibraSaldo = str(equilibraSaldo)
                            print(f'Transferindo: {equilibraSaldo} DOGE')

                            urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
                                int(
                                    time.time())) + '&asset=DOGE&quantity=' + equilibraSaldo + '&exchangeto=1&' + 'accountto=' + emailBLEU

                            # sign
                            sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(),
                                            hashlib.sha512).hexdigest()
                            # Adding sign to header
                            headers = {'apisign': sign}
                            # Make request
                            response = requests.get(url=urlDirecttransferEXC, headers=headers)
                            print(response.json())

                            # Mostra saldo atualizado após transferência de equilíbrio
                            print(f'Saldo atualizado na EXC: {saldoDOGE_EXC:.8f} DOGE')
                            print(f'Saldo atualizado na BLEU: {saldoDOGE_BLEU:.8f} DOGE')

                            ############ TRANSFERÊNCIA EQUILIBRA SALDO ##########

                        else:
                            print('>> SEM TRANSFERÊNCIA << Saldos iguais')

                        print('---')

                        ############################## EQUILIBRA SALDO ###############################

                    else:
                        ##################################
                        # TRANSFERENCIA                  #
                        # Transferência da EXC para BLEU #
                        ##################################
                        print(f'\nTransferindo... {quantidade_comprandoBLEU:.8f}')
                        mCOMPRA2 = str(quantidade_comprandoBLEU)
                        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
                            int(
                                time.time())) + '&asset=ETH&quantity=' + mCOMPRA2 + '&exchangeto=1&' + 'accountto=' + emailBLEU

                        # sign
                        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
                        # Adding sign to header
                        headers = {'apisign': sign}
                        # Make request
                        response = requests.get(url=urlDirecttransferEXC, headers=headers)
                        print(response.json())

                        # Aguarda 2 segundos
                        time.sleep(2)

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Transferência da EXC para BLEU \nQuantidade: {quantidade_comprandoBLEU:.8f}\n{response.json()}')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write('-' * 10)
                        log.write(f'\nTransferência da EXC para BLEU \nQuantidade: {quantidade_comprandoBLEU:.8f}\n{response.json()}\n')
                        log.write('-' * 10)
                        log.write('\n')
                        log.close()

                        ###############################################################
                        # VENDA - Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade #
                        ###############################################################
                        print(f'\nVendendo... {quantidade_comprandoBLEU:.8f}')
                        faz_vendaBLEU = key_secretBLEU.sell_limit('ETH_DOGE', compraAtivoEXC, quantidade_comprandoBLEU)
                        print(faz_vendaBLEU)

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Faz VENDA na BLEU \nQuantidade: {quantidade_comprandoBLEU:.8f}\n{faz_vendaBLEU}\n')

                        log = open('logs/ETH_DOGE.txt', 'a')
                        log.write(f'Faz VENDA na BLEU \nQuantidade: {quantidade_comprandoBLEU:.8f}\n{faz_vendaBLEU}\n')
                        log.write('-' * 10)
                        log.write('\n')
                        log.close()

####################################################################################
# EDIT 2 - FIM                                                                     #
####################################################################################

            elif vendaAtivoEXC < compraAtivoBLEU and compraAtivoBLEU - vendaAtivoEXC < diferencaSatoshi_ETH_DOGE:
                print(f'\n>> AGUARDE << Venda na EXC está mais barata que compra na BLEU, mas diferença abaixo de {diferencaSatoshi_ETH_DOGE:.8f} satoshi\n')

            elif vendaAtivoEXC > compraAtivoBLEU:
                print('\n>> AGUARDE << Sem oportunidades.\n')

            else:
                print('\n>> AGUARDE << Valores igual!!!\n')

            ########################################################################
            print('=' * 40)
            print('-x-' * 20, '\n')
            ########################################################################

    except Exception as e:
        print(f'Tipo de erro: {e}')
        log = open('logs/ETH_DOGE.txt', 'a')
        log.write(f'ERRO: {e}\n')
        log.close()
