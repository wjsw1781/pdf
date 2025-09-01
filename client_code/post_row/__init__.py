from ._anvil_designer import post_rowTemplate
from anvil import *
from routing import router
import anvil.server
import stripe.checkout
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime as dt

class post_row(post_rowTemplate):

    def __init__(self, **props):
        self.init_components(**props)
        self.rp_child.item_template = post_row      # ← 关键行
        self._render()

    # 把一条评论渲染到组件
    def _render(self):
        row = self.item
        if not row:
            return
        self.lbl_user.text   = row['user']['email'] if row['user'] else '匿名'
        self.lbl_time.text   = row['create_at'].strftime('%Y-%m-%d %H:%M')
        self.lbl_content.text = row['content']

        # 如果你想“自动缩进 = 嵌套层级 × 20px”可用下面 4 行；
        # 若在设计器里已给 rp_child 设置 padding-left=20px，可把这段删掉。
        depth, n = 0, row
        while n['parent']:
            depth += 1
            n = n['parent']
        self.wrapper.role = f"indent-{depth}"        # role 写在 theme.css；或换成:
        # self.wrapper.spacing_above  # 也可以直接改 style: self.wrapper.style['margin-left']=f'{depth*20}px'

        # 把孩子放进 rp_child
        self.rp_child.items = app_tables.handle_post.search(parent=row)




    def reply_area_change(self, **event_args):
        """This method is called when the text in this text area is edited"""
        pass
        
    # 点击“回复”

    def lnk_reply_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.reply_box.visible = True
        self.reply_area.focus()
        
    # 发送子评论
    def btn_send_reply_click(self, **event_args):
        """This method is called when the button is clicked"""
        txt = self.reply_area.text.strip()
        if not txt:
            Notification('内容不能为空', style='danger').show(); return
        new = app_tables.handle_post.add_row(
            user      = anvil.users.get_user(),
            content   = txt,
            parent    = self.item,
            root      = self.item['root'] or self.item,
            article   = self.item['article'],
            create_at = dt.utcnow()
        )
        self.reply_area.text  = ''
        self.reply_box.visible = False
        # 追加到子列表即可即时显示
        self.rp_child.items = list(self.rp_child.items) + [new]

