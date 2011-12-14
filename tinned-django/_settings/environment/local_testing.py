import os
from _settings import ROOT_PATH


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testing.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

TEST_RUNNER = 'testing.AdvancedTestSuiteRunner'

SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True

COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False

#logging.basicConfig(level=logging.ERROR)
BROKER_URL = "redis://localhost:6379/14"

JENKINS_TASKS = ('django_jenkins.tasks.run_pylint',
                 'django_jenkins.tasks.run_pep8',
                 'django_jenkins.tasks.run_jslint',
                 'django_jenkins.tasks.with_coverage',
                 'django_jenkins.tasks.django_tests',)

PYLINT_RCFILE = os.path.join(ROOT_PATH, '_settings', 'applications', 'pylint.rc')
COVERAGE_RCFILE = os.path.join(ROOT_PATH, '_settings', 'applications', 'coverage.rc')
