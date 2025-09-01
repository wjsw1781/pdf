
git config user.name 'wjsw1781'
git config user.password '1781wjsw'
git config user.email '1781591279@qq.com'
git config  credential.helper store



sudo apt install certbot
sudo certbot certonly --standalone -d l4proxy.top -m 1781591279@qq.com --agree-tos --non-interactive
/etc/letsencrypt/live/l4proxy.top/privkey.pem

sudo certbot renew --dry-run


数据库删除
rm -rf /root/pdf/.anvil-data 

anvil-app-server --ip 0.0.0.0 --port 8443

anvil-app-server --origin https://l4proxy.top --manual-cert-file /etc/letsencrypt/live/l4proxy.top/fullchain.pem --manual-cert-key-file /etc/letsencrypt/live/l4proxy.top/privkey.pem --port 443

nohup anvil-app-server --origin https://l4proxy.top --manual-cert-file /etc/letsencrypt/live/l4proxy.top/fullchain.pem --manual-cert-key-file /etc/letsencrypt/live/l4proxy.top/privkey.pem --port 443
 >/dev/null 2>&1 &

ps aux | grep anvil-app-server 
ps aux | grep anvil-app-server | awk '{print $2}' | xargs kill -9


101.132.61.226

curl  http://l4proxy.top 


curl  https://l4proxy.top 
