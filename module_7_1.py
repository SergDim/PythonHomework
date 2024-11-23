

class Product:

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return self.name + ", " + str(self.weight) + ", " + self.category


class Shop:

    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, mode = 'tr')
        s = file.read()
        file.close()
        return s

    def add(self, *products):
        file_products  = self.get_products()
        file = open(self.__file_name, mode='a')
        for p in products:
            if file_products.find(p.name) != -1:
                print(f"Продукт {p.name} уже есть в магазине")
            else:
                file.write(str(p))
                file.write("\n")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())