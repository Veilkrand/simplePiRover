cp startTcpVideoServer.sh /usr/local/bin/startTcpVideoServer.sh
cp videoServer.service /etc/systemd/system/videoServer.service
systemctl enable videoServer.service
systemctl start videoServer.service
systemctl status videoServer.service