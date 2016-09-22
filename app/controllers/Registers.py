from system.core.controller import *

class Registers(Controller):
  def __init__(self, action):
    super(Registers, self).__init__(action)
    self.load_model('Register')
    self.db = self._app.db

  def index(self):
    return self.load_view('registration/register.html')

  def new(self):
    return self.load_view('registration/register.html')

  def add(self):
    userInfo = {}
    userInfo['firstname'] = request.form['firstname']
    userInfo['lastname'] = request.form['lastname']
    userInfo['email'] = request.form['email']
    userInfo['password'] = request.form['password']
    userInfo['confirm_password'] = request.form['confirm_password']

    createStatus = self.models['Register'].createUser(userInfo)
    print "createstatus: {}".format(createStatus)
    if createStatus['status'] == True:
      session['user'] = createStatus['user']
    else:
      for message in createStatus['errors']:
        flash(message, 'regis_errors')
      return self.load_view('registration/register.html', error=createStatus['errors'])

    return redirect('/products/new')  # redirect to product

  def login(self):
    userInfo = {}
    userInfo['email'] = request.form['login-email']

    userInfo['password'] = request.form['login-password']
    loginStatus = self.models['Register'].checkUser(userInfo)

    if loginStatus['status'] == True:
      session['user'] = loginStatus['user']

    else:

      for message in loginStatus['errors']:
        flash(message, 'regis_errors')
      return self.load_view('registration/register.html', error=loginStatus['errors'])

    return redirect('/products/display')  # redirect to product

