import os
import re
from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([a-zA-Z0-9.]+)['"]''')


def get_version():
    init = open(os.path.join(ROOT, '{{cookiecutter.directory_name}}', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='{{cookiecutter.directory_name}}',
    version=get_version(),
    description="{{cookiecutter.plugin_description}}",
    author="Red Hat Inc",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    entry_points={

            '{{cookiecutter.teflo_plugin_type}}_plugins': '{{cookiecutter.plugin_name}} = {{cookiecutter.directory_name}}:{{cookiecutter.plugin_class_name}}',

    }
)
