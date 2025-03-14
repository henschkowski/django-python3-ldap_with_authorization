from setuptools import setup, find_packages

from django_python3_ldap import __version__


version_str = ".".join(str(n) for n in __version__)


with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="django-python3-ldap-with-atz",
    version=version_str,
    license="BSD",
    description="Django LDAP user authentication backend for Python 3., with extra Authorization",
    long_description=long_description,
    author="Dave Hall",
    author_email="dave@etianen.com",
    url="https://github.com/henschkowski/django-python3-ldap_with_authorization",
    packages=find_packages(),
    install_requires=[
        "django>=1.11",
        "ldap3>=2.5,<3",
        "pyasn1>=0.4.6,<0.6",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.12",
        "Framework :: Django",
    ],
)
