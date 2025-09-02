from ._anvil_designer import MediaPlayerFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class MediaPlayerForm(MediaPlayerFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.repeating_panel_1.items = app_tables.handle_media.search()

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        anvil.server.call('sync_dir_to_table_handle_media')
