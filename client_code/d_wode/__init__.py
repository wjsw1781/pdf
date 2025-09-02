from ._anvil_designer import d_wodeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users


class d_wode(d_wodeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

        while anvil.users.get_user() is None:
            anvil.users.login_with_form(allow_cancel=True)
        