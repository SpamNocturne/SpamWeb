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