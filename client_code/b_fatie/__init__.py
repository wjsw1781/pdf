from ._anvil_designer import b_fatieTemplate
from anvil import *
import stripe.checkout
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
        app_tables.handle_article.add_row(        # 写库
            title=self.title_tb.text,             # 标题输入框 id 叫 title_tb
            content=self.content_rt.text,      # 正文富文本框 id 叫 content_rt
            user=anvil.users.get_user(),        # 当前登录用户
            create_time=dt.utcnow()
        )             
