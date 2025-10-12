from typing import List
from model.order import Order


class OrderView:
    def display_message(self, message: str) -> None:
        print(f"\n--- {message} ---\n")

    def display_success_message(self, message: str) -> None:
        print(f"\n✅ SUCESSO: {message}\n")

    def display_error_message(self, message: str) -> None:
        print(f"\n❌ ERRO: {message}\n")

    def get_client_cpf_for_order(self) -> str:
        return input("Digite o CPF do cliente para este pedido: ")

    def get_item_to_add(self) -> str:
        return input(
            "Digite o nome do item a ser adicionado (ou digite 'done' para finalizar): "
        )

    def get_quantity(self) -> int:
        try:
            return int(input("Digite a quantidade: "))
        except ValueError:
            return 0

    def display_current_order(self, order: Order) -> None:
        print("\n--- Pedido Atual ---")
        for item in order.items:
            print(f"- {item.quantity}x {item.menu_item.name}")
        print(f"Total Atual: R$ {order.total:.2f}")
        print("---------------------")

    def display_final_order_summary(self, order: Order) -> None:
        print("\n--- Resumo do Pedido ---")
        print(f"Pedido #{order.id} para o Cliente: {order.client.name}")
        for item in order.items:
            print(
                f"- {item.quantity}x {item.menu_item.name} (Sub: R$ {item.subtotal:.2f})"
            )
        print(f"TOTAL FINAL: R$ {order.total:.2f}")
        print("---------------------")

    def display_order_list(self, orders: List[Order]) -> None:
        print("\n--- Todos os Pedidos ---")
        if not orders:
            print("Não há pedidos registrados.")
        for order in orders:
            print(
                f"Pedido #{order.id} | Cliente: {order.client.name} | Total: R$ {order.total:.2f}"
            )
        print("------------------")
