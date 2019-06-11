import config
import excBot
import bleuBot
import time
import hmac
import requests
import hashlib

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

print('=' * 40)
print('excBOT v0.1.1\nFerramenta de Transferenência EXC/BLEU')
print('=' * 40)

acao = 0
while acao != 99:
    print('''    Escolha uma opção:

    EXC/BLEU
    [1] DOGE
    [2] SMART
    [3] WAVES
    [4] ETH
    [5] LTC
    [6] BTC
    [7] BC

    BLEU/EXC
    [21] DOGE
    [22] SMART
    [23] WAVES
    [24] ETH
    [25] LTC
    [26] BTC
    [27] BC
    

    [99] Sair''')

    acao = int(input('\nO que deseja fazer?: '))

    if acao == 1:
        print('DOGE: Transferir da EXC para BLEU')

        quantidade_transferirEXCBLEU = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da EXC para BLEU #
        ##################################
        print('\nTransferindo da EXC para BLEU...')
        mCOMPRA = str(quantidade_transferirEXCBLEU)
        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
            int(time.time())) + '&asset=DOGE&quantity=' + mCOMPRA + '&exchangeto=1&' + 'accountto=' + emailBLEU

        # sign
        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferEXC, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 2:
        print('SMART: Transferir da EXC para BLEU')

        quantidade_transferirEXCBLEU = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da EXC para BLEU #
        ##################################
        print('\nTransferindo da EXC para BLEU...')
        mCOMPRA = str(quantidade_transferirEXCBLEU)
        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
            int(time.time())) + '&asset=SMART&quantity=' + mCOMPRA + '&exchangeto=1&' + 'accountto=' + emailBLEU

        # sign
        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferEXC, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 3:
        print('WAVES: Transferir da EXC para BLEU')

        quantidade_transferirEXCBLEU = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da EXC para BLEU #
        ##################################
        print('\nTransferindo da EXC para BLEU...')
        mCOMPRA = str(quantidade_transferirEXCBLEU)
        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
            int(time.time())) + '&asset=WAVES&quantity=' + mCOMPRA + '&exchangeto=1&' + 'accountto=' + emailBLEU

        # sign
        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferEXC, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 4:
        print('ETH: Transferir da EXC para BLEU')

        quantidade_transferirEXCBLEU = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da EXC para BLEU #
        ##################################
        print('\nTransferindo da EXC para BLEU...')
        mCOMPRA = str(quantidade_transferirEXCBLEU)
        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
            int(time.time())) + '&asset=ETH&quantity=' + mCOMPRA + '&exchangeto=1&' + 'accountto=' + emailBLEU

        # sign
        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferEXC, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 5:
        print('LTC: Transferir da EXC para BLEU')

        quantidade_transferirEXCBLEU = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da EXC para BLEU #
        ##################################
        print('\nTransferindo da EXC para BLEU...')
        mCOMPRA = str(quantidade_transferirEXCBLEU)
        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
            int(time.time())) + '&asset=LTC&quantity=' + mCOMPRA + '&exchangeto=1&' + 'accountto=' + emailBLEU

        # sign
        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferEXC, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 6:
        print('BTC: Transferir da EXC para BLEU')

        quantidade_transferirEXCBLEU = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da EXC para BLEU #
        ##################################
        print('\nTransferindo da EXC para BLEU...')
        mCOMPRA = str(quantidade_transferirEXCBLEU)
        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
            int(time.time())) + '&asset=BTC&quantity=' + mCOMPRA + '&exchangeto=1&' + 'accountto=' + emailBLEU

        # sign
        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferEXC, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 7:
        print('BC: Transferir da EXC para BLEU')

        quantidade_transferirEXCBLEU = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da EXC para BLEU #
        ##################################
        print('\nTransferindo da EXC para BLEU...')
        mCOMPRA = str(quantidade_transferirEXCBLEU)
        urlDirecttransferEXC = 'https://trade.exccripto.com/api/v3/private/directtransfer?apikey=' + keyEXC + '&nonce=' + str(
            int(time.time())) + '&asset=BC&quantity=' + mCOMPRA + '&exchangeto=1&' + 'accountto=' + emailBLEU

        # sign
        sign = hmac.new(secretEXC.encode(), urlDirecttransferEXC.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferEXC, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 21:
        print('DOGE: Transferir da BLEU para EXC')

        quantidade_transferirBLEUEXC = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da BLEU para EXC #
        ##################################
        print('\nTransferindo da BLEU para EXC...')
        mCOMPRA = str(quantidade_transferirBLEUEXC)
        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
            int(time.time())) + '&asset=DOGE&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC

        # sign
        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 22:
        print('SMART: Transferir da BLEU para EXC')

        quantidade_transferirBLEUEXC = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da BLEU para EXC #
        ##################################
        print('\nTransferindo da BLEU para EXC...')
        mCOMPRA = str(quantidade_transferirBLEUEXC)
        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
            int(time.time())) + '&asset=SMART&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC

        # sign
        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 23:
        print('WAVES: Transferir da BLEU para EXC')

        quantidade_transferirBLEUEXC = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da BLEU para EXC #
        ##################################
        print('\nTransferindo da BLEU para EXC...')
        mCOMPRA = str(quantidade_transferirBLEUEXC)
        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
            int(time.time())) + '&asset=WAVES&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC

        # sign
        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 24:
        print('ETH: Transferir da BLEU para EXC')

        quantidade_transferirBLEUEXC = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da BLEU para EXC #
        ##################################
        print('\nTransferindo da BLEU para EXC...')
        mCOMPRA = str(quantidade_transferirBLEUEXC)
        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
            int(time.time())) + '&asset=ETH&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC

        # sign
        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 25:
        print('LTC: Transferir da BLEU para EXC')

        quantidade_transferirBLEUEXC = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da BLEU para EXC #
        ##################################
        print('\nTransferindo da BLEU para EXC...')
        mCOMPRA = str(quantidade_transferirBLEUEXC)
        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
            int(time.time())) + '&asset=LTC&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC

        # sign
        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 26:
        print('BTC: Transferir da BLEU para EXC')

        quantidade_transferirBLEUEXC = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da BLEU para EXC #
        ##################################
        print('\nTransferindo da BLEU para EXC...')
        mCOMPRA = str(quantidade_transferirBLEUEXC)
        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
            int(time.time())) + '&asset=BTC&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC

        # sign
        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 27:
        print('BC: Transferir da BLEU para EXC')

        quantidade_transferirBLEUEXC = float(input('\nQual a quantidade para transferir: '))

        ##################################
        # TRANSFERÊNCIA                  #
        # Transferência da BLEU para EXC #
        ##################################
        print('\nTransferindo da BLEU para EXC...')
        mCOMPRA = str(quantidade_transferirBLEUEXC)
        urlDirecttransferBLEU = 'https://bleutrade.com/api/v3/private/directtransfer?apikey=' + keyBLEU + '&nonce=' + str(
            int(time.time())) + '&asset=BC&quantity=' + mCOMPRA + '&exchangeto=2&' + 'accountto=' + emailEXC

        # sign
        sign = hmac.new(secretBLEU.encode(), urlDirecttransferBLEU.encode(), hashlib.sha512).hexdigest()
        # Adding sign to header
        headers = {'apisign': sign}
        # Make request
        response = requests.get(url=urlDirecttransferBLEU, headers=headers)
        print(response.json())

        # Aguarda 2 segundos
        time.sleep(2)

    elif acao == 99:
        print('Sair do Programa')

    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    time.sleep(2)

print('Fim do programa!')

