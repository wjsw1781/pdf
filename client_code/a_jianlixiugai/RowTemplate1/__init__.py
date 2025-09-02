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

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        try:
            media = anvil.server.call(
                'download_pdf',
                self.item['pdf_file_path'],     # 唯一存储名
                self.item['file_name']       # 给用户看的原名
            )
            anvil.media.download(media)      # 触发浏览器保存
        except Exception as e:
            alert(str(e))