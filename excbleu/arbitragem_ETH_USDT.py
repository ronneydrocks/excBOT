import requests
import json
import bleuBot
import excBot
import time
import hmac
import hashlib
import datetime
import config
import func


########################################################################
# EXC CRIPTO
########################################################################
emailEXC = config.emailEXC
keyEXC = config.keyEXC
secretEXC = config.secretEXC
key_secretEXC = excBot.excBot(keyEXC, secretEXC, nonce=True)

feeEXC = config.feeEXC
funMinima_BLEU_EXC_ETH_USDT = config.funMinima_BLEU_EXC_ETH_USDT
########################################################################
# BLEUTRADE
########################################################################
emailBLEU = config.emailBLEU
keyBLEU = config.keyBLEU
secretBLEU = config.secretBLEU
key_secretBLEU = bleuBot.bleuBot(keyBLEU, secretBLEU, nonce=True)

feeBLEU = config.feeBLEU
funMinima_EXC_BLEU_ETH_USDT = config.funMinima_EXC_BLEU_ETH_USDT
########################################################################
# GLOBAL
########################################################################
spread_ETH_USDT = config.spread_ETH_USDT    # SPREAD entre os preços em USDT
minima_ETH_USDT = config.minima_ETH_USDT    # COMPRA MÍNIMA
tempoVerificacao = config.tempoVerificacao  # TEMPORIZADOR DA VERIFICAÇÃO
########################################################################
# FUNÇÕES
########################################################################
funCancelaTodasOrdens_EXC_BLEU = config.funCancelaTodasOrdens_EXC_BLEU    
funAutoBalance_USDT = config.funAutoBalance_USDT 
funVendeMercadoAlta = config.funVendeMercadoAlta   

# funcVendaQuantidadeMinima = config.funcVendaQuantidadeMinima    
########################################################################
# ERRO
########################################################################
listaErro1 = config.listaErro1
listaErroMinima = config.listaErroMinima
########################################################################

while True:
    try:
        contador = 0
        while contador <= 1000000:
            contador += 1
            print('=' * 50)
            print(f'\nVERIFICAÇÃO: {contador}')
            dataEhora = datetime.datetime.now()
            dataEhora = dataEhora.strftime('%d/%m/%Y %H:%M')
            print(f'{dataEhora}')

            for contagem in range(10, -1, -1):
                time.sleep(tempoVerificacao)
                print('', end='.')

            ########################################################################
            print('\n')
            print('=' * 50)
            ########################################################################

            url_vETH_USDT = config.urlGettickerEXC_ETH_USDT
            r_vETH_USDT = requests.get(url_vETH_USDT)
            j_vETH_USDT = json.loads(r_vETH_USDT.text)
            vETH_USDT = j_vETH_USDT['result'][0]['Last']

            urlGetOrderBookBLEU_BUY_ETH_USDT = config.urlGetOrderBookBLEU_BUY_ETH_USDT
            rBLEU = requests.get(urlGetOrderBookBLEU_BUY_ETH_USDT)
            jBLEU = json.loads(rBLEU.text)
            quantidade_comprandoBLEU = jBLEU['result']['buy'][0]['Quantity']

            urlGetOrderBookBLEU_SELL_ETH_USDT = config.urlGetOrderBookBLEU_SELL_ETH_USDT
            rBLEU = requests.get(urlGetOrderBookBLEU_SELL_ETH_USDT)
            jBLEU = json.loads(rBLEU.text)
            quantidade_vendendoBLEU = jBLEU['result']['sell'][0]['Quantity']

            urlGetOrderBookEXC_BUY_ETH_USDT = config.urlGetOrderBookEXC_BUY_ETH_USDT
            rEXC = requests.get(urlGetOrderBookEXC_BUY_ETH_USDT)
            jEXC = json.loads(rEXC.text)
            quantidade_comprandoEXC = jEXC['result']['buy'][0]['Quantity']

            urlGetOrderBookEXC_SELL_ETH_USDT = config.urlGetOrderBookEXC_SELL_ETH_USDT
            rEXC = requests.get(urlGetOrderBookEXC_SELL_ETH_USDT)
            jEXC = json.loads(rEXC.text)
            quantidade_vendendoEXC = jEXC['result']['sell'][0]['Quantity']

            urlGettickerEXC = config.urlGettickerEXC_ETH_USDT
            rEXC = requests.get(urlGettickerEXC)
            jEXC = json.loads(rEXC.text)

            lastAtivoEXC = float(jEXC['result'][0]['Last'])
            compraAtivoEXC = float(jEXC['result'][0]['Bid'])
            vendaAtivoEXC = float(jEXC['result'][0]['Ask'])

            urlGettickerBLEU = config.urlGettickerBLEU_ETH_USDT
            rBLEU = requests.get(urlGettickerBLEU)
            jBLEU = json.loads(rBLEU.text)

            lastAtivoBLEU = float(jBLEU['result'][0]['Last'])
            compraAtivoBLEU = float(jBLEU['result'][0]['Bid'])
            vendaAtivoBLEU = float(jBLEU['result'][0]['Ask'])

            ########################################################################
            # FUNÇÃO CANCELA TODAS AS ORDENS EXC/BLEU
            ########################################################################
            func.cancelaTodasOrdens_EXC_BLEU()
            ########################################################################
            
####################################################################################
# VERIFICAÇÃO:  COMPRAR na BLEU, VENDER na EXC 1
####################################################################################

            print('=' * 50)
            print(f'\n<< VERIFICANDO >> COMPRAR na BLEU, para VENDER na EXC\n')
            print('MERCADO BLEU: ETH_USDT')
            print(f'Compra: {compraAtivoBLEU:.8f} / Quantidade: {quantidade_comprandoBLEU:.8f}')
            print(f'Venda: {vendaAtivoBLEU:.8f} / Quantidade: {quantidade_vendendoBLEU:.8f}')

            if vendaAtivoBLEU < compraAtivoEXC and compraAtivoEXC - vendaAtivoBLEU > spread_ETH_USDT:
                ########################################################################
                #     OPORTUNIDADE     
                ########################################################################
                print(f'\n>> OPORTUNIDADE << VENDA na BLEU mais barata que COMPRA na EXC e SPREAD acima de: {spread_ETH_USDT:.8f} USDT\n')

                ########################################################################
                # SPREAD VARIAÇÃO PERCENTUAL & USDT
                ########################################################################
                
                vPercentual = (compraAtivoEXC - vendaAtivoBLEU) / vendaAtivoBLEU * 100
                spreadUSDT = compraAtivoEXC - vendaAtivoBLEU

                print(f'>> VALORES: \nComprar por: {vendaAtivoBLEU:.8f} \nVende por: {compraAtivoEXC:.8f} \nQuantidade de:{quantidade_vendendoBLEU:.8f}\n')
                print(f'>> SPREAD: {vPercentual:.2f}%')
                print(f'>> SPREAD: {spreadUSDT:.8f} USDT\n')

                if float(quantidade_vendendoBLEU) < float(quantidade_comprandoEXC):

                    print(f'>> AÇÃO:\nComprando na BLEU... {quantidade_vendendoBLEU:.8f}')

                    ########################################################################
                    # calcula fee
                    ########################################################################
                    
                    pagafee = (feeBLEU / 100) * quantidade_vendendoBLEU
                    pagafee = pagafee * compraAtivoEXC
                    print(f'Fee: {pagafee:.8f}')

                    ########################################################################
                    # calcula arbitragem
                    ########################################################################
                    
                    calculoArbitragem = (quantidade_vendendoBLEU * compraAtivoEXC) - (quantidade_vendendoBLEU * vendaAtivoBLEU)
                    calculoArbitragem = calculoArbitragem - (pagafee * 2)
                    print(f'Arbitragem: {calculoArbitragem:.8f} USDT\n')

##########################################################################################
# EDIT 1            # AÇÃO COMPRA - Faz COMPRA na BLEU: MOEDA_MERCADO, PREÇO, QUANTIDADE #
##########################################################################################

                    faz_compraBLEU = key_secretBLEU.buy_limit('ETH_USDT', vendaAtivoBLEU, quantidade_vendendoBLEU)
                    # print(faz_compraBLEU['result'])
                    print(f'Resposta: \n{faz_compraBLEU}')

                    ########################################################################
                    # ERRO
                    ########################################################################
                    
                    respostaResult = faz_compraBLEU['result']
                    if respostaResult == listaErro1[0]:
                        print('>> ERRO << Reiniciando verificação!')
                        break
                    elif respostaResult == listaErro1[1]:
                        print('>> ERRO << Reiniciando verificação!')
                        break
                    elif respostaResult == listaErro1[2]:
                        print('>> ERRO << Reiniciando verificação!')
                        break
                    elif respostaResult == listaErro1[3]:
                        if config.funcVendaQuantidadeMinima == 1:
                            print('\n>> FUNÇÃO VQM (Venda Quantidade Mínima) - Habilitado')
                            print(f'Quantidade mínima configurada para ETH_USDT: {minima_ETH_USDT}\n')
                            func.vendaMinimaEXC_ETH_USDT()
                            time.sleep(1)

                    ########################################################################
                    # Mensagem Telegram
                    ########################################################################
                    
                    config.mensagem_telegram('__' * 15)
                    config.mensagem_telegram('>> OPORTUNIDADE BLEU <<\nMercado: ETH_USDT\n')
                    config.mensagem_telegram(f'>> VALORES: \nCompra: {vendaAtivoBLEU:.8f} \nVenda: {compraAtivoEXC:.8f} \nQuantidade: {quantidade_vendendoBLEU:.8f}\n')
                    config.mensagem_telegram(f'>> SPREAD: {vPercentual:.2f}%\n>> FEE: {pagafee:.8f}\n')
                    config.mensagem_telegram(f'Arbitragem: {calculoArbitragem:.8f}\n')
                    config.mensagem_telegram(f'>> AÇÃO:\nComprando na BLEU \nQuantidade: {quantidade_vendendoBLEU:.8f}\n{faz_compraBLEU}\n')

                    ############################
                    #   aqui tinha log txt
                    ############################

                    # Recebe mensagem do saldo
                    respostaFazCompra = faz_compraBLEU['result']

                    # Verifica se o saldo é insuficiente e retorna uma mensagem
                    if respostaFazCompra == 'ERR_INSUFICIENT_BALANCE':
                        print('\nATENÇÃO >> SALDO INSUFICIENTE << \n')

                        ########################################################################
                        # FUNÇÃO: AUTO BALANCE (USDT)
                        ########################################################################
                        func.autoBalance_USDT()                        
                        ########################################################################
                        
                        time.sleep(1)                     
                        
                        ########################################################################
                        # FUNÇÃO: MÍNIMA BLEU/EXC (ETH_USDT)
                        ########################################################################
                        func.minima_BLEU_EXC_ETH_USDT()
                        ########################################################################
                        
                    else:
                        ########################################################################
                        # TRANSFERÊNCIA  da BLEU para EXC 
                        ########################################################################
                        
                        print('\nTransferindo da BLEU para EXC...\n')
                        mCOMPRA = str(quantidade_vendendoBLEU)
                        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(int(time.time())) + '&asset=ETH&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC

                        # sign
                        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
                        # Adding sign to header
                        headers = {'apisign': sign}
                        # Make request
                        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
                        print(f'Resposta: \n{response.json()}')

                        # Aguarda 2 segundos
                        time.sleep(2)

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Transferência da BLEU para EXC \nQuantidade: {quantidade_vendendoBLEU:.8f}\n{response.json()}')

                        ############################
                        # aqui tinha log txt
                        ############################

                        ########################################################################
                        # VENDA - Faz VENDA na EXC: MOEDA_MERCADO, preço, quantidade 
                        ########################################################################
                        
                        print('\nVendendo na EXC...\n')
                        faz_vendaEXC = key_secretEXC.sell_limit('ETH_USDT', compraAtivoEXC, quantidade_vendendoBLEU)
                        print(f'Resposta: \n{faz_vendaEXC}')

                        ########################################################################
                        # Mensagem Telegram
                        ########################################################################
                        
                        config.mensagem_telegram(f'Faz VENDA na EXC \nQuantidade: {quantidade_vendendoBLEU:.8f}\n{faz_vendaEXC}\n')

                        ############################
                        # aqui tinha log txt
                        ############################

                        ########################################################################
                        # ORDENS LOG WEB
                        ########################################################################
                        
                        log = open('logs/ETH_USDT.txt', 'a')
                        log.write(f'{dataEhora}, ETH_USDT, {vendaAtivoBLEU:.8f}, {compraAtivoEXC:.8f}, {quantidade_vendendoBLEU:.8f}, {vPercentual:.2f}, {calculoArbitragem:.8f}, {pagafee:.8f}\n')
                        log.close()                        
                        
                        ########################################################################

####################################################################################
# EDIT 1 - FIM                                                                     
####################################################################################
####################################################################################
# VERIFICAÇÃO: COMPRAR na BLEU, VENDER na EXC 2                                   
####################################################################################

                elif float(quantidade_vendendoBLEU) > float(quantidade_comprandoEXC):
                    print(f'Comprando na BLEU... {quantidade_comprandoEXC:.8f}')

                    ########################################################################
                    # calcula fee
                    ########################################################################
                    
                    pagafee = (feeBLEU / 100) * quantidade_comprandoEXC
                    pagafee = pagafee * compraAtivoEXC
                    print(f'Fee: {pagafee:.8f}')

                    ########################################################################
                    # calcula arbitragem
                    ########################################################################
                    
                    calculoArbitragem = (quantidade_comprandoEXC * compraAtivoEXC) - (quantidade_comprandoEXC * vendaAtivoBLEU)
                    calculoArbitragem = calculoArbitragem - (pagafee * 2)
                    print(f'Arbitragem: {calculoArbitragem:.8f} USDT\n')

##########################################################################################
# EDIT 2            # AÇÃO COMPRA - Faz COMPRA na BLEU: MOEDA_MERCADO, PREÇO, QUANTIDADE #
##########################################################################################

                    faz_compraBLEU = key_secretBLEU.buy_limit('ETH_USDT', vendaAtivoBLEU, quantidade_comprandoEXC)
                    # print(faz_compra['result'])
                    print(f'Resposta: \n{faz_compraBLEU}')

                    ########################################################################
                    # ERRO
                    ########################################################################
                    
                    respostaResult = faz_compraBLEU['result']
                    if respostaResult == listaErro1[0]:
                        print('>> ERRO << Reiniciando verificação!')
                        break
                    elif respostaResult == listaErro1[1]:
                        print('>> ERRO << Reiniciando verificação!')
                        break
                    elif respostaResult == listaErro1[2]:
                        print('>> ERRO << Reiniciando verificação!')
                        break
                    elif respostaResult == listaErro1[3]:
                        if config.funcVendaQuantidadeMinima == 1:
                            print('\n>> FUNÇÃO VQM (Venda Quantidade Mínima) - Habilitado')
                            print(f'Quantidade mínima configurada para ETH_USDT: {minima_ETH_USDT}\n')
                            func.vendaMinimaEXC_ETH_USDT()
                            time.sleep(1)

                    ########################################################################
                    # Mensagem Telegram
                    ########################################################################
                    
                    config.mensagem_telegram('__' * 15)
                    config.mensagem_telegram('>> OPORTUNIDADE BLEU <<\nMercado: ETH_USDT\n')
                    config.mensagem_telegram(f'>> VALORES: \nCompra: {vendaAtivoBLEU:.8f} \nVenda: {compraAtivoEXC:.8f} \nQuantidade: {quantidade_comprandoEXC:.8f}\n')
                    config.mensagem_telegram(f'>> SPREAD: {vPercentual:.2f}%\n>> FEE: {pagafee:.8f}\n')
                    config.mensagem_telegram(f'Arbitragem: {calculoArbitragem:.8f}\n')
                    config.mensagem_telegram(f'>> AÇÃO:\nComprando na BLEU \nQuantidade: {quantidade_comprandoEXC:.8f}\n{faz_compraBLEU}\n')

                    ############################
                    # aqui tinha log txt
                    ############################

                    # Recebe mensagem do saldo
                    respostaFazCompra = faz_compraBLEU['result']

                    # Verifica se o saldo é insuficiente e retorna uma mensagem
                    if respostaFazCompra == 'ERR_INSUFICIENT_BALANCE':
                        print('\nATENÇÃO >> SALDO INSUFICIENTE << \n')

                        ########################################################################
                        # FUNÇÃO: AUTO BALANCE (USDT)
                        ########################################################################
                        func.autoBalance_USDT()
                        ########################################################################

                        time.sleep(1)

                        ########################################################################
                        # FUNÇÃO: MÍNIMA BLEU/EXC (ETH_USDT)
                        ########################################################################
                        func.minima_BLEU_EXC_ETH_USDT()
                        ########################################################################
                        
                    else:
                        ########################################################################
                        # TRANSFERÊNCIA da BLEU para EXC 
                        ########################################################################
                        
                        print('\nTransferindo da BLEU para EXC...\n')
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
                        print(f'Resposta: \n{response.json()}')

                        # Aguarda 2 segundos
                        time.sleep(2)

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Transferência da BLEU para EXC \nQuantidade: {quantidade_comprandoEXC:.8f}\n{response.json()}')

                        ############################
                        # aqui tinha log txt
                        ############################

                        ########################################################################
                        # VENDA - Faz VENDA na EXC: MOEDA_MERCADO, preço, quantidade 
                        ########################################################################
                        print('\nVendendo na EXC...\n')
                        faz_vendaEXC = key_secretEXC.sell_limit('ETH_USDT', compraAtivoEXC, quantidade_comprandoEXC)
                        print(f'Resposta: \n{faz_vendaEXC}')

                        ########################################################################
                        # Mensagem Telegram
                        ########################################################################
                        
                        config.mensagem_telegram(f'Faz VENDA na EXC \nQuantidade: {quantidade_comprandoEXC:.8f}\n{faz_vendaEXC}\n')

                        ############################
                        # aqui tinha log txt
                        ############################

                        ########################################################################
                        # ORDENS LOG WEB
                        ########################################################################
                        
                        log = open('logs/ETH_USDT.txt', 'a')
                        log.write(f'{dataEhora}, ETH_USDT, {vendaAtivoBLEU:.8f}, {compraAtivoEXC:.8f}, {quantidade_comprandoEXC:.8f}, {vPercentual:.2f}, {calculoArbitragem:.8f}, {pagafee:.8f}\n')
                        
                        ########################################################################

####################################################################################
# EDIT 2 - FIM                                                                     #
####################################################################################

            elif vendaAtivoBLEU < compraAtivoEXC and compraAtivoEXC - vendaAtivoBLEU < spread_ETH_USDT:
                print(f'\n>> AGUARDE << VENDA na BLEU mais barata que COMPRA na EXC, mas SPREAD abaixo de: {spread_ETH_USDT:.8f} USDT\n')

            elif vendaAtivoBLEU > compraAtivoEXC:
                print('\n>> AGUARDE <<  Sem oportunidades.\n')

            else:
                print('\n>> AGUARDE <<  Valores igual!!!\n')

####################################################################################
# VERIFICAÇÃO: COMPRAR na EXC, VENDER na BLEU 1
####################################################################################
            print('-' * 40)
            print('\n<< VERIFICANDO >> COMPRAR na EXC, VENDER na BLEU\n')
            print('MERCADO EXC: ETH_USDT')
            print(f'Compra: {compraAtivoEXC:.8f} / Quantidade: {quantidade_comprandoEXC:.8f}')
            print(f'Venda: {vendaAtivoEXC:.8f} / Quantidade: {quantidade_vendendoEXC:.8f}')

            if vendaAtivoEXC < compraAtivoBLEU and compraAtivoBLEU - vendaAtivoEXC > spread_ETH_USDT:
                ########################################################################
                #     OPORTUNIDADE     
                ########################################################################
                
                print(f'\n>> OPORTUNIDADE << VENDA na EXC mais barata que COMPRA na BLEU e SPREAD acima de: {spread_ETH_USDT:.8f} USDT\n')

                ########################################################################
                # SPREAD VARIAÇÃO PERCENTUAL & USDT
                ########################################################################
                
                vPercentual = (compraAtivoBLEU - vendaAtivoEXC) / vendaAtivoEXC * 100
                spreadUSDT = compraAtivoBLEU - vendaAtivoEXC

                print(f'>> VALORES: \nComprar por: {vendaAtivoEXC:.8f} \nVende por: {compraAtivoBLEU:.8f} \nQuantidade de: {quantidade_vendendoEXC:.8f}\n')
                print(f'>> SPREAD: {vPercentual:.2f}%')
                print(f'>> SPREAD: {spreadUSDT:.8f} USDT\n')

                if float(quantidade_vendendoEXC) < float(quantidade_comprandoBLEU):
                    print(f'>> AÇÃO:\nComprando na EXC... {quantidade_vendendoEXC:.8f}')

                    ########################################################################
                    # calcula fee
                    ########################################################################
                    
                    pagafee = (feeEXC / 100) * quantidade_vendendoEXC
                    pagafee = pagafee * compraAtivoBLEU
                    print(f'Fee: {pagafee:.8f}')

                    ########################################################################
                    # calcula arbitragem
                    ########################################################################
                    
                    calculoArbitragem = (quantidade_vendendoEXC * compraAtivoBLEU) - (quantidade_vendendoEXC * vendaAtivoEXC)
                    calculoArbitragem = calculoArbitragem - (pagafee * 2)
                    print(f'Arbitragem: {calculoArbitragem:.8f} USDT\n')

####################################################################################
# EDIT 1            # COMPRA - Faz COMPRA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE #
####################################################################################

                    faz_compraEXC = key_secretEXC.buy_limit('ETH_USDT', vendaAtivoBLEU, quantidade_vendendoEXC)
                    # print(faz_compra['result'])
                    print(f'Resposta: \n{faz_compraEXC}')

                    ########################################################################
                    # ERRO
                    ########################################################################
                    
                    respostaResult = faz_compraEXC['result']
                    if respostaResult == listaErro1[0]:
                        print('>> ERRO << Reiniciando verificação!')
                        break
                    elif respostaResult == listaErro1[1]:
                        print('>> ERRO << Reiniciando verificação!')
                        break
                    elif respostaResult == listaErro1[2]:
                        print('>> ERRO << Reiniciando verificação!')
                        break
                    elif respostaResult == listaErro1[3]:
                        if config.funcVendaQuantidadeMinima == 1:
                            print('\n>> FUNÇÃO VQM (Venda Quantidade Mínima) - Habilitado')
                            print(f'Quantidade mínima configurada para ETH_USDT: {minima_ETH_USDT}\n')
                            func.vendaMinimaEXC_ETH_USDT()
                            time.sleep(1)

                    ########################################################################
                    # Mensagem Telegram
                    ########################################################################
                    
                    config.mensagem_telegram('__' * 15)
                    config.mensagem_telegram(f'>> OPORTUNIDADE EXC <<\nMercado: ETH_USDT\n')
                    config.mensagem_telegram(f'>> VALORES: \nCompra: {vendaAtivoEXC:.8f} \nVenda: {compraAtivoBLEU:.8f} \nQuantidade: {quantidade_vendendoEXC:.8f}\n')
                    config.mensagem_telegram(f'>> SPREAD: {vPercentual:.2f}%\n>> FEE: {pagafee:.8f}\n')
                    config.mensagem_telegram(f'Arbitragem: {calculoArbitragem:.8f}\n')
                    config.mensagem_telegram(f'>> AÇÃO:\nComprando na EXC \nQuantidade: {quantidade_vendendoEXC:.8f}\n{faz_compraEXC}\n')

                    ############################
                    # aqui tinha log txt
                    ############################

                    # recebe mensagem do saldo
                    respostaFazCompraEXC = faz_compraEXC['result']

                    # Verifica se o saldo é insuficiente e retorna uma mensagem
                    if respostaFazCompraEXC == 'ERR_INSUFICIENT_BALANCE':
                        print('\nATENÇÃO >> SALDO INSUFICIENTE << ')

                        ########################################################################
                        # FUNÇÃO: AUTO BALANCE (USDT)
                        ########################################################################
                        func.autoBalance_USDT()
                        ########################################################################

                        time.sleep(1)

                        ########################################################################
                        # FUNÇÃO: MÍNIMA EXC/BLEU (ETH_USDT)
                        ########################################################################
                        func.minima_EXC_BLEU_ETH_USDT()
                        ########################################################################
                        
                    else:
                        ########################################################################
                        # TRANSFERENCIA da EXC para BLEU 
                        ########################################################################
                        
                        print(f'\nTransferindo... {quantidade_vendendoEXC:.8f}\n')
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
                        print(f'Resposta: \n{response.json()}')

                        # Aguarda 2 segundos
                        time.sleep(2)

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Transferência da EXC para BLEU \nQuantidade: {quantidade_vendendoEXC:.8f}\n{response.json()}')

                        ############################
                        # aqui tinha log txt
                        ############################

                        ########################################################################
                        # VENDA - Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade 
                        ########################################################################
                        print(f'\nVendendo... {quantidade_vendendoEXC:.8f}\n')
                        faz_vendaBLEU = key_secretBLEU.sell_limit('ETH_USDT', compraAtivoEXC, quantidade_vendendoEXC)
                        print(f'Resposta: \n{faz_vendaBLEU}')

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Faz VENDA na BLEU \nQuantidade: {quantidade_vendendoEXC:.8f}\n{faz_vendaBLEU}\n')

                        ############################
                        # aqui tinha log txt
                        ############################

                        ########################################################################
                        # ORDENS LOG WEB
                        ########################################################################
                        
                        log = open('logs/ETH_USDT.txt', 'a')
                        log.write(f'{dataEhora}, ETH_USDT, {vendaAtivoEXC:.8f}, {compraAtivoBLEU:.8f}, {quantidade_vendendoEXC:.8f}, {vPercentual:.2f}, {calculoArbitragem:.8f}, {pagafee:.8f}\n')
                        log.close()
                        
                        ########################################################################

####################################################################################
# EDIT 1 - FIM                                                                     #
####################################################################################
####################################################################################
# VERIFICAÇÃO: COMPRAR na EXC, VENDER na BLEU 2
####################################################################################

                elif float(quantidade_vendendoEXC) > float(quantidade_comprandoBLEU):
                    print(f'>> OPORTUNIDADE << Comprando na EXC... {quantidade_comprandoBLEU:.8f}')

                    print(f'\nComprando... {quantidade_comprandoBLEU:.8f}')

                    ########################################################################
                    # calcula fee
                    ########################################################################
                    
                    pagafee = (feeEXC / 100) * quantidade_comprandoBLEU
                    pagafee = pagafee * compraAtivoBLEU
                    print(f'Fee: {pagafee:.8f}')

                    ########################################################################
                    # calcula arbitragem
                    ########################################################################
                    
                    calculoArbitragem = (quantidade_comprandoBLEU * compraAtivoBLEU) - (quantidade_comprandoBLEU * vendaAtivoEXC)
                    calculoArbitragem = calculoArbitragem - (pagafee * 2)
                    print(f'Arbitragem: {calculoArbitragem:.8f} USDT\n')

####################################################################################
# EDIT 2            # COMPRA - Faz COMPRA na EXC: MOEDA_MERCADO, PREÇO, QUANTIDADE #
####################################################################################

                    faz_compraEXC = key_secretEXC.buy_limit('ETH_USDT', vendaAtivoBLEU, quantidade_comprandoBLEU)
                    # print(faz_compra['result'])
                    print(f'Resposta: \n{faz_compraEXC}')

                    ########################################################################
                    # ERRO
                    ########################################################################
                    
                    respostaResult = faz_compraEXC['result']
                    if respostaResult == listaErro1[0]:
                        print('>> ERRO << Reiniciando verificação!')
                        break
                    elif respostaResult == listaErro1[1]:
                        print('>> ERRO << Reiniciando verificação!')
                        break
                    elif respostaResult == listaErro1[2]:
                        print('>> ERRO << Reiniciando verificação!')
                        break
                    elif respostaResult == listaErro1[3]:
                        if config.funcVendaQuantidadeMinima == 1:
                            print('\n>> FUNÇÃO VQM (Venda Quantidade Mínima) - Habilitado')
                            print(f'Quantidade mínima configurada para ETH_USDT: {minima_ETH_USDT}\n')
                            func.vendaMinimaEXC_ETH_USDT()
                            time.sleep(1)

                    ########################################################################
                    # Mensagem Telegram
                    ########################################################################
                    
                    config.mensagem_telegram('__' * 15)
                    config.mensagem_telegram('>> OPORTUNIDADE EXC <<\nMercado: ETH_USDT\n')
                    config.mensagem_telegram(f'>> VALORES: \nCompra: {vendaAtivoEXC:.8f} \nVenda: {compraAtivoBLEU:.8f} \nQuantidade: {quantidade_comprandoBLEU:.8f}\n')
                    config.mensagem_telegram(f'>> SPREAD: {vPercentual:.2f}%\n>> FEE: {pagafee:.8f}\n')
                    config.mensagem_telegram(f'Arbitragem: {calculoArbitragem:.8f}\n')
                    config.mensagem_telegram(f'>> AÇÃO:\nComprando na EXC \nQuantidade: {quantidade_comprandoBLEU:.8f}\n{faz_compraEXC}\n')

                    ############################
                    # aqui tinha log txt
                    ############################

                    # recebe mensagem do saldo
                    respostaFazCompraEXC = faz_compraEXC['result']

                    # Verifica se o saldo é insuficiente e retorna uma mensagem
                    if respostaFazCompraEXC == 'ERR_INSUFICIENT_BALANCE':
                        print('\nATENÇÃO >> SALDO INSUFICIENTE << ')

                        ########################################################################
                        # FUNÇÃO: AUTO BALANCE (USDT)
                        ########################################################################
                        func.autoBalance_USDT()
                        ########################################################################

                        time.sleep(1)

                        ########################################################################
                        # FUNÇÃO: MÍNIMA EXC/BLEU (ETH_USDT)
                        ########################################################################
                        func.minima_EXC_BLEU_ETH_USDT()
                        ########################################################################
                        
                    else:
                        ########################################################################
                        # TRANSFERENCIA da EXC para BLEU 
                        ########################################################################
                        
                        print(f'\nTransferindo... {quantidade_comprandoBLEU:.8f}\n')
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
                        print(f'Resposta: \n{response.json()}')

                        # Aguarda 2 segundos
                        time.sleep(2)

                        # Mensagem Telegram
                        config.mensagem_telegram(f'Transferência da EXC para BLEU \nQuantidade: {quantidade_comprandoBLEU:.8f}\n{response.json()}')

                        ############################
                        # aqui tinha log txt
                        ############################

                        ########################################################################
                        # VENDA - Faz VENDA na BLEU: MOEDA_MERCADO, preço, quantidade 
                        ########################################################################
                        print(f'\nVendendo... {quantidade_comprandoBLEU:.8f}\n')
                        faz_vendaBLEU = key_secretBLEU.sell_limit('ETH_USDT', compraAtivoEXC, quantidade_comprandoBLEU)
                        print(f'Resposta: \n{faz_vendaBLEU}')

                        ########################################################################
                        # Mensagem Telegram
                        ########################################################################
                        
                        config.mensagem_telegram(f'Faz VENDA na BLEU \nQuantidade: {quantidade_comprandoBLEU:.8f}\n{faz_vendaBLEU}\n')

                        ############################
                        # aqui tinha log txt
                        ############################

                        ########################################################################
                        # ORDENS LOG WEB
                        ########################################################################
                        
                        log = open('logs/ETH_USDT.txt', 'a')
                        log.write(f'{dataEhora}, ETH_USDT {vendaAtivoEXC:.8f}, {compraAtivoBLEU:.8f}, {quantidade_comprandoBLEU:.8f}, {vPercentual:.2f}, {calculoArbitragem:.8f}, {pagafee:.8f}\n')
                        log.close()
                        
                        ########################################################################

####################################################################################
# EDIT 2 - FIM                                                                     #
####################################################################################

            elif vendaAtivoEXC < compraAtivoBLEU and compraAtivoBLEU - vendaAtivoEXC < spread_ETH_USDT:
                print(f'\n>> AGUARDE << Venda na EXC está mais barata que compra na BLEU, mas SPREAD abaixo de {spread_ETH_USDT:.8f} USDT\n')

            elif vendaAtivoEXC > compraAtivoBLEU:
                print('\n>> AGUARDE << Sem oportunidades.\n')

            else:
                print('\n>> AGUARDE << Valores igual!!!\n')

            ########################################################################
            print('=' * 50)
            ########################################################################

    except Exception as e:
        print(f'Tipo de erro: {e}')
        log = open('logs/erroETH_USDT.txt', 'a')
        log.write(f'ERRO: {e}\n')
        log.close()
