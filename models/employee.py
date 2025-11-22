from models.user import User


class Employee(User):
    def __init__(
        self,
        name: str,
        cpf: str,
        email: str,
        phone: str,
        position: str,
    ):
        super().__init__(name, cpf, email, phone)
        self.__position = None
        self.__salary = None

        if isinstance(position, str):
            self.__position = position

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, value: str):
        if isinstance(value, str):
            self.__position = value
        else:
            raise IsNotInstanceError("Position must be a string")

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value: float):
        if isinstance(value, (int, float)):
            self.__salary = float(value)
        else:
            raise IsNotInstanceError("Salary must be a number")

    def display_info(self):
        print(
            f"[Funcionário] ID: {super().id} | Nome: {super().name} | Cargo: {self.__position}"
        )
