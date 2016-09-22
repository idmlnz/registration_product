from flask.ext.bcrypt import Bcrypt
from system.core.model import Model
import re

class Register(Model):
    def __init__(self):
        super(Register, self).__init__()

    def checkUser(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 1:
            errors.append('Password must be at least 8 characters long')

        if errors:
            return {"status": False, "errors": errors}
        else:
            get_user_query = "SELECT * FROM user WHERE email=\"{}\"".format(info['email'])
            user = self.db.query_db(get_user_query)[0]
            if (info['password'] == user['password']):
                return {"status": True, "user": user}
            else:
                errors.append('Login account is incorrect!!')
                return {"status": False, "errors": errors}

    def createUser(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # Some basic validation
        if not info['firstname']:
            errors.append('firstname cannot be blank')
        elif not info['lastname']:
            errors.append('lastname cannot be blank')
        elif len(info['firstname']) < 2:
            errors.append('firstname must be at least 2 characters long')
        elif len(info['lastname']) < 2:
            errors.append('lastname must be at least 2 characters long')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 1:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['confirm_password']:
            errors.append('Password and confirmation must match!')

        if errors:
            return {"status": False, "errors": errors}
        else:
            # add user to DB
            #pw_hash = bcrypt.generate_password_hash(info['password'])
            pw_hash = info['password']
            insertQuery = "INSERT INTO user (firstname, lastname, email, password, created_at, updated_at) \
                VALUES (:firstname, :lastname, :email, :password, NOW(), NOW())"

            userData = {
                'firstname': info['firstname'],
                'lastname': info['lastname'],
                'email': info['email'],
                'password': pw_hash
            }
            print "userdata: {}".format(userData)
            self.db.query_db(insertQuery, userData)

            get_user_query = "SELECT * FROM user ORDER BY id DESC LIMIT 1"
            user = self.db.query_db(get_user_query)
            return {"status": True, "user": user[0]}

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
