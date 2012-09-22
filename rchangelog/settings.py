# -*- coding: utf-8 -*-

# Django settings for rchangelog project.

# rChangelog specifikus beallitasok, tehat nem Django default

PROJECT_ROOT = '/path/to/rchangelog' # project mappa (itt talalhato a manage.py fajl)
SITE_NAME = 'rWorld Changelog' # oldal neve, ez jelenik meg a cimsavban, menuben es a page-header-ben
SITE_FOOTER_ADDRESS = '<a href="http://rworld.hu/">rWorld</a>' # ez jelenik meg alul a footerben a "&copy; ev" utan
SITE_INDEX_CHANGELOG_EXPLANATION = '''
<h4>Javítások</h4>
<p>A javítások (amik néha rontások) elsődlegesen a <a href="http://www.trinitycore.org/" target="_blank">TrinityCore</a>-tól (<abbr title="TrinityCore">TC</abbr>) származnak, de jó pár fixet mi magunk írunk meg. A <abbr title="TrinityCore">TC</abbr> javításai (<a href="https://github.com/TrinityCore/TrinityCore/commits" target="_blank">commitok</a>) a <a href="https://github.com/TrinityCore/TrinityCore" target="_blank">saját repository</a>-jában (az emu &quot;tárhelye&quot;) tekinthetők meg.</p>
<p>Mivel viszonylag sok fixet nyújt a <abbr title="TrinityCore">TC</abbr>, így ezeket is próbáljuk írni a changelog-ba, persze csak azokat, amelyeket egy átlagos player képes megérteni és kihathatnak a játékára. Ne feledd, hogy vannak olyan javítások is (elsősorban a <abbr title="TrinityCore">TC</abbr>-től), amik nálunk még nem elérhetők (pl.: insta fixek), mert az adott &quot;dolog&quot; még nincs engedélyezve.</p>
<p>Minden egyes frissítés közben (ha késik, akkor utána) megpróbáljuk az adott frissítés által hozott változásokat <strong>itt</strong> közzé tenni. A changelogokat próbáljuk logikusan, átláthatóan felépíteni.</p>
<h4>rCore</h4>
<p>A saját repositorynk (rCore) utolsó pár commitja megtekinhető <a href="http://cia.vc/stats/project/rCore" target="_blank">itt</a>. Ez valós időben frissül, tehát gyorsabban és néha többet is megtudni belőle, mint a konkrét changelog bejegyzésekből.</p>
<h4>Bug jelentő</h4>
<p>Ha a munkánkat szeretnéd segíteni, akkor szívesen fogadunk bugokat a <a href="http://bug.rworld.hu/" target="_blank">bug jelentő oldalunkon</a> (és nem ticketben).</p>
<h4>IRC</h4>
<p>Ha munkánkat közvetettebben szeretnéd segíteni (talán a fejlesztők rögös útját szeretnéd járni), akkor pedig <a href="http://hu.wikipedia.org/wiki/Internet_Relay_Chat" target="_blank">IRC</a>-re érdemes először felnézned, ott biztosan akad valaki, aki foglalkozzon a tehetségekkel: <a href="http://irc.rworld.hu/" target="_blank">irc.rworld.hu</a>.</p>
''' # ez jelenik meg az index oldalon a "Bovebben" gombra kattintva
    # tovabba a "Bovebben" gomb felett megjelenik a szoveg <p>elso paragrafusa</p> is, (ha egy sincs akkor az egesz szoveg)
SITE_INDEX_COL2 = '''
<div class="fb-like-box" data-href="https://www.facebook.com/rWorld.hu" data-width="292" data-height="300" data-show-faces="true" data-stream="false" data-header="false" style="position: absolute; right: 2%;"></div>
<div id="fb-root"></div>
<script>(function(d, s, id) {
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
js = d.createElement(s); js.id = id;
js.src = "//connect.facebook.net/hu_HU/all.js#xfbml=1";
fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
''' # index oldalon a 2. "oszlopban" jelenik meg
    # facebook like oldalt erdemes ide tenni
    # ha semmit sem, akkor siman ures string: SITE_INDEX_COL2 = ''

# #############################################################################

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'rchangelog',                      # Or path to database file if using sqlite3.
        'USER': 'rchangelogger',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '/var/run/mysqld/mysqld.sock',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Budapest'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'hu-HU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '%s/static' % PROJECT_ROOT

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6nd06inyg7d(&amp;hgi#@(!a2lhh8ufn%+ko4@$tp9^q(7w%+8z*4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'rchangelog.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'rchangelog.wsgi.application'

TEMPLATE_DIRS = (
    '%s/template' % PROJECT_ROOT,
)

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'changelog.context_processor.my_context_processor',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'changelog',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
