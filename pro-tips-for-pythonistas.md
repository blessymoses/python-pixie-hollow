# Pro-tips for Pythonistas

## Key concepts from the zen of Python
- Type Hinting
- PEP-8 style Guideline
- 
### Type Hinting
- indicates the type of a value, PEP 484 standard
- Type hinting only hints about the type and does not enforce.
- Python is a dynamically typed language. To enforce type checking, type hinting can be combined with mypy(static type checker)
- Pros:
  - improves code readability
  - helps to catch certain errors
  - helps to document the code
  - helps to build and maintain a cleaner architecture
  - adds lot of value in libraries published to PyPI
- Cons:
  - takes time and effort to add
  - introduces a slight penalty in starting time
  - adds little value in short throwaway scripts
#### uncommon hinting styles
  - Use Union when something could be one of a few types
    ```python
    x: List[Union[int, str]] = [3, 5, "test", "fun"]
    ```
  - Use Any if you don't know the type of something or it's too dynamic to write a type for
    ```python
    x: Any = mystery_function()
    ```
  - positional args and keywords args can also be hinted
    ```python
    def call(self, *args: str, **kwargs: str) -> str:
        request = make_request(*args, **kwargs)
        return self.do_api_query(request)
    ```


## Design Considerations
- Pin down the dependencies
  - Pros:
    - Ensures that the released library works as expected
    - Prevents breaking changes and guarantees safe, repeatable builds
    - Still, allows the user to upgrade dependencies on their own risk
    - Reproducibility
  - Cons:
    - Dependency conflicts & Diamond dependency problems
- Not pinning the dependencies
  - Pros:
    - Fewer constraints on the library
    - Easier to incorporate to existing project/stack
    - Reusability

## Basics
- Virtual environments
- 