import FreeSimpleGUI as sg

from views.abstract_view import AbstractView


class SystemView(AbstractView):
    def display_main_menu(self) -> str:
        layout = [
            [sg.Text("Polenta's Burguers", font=("Arial", 25))],
            [sg.Button("Gestão de Clientes", key="1", size=(30, 2))],
            [sg.Button("Gestão de Funcionários", key="2", size=(30, 2))],
            [sg.Button("Gestão de Cardápios", key="3", size=(30, 2))],
            [sg.Button("Gestão de Pedidos", key="4", size=(30, 2))],
            [sg.Button("Sair do Sistema", key="0", size=(30, 2))],
        ]
        window = sg.Window("Menu Principal", layout, element_justification="c")
        event, values = window.read()
        window.close()
        if event is None:
            return "0"
        return event
