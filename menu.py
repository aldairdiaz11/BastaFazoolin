class Menu:
    def __init__(self, name: int, items: dict, start_time: int, end_time: int):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def calculate_bill(self, purchased_items: list):
        total = 0
        for item in purchased_items:
            total += self.items[item]
        return total
  
    def __repr__(self):
        return f"Menu: {self.name}, this menu is available between {self.start_time} and {self.end_time}"
    