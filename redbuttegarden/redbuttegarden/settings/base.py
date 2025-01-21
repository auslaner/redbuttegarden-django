"""
Django settings for redbuttegarden project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Application definition

INSTALLED_APPS = [
    'axe',
    'concerts',
    'custom_user',
    'events',
    'home',
    'journal',
    'plants',
    'redbuttegarden.apps.CustomUsersAppConfig',
    'search',
    'shop',

    'wagtail.contrib.forms',
    'wagtail.contrib.frontend_cache',
    'wagtail.contrib.redirects',
    'wagtail.contrib.routable_page',
    'wagtail.contrib.search_promotions',
    'wagtail.contrib.settings',
    "wagtail.contrib.table_block",
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',

    'cas',  # Sometimes necessary to comment this app out to dump database
    'corsheaders',
    'django_tables2',
    'modelcluster',
    'rest_framework',
    'rest_framework.authtoken',
    'storages',
    'taggit',
    'wagtailaccessibility',
    'webpack_loader',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # TODO - re-enable Django-CSP

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'redbuttegarden.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'redbuttegarden.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Denver'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
    os.path.join(BASE_DIR, '..', 'frontend', 'assets'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


AUTH_USER_MODEL = 'custom_user.User'


# Wagtail settings
WAGTAIL_SITE_NAME = "redbuttegarden"
WAGTAILEMBEDS_RESPONSIVE_HTML = True
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 4.5 * 1024 * 1024  # i.e. 4.5MB - Needed to avoid hitting AWS API Gateway payload limits
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
        'SEARCH_CONFIG': 'english',
    },
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = 'https://redbuttegarden.org'

# Safe to do this as since our docs/images shouldn't contain sensitive info. Info: https://docs.wagtail.io/en/v2.8/reference/settings.html?highlight=images#documents
WAGTAILDOCS_SERVE_METHOD = 'direct'

# Zappa settings to strip the stage name from urls (requires X_FORWARDED_HOST custom header in Cloudfront)
USE_X_FORWARDED_HOST = True
FORCE_SCRIPT_NAME = ''

# CAS
MIDDLEWARE_CLASSES = (
    'cas.middleware.CASMiddleware',
)
CAS_SERVER_URL = "https://go.utah.edu/cas/"
WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'cas.backends.CASBackend',
)
CAS_LOGOUT_COMPLETELY = True
CAS_PROVIDE_URL_TO_LOGOUT = True
CAS_AUTO_CREATE_USER = False
CAS_RESPONSE_CALLBACKS = (
    'custom_user.cas_handler.create_cas_user',
)

ADMINS = [('IT', os.environ.get('IT_EMAIL'))]
DEFAULT_FROM_EMAIL = 'admin@redbuttegarden.org'
SERVER_EMAIL = os.environ.get('IT_EMAIL')

# This was setup to allow authentication for viewing VR Tours
PASSWORD_REQUIRED_TEMPLATE = 'custom_user/password_required.html'
LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/'

# Prep for upgrade to Django 3.2
# https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

MAPBOX_API_TOKEN = "pk.eyJ1IjoiYXVzbGFuZXIiLCJhIjoiY2tlMXZ2Yml0MDNlODJ1c3p6d2IweWRobiJ9.UPSxvlFp9B5NYelSHUwhRw"

# hCaptcha
HCAPTCHA_SITE_KEY = os.environ.get('HCAPTCHA_SITE_KEY')
HCAPTCHA_SECRET_KEY = os.environ.get('HCAPTCHA_SECRET_KEY')

# Comet Chat
COMET_CHAT_APP_ID = os.environ.get('COMET_CHAT_APP_ID')
COMET_CHAT_REGION = 'US'
COMET_CHAT_AUTH_KEY = os.environ.get('COMET_CHAT_AUTH_KEY')
COMET_CHAT_WIDGET_ID = os.environ.get('COMET_CHAT_WIDGET_ID')

# OpenWeather API
OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')
