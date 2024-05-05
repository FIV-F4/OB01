class Store:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = {}
    def add_item(self, item, price):
        pass
    def remove_item(self, item):
        pass
    def show_price_item(self):
        pass
    def update_price_item(self):
        pass


Store1 = Store("Shop", "Moscow")
Store2 = Store("KB", "SPB")
Store3 = Store("NY", "NY")

Store1.add_item("Гвоздь", 10)
Store2.add_item("Дубель", 15)
Store3.add_item("Линейка", 20)