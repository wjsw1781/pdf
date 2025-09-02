from ._anvil_designer import RowTemplate7Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate7(RowTemplate7Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    
    def button_1_click(self, **event_args):
        # 1. 取到 Media 对象


        media = anvil.server.call('fetch', self.item)
        mime  = (media.content_type or '').lower()

        # ② 得 URL
        url = media.get_url(False) or anvil.media.TempUrl(media).url

        # ③ 拿容器的 DOM 节点并清空
        card_dom = anvil.js.get_dom_node(get_open_form().media_card)
        while card_dom.firstChild:
            card_dom.removeChild(card_dom.firstChild)

        # ④ 按类型创建标签
        if mime.startswith('image'):
            el = anvil.js.window.document.createElement("img")
            el.src = url
            el.style.width = "100%"

        elif mime.startswith('audio'):
            el = anvil.js.window.document.createElement("audio")
            el.src = url
            el.controls = True
            el.style.width = "100%"

        elif mime.startswith('video'):
            el = anvil.js.window.document.createElement("video")
            el.src = url
            el.controls = True
            el.style.width = "100%"
            el.style.height = "auto"

        elif mime.startswith('text'):
            txt = media.get_bytes().decode('utf-8', errors='ignore')
            el  = anvil.js.window.document.createElement("pre")
            el.style.whiteSpace = "pre-wrap"
            el.innerText = txt

        else:
            el = anvil.js.window.document.createElement("a")
            el.href = url
            el.download = ""          # 让浏览器下载
            el.innerText = "下载文件"

        # ⑤ 挂到容器
        card_dom.appendChild(el)

