class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        data = file.read()
        file.close()
        return data

    def add(self, *products):
        prod = products
        for i in prod:
            data = self.get_products()
            if data.find(i.name) == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i.name}, {i.weight}, {i.category}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')

if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)

    s1.add(p1, p2, p3)

    print(s1.get_products())