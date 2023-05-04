
import setuptools 

setuptools.setup(name='silverwinner',
      version='0.0.2', 
      author = 'Rhian McClelland',
      python_requires='>=3.11.0',
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src")
      ) 