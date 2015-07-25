from setuptools import setup
try:
    import pypandoc
    description = pypandoc.convert('README.md','rst')
    
except:
    description=''
setup(name='PyLyrics',
      version="1.1.0",
      description='Pythonic Implementation of lyrics.wikia.com',
      long_description=description,
      author="Pradipta Bora",
      author_email='pradd@outlook.com',
      license='MIT',
      packages=['PyLyrics'],
      url="http://github.com/geekpradd/PyLyrics",
      install_requires=[
            'beautifulsoup4','requests',],
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Topic :: Internet",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
      ],
      zip_safe=False)
