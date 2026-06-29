from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..ArticleEdit import ArticleEdit


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("add_article_button", "click")
  def add_article_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form(ArticleEdit())
