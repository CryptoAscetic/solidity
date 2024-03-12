```shell
Please make sure sudo permission can be used
1. download & unzip
curl -o apphub-linux-amd64.tar.gz https://assets.coreservice.io/public/package/60/app-market-gaga-pro/1.0.4/app-market-gaga-pro-1_0_4.tar.gz && tar -zxf apphub-linux-amd64.tar.gz && rm -f apphub-linux-amd64.tar.gz && cd ./apphub-linux-amd64
2. remove exist service and install new service
sudo ./apphub service remove && sudo ./apphub service install
3. start service
sudo ./apphub service start
4. check app status
./apphub status
check gaganode status is 'RUNNING'
5. set token
sudo ./apps/gaganode/gaganode config set --token=自己的token
6. restart app
./apphub restart
for more tutorials check  
https://docs.gaganode.com
```
