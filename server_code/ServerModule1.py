import anvil.server
from anvil.tables import app_tables
from datetime import datetime


@anvil.server.callable
def get_categories():
  return [
    (cat['name'], cat.get_id())
    for cat in app_tables.categories.search()
  ]


@anvil.server.callable
def add_article(title, content, category_id):
  if not title:
    raise Exception("Title is required")

  if not content:
    raise Exception("Content is required")

  if not category_id:
    raise Exception("Category is required")

  category = app_tables.categories.get_by_id(category_id)

  if category is None:
    raise Exception("Category not found")

  app_tables.articles.add_row(
    title=title,
    content=content,
    categories=[category],
    created=datetime.now(),
    updated=datetime.now()
  )

  return True