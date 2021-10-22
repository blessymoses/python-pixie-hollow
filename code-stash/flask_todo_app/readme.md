# Flask App

## Structuring the app
1. app.py
    - the entry & exit point to the application.
    - application layer
2. service.py
    - converts the request into a response.
    - business logic
3. models.py
    - handles everything that involves a Database.
    - data

## To consume the backend API
```python
requests.post("http://127.0.0.1:5000/todo", json = {"title": "First item", "description": "my first todo item"})

requests.put("http://127.0.0.1:5000/todo/1", json = {"title": "Firsttt item"})

requests.delete("http://127.0.0.1:5000/todo/1")
```