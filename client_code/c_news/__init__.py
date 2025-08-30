from ._anvil_designer import c_newsTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class c_news(c_newsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.repeating_panel_1.items = app_tables.handle_article.search()

        # Any code you write here will run before the form opens.
