# First, we try to use setuptools. If it's not available locally,
# we fall back on ez_setup.
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

long_description = ''

install_requires = []
with open('requirements.txt') as requirements_file:
    for line in requirements_file:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == '#':
            continue
        pinned_version = line.split()[0]
        install_requires.append(pinned_version)

setup(
    name='translator-modules',
    description='NCATS Translator Reasoner modules',
    packages=['translator_modules'],
    url='https://github.com/ncats/translator-modules',
    download_url='https://github.com/ncats/translator-modules',
    long_description=long_description,
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'mock'],
    license='Apache 2.0',
    zip_safe=False,
    author='James Eddy',
    author_email='james.a.eddy@gmail.com',
    version='0.2.0'
)