class SystemView:
    def display_main_menu(self) -> str:
        print("\n--- Polenta's Burguers ---")
        print("1: Gestão de Clientes")
        print("2: Gestão de Funcionários")
        print("3: Gestão de Cardápios")
        print("4: Criar Novo Pedido")
        print("0: Sair do Sistema")
        return input("Escolha uma opção: ")

    def display_client_menu(self) -> str:
        print("\n--- Gestão de Clientes ---")
        print("1: Adicionar Cliente")
        print("2: Listar Clientes")
        # Adicione update/delete aqui se desejar
        print("0: Voltar ao Menu Principal")
        return input("Escolha uma opção: ")

    def display_employee_menu(self) -> str:
        print("\n--- Gestão de Funcionários ---")
        print("1: Adicionar Funcionário")
        print("2: Listar Funcionários")
        print("0: Voltar ao Menu Principal")
        return input("Escolha uma opção: ")

    def display_message(self, message: str) -> None:
        print(f"\n--- {message} ---\n")

    def display_error_message(self, message: str) -> None:
        print(f"\n❌ ERRO: {message}\n")
