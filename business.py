class Business:
    def __init__(self, name: str, franchise: list) -> None:
        self.name = name
        self.franchise = franchise
    
    def __repr__(self) -> str:
        return f"Business name: {self.name}, franchises: {self.franchise}"