from setuptools import setup, find_packages

setup(
    name='drf-renderer-xlsx',
    version="1.0.0",
    description='Stub to alias the `drf-excel` package.',
    author='Tim Allen',
    author_email='tallen@wharton.upenn.edu',
    url='https://github.com/wharton/drf-excel',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'drf-excel',
    ],
)
