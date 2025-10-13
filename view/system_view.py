from view.abstract_view import AbstractView


class SystemView(AbstractView):
    def display_main_menu(self) -> str:
        print("\n--- Polenta's Burguers ---")
        print("1: Gestão de Clientes")
        print("2: Gestão de Funcionários")
        print("3: Gestão de Cardápios")
        print("4: Criar Novo Pedido")
        print("5: Relatórios")
        print("0: Sair do Sistema")
        return input("Escolha uma opção: ")
