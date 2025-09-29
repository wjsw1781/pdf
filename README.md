

cd /root/socks_ss_gfw_ss_socks/pdf



pip install anvil-app-server
sudo apt install openjdk-17-jdk

anvil-app-server --app . --ip 0.0.0.0 --port 9191 --auto-migrate 


iptables -t nat -A PREROUTING -p tcp --dport 59191 -j DNAT --to-destination 10.92.4.254:9191
iptables -t nat -A POSTROUTING -p tcp -d 10.92.4.254 --dport 9191 -j MASQUERADE

iptables -t mangle -A FORWARD -o 10_+ -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
iptables -t mangle -A FORWARD -i 10_+ -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu



192.168.171.71:9191


101.132.61.226:9191






