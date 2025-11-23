from abc import ABC

import FreeSimpleGUI as sg


class AbstractView(ABC):
    def __init__(self):
        sg.theme("SystemDefault")

    def _show_popup(self, title: str, message: str) -> None:
        layout = [
            [sg.Text(message, font=("Helvetica", 12), justification="center")],
            [sg.Button("OK", size=(10, 1))],
        ]
        window = sg.Window(
            title, layout, element_justification="c", modal=True
        )
        window.read()
        window.close()

    def display_message(self, message: str) -> None:
        self._show_popup("Mensagem", message)

    def display_success_message(self, message: str) -> None:
        self._show_popup("Sucesso", message)

    def display_error_message(self, message: str) -> None:
        self._show_popup("Erro", message)
