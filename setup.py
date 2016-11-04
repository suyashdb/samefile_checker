from setuptools import setup, find_packages
import sys, os, glob, filecmp

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    filecmp
    glob
    os

    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


setup(name='helloworld',
    version=version,
    description="'packagec creator test'",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='test',
    author='suyashdb',
    author_email='suyashdb@gmail.com',
    url='',
    license='PDDL',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['samefile_checker=samefile_checker:main']
    }
)
