from abc import ABC


class AbstractView(ABC):
    def display_message(self, message: str) -> None:
        print(f"\n--- {message} ---\n")

    def display_success_message(self, message: str) -> None:
        print(f"\n✅ SUCESSO: {message}\n")

    def display_error_message(self, message: str) -> None:
        print(f"\n❌ ERRO: {message}\n")