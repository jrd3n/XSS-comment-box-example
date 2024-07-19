# Basic webpage to show basic XSS

## Install

Fresh RPI RPI install

SSH in

```bash

mkdir XSS

cd XSS

wget https://github.com/jrd3n/XSS-comment-box-example/archive/refs/heads/main.zip

unzip main.zip

pip install flask --break-system-packages

(crontab -l 2>/dev/null; echo "@reboot /usr/bin/python3 /home/pi/XSS/XSS-comment-box-example-main/app.py") | crontab -


```
