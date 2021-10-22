from models import ToDoModel


class ToDoService:
    def __init__(self) -> None:
        self.model = ToDoModel()

    def create(self, params):
        return self.model.create(params["title"], params["description"])

    def update(self, item_id, params):
        return self.model.update(item_id, params)

    def delete(self, item_id):
        return self.model.delete(item_id)

    def list(self):
        return self.model.select()

    def get_by_id(self, item_id):
        return self.model.select_by_id(item_id)
