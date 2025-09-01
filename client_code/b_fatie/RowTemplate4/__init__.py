from ._anvil_designer import RowTemplate4Template
from anvil import *
from routing import router
import anvil.server
import stripe.checkout
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...c_new import c_new


class RowTemplate4(RowTemplate4Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        pop= c_new(item = self.item)
        alert(pop,large=True)
        pass
        
