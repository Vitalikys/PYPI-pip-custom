- Create a setup.py file in the directory
- Create a directory named mypackage (same as the name in setup.py)
and put your module inside it.
-Create a README.md file to describe your package.
- Create a .pypirc file in your home directory with the following content:
```shell
[distutils]
index-servers =
    pypi

[pypi]
repository: https://upload.pypi.org/legacy/
username: username
password: password

```
- Install twine package to upload the package to PyPI:
```shell
pip install twine
```
- Build the package: 
```shell
python setup.py sdist bdist_wheel
```
This will create a dist directory containing the source distribution (*.tar.gz) and a binary distribution (*.whl).
- Upload the package to PyPI:
```shell
twine upload dist/*
twine upload --repository testpypi dist/*
```




