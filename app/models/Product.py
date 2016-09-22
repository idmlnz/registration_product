from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def getProducts(self):
        query = "SELECT * from product"
        return self.db.query_db(query)


    def getProductById(self, productId):
        query = "SELECT * from product where id={}".format(productId)
        return self.db.query_db(query)

    def updateProductById(self, product, productId):
        query = "UPDATE product SET name = :name, description = :description, price = :price, updated_at=NOW() "\
          "WHERE id = {}".format(productId)
        data = {
            'name': product['name'],
            'description': product['description'],
            'price': product['price']
        }
        return self.db.query_db(query, data)

    def addProduct(self, product):
        query = "INSERT into product (name, description, price, created_at, updated_at ) values (:name, :description, :price, NOW(), NOW())"
        data = {
            'name': product['name'],
            'description': product['description'],
            'price': product['price'],
        }
        return self.db.query_db(query, data)

    def deleteProductById(self, productId):
        query = "DELETE FROM product WHERE id = {}".format(productId)
        return self.db.query_db(query)
