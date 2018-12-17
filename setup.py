from setuptools import setup

setup(
    name='mdsite',
    version='0.1.0',
    packages=['mdsite'],
    install_requires=[
        'Click',
        'markdown',
        'jinja2',
        'python-markdown-math',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'mdsite = mdsite.__main__:cli'
        ]
    },
)
