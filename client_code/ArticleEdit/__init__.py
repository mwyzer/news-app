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

  @handle("save_button", "click")
  def save_button_click(self, **event_args):
    title = self.title_box.text
    content = self.content_box.text
    category_id = self.category_box.selected_value

    if not title:
      Notification("Title is required").show()
      return

    if not category_id:
      Notification("Please select a category").show()
      return

    anvil.server.call(
      'add_article',
      title,
      content,
      category_id
    )

    Notification("Article saved").show()
    open_form('Homepage')

  @handle("cancel_button", "click")
  def cancel_button_click(self, **event_args):
    open_form('Homepage')