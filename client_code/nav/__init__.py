from ._anvil_designer import navTemplate
from anvil import *
import anvil
import base64

class nav(navTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    
    # 选完文件以后会自动触发此事件
    def file_loader_1_change(self, file, **event_args):
        if file is None:                 # 用户点取消
            return
    
        # 简单做个类型校验（可选）
        if file.content_type != 'application/pdf':
            alert("请上传 pdf 文件")        # 也可以做更完善的判断
            return

        # 1. 把 Media 对象转成 data URL（base64）
        b64 = base64.b64encode(file.get_bytes()).decode("ascii")
        data_url = f"data:application/pdf;base64,{b64}"
    
        self.iframe_1.url = data_url