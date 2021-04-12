class Category:
    def __init__(self, category_id, product_id, category_name, description):
        self.category_id = category_id
        self.product_id = product_id
        self.category_name = category_name
        self.description = description


    def __str__(self):
        return self.category_name + ", " + self.description

class Product:
    def __init__(self, product_id, category_id, product_name, value, description, category_name):
        self.product_id = product_id
        self.category_id = category_id
        self.product_name = product_name
        self.value = value
        self.description = description
        self.category_name = category_name

    
    def __str__(self):
        return self.product_name + ", " + str(self.value) + ", " + self.description + ", " + self.category_name
