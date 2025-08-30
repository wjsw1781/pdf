from ._anvil_designer import a_jianlixiugaiTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from anvil import *
import anvil
import base64
import re

class a_jianlixiugai(a_jianlixiugaiTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
    def file_loader_1_change(self, file, **event_args):
        try:
            if file is None or file.content_type != 'application/pdf':
                raise ValueError("请上传 pdf 文件")

            data     = file.get_bytes()
            size_kb  = len(data) / 1024
            first_ln = data.split(b'\n', 1)[0].decode('latin1', errors='ignore')

            # 把元信息等展示在 outlined_card_1 中
            self.outlined_card_1.clear()
            self.outlined_card_1.add_component(Label(text=f"文件名：{file.name}"))
            self.outlined_card_1.add_component(Label(text=f"文件大小：{size_kb:.1f} KB"))
            self.outlined_card_1.add_component(Label(text=f"PDF 版本号：{first_ln}"))


            result_msg = anvil.server.call('save_pdf', file.name, data)

        except Exception as e:
            alert(str(e))
        self.file_loader_1.clear()
