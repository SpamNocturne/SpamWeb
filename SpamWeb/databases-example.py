# Utiliser ce modèle pour le fichier databases.py qui est import dans settings.py
# Ce fichier est versionné pour servir d'exemple de structure
# Contrairement à databases.py qui n'est pas versionné


def getDatabaseConfig():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'webspam-bdd',
            'HOST': '',
            'PASSWORD': '',
            'PORT': '',
            'USER': 'root',
        }
    }
    return DATABASES

# ou
def getDatabaseConfig():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'webspam-bdd',
            'HOST': '',
            'PASSWORD': '',
            'PORT': '5432',
            'USER': 'postgres',
        }
    }
    return DATABASES