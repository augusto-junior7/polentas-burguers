class IsNotInstanceError(TypeError):
    def __init__(self, message="Value is not of the expected type."):
        self.message = message
        super().__init__(self.message)
