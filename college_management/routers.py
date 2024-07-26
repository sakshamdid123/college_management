class Vetting2425Router:
    """
    A router to control all database operations on models in the
    vetting_2425 schema.
    """
    def db_for_read(self, model, **hints):
        """Point all operations on vetting_2425 models to 'vetting_db'."""
        if model._meta.app_label == 'vetting_2425':
            return 'vetting_db'
        return None

    def db_for_write(self, model, **hints):
        """Point all operations on vetting_2425 models to 'vetting_db'."""
        if model._meta.app_label == 'vetting_2425':
            return 'vetting_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in vetting_2425 is involved."""
        if obj1._meta.app_label == 'vetting_2425' or \
           obj2._meta.app_label == 'vetting_2425':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the vetting_2425 app only appears in the 'vetting_db'
        database.
        """
        if app_label == 'vetting_2425':
            return db == 'vetting_db'
        return None
