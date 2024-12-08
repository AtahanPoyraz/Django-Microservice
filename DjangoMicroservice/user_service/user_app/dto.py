from typing import Any, Dict

class GenericResponseDTO:
    def __init__(self, data: Any = None, message: str = "Success", status: int = 200):
        self.status = status
        self.message = message
        self.data = data or {}

    def to_dict(self) -> Dict:
        return {
            "status": self.status,
            "message": self.message,
            "data": self.data
        }
