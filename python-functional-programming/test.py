def my_func(a: "annotation for a", b: "annotation for b" = 1) -> "returns ab":
    "returns a*b"
    return a * b


# python3 -c "from test import my_func; my_func.__doc__"
# python3 -c "from test import my_func; print(my_func.__annotations__)"
