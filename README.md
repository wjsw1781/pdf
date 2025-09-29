

cd /root/socks_ss_gfw_ss_socks/pdf



pip install anvil-app-server
sudo apt install openjdk-17-jdk


pkill -f anvil-app-server

cd /root/socks_ss_gfw_ss_socks/pdf && anvil-app-server --app . --ip 0.0.0.0 --port 9191 --auto-migrate 

192.168.171.71:9191


101.132.61.226:9191




