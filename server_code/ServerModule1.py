import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:

import os

import datetime
import base64
def md5(s):
    return base64.urlsafe_b64encode(str(s).encode()).decode().rstrip('=')




@anvil.server.callable
def download_pdf(store_name, orig_name):
    """
    store_name : 保存时生成的唯一文件名
    orig_name  : 想让用户下载时看到的原始文件名
    """
    user = anvil.users.get_user()
    if user is None:
        raise Exception("请先登录")
    file_path = f"./files/pdf/{md5(user['email'])}/{orig_name}"

    with open(file_path, "rb") as fp:
        data = fp.read()

    return anvil.BlobMedia(
        "application/pdf",
        data,
        name=orig_name            # 浏览器保存时显示的名字
    )


@anvil.server.callable
def save_pdf(fileobj):

    # 1. 你想把文件放到哪里
    user = anvil.users.get_user()
    if user is None:
        raise Exception("请先登录")
    file_path = f"./files/pdf/{md5(user['email'])}/{fileobj.name}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    unique_name = md5(file_path)
    public_url = f"/_/api/pdfs/{unique_name}"



    if os.path.exists(file_path):
        return public_url

    with open(file_path, 'wb') as fp:
        fp.write(fileobj._content)


    app_tables.handle_pdf.add_row(
        user          = user,
        pdf_file_path = public_url,   # 只是 text
        file_name = fileobj.name,   # 只是 text
        status        = "uploaded",
        create_time        = datetime.datetime.now()
    )

    return public_url


# 通用媒体播放系统
import anvil.server, anvil.media, os, mimetypes,datetime

ROOT = '/root/pdf/files/txt_img_video_audio_play'
@anvil.server.callable
def sync_dir_to_table_handle_media():
    for f in sorted(os.listdir(ROOT)):
        if os.path.isfile(os.path.join(ROOT, f)):
            if len(app_tables.handle_media.search(file_name=f)) ==0:
                app_tables.handle_media.add_row(**{
                    "file_name": f,
                    "mime": mimetypes.guess_type(f)[0] or "",
                    "create_time":datetime.datetime.now(),
                    'size':os.path.getsize(os.path.join(ROOT, f)),
                    "file_path": os.path.join(ROOT, f),
                })



from anvil import BlobMedia          # ← 关键

@anvil.server.callable
def fetch(item):
    file_path = item['file_path']
    # print(file_path)
    mime = mimetypes.guess_type(file_path)[0] or "application/octet-stream"
    with open(file_path, "rb") as fp:
        data = fp.read()
    blob = BlobMedia(mime,
                     data,
                     name=os.path.basename(file_path))  
    # print(anvil.media.get_url(blob)  )
    return blob