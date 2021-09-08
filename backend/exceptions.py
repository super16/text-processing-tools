class AlreadyExistsException(Exception):
    
    def __init__(self, title: str):
        self.title = title

class DoesNotExistException(Exception):
    
    def __init__(self, id: int):
        self.id = id