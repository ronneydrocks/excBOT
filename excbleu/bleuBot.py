import requests
import hmac
import hashlib
import time


class bleuBot:

    # Construtor
    def __init__(self, apikey=None, apisecret=None, nonce=False, baseurl='https://bleutrade.com/api/v3/'):
        self._url = ''
        self._baseurl = baseurl
        self._params = {}
        self._apiKey = apikey
        self._apiSecret = apisecret
        self._nonce = nonce
        self.redefinir_url()

    # Definições
    # Definir URL para usar na próxima solicitação
    def definir_url(self, url):
        self._url = url

    # Definir parâmetros para usar na próxima solicitação
    def definir_parametros(self, params):
        self._params = params

    # Redefine _url para _baseurl
    def redefinir_url(self):
        self.definir_url(self._baseurl)

    # Faz pedido(requisição) e retorna o resultado como um objeto codificado em json.
    def obter_requisicao(self, headers=None):
        if headers is not None:
            r = requests.get(
                self.obter_url(), params=self.obter_parametros(), headers=headers)
        else:
            r = requests.get(self.obter_url(), params=self.obter_parametros())
        return r.json()

    # 'make_public_api_call': Pega a consulta construída e chama API pública
    # params: query
    # return: result
    def fazer_chamada_api_publica(self, query):
        # Definir _url para o URL base
        self.redefinir_url()

        # Atualize o URL para incluir a consulta
        self.definir_url(self.obter_url() + query)

        result = self.obter_requisicao()

        # Limpar a lista de parâmetros
        empty_dict = {}
        self.definir_parametros(empty_dict)

        return result

    # 'make_private_api_call': Pega a consulta construída e chama API privada
    # params: query
    # return: result
    def fazer_chamada_api_privada(self, query):
        # Verificar se a KEY e SECRET da API estão disponíveis
        if self._apiSecret is None or self._apiKey is None:     # VERIFICAR ESSA LINHA #
            print('Você deve definir uma KEY e SECRET da API para fazer chamadas privadas')
            return None

        # Define _url para o URL base
        self.redefinir_url()

        # Verifica se selecionou "nonce"
        if self._nonce == True:
            self._params['nonce'] = str(int(time.time()))   # VERIFICAR ESSA LINHA #

        # Adiciona KEY da API à lista de parâmetros
        self._params['apikey'] = self.obter_api_key()

        # Atualiza URL para incluir a consulta
        self.definir_url(self.obter_url() + query)

        # Gera apisign
        # print(self.obter_api_key())       # PRINT AJUDA
        # print(self.obter_api_secret())    # PRINT AJUDA
        # print(self.form_hash_url())       # PRINT AJUDA MOSTRA URL COMPLETA
        sign = hmac.new(self.obter_api_secret().encode(), self.form_hash_url().encode(), hashlib.sha512).hexdigest()  # VERIFICAR ESSA LINHA #

        # Adiciona cabeçalho personalizado
        headers = {'apisign': sign}
        result = self.obter_requisicao(headers)

        # Limpa a lista de parâmetros
        empty_dict = {}
        self.definir_parametros(empty_dict)

        return result

    #  Form hash url
    def form_hash_url(self):

        return_url = self.obter_url() + '?'
        # Gera uma URL, para ser usada no hash do "sign"
        for key, value in self._params.items():
            return_url += key + '=' + str(value) + '&'

        # Trim trailing &
        return_url = return_url[:-1]
        return return_url

    # Obter
    def obter_url(self):

        return self._url

    def obter_parametros(self):

        return self._params

    def obter_api_key(self):

        return self._apiKey

    def obter_api_secret(self):

        return self._apiSecret

    def obter_url_base(self):

        return self._baseurl

    ######################################################################
    #               FUNÇÕES PÚBLICAS
    ######################################################################

    # 'public/getcurrencies': Lista de todos as moedas negociados na Exchange
    # params: null
    # return: JSON
    def get_assets(self):
        query = 'public/getassets'
        params = {}
        self.definir_parametros(params)
        result = self.fazer_chamada_api_publica(query)
        return result

    # 'public/getmarkets': Obter a lista de todos os pares negociados
    # params: null
    # return: JSON
    def get_markets(self):
        query = 'public/getmarkets'
        params = {}
        self.definir_parametros(params)
        result = self.fazer_chamada_api_publica(query)
        return result

    # 'public/getticker': Usado para obter os valores de um mercado específico.
    # params: market: string (ex: LTC_BTC)
    # return: JSON
    def get_ticker(self, market):
        query = 'public/getticker'
        params = {'market': market}
        self.definir_parametros(params)
        result = self.fazer_chamada_api_publica(query)
        return result

    # 'public/getmarketsummary': Usado para obter o último resumo de 24 horas de mercado específico
    # params: market: string (ex: LTC_BTC)
    # return: JSON
    def get_market_summary(self, market):
        query = 'public/getmarketsummary'
        params = {'market': market}
        self.definir_parametros(params)
        result = self.fazer_chamada_api_publica(query)
        return result

    # 'public/getmarketsummaries': Usado para obter o último resumo de 24 horas de todos os mercados ativos
    # params: null
    # return: JSON
    def get_market_summaries(self):
        query = 'public/getmarketsummaries'
        params = {}
        self.definir_parametros(params)
        result = self.fazer_chamada_api_publica(query)
        return result

    # 'public/getorderbook': Carrega o mercado específico do BOOK.
    # params: market: string (ex: LTC_BTC)
    #         type:   string (BUY|SELL|ALL)
    #         depth:  int    (opcional, o padrão é 20)
    # return: JSON
    def get_order_book(self, market, rType='ALL', depth=20):
        query = 'public/getorderbook'
        params = {
            'market': market,
            'type': rType,
            'count': depth
        }
        self.definir_parametros(params)
        result = self.fazer_chamada_api_publica(query)
        return result

    # 'public/getmarkethistory': Obter o histórico de trades de um mercado específico
    # params: market: string (ex: LTC_BTC)
    #         count : int    (opcional, padrão: 20, max: 200)
    # return: JSON
    def get_market_history(self, market, count=20):
        query = 'public/getmarkethistory'
        params = {
            'market': market,
            'count': count
        }
        self.definir_parametros(params)
        result = self.fazer_chamada_api_publica(query)
        return result

    # 'public/getcandles': Obter candles de um mercado específico
    # params: market    : string (ex: LTC_BTC)
    #         period    : string (1m, 2m, 3m, 4m, 5m, 6m, 10m, 12m, 15m, 20m, 30m, 1h, 2h, 3h, 4h, 6h, 8h, 12h, 1d)
    #         count     : int    (default: 1000, max: 999999)
    #         lasthours: int    (default: 24, max: 720)
    # return: JSON
    def get_candles(self, market, period='30m', count=1000, lasthours=24):
        query = 'public/getcandles'
        params = {
            'market': market,
            'period': period,
            'count': count,
            'lasthours': lasthours
        }
        self.definir_parametros(params)
        result = self.fazer_chamada_api_publica(query)
        return result
    ######################################################################
    #               FUNÇÕES PRIVADAS
    ######################################################################

    # 'private/getbalance': Obter saldo de uma moeda específica
    # params: currency: string (ex: BTC)
    # return: JSON
    def get_balance(self, currency):
        query = 'private/getbalance'
        params = {'asset': currency}
        self.definir_parametros(params)
        result = self.fazer_chamada_api_privada(query)
        return result

    # 'private/getbalances': Obter saldo de todas as moedas
    # params: currencies: string (opcional, default=ALL, por exemplo: 'DOGE;BTC;LTC')
    # return: JSON
    def get_balances(self):
        query = 'private/getbalances'
        params = {}
        self.definir_parametros(params)
        result = self.fazer_chamada_api_privada(query)
        return result

    # 'private/buylimit': Use para enviar ordem de COMPRA
    # params: market  : string (ex: LTC_BTC)
    #         rate    : string (ex: 10.00000000)
    #         quantity: string (ex: 10.00000000)
    #         comments: string (opcional, até 128 caracteres
    # return: JSON
    def buy_limit(self, market, rate, quantity, comments=''):
        query = 'private/buylimit'
        params = {
            'market': market,
            'rate': rate,
            'quantity': quantity,
            'comments': comments
        }
        self.definir_parametros(params)
        result = self.fazer_chamada_api_privada(query)
        return result

    # 'private/selllimit': Use para enviar ordem de VENDA
    # params: market  : string (ex: LTC_BTC)
    #         rate    : string (ex: 1234.12345678)
    #         quantity: string (ex: 1234.12345678)
    #         comments: string (opcional, até 128 caracteres)
    # return: JSON
    def sell_limit(self, market, rate, quantity, comments=''):
        query = 'private/selllimit'
        params = {
            'market': market,
            'rate': rate,
            'quantity': quantity,
            'comments': comments
        }
        self.definir_parametros(params)
        result = self.fazer_chamada_api_privada(query)
        return result

    # 'private/buylimitami': Usado para enviar ordens de compra com características AMI (Auto Maker Inversible).

    # 'private/selllimitami': Usado para enviar pedidos de venda com características AMI (Auto Maker Inversible).

    # 'private/buystoplimit': Usado para enviar pedidos com limite de compra.

    # 'private/sellstoplimit': Usado para enviar pedidos com limite de vendas.

    # 'private/ordercancel': Cancelar uma ordem
    # params: orderid: int
    # return: JSON
    def cancel(self, orderid):
        query = 'private/ordercancel'
        params = {'orderid': orderid}
        self.definir_parametros(params)
        result = self.fazer_chamada_api_privada(query)
        return result

    # 'private/getopenorders': Obter lista das ordens abertas
    # params: null
    # return: JSON
    def get_open_orders(self):
        query = 'private/getopenorders'
        params = {}
        self.definir_parametros(params)
        result = self.fazer_chamada_api_privada(query)
        return result

    # 'private/getdepositaddress': Obter o endereço de depósito da moeda específica
    # params: currency: string (ex: BTC)
    # return: JSON
    def get_deposit_address(self, currency):
        query = 'private/getdepositaddress'
        params = {'currency': currency}
        self.definir_parametros(params)
        result = self.fazer_chamada_api_privada(query)
        return result

    # 'private/getdeposithistory': - Histórico de depósitos que recebeu das transferência diretas
    # params: none
    # return: JSON
    def get_deposit_history(self):
        query = 'private/getdeposithistory'
        params = {}
        self.definir_parametros(params)
        result = self.fazer_chamada_api_privada(query)
        return result

    # 'private/getmytransactions': Obtenha suas transações gerais históricas.

    # 'private/withdraw': Use para withdraw(saque) para outra carteira
    # params: currency: string (ex: BTC)
    #         quantity: string (ex: 1.12345678)
    #         address : string (ex: 234nOtReAl4kjh5kjhv98er76t938dsf)
    # return: JSON
    def withdraw(self, currency, quantity, address):
        query = 'private/withdraw'
        params = {
            'currency': currency,
            'quantity': quantity,
            'address': address
        }
        self.definir_parametros(params)
        result = self.fazer_chamada_api_privada(query)
        return result

    # 'private/directtransfer': Transferência direta sem taxas
    # params: currency : string (ex: BTC)
    #         quanitity: string (ex: 1.122345678)
    #         touser   : string (email destino, cadastrado na Bleutrade)
    # return: JSON
    def direct_transfer(self, asset, quantity, exchangeto, accountto):
        query = 'private/directtransfer'
        params = {
            'asset': asset,
            'quantity': quantity,
            'exchangeto': exchangeto,
            'accountto': accountto
        }
        self.definir_parametros(params)
        result = self.fazer_chamada_api_privada(query)
        return result

    # 'private/getwithdrawhistory': - Histórico de withdraw(saque) que recebeu das transferência diretas
    # params: none
    # return: JSON
    def get_withdraw_history(self):
        query = 'private/getwithdrawhistory'
        params = {}
        self.definir_parametros(params)
        result = self.fazer_chamada_api_privada(query)
        return result

