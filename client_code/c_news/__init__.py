from ._anvil_designer import c_newsTemplate
from anvil import *
from routing import router
import anvil.server
import stripe.checkout
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from routing.router import launch


launch()                      # 激活路由器


class c_news(c_newsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        all_articl = app_tables.handle_article.search()
        self.repeating_panel_1.items = all_articl