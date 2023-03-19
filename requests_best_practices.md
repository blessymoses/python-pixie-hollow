# Python requests

- If a Response instance is used in a conditional expression, it will evaluate to `True` if the status code was between 200 and 400, and `False` otherwise.
```python
response = requests.get('https://api.github.com')

if response:
    print('Success!')
else:
    print('An error has occurred.')
```

<b>Technical Detail</b>: This `Truth Value Test` is made possible because `__bool__()` is an overloaded method on Response.

This means that the default behavior of `Response` has been redefined to take the status code into account when determining the truth value of the object.


- Let’s say you don’t want to check the response’s status code in an `if` statement. Instead, you want to raise an exception if the request was unsuccessful. You can do this using `.raise_for_status()`:
```python
import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')

```

## performance of requests in production application environment
- timeout control
  - By default, requests will wait indefinitely on the response, so you should almost always specify a timeout duration to prevent these things from happening.
  - `timeout` can be an integer or float representing the number of seconds to wait on a response before timing out
  - You can also pass a tuple to timeout with the first element being a `connect timeout` (the time it allows for the client to establish a connection to the server), and the second being a `read timeout` (the time it will wait on a response once your client has established a connection)
  - Timeout exception:
  ```python
  import requests
  from requests.exceptions import Timeout
  
  try:
    response = requests.get('https://api.github.com', timeout=1)
  except Timeout:
    print('The request timed out')
  else:
    print('The request did not time out')
  ```
- sessions
  - Sessions are used to persist parameters across requests. For example, if you want to use the same authentication across multiple requests, you could use a session:
  ```python
  import requests
  from getpass import getpass
  # By using a context manager, you can ensure the resources used by the session will be released after use
  with requests.Session() as session:
    session.auth = ('username', getpass())

    # Instead of requests.get(), you'll use session.get()
    response = session.get('https://api.github.com/user')
  # You can inspect the response just like you did before
  print(response.headers)
  print(response.json())

  ```
- retry limits



https://realpython.com/python-requests/