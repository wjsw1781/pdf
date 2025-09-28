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
def upload_binary_file(file):
    user = anvil.users.get_user()

    if user is None:
        raise Exception("请先登录")
        
    import os
    file_name = file.name
    file_content = file._content

    server_path = f'./upload_binary_file/{file_name}'
    os.makedirs(os.path.dirname(server_path), exist_ok=True)
    with open(server_path,'wb') as f:
        f.write(file_content)

    # 保存数据库
    data_row = app_tables.binary_file_up_down.search(server_path=server_path)
    if len(data_row) == 0:
        app_tables.binary_file_up_down.add_row(
            server_path=server_path,
            file_name=file_name,
            status = '上传完成',
            tags = "",
            user = user,
        )
    else:
        row = app_tables.binary_file_up_down.get(server_path=server_path)
        row['file_name'] = file_name
        row['tags'] = ""
    pass


@anvil.server.callable
def get_binary_file(item):
    server_path = item['server_path']
    import anvil.media
    media_object = anvil.media.from_file(server_path, "text/plain")
    return media_object



# 修改wg_server_public_ip 为 adsl 最新 ip
@anvil.server.http_endpoint("/wg_server_public_ip_update", methods=["POST","GET"], authenticate_users=False)
def wg_server_public_ip_update(**kw):
    data = kw
    if not data or "wg_server_ip" not in data or "wg_server_public_ip" not in data:
        return (400, "need both     ---- wg_server_ip   wg_server_public_ip")

    row = app_tables.wg_conf.get(wg_server_ip=data["wg_server_ip"])
    if row is None:
        return (404, "wg_server_ip not exit")

    row["wg_server_public_ip"] = data["wg_server_public_ip"]
    return dict(row)





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