from setuptools import setup, find_packages
import os

version = '1.4'

setup(
        name='plonetheme.transition',
        description='Transition, is an installable Diazo theme for Plone 4',
        long_description=open('README.rst', 'rb').read()+'\n'+
                         open(os.path.join("docs", "INSTALL.txt")).read()+'\n'+
                         open(os.path.join("docs", "HISTORY.txt")).read(),
        version=version,
        author='Guido Stevens',
        author_email='guido.stevens@cosent.net',
        maintainer='Leonardo Caballero',
        maintainer_email='leonardocaballero@gmail.com',
        url='http://github.com/gyst/plonetheme.transition',
        license='GPL',
        packages=find_packages(),
        include_package_data=True,
        namespace_packages=[
            'plonetheme'
            ],
        install_requires=[
            'setuptools',
            'plone.app.theming',
            ],
        # Get more strings from
        # https://pypi.org/pypi?:action=list_classifiers
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Web Environment",
            "Framework :: Plone",
            "Framework :: Plone :: 4.1",
            "Framework :: Plone :: 4.2",
            "Framework :: Plone :: 4.3",
            "Framework :: Plone :: Theme",
            "Framework :: Zope2",
            "Framework :: Zope3",
            "Intended Audience :: Developers",
            "Intended Audience :: End Users/Desktop",
            "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Topic :: Internet",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
        keywords='web zope plone diazo theme plonetheme transition cms',
        entry_points={
            'z3c.autoinclude.plugin': 'target = plone',
            }
        )
