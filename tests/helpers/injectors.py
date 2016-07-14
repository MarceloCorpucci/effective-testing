import imp


class UserInjector():

    def create_new(self, mail, password, name, is_admin):
        models = imp.load_source('models', '/home/marcelo/Projects/testingblog/models.py')
        models.User.create(mail, password=password, name=name, admin=is_admin)
