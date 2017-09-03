from setuptools import setup

setup(name='myapp',
      version='0.1',
      description='',
      url='',
      author='Manfred Schroeder',
      author_email='manfred@verifaction.co.za',
      license='Private/Proprietary copywrite VerifAction 2017',
      packages=['myapp','myapp/models','myapp/config','myapp/util'],
      package_dir={'': 'src/'},
      package_data={'myapp': ['etc/*.cfg']},
      zip_safe=False)

