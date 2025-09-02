import anvil.server, anvil.users
from anvil.tables import app_tables
import os, uuid




import anvil.server

anvil.server.connect("server_BMGI7W2DOLRQZMATAMIU45GO-LBFN3UH6VBCSDU2G")


# 1. 你想把文件放到哪里
STORAGE_DIR = '/opt/anvil/pdfs'      # 确保目录存在并且进程有写权限
os.makedirs(STORAGE_DIR, exist_ok=True)

# 2. 暴露一个 http_endpoint 用来回取文件
@anvil.server.http_endpoint('/pdfs/:fname')
def get_pdf(fname, **qs):
    """
    访问  https://your-domain/_/api/pdfs/<fname>  可以下载 PDF
    """
    full_path = os.path.join(STORAGE_DIR, fname)
    if not os.path.isfile(full_path):
        return anvil.server.HttpResponse(404, "Not found")
    with open(full_path, 'rb') as fp:
        data = fp.read()
    return anvil.server.HttpResponse(
        200,
        data,
        headers={"Content-Type": "application/pdf"}
    )


# 3. 真正的保存接口，供前端调用
@anvil.server.callable
def save_pdf(filename, file_bytes):
    user = anvil.users.get_user()
    if user is None:
        raise Exception("请先登录")

    # 生成防重名文件名
    unique_name = f"{uuid.uuid4().hex}_{filename}"
    full_path   = os.path.join(STORAGE_DIR, unique_name)

    with open(full_path, 'wb') as fp:
        fp.write(file_bytes)

    # 生成可公开访问的 URL（如不需要外网访问，可仅存文件系统路径）
    public_url = f"/_/api/pdfs/{unique_name}"

    # 记到表里
    app_tables.handle_pdf.add_row(
        user          = user,
        pdf_file_path = public_url,   # 只是 text
        status        = "uploaded"
    )

    return public_url
if __name__ == '__main__':
    anvil.server.run_forever()