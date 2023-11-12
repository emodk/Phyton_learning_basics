class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        by_first_letter_list = []
        for i in range(len(self.products)):
            element = self.products[i]
            if element[0] == first_letter:
                by_first_letter_list.append(self.products[i])
        return by_first_letter_list

    def __repr__(self):
        a = '\n'.join(sorted(self.products))
        return f'Items in the {self.name} catalogue:\n{a}'


# test code
catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
