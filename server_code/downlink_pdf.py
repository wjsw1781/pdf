import anvil.server, anvil.users
from anvil.tables import app_tables
import os, uuid




import anvil.server

anvil.server.connect("server_ADNWFSLCNZZJXF3D6PENXVYA-LBFN3UH6VBCSDU2G")

def md5(string):
    import hashlib
    string=str(string)
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))
    return md5_hash.hexdigest()






# 2. 暴露一个 http_endpoint 用来回取文件
@anvil.server.http_endpoint('/pdfs/:fname')
def get_pdf(fname, **qs):
    """
    访问  https://your-domain/_/api/pdfs/<fname>  可下载文件
    """
    full_path = os.path.join(STORAGE_DIR, fname)
    if not os.path.isfile(full_path):
        return anvil.server.HttpResponse(404, "Not found")

    with open(full_path, 'rb') as fp:
        data = fp.read()

    # 告诉浏览器直接下载，并用原来的文件名显示
    return anvil.server.HttpResponse(
        200,
        data,
        headers={
            "Content-Type": "application/pdf",
            "Content-Disposition": f'attachment; filename="{fname}"'
        }
    )



# 3. 真正的保存接口，供前端调用
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
        status        = "uploaded"
    )

    return public_url
if __name__ == '__main__':
    anvil.server.run_forever()