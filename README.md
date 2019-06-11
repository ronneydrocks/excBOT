# excBOT
BOT que monitora as exchanges EXC CRIPTO e BLEUTRADE em busca de oportunidades.

# COMO FUNCIONA
O BOT monitora os books e compra os valores, caso encontre oportunidade de compra mais barato em uma exchange e vender mais caro na outra, automaticamente executa os comandos em alguns segundos.

# COMO EXECUTAR
Após instalação e configuração. Abra um terminal e execute o comando para que o BOT inicie o trabalho.

# INSTALAÇÃO
1. Cadastre na EXC CRIPTO(exccripto.com) e BLEUTRADE(bleutrade.com)
2. Gerar Key na EXC e BLEU
3. Instalar python, pip e requests
4. Configurar BOT com KEYs (EXC e BLEU)
5. Rodar

# VERSÃO
VERSÃO: 0.1.4
- Adicionado verificação de saldo
- Função que informa se houve lucros ou perdas

VERSÃO: 0.1.3
- Adicionado Mercado USDT (excbleu BTC/USDT)
- Adicionado informação do lucro nas arbitragens
- Formatação logs telegram
- Formatação logs txt

VERSÃO: 0.1.2
- Adicionado logs em txt
- Adicionado logs via Telegram 

VERSÃO: 0.1.1
- Adicionado auto balance
- Adicionado compra mínima

VERSÃO: 0.1.0
- Adicionado ordem de compra
- Adicionado ordem de transferência via DIREC TRANSFER
- Adicionado ordem de venda

VERSÃO: 0.0.1
- Busca informações nas exchanges EXC e BLEU
- Monitora book no mercado BTC
- Monitora book no mercado DOGE
- Compara valores de compra e venda nas exchanges EXC e BLEU
- Verifica se existe oportunidade de arbitragem entre as exchanges









