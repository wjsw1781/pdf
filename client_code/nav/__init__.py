from ._anvil_designer import navTemplate
from anvil import *
from routing import router
import anvil.server
import stripe.checkout
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users


class nav(navTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def link_1_click(self, **event_args):
       open_form('a_jianlixiugai')

    def link_2_copy_click(self, **event_args):
        open_form('d_wode')

    def link_2_copy_2_click(self, **event_args):
        open_form('c_news')

    def link_2_click(self, **event_args):
        open_form('b_fatie')
