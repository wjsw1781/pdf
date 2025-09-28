from ._anvil_designer import a_jianlixiugaiTemplate
from anvil import *
import anvil.server
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
        self.repeating_panel_1.items = app_tables.binary_file_up_down.search(user=anvil.users.get_user())

    def file_loader_1_change(self, file, **event_args):
        """This method is called when a new file is loaded into this FileLoader"""
        if file:
            try:
                # 调用服务器函数上传文件
                anvil.server.call('upload_binary_file', file)
                self.repeating_panel_1.items = app_tables.binary_file_up_down.search()
                Notification(f"文件 '{file.name}' 上传成功！").show()

            except Exception as e:
                Notification(f"文件上传失败: {e}", title="错误", style="danger").show()
        else:
            Notification("未选择文件进行上传。", style="warning").show()




 