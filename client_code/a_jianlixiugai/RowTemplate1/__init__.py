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
        url = self.item['pdf_file_path']     # 形如 "/_/api/pdfs/<hash>"
        if url:
            # 在新标签页打开，浏览器会直接开始下载
            anvil.js.window.open(url, "_blank")
        else:
            alert("找不到下载地址")