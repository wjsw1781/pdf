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


    def down_item_click(self, **event_args):
        try:
            media_object = anvil.server.call('get_binary_file',dict(self.item))
            Notification(f"开始下载文件: {media_object.name}").show()
            anvil.media.download(media_object)
        except Exception as e:
            alert(str(e))

    def del_item_click(self, **event_args):
        self.item.delete()
        self.parent.parent.parent.parent.parent.repeating_panel_1.items = app_tables.binary_file_up_down.search()
