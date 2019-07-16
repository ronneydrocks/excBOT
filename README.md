# excBOT
Atualmente o BOT está na versão v0.1.5(TESTE) e sua função é automatizar arbitragens entre as EXC CRIPTO e BLEUTRADE. Sua estratégia principal é comprar mais barato e vender mais caro conforme SPREAD configurado pelo usuário.


# FUNÇÕES
* Monitorar livro de ordens
* Analisa e compara valores
* Analisa quantidades para definir compra
* Efetua compra, transferência e venda
* Mostrar saldo via Telegram
* Mostrar informações da arbitragem via Telegram
* Compra de valores mínimos se saldo for insuficiente
* Auto balance
* Tratamento de erros response
* Calcula SPREAD
* Calcula FEE
* Simulador de arbitragem


# ATENÇÃO:
O BOT está em fase de testes, NÃO HÁ NENHUMA GARANTIA DE GANHOS. O BOT está sendo desenvolvido, está sujeito a erros e por esse motivo está em constantes atualizações. O desenvolvedor do excBOT NÃO SE RESPONSABILIZA POR PREJUÍZOS ocasionados por mal uso do BOT.

DICA:
* A principal configuração do BOT para ficar positivo, é o SPREAD. No arquivo de configuração, config.py, tem uma opção para configura-lo.
* Para ficar positivo é necessário configurar o SPREAD + FEE.
* FEE  0.25 (EXC/BLEU)
* Configurar o spread correto para não ficar negativo por causa da FEE.

Spread refere-se à diferença entre o preço de compra (procura) e venda (oferta) de um ativo.

# COMO FUNCIONA
O BOT monitora os books e compara os valores, caso encontre oportunidades, compra mais barato em uma exchange e vender mais caro na outra e automaticamente executa os comandos em alguns segundos.

# COMO EXECUTAR
Após instalação e configuração. Abra um terminal e execute o comando para que o BOT inicie o trabalho.

# INSTALAÇÃO
1. Cadastre na EXC CRIPTO(https://exccripto.com) e BLEUTRADE(https://bleutrade.com)
2. Gerar Key/Secret na EXC e BLEU
3. Instalar python, pip e requests
4. Configurar BOT com KEYs (EXC e BLEU)
5. Rodar

#ATUALIZAÇÕES

VERSÃO: 0.1.5
- Melhora no tratamento dos erros (RESPONSE)
- Adicionado informação sobre FEE
- Adicionado informação sobre Arbitragem
- Adicionado informação sobre SPREAD (em % e USDT)
- Adicionado simulador de arbitragem (Ajuda escolher melhor SPREAD)
- Correção ordens venda mínima (Muita ordens abertas no book)
 - Melhora da função AUTO BALANCE

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
