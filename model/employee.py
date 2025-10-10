from model.user import User


class Employee(User):
    def __init__(
        self, name: str, cpf: str, email: str, phone: str, position: str
    ):
        super().__init__(name, cpf, email, phone)
        self._position = None
        self._salary = None

        if isinstance(position, str):
            self._position = position

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value: str):
        if isinstance(value, str):
            self._position = value
        else:
            raise IsNotInstanceError("Position must be a string")

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float):
        if isinstance(value, (int, float)):
            self._salary = float(value)
        else:
            raise IsNotInstanceError("Salary must be a number")

    def display_info(self):
        print(
            f"[Funcionário] ID: {self._id} | Nome: {self._name} | Cargo: {self._position}"
        )
