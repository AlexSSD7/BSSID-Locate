import setuptools
import sys
import os

with open("bssid-locate.py", "r") as f:
    text = f.read()

try:
    os.mkdir("build")
except:
    pass

with open("build/bssid-locate", "w") as f:
    f.write("#!" + sys.executable + "\n" + text)

setuptools.setup(
     name='bssid-locate',
     version='0.1',
     scripts=['build/bssid-locate'] ,
     author="Alexander Sadovskyi",
     author_email="",
     description="Get location by bssid",
     url="https://github.com/AlexSSD7/bssid-locate",
     packages=setuptools.find_packages(),
    install_requires=[
          "requests"
      ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )