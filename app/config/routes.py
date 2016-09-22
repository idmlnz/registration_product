from system.core.router import routes

#routes['default_controller'] = 'Products'
routes['default_controller'] = 'Registers'

routes['GET']['/products/display'] = 'Products#display'
routes['GET']['/products/new'] = 'Products#new'
routes['POST']['/products/add'] = 'Products#addProduct'
routes['POST']['/products/doAction/<productId>'] = 'Products#doAction'
routes['POST']['/products/update/<productId>'] = 'Products#update'
routes['POST']['/products/delete/<productId>'] = 'Products#delete'

routes['GET']['/registers/new'] = 'Registers#new'
routes['POST']['/registers/add'] = 'Registers#add'
routes['POST']['/registers/login'] = 'Registers#login'
