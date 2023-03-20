import os
from pathlib import Path
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }


BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING!
SECRET_KEY = 'django-insecure-0^+c%&_9v((7=ost_iooj8$rw*50o=j)$uze*)iv&b_*d$qbxj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps
    'jazzmin',
    'livereload',
    # 'social_django',


    # custom apps
    'taskManager',
    'users',
]
 
JAZZMIN_SETTINGS = {
    "site_title": "ParkingBD Admin",
    "site_header": "ParkingBD",
    "site_brand": "ParkingBD",
    "site_logo": None,
    "login_logo": None,
}
# Admin options for JAZZMIN admin panel
# JAZZMIN_SETTINGS["show_ui_builder"] = True

JAZZMIN_UI_TWEAKS = {
    "theme": "simplex",
    # "dark_mode_theme": "darkly",
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 3rd party middleware
    
    'livereload.middleware.LiveReloadScript',
    # 'social_django.middleware.SocialAuthExceptionMiddleware',

]

ROOT_URLCONF = 'OfficeTaskManager2023.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # 3rd party context processors
                
                # 'social_django.context_processors.backends', 
                # 'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'OfficeTaskManager2023.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR/'static']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'media'

LOGIN_REDIRECT_URL = '/user/profile'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# NOT NECESSARY

# SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/'
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

# # social auth configs for google
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '959252773314-o541u9toune9fdn5nh961ad3sa52gj5j.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'


# ####
# # This is for development purpose only (email reset infos would be shown in console)
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# #### email configs (web)
# # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # EMAIL_HOST = 'smtp.gmail.com'
# # EMAIL_USE_TLS = True
# # EMAIL_PORT = 587
# # EMAIL_HOST_USER = 'your gmail as string'
# # EMAIL_HOST_PASSWORD = 'your gmail password as string' 
# # DEFAULT_FROM_EMAIL = 'noreply<no_reply@domain.com>'

# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.google.GoogleOAuth2',
#     'social_core.backends.google.GoogleOAuth',

#     'django.contrib.auth.backends.ModelBackend',
# )



# SOCIAL_AUTH_PIPELINE = (
#     'social_core.pipeline.social_auth.social_details',
#     'social_core.pipeline.social_auth.social_uid',
#     'social_core.pipeline.social_auth.social_user',
#     'social_core.pipeline.user.get_username',
#     'social_core.pipeline.social_auth.associate_by_email',
#     'social_core.pipeline.user.create_user',
#     'social_core.pipeline.social_auth.associate_user',
#     'social_core.pipeline.social_auth.load_extra_data',
#     'social_core.pipeline.user.user_details',
# )