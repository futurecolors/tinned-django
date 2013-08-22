# coding: utf-8
import os
import sh
import logging
import shutil
import tempfile

from unittest import TestCase
from nose.tools import nottest


class UncanningTest(TestCase):
    """ Let's try to uncan a new project and run tests to see everything is ok

        Estimated running time 260s"""
    def setUp(self):
        """ Prepare for tests """
        self.tmp_dir_src = tempfile.mkdtemp(prefix='tinned_django')
        self.tmp_dir_env = tempfile.mkdtemp(prefix='tinned_django.env')

    def tearDown(self):
        """ Clean up dirs after myself """
        shutil.rmtree(self.tmp_dir_src)
        shutil.rmtree(self.tmp_dir_env)

    @nottest
    def uncan_it(self):
        template_path = os.path.abspath('./tinned_django')
        managepy = sh.Command('django-admin.py')
        managepy('startproject', 'test_project', self.tmp_dir_src,
                 '--extension', '.py,.gitignore', '--template', template_path)

    @nottest
    def create_virtualenv(self):
        sh.virtualenv(self.tmp_dir_env, python='python2.7')
        pip = sh.Command(os.path.join(self.tmp_dir_env, 'bin/pip'))
        reqs_file = os.path.join(self.tmp_dir_src, 'requirements.txt')

        print('Installing virtualenv...')
        for line in pip.install(requirement=reqs_file, _iter=True):
            print(line)

    @nottest
    def launch_project_tests(self):
        sh.cd(self.tmp_dir_src)
        python = sh.Command(os.path.join(self.tmp_dir_env, 'bin/python'))
        print(python(os.path.join(self.tmp_dir_src, 'runtests.py'), verbosity=2))

    def test_sanity(self):
        """ Let's try to uncan our project """
        logging.basicConfig()

        self.uncan_it()
        test_templating_path = os.path.join(self.tmp_dir_src, 'manage.py')
        test_gitignore_path = os.path.join(self.tmp_dir_src, '.gitignore')
        self.assert_('test_project.settings' in open(test_templating_path).read())
        self.assert_('/test_project/local_settings.py' in open(test_gitignore_path).read())
        self.create_virtualenv()
        try:
            self.launch_project_tests()
        except sh.ErrorReturnCode as e:
            print(e.stderr)
            exit(1)
        self.assert_('No error code raised')
