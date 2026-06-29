import anvil.server
from anvil.tables import app_tables


@anvil.server.callable
def get_categories():
  categories = []

  for cat in app_tables.categories.search():
    categories.append((cat['name'], cat.get_id()))

  return categories