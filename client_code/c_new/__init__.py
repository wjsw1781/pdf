from ._anvil_designer import c_newTemplate
from anvil import *
import anvil.server
import anvil.tables as tables, anvil.users
from anvil.tables import app_tables
from datetime import datetime as dt

class c_new(c_newTemplate):

    def __init__(self, **props):
        self.init_components(**props)
        self.article = props['item']                    # 文章 row

        # 文章信息
        self.title.text  = self.article['title']
        self.user.text   = self.article['user']['email']
        self.create_time.text = self.article['create_time']
        self.content.text = self.article['content']

        # 顶级评论列表
        self.rp_top.items = app_tables.handle_post.search(
            article=self.article, parent=None)

    # 发表一级评论
    def btn_top_click(self, **e):
        txt = self.ta_top.text.strip()
        if not txt: return
        row = app_tables.handle_post.add_row(
            user=anvil.users.get_user(), content=txt,
            parent=None,  article=self.article,
            create_at=dt.utcnow())
        row['root'] = row; row.update()                 # 自己作为根
        self.ta_top.text = ''
        self.rp_top.items = list(self.rp_top.items) + [row]
