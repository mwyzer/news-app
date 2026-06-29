from ._anvil_designer import ArticleEditTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ArticleEdit(ArticleEditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

    self.categories = [
      (cat['name'], cat) for cat in app_tables.categories.search()
    ]

    self.category_box.items = self.categories

  @handle("category_box", "change")
  def category_box_change(self, **event_args):
    """This method is called when an item is selected"""
    pass  # Write Code Here

    
