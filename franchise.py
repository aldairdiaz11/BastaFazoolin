class Franchise:
    def __init__(self, address: str, menus: list) -> None:
        self.address = address
        self.menus = menus
    
    def __repr__(self) -> str:
        return self.address
    
    def available_menus(self, time: int) -> list:
        available_menu = []
        for menu in self.menus:
            if menu.start_time <= time < menu.end_time:
                available_menu.append(menu) 
        return available_menu
