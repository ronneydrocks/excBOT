import uuid
import time

import requests
from decimal import *

class Client(object):
    def __init__(self, url, public_key, secret):
        self.url = url + "/api/2"
        self.session = requests.session()
        self.session.auth = (public_key, secret)

    def get_symbol(self, symbol_code):
        """Get symbol."""
        return self.session.get("%s/public/symbol/%s" % (self.url, symbol_code)).json()

    def get_orderbook(self, symbol_code):
        """Get orderbook. """
        return self.session.get("%s/public/orderbook/%s" % (self.url, symbol_code)).json()

    def get_address(self, currency_code):
        """Get address for deposit."""
        return self.session.get("%s/account/crypto/address/%s" % (self.url, currency_code)).json()

    def get_account_balance(self):
        """Get main balance."""
        return self.session.get("%s/account/balance" % self.url).json()

    def get_trading_balance(self):
        """Get trading balance."""
        return self.session.get("%s/trading/balance" % self.url).json()

    def transfer(self, currency_code, amount, to_exchange):
        return self.session.post("%s/account/transfer" % self.url, data={
                'currency': currency_code, 'amount': amount,
                'type': 'bankToExchange' if to_exchange else 'exchangeToBank'
            }).json()

    def transfer2(self, currency_code, amount, to_exchange):
        return self.session.post("%s/account/transfer" % self.url, data={
                'currency': currency_code, 'amount': amount,
                'type': 'exchangeToBank' if to_exchange else 'bankToExchange'
            }).json()

    def new_order(self, client_order_id, symbol_code, side, quantity, price=None):
        """Place an order."""
        data = {'symbol': symbol_code, 'side': side, 'quantity': quantity}

        if price is not None:
            data['price'] = price

        return self.session.put("%s/order/%s" % (self.url, client_order_id), data=data).json()

    def get_order(self, client_order_id, wait=None):
        """Get order info."""
        data = {'wait': wait} if wait is not None else {}

        return self.session.get("%s/order/%s" % (self.url, client_order_id), params=data).json()

    def cancel_order(self, client_order_id):
        """Cancel order."""
        return self.session.delete("%s/order/%s" % (self.url, client_order_id)).json()

    def withdraw(self, currency_code, amount, address, network_fee=None):
        """Withdraw."""
        data = {'currency': currency_code, 'amount': amount, 'address': address}

        if network_fee is not None:
            data['networkfee'] = network_fee

        return self.session.post("%s/account/crypto/withdraw" % self.url, data=data).json()

    def get_transaction(self, transaction_id):
        """Get transaction info."""
        return self.session.get("%s/account/transactions/%s" % (self.url, transaction_id)).json()


if __name__ == "__main__":
    public_key = ""
    secret = ""

    btc_address = "3GWgpx5VsYsCr4neydiWQtmBsqX2LBp8q6"
    Smartcash_address = "Sc67u6beKyojTuzcJT3WDtPwg1BWwbeAtW"

    client = Client("https://api.hitbtc.com", public_key, secret)

    SMART_btc = client.get_symbol('SMARTBTC')
    address = client.get_address('SMART')     # obter endereço SMART para depósito

    print('SMART deposit address: "%s"' % address)

    # transferir todas as SMARTs depositadas da account para trading balance
    balances = client.get_account_balance()
    for balance in balances:
        if balance['currency'] == 'SMART' and float(balance['available']) > float(SMART_btc['quantityIncrement']):
            client.transfer('SMART', balance['available'], True)
            print('SMART Account balance: %s'% balance['available'])
            time.sleep(1)   # wait till transfer completed

    # get SMART trading balance
    SMART_balance = 0.0
    balances = client.get_trading_balance()
    for balance in balances:
        if balance['currency'] == 'SMART':
            SMART_balance = float(balance['available'])

    print('Current SMART balance: %s' % SMART_balance)

    # vender SMART ao melhor preço
    if SMART_balance >= float(SMART_btc['quantityIncrement']):
        client_order_id = uuid.uuid4().hex
        orderbook = client.get_orderbook('SMARTBTC')
        # set price a little high
        best_price = Decimal(orderbook['bid'][0]['price']) + Decimal(SMART_btc['tickSize'])

        print("Selling at %s" % best_price)

        order = client.new_order(client_order_id, 'SMARTBTC', 'sell', SMART_balance, best_price)
        if 'error' not in order:
            if order['status'] == 'filled':
                print("Order filled", order)
            elif order['status'] == 'new' or order['status'] == 'partiallyFilled':
                print("Waiting order...")
                for k in range(0, 3):
                    order = client.get_order(client_order_id, 20000)
                    print(order)

                    if 'error' in order or ('status' in order and order['status'] == 'filled'):
                        break

                # cancelar pedido se não estiver preenchido
                if 'status' in order and order['status'] != 'filled':
                    cancel = client.cancel_order(client_order_id)
                    print('Cancel order result', cancel)
        else:
            print(order['error'])

    # transferir todos os BTC disponíveis após trading to account balance
    balances = client.get_trading_balance()
    for balance in balances:
        if balance['currency'] == 'BTC':
            transfer = client.transfer('BTC', balance['available'], False)
            print('Transfer', transfer)
            time.sleep(1)

    # obtém o saldo da conta e saca o BTC
    balances = client.get_account_balance()
    for balance in balances:
        if balance['currency'] == 'BTC' and float(balance['available']) > 0.101:
            payout = client.withdraw('BTC', '0.1', btc_address, '0.0005')

            if 'error' not in payout:
                transaction_id = payout['id']
                print("Transaction ID: %s" % transaction_id)
                for k in range(0, 5):
                    time.sleep(20)
                    transaction = client.get_transaction(transaction_id)
                    print("Payout info", transaction)
            else:
                print(payout['error'])


