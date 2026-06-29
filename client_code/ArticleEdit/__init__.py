from ._anvil_designer import ArticleEditTemplate
from anvil import *
import anvil.server


class ArticleEdit(ArticleEditTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)

    self.categories = anvil.server.call('get_categories')
    self.category_box.items = self.categories

  @handle("category_box", "change")
  def category_box_change(self, **event_args):
    selected_category_id = self.category_box.selected_value
    print("Selected category ID:", selected_category_id)