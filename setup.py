from setuptools import setup, find_packages

with open('README.srt', encoding='UTF-8') as f:
    readme = f.read()
setup( name='hr',
        version ='0.1.0',
        description = 'Database for human resources',
        long_description = readme,
        author = 'Daniel',
        author_email = 'daniel.mendozapupo@gmail.com',
        install_requires=[],
        packages = find_packages('src'),
        package_dir={'':'src'}
