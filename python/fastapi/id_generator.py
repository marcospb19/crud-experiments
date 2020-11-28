Id = int

# This IdGenerator is simple and unreliable
class IdGenerator:
    """Generates unique Ids for Todo entries"""
    def __init__(self):
        # Start generating at 0
        self.start: Id = 0
    def next(self) -> Id:
        self.start += 1
        return self.start - 1
