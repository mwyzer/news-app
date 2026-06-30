from ._anvil_designer import HomepageTemplate
from anvil import *

from ..ArticleEdit import ArticleEdit


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)

  @handle("add_article_button", "click")
  def add_article_button_click(self, **event_args):
    open_form(ArticleEdit())