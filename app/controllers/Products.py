from system.core.controller import *

class Products(Controller):
  def __init__(self, action):
    super(Products, self).__init__(action)
    self.load_model('Product')
    self.db = self._app.db

  def index(self):
    pass

  def display(self):
    products = self.models['Product'].getProducts()
    return self.load_view('products/products.html', products=products)

  def new(self):
    return self.load_view('products/add.html')

  def addProduct(self):
    productData = {
      'name': request.form['name'],
      'description': request.form['description'],
      'price': request.form['price']
    }

    self.models['Product'].addProduct(productData)
    return redirect('/products/display')

  def displayUpdateView(self, productId):
    product = self.models['Product'].getProductById(productId)
    return self.load_view('products/update.html', product=product[0])

  def displayShowView(self, productId):
    product = self.models['Product'].getProductById(productId)
    return self.load_view('products/show.html', product=product[0])

  def update(self, productId):
    product = {}
    product['name'] = request.form['name']
    product['description'] = request.form['description']
    product['price'] = request.form['price']
    product = self.models['Product'].updateProductById(product, productId)
    return redirect('/products/display')

  def delete(self, productId):
    product = self.models['Product'].deleteProductById(productId)
    return redirect('/products/display')

  def doAction(self, productId):
    action = request.form['action']
    if (action == 'Show'):
      return self.displayShowView(productId)

    if (action == 'Edit'):
      return self.displayUpdateView(productId)

    if (action == 'Remove'):
      return self.delete(productId)

