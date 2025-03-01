current_balance = 0

def deposit():
    """Realiza o depósito de um valor na conta."""
    global current_balance
    print('\n- - - D E P Ó S I T O - - -')
    
    try:
        amount = float(input('\nQuanto você deseja depositar? R$'))
        if amount > 0:
            current_balance += amount
            print(f'\nDepósito realizado com sucesso! Novo saldo: R${current_balance:.2f}')
        else:
            print('\nValor inválido! O depósito deve ser maior que R$0.')
    except ValueError:
        print('\nErro! Digite um número válido.')

def view_balance():
    """Exibe o saldo atual da conta."""
    print('\n- - - S A L D O - - -')
    print(f'\nSeu saldo atual é R${current_balance:.2f}')

def transfer():
    """Realiza uma transferência para outro usuário."""
    global current_balance
    print('\n- - - T R A N S F E R Ê N C I A - - -')
    recipient_email = input('\nEmail do destinatário: ').strip()
    
    while True:
        try:
            amount = float(input('Quantia a ser transferida: R$'))
            if amount <= 0:
                print('\nValor inválido! A quantia deve ser maior que zero.')
            elif amount > current_balance:
                print('\nSaldo insuficiente. Por favor, tente novamente!')
            else:
                current_balance -= amount
                print(f'\nTransferência de R${amount:.2f} concluída para {recipient_email}!')
                break
        except ValueError:
            print('\nErro! Digite um valor numérico válido.')

def withdraw():
    """Realiza um saque da conta."""
    global current_balance
    print('\n- - - S A Q U E - - -')
    
    try:
        amount = float(input('\nQuanto deseja sacar? R$'))
        if amount <= 0:
            print('\nValor inválido! O saque deve ser maior que R$0.')
        elif amount > current_balance:
            print('\nSaldo insuficiente!')
        else:
            current_balance -= amount
            print(f'\nSaque realizado com sucesso! Novo saldo: R${current_balance:.2f}')
    except ValueError:
        print('\nErro! Digite um valor numérico válido.')

def invest():
    """Menu de investimentos (ações e criptomoedas)."""
    stocks = ['NVDA', 'AMZO34', 'IBOV', 'GOGL34', 'MSFT34']
    cryptocurrencies = ['BTC', 'ETH', 'XRP']
    user_stocks = []
    user_cryptos = []

    def stock_exchange():
        """Compra e venda de ações."""
        print('\n- - - B O L S A - - -')
        while True:
            choice = input('\n1 - Comprar ações\n2 - Vender ações\n3 - Voltar\n\n').strip()
            if choice == '1':
                print('\nAções disponíveis:', ', '.join(stocks))
                stock = input('Digite o nome da ação que deseja comprar: ').strip().upper()
                if stock in stocks:
                    user_stocks.append(stock)
                    print(f'\nVocê comprou ações da {stock}!')
                else:
                    print('\nAção inválida!')
            elif choice == '2':
                if not user_stocks:
                    print('\nVocê não possui ações para vender.')
                else:
                    print('\nSuas ações:', ', '.join(user_stocks))
                    stock = input('Digite o nome da ação que deseja vender: ').strip().upper()
                    if stock in user_stocks:
                        user_stocks.remove(stock)
                        print(f'\nVocê vendeu ações da {stock}!')
                    else:
                        print('\nVocê não possui essa ação.')
            elif choice == '3':
                break
            else:
                print('\nOpção inválida!')

    def crypto():
        """Compra e venda de criptomoedas."""
        print('\n- - - C R I P T O M O E D A S - - -')
        while True:
            choice = input('\n1 - Comprar criptos\n2 - Vender criptos\n3 - Voltar\n\n').strip()
            if choice == '1':
                print('\nCriptomoedas disponíveis:', ', '.join(cryptocurrencies))
                crypto = input('Digite o nome da criptomoeda que deseja comprar: ').strip().upper()
                if crypto in cryptocurrencies:
                    user_cryptos.append(crypto)
                    print(f'\nVocê comprou {crypto}!')
                else:
                    print('\nCriptomoeda inválida!')
            elif choice == '2':
                if not user_cryptos:
                    print('\nVocê não possui criptos para vender.')
                else:
                    print('\nSuas criptomoedas:', ', '.join(user_cryptos))
                    crypto = input('Digite o nome da criptomoeda que deseja vender: ').strip().upper()
                    if crypto in user_cryptos:
                        user_cryptos.remove(crypto)
                        print(f'\nVocê vendeu {crypto}!')
                    else:
                        print('\nVocê não possui essa criptomoeda.')
            elif choice == '3':
                break
            else:
                print('\nOpção inválida!')

    def view_investments():
        """Exibe os investimentos atuais (ações e criptomoedas)."""
        print('\n- - - S E U S  I N V E S T I M E N T O S - - -')
        if user_stocks:
            print('\nAções:', ', '.join(user_stocks))
        else:
            print('\nNenhuma ação comprada!')
        if user_cryptos:
            print('\nCriptomoedas:', ', '.join(user_cryptos))
        else:
            print('\nNenhuma criptomoeda comprada!')
    
    while True:
        choice = input('\n1 - Bolsa de valores\n2 - Criptomoedas\n3 - Ver investimentos\n4 - Voltar\n\n').strip()
        if choice == '1':
            stock_exchange()
        elif choice == '2':
            crypto()
        elif choice == '3':
            view_investments()
        elif choice == '4':
            break
        else:
            print('\nOpção inválida!')

def main():
    """Função principal do banco."""
    print('- - - B A N C O  A R C O V E R D E - - -')
    while True:
        choice = input('\n1 - Depositar\n2 - Retirar\n3 - Transferir\n4 - Ver saldo\n5 - Investimentos\n6 - Sair\n\n').strip()
        if choice == '1':
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            transfer()
        elif choice == '4':
            view_balance()
        elif choice == '5':
            invest()
        elif choice == '6':
            print('\nEncerrando...')
            break
        else:
            print('\nOpção inválida!')

if __name__ == '__main__':
    main()