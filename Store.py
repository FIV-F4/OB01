class Store:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = {}
    def add_item(self, item, price):
        if item in self.items:
            print("Товар уже существует")
        else:
            self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print("Такого товара нет")
    def show_price_item(self, item):
        if item in self.items:
            return self.items[item]
        else:
            print("Такого товара нет")
    def update_price_item(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price
        else:
            print("Такого товара нет")


Store1 = Store("Shop", "Moscow")
Store2 = Store("KB", "SPB")
Store3 = Store("NY", "NY")

Store1.add_item("Гвоздь", 10)
Store1.add_item("Дубель", 15)
Store1.add_item("Гвоздь", 10)
Store1.add_item("Линейка", 20)
print(Store1.items)

Store1.remove_item("Гвоздь")
print(Store1.items)

print(Store1.show_price_item("Линейка"))

Store1.update_price_item("Линейка", 25)
Store1.update_price_item("Арбуз", 25)
print(Store1.items)


