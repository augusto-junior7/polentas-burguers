class EntityNotFoundError(Exception):
    def __init__(self, message="Entity not found."):
        self.message = message
        super().__init__(self.message)
