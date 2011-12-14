# -*- coding: utf-8 -*-
import os
import re

from django.conf import LazySettings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.loading import get_app
from django.test.simple import DjangoTestSuiteRunner, build_test, build_suite
from django.utils import unittest

from django.utils.importlib import import_module
from django.test._doctest import DocTestSuite
from django.test.testcases import DocTestRunner
from django.test.simple import doctestOutputChecker

settings = LazySettings()


class AdvancedTestSuiteRunner(DjangoTestSuiteRunner):
    """A test suite runner."""

    def __init__(self, *args, **kwargs):
        super(AdvancedTestSuiteRunner, self).__init__(*args, **kwargs)

    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        suite = unittest.TestSuite()

        if not test_labels and hasattr(settings, 'PROJECT_APPS'):
            test_labels = [app_name.split('.')[-1] for app_name in settings.PROJECT_APPS]

        if test_labels:
            for label in test_labels:
                if '.' in label:
                    suite.addTest(build_test(label))
                else:
                    try:
                        app = get_app(label)
                        suite.addTest(build_suite(app))
                    except ImproperlyConfigured:
                        pass
        else:
            suite = super(AdvancedTestSuiteRunner, self).build_suite(test_labels, extra_tests, **kwargs)
        return suite