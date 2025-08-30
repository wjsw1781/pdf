

anvil-app-server --app . --ip 0.0.0.0 --port 3030 
nohup anvil-app-server --app . --ip 0.0.0.0 --port 3030 >/dev/null 2>&1 &

ps aux | grep anvil-app-server 
ps aux | grep anvil-app-server | awk '{print $2}' | xargs kill -9


101.132.61.226:3030

curl 101.132.61.226:3030

