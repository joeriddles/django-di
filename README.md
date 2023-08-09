# Django DI

Django dependency injection inspired by ASP.NET 

### Build

Note: these comands assume a valid [`~/.pypirc`](https://packaging.python.org/en/latest/specifications/pypirc/) file is configured.

See the [official packaging docs](https://packaging.python.org/en/latest/tutorials/packaging-projects/) for more info.

```shell
python3 -m pip install --upgrade build twine
python3 -m build
```

Upload to [test.pypi.org](https://test.pypi.org).

```shell
python3 -m twine upload --repository testpypi dist/*
```

Upload to [PyPI](https://pypi.org)

```shell
python3 -m twine upload dist/*
```

