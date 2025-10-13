class InvalidCPFError(Exception):
    def __init__(self, message="Invalid CPF."):
        self.message = message
        super().__init__(self.message)
