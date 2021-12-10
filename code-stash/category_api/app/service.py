from models import CategoryModel


class CategoryService:
    def __init__(self) -> None:
        self.model = CategoryModel()

    def update(self, item_id, params):
        return self.model.update(item_id, params)

    def list(self):
        return self.model.select()

    def get_by_id(self, item_id):
        return self.model.select_by_id(item_id)
