from typing import List

from model.order import Order
from view.abstract_view import AbstractView


class OrderView(AbstractView):
    def display_order_menu(self) -> str:
        print("\n--- Menu de Pedidos ---")
        print("1: Criar Pedido")
        print("2: Listar Pedidos")
        print("3: Cancelar Pedido")
        print("4: Gerar Relatório de Vendas de Produtos")
        print("0: Voltar ao Menu Principal")
        return input("Selecione uma opção: ")

    def get_client_cpf_for_order(self) -> str:
        return input("Digite o CPF do cliente para este pedido: ")

    def get_order_id_for_update(self) -> int:
        try:
            return int(input("Digite o ID do pedido a ser cancelado: "))
        except ValueError:
            return 0

    def get_item_to_add(self) -> str:
        return input(
            "Digite o nome do item a ser adicionado (ou digite 'concluir' para finalizar): "
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
            if order.status == "Ativo":
                print(
                    f"Pedido #{order.id} | Cliente: {order.client.name} | Total: R$ {order.total:.2f} | Status: {order.status}"
                )
            else:
                print(
                    f"Pedido #{order.id} | Cliente: {order.client.name} | Total: R$ {order.total:.2f} | Status: {order.status}"
                )
        print("------------------")

    def display_product_sales_report(self, sales_data: dict) -> None:
        """Exibe relatório de vendas de produtos."""
        print("\n=== Relatório de Vendas de Produtos ===")
        if not sales_data:
            print("Nenhum dado disponível.")
            return

        print(f"{'Produto':<30} {'Quantidade':<15} {'Receita (R$)':<15}")
        print("-" * 60)

        total_quantity = 0
        total_revenue = 0.0

        for product, data in sorted(sales_data.items()):
            quantity = data["quantity"]
            revenue = data["revenue"]
            total_quantity += quantity
            total_revenue += revenue
            print(f"{product:<30} {quantity:<15} {revenue:<15.2f}")

        print("-" * 60)
        print(f"{'TOTAL':<30} {total_quantity:<15} {total_revenue:<15.2f}")
        print("=" * 60)
