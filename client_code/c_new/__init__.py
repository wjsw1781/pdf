from ._anvil_designer import c_newTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users


class c_new(c_newTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        item = properties['item']
        print(item)

        self.title.text = item['title']
        self.user.text = item['user'].email
        self.create_time.text = item['create_time']
        self.user.content = item['content']

        # Any code you write here will run before the form opens.
