
class DatabaseAppsRouter(object):
    def db_for_read(self, model, **hints):
        """"Point all read operations to the specific database."""
        if model._meta.app_label == 'app2_de2_test':
            return "db2"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "app2_de2_test":
            return "db2"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'app2_de2_test' or obj2._meta.app_label == 'app2_de2_test':
            return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'app2_de2_test':
            return db == 'db2'
        return None


