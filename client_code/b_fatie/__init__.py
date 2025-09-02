from ._anvil_designer import b_fatieTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from datetime import datetime as dt          # 放文件最上面一次就行


class b_fatie(b_fatieTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.repeating_panel_1.items = list(app_tables.handle_article.search(user=anvil.users.get_user()))

        # Any code you write here will run before the form opens.
        
    def submit_article_click(self, **e):
        # 1. 写库
        app_tables.handle_article.add_row(
            title=self.title_tb.text,
            content=self.content_rt.text,
            user=anvil.users.get_user(),
            create_time=dt.utcnow()
        )
    
        # 2. 清空输入框（可选）
        self.title_tb.text   = ""
        self.content_rt.text = ""
    
        # 3. 重新查询并绑定，Repeating-Panel 会立即刷新但页面不重载
        self.repeating_panel_1.items = list(
            app_tables.handle_article.search(
                user=anvil.users.get_user(),
            )
        )
    
