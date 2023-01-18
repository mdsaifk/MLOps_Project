from setuptools import setup

with open("README.md","r",encoding = "utf-8") as f:
    long_description = f.read()


setup(name = "src",
     verwsion = "0.1",
     author = "mdsaifk",
     description = "wafer project with MLops",
     long_description = long_description,
     url = "https://github.com/mdsaifk/MLOps_Project",
     author_email= "mdsaifkhan200@gmail.com",
     package_name = ["src"],
     licence = "MIT License",
     pythoon_requires = ">=3.7",
     install_requires= ['dvc','pandas','scikit-learn','numpy'])