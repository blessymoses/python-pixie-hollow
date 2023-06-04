# Callable Instances using __call__() method

- A `callable` is any object that you can call using a pair of parentheses and, optionally, a series of arguments.
- Examples: Functions, classes, and methods
- To create custom classes that produce `callable instances`, add the `.__call__()` special method to your class.
> Even though you can call special methods like `.__call__()` directly, doing so isn’t a recommended or best practice. Instead, call the functions as usual.
- To check whether a Python object is callable, you can use the built-in `callable()` function.
```python
>>> callable(abs)
True
```
https://realpython.com/python-callable-instances/#exploring-advanced-use-cases-of-__call__