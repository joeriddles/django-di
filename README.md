# Django DI

<p style="align: center">
    <a href="https://pypi.org/project/django-di" target="_blank">
        <img src="https://img.shields.io/pypi/v/django-di?label=PyPI" alt="Package version">
    </a>
</p

<h3>What is django-di and why you need it</h3>

django-di is a revolutionary tool designed to supercharge your Django app development. It harnesses the power of the dependency injection pattern, allowing you to manage complex dependencies and reduce tight coupling in your code with ease. No more spaghetti code or tangled dependencies - with django-di, you can focus on building clean, modular, and maintainable apps.

### Benefits of using dependency injection in Django

Dependency injection promotes loose coupling by externalizing dependencies. This means instead of hardcoding dependencies directly into your code, you define them externally, and django-di handles the rest. This decoupling improves overall code structure, organization, and facilitates easier maintenance, testing, and swapping out of components.

---

### Build

Note: these comands assume a valid [`~/.pypirc`](https://packaging.python.org/en/latest/specifications/pypirc/) file is configured.

See the [official packaging docs](https://packaging.python.org/en/latest/tutorials/packaging-projects/) for more info.

```shell
python3 -m pip install --upgrade build twine
python3 -m build
```

Upload to [test.pypi.org](https://test.pypi.org)

```shell
python3 -m twine upload --repository testpypi dist/*
```

Upload to [PyPI](https://pypi.org)

```shell
python3 -m twine upload dist/*
```

