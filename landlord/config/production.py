ADMINS = ()
MANAGERS = ADMINS
DEBUG = True
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = '7otdo_u@#d9c6!0@83%dsq4%_tf3aez=9evh!8j7$%9oh$#28g'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'landlord_db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'landlord',
        'PASSWORD': 'jkui',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}