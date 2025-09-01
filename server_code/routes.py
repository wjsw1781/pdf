import anvil.stripe
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# routes.py
from routing.router import Route

class Home(Route):
    path = "/c_new"        # 访问根路径时
    form = "c_new"     # 打开名字叫 "Home" 的 Form

class About(Route):
    path = "/c_news"
    form = "c_news"

# 如果想加参数：
# class Article(Route):
#     path = "/article/:id"      # id 会作为参数传递
#     form = "Article"
