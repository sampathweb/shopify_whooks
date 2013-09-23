import os
basedir = os.path.abspath(os.path.dirname(__file__))


# Database Related
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'shopify_whooks.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# Forms Related
CSRF_ENABLED = True
SECRET_KEY = 'Why-is-Sync-so-hard-in-2013'