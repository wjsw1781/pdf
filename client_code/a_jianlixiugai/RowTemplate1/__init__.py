from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate1(RowTemplate1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        


    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.item.delete()
        self.parent.parent.parent.parent.parent.repeating_panel_1.items = app_tables.binary_file_up_down.search()

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        try:
            media_object = anvil.server.call('get_binary_file',dict(self.item))
            Notification(f"开始下载文件: {media_object.name}").show()
            anvil.media.download(media_object)
        except Exception as e:
            alert(str(e))
