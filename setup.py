from setuptools import setup, find_packages


with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup( name='hr',
        version ='0.1.0',
        description = 'Commandline user management utility for human resources',
        long_description = readme,
        author = 'Daniel',
        author_email = 'daniel.mendozapupo@gmail.com',
        packages = find_packages('src'),
        package_dir={'':'src'},
        install_requires=[],
        entry_points={
            'console_scrips': 'hr=hr.cli:main',
            },
        )
