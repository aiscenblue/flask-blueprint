from distutils.core import setup
from flask_blueprint import __version__

setup(
    name='flask-blueprint',
    version=__version__,
    description='Flask blueprint generator',
    author='Jeffrey Marvin Forones',
    author_email='aiscenblue@gmail.com',
    url='https://github.com/aiscenblue/flask-blueprint',
    license='MIT',
    packages=['flask_blueprint'],
    keywords=['flask', 'blueprint', 'flask-blueprint', 'flask_blueprint'],  # arbitrary keywords
    install_requires=[
        # list of this package dependencies
    ],
    entry_points=None,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Flask'
    ]
)
