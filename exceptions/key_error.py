class KeyErrorException(Exception):
    def __init__(self, message: str = "Key not found in DAO."):
        self.message = message
        super().__init__(self.message)
