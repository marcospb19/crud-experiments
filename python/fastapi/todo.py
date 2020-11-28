from typing import Dict, Union

TodoKey = Union[str, int]
TodoValue = str

class Todo:
    """TODO example class"""
    def __init__(self, description: str, category: str, id_: int) -> None:
        self.description: str = description
        self.category: str = category
        self.id: int = id_

    def __iter__(self) -> Dict[TodoKey, TodoValue]:
        return {
            'description': self.description,
            'category': self.category,
        }
