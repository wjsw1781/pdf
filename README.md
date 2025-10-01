

cd /root/socks_ss_gfw_ss_socks/pdf



pip install anvil-app-server
sudo apt install openjdk-17-jdk

pkill -f anvil-app-server 


pkill -f anvil-app-server

cd /root/socks_ss_gfw_ss_socks/pdf && anvil-app-server --app . --ip 0.0.0.0 --port 9191 --auto-migrate 

nohup anvil-app-server --app . --ip 0.0.0.0 --port 9191 --auto-migrate  2>&1 &


<!-- 远程服务器这 4 个指令必不可少 别太自信 这个是可以论证跑通的下次直接用看看效果 -->

iptables -t nat -D PREROUTING -p tcp --dport 59191 -j DNAT --to-destination 10.92.2.254:59191
iptables -t nat -D POSTROUTING -p tcp -d 10.92.2.254 -j MASQUERADE

iptables -t nat -A PREROUTING -p tcp --dport 59191 -j DNAT --to-destination 10.92.2.254:59191
iptables -t nat -A POSTROUTING -p tcp -d 10.92.2.254 -j MASQUERADE

iptables -t mangle -D FORWARD -o 10_+ -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
iptables -t mangle -D FORWARD -i 10_+ -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu


iptables -t mangle -A FORWARD -o 10_+ -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
iptables -t mangle -A FORWARD -i 10_+ -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu


192.168.171.71:9191


101.132.61.226:9191






