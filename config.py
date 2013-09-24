import os
basedir = os.path.abspath(os.path.dirname(__file__))

print basedir

# Database Related
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/shopify_whooks.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

print SQLALCHEMY_DATABASE_URI

# Forms Related
CSRF_ENABLED = True
SECRET_KEY = 'Why-is-Sync-so-hard-in-2013'