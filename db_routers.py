# User

class UserRouter:

    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin', 'User'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'User_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'User_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels  or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'User_db'
        return None


# Products
class ProductRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Product':
            return 'Product_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Product':
            return 'Product_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label == "Product" or
            obj2._meta.app_label == "Product"
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "Product":
            return db == 'Product_db'
        return None

        