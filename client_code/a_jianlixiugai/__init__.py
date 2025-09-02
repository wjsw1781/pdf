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
        self.refresh_grid()

    def file_loader_1_change(self, file, **event_args):
        try:
            if file is None or file.content_type != 'application/pdf':
                raise ValueError("请上传 pdf 文件")
    
            # 把字节流发给服务器保存
            url =  anvil.server.call('save_pdf', file)

    
            # 刷新列表
            self.refresh_grid()
    
            Notification(f"上传成功，可下载 URL:\n{url}",
                        timeout=5, style='success').show()
    
        except Exception as e:
            alert(str(e))
        finally:
            self.file_loader_1.clear()

    # 重新读取当前用户的 PDF 列表
    def refresh_grid(self):
        self.repeating_panel_1.items = app_tables.handle_pdf.search(
            user=anvil.users.get_user(),
        )
