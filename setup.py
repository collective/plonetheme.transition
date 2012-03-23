from setuptools import setup, find_packages
import os

version = '1.1'

setup(
        name='plonetheme.transition',
        description='An installable Diazo theme for Plone 4.1',
        long_description=open('README.rst', 'rb').read()+'\n'+
                         open(os.path.join("docs", "INSTALL.txt")).read()+'\n'+
                         open(os.path.join("docs", "HISTORY.txt")).read(),
        version='1.1',
        author='Guido Stevens',
        author_email='guido.stevens@cosent.net',
        url='http://github.com/gyst/plonetheme.transition',
        packages=find_packages(),
        include_package_data=True,
        namespace_packages=[
            'plonetheme'
            ],
        install_requires=[
            'setuptools',
            'plone.app.theming',
            ],
        classifiers=[
            "Framework :: Plone",
            "Programming Language :: Python",
            ],
        entry_points={
            'z3c.autoinclude.plugin': 'target = plone',
            }
        )


