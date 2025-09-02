
git config user.name 'wjsw1781'
git config user.password '1781wjsw'
git config user.email '1781591279@qq.com'
git config  credential.helper store



sudo apt install certbot
sudo certbot certonly --standalone -d l4proxy.top -m 1781591279@qq.com --agree-tos --non-interactive

Certificate is saved at: /etc/letsencrypt/live/l4proxy.top/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/l4proxy.top/privkey.pem

sudo certbot renew --dry-run


数据库删除
rm -rf /root/pdf/.anvil-data 

使用 nginx 转发 同时过滤掉这些被扫描的垃圾流量

<!-- 首先安装 openresty nginx -->
sudo apt-get -y install --no-install-recommends wget gnupg ca-certificates
wget -O - https://openresty.org/package/pubkey.gpg | sudo apt-key add -
echo "deb http://openresty.org/package/ubuntu $(lsb_release -sc) main" > openresty.list
sudo cp openresty.list /etc/apt/sources.list.d/
sudo apt-get update
sudo apt-get -y install --no-install-recommends openresty
which openresty

<!-- 添加配置 -->
/root/pdf/nginx_conf.conf

/usr/local/openresty/nginx/sbin/nginx  -t  -c /root/pdf/nginx_conf.conf

<!-- 直接运行 -->
/usr/local/openresty/nginx/sbin/nginx -c /root/pdf/nginx_conf.conf
/usr/local/openresty/nginx/sbin/nginx -c /root/pdf/nginx_conf.conf -s stop
/usr/local/openresty/nginx/sbin/nginx -c /root/pdf/nginx_conf.conf -s reload

anvil-app-server --ip 0.0.0.0 --port 8443

anvil-app-server --origin https://l4proxy.top --manual-cert-file /etc/letsencrypt/live/l4proxy.top/fullchain.pem --manual-cert-key-file /etc/letsencrypt/live/l4proxy.top/privkey.pem --port 443

nohup anvil-app-server --origin https://l4proxy.top --manual-cert-file /etc/letsencrypt/live/l4proxy.top/fullchain.pem --manual-cert-key-file /etc/letsencrypt/live/l4proxy.top/privkey.pem --port 443 >/dev/null 2>&1 &

ps aux | grep anvil-app-server 
ps aux | grep anvil-app-server | awk '{print $2}' | xargs kill -9  



curl  http://l4proxy.top 


curl  https://l4proxy.top 



提交paddle