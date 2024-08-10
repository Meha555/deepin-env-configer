#!/bin/bash

# 1. 联网


# 2. 激活系统


# 3. 改密码、改安全中心（pygui）


# 4. 改源、更新源


# 5. 装依赖
sudo apt install -y openssh-server git && \
sudo apt install -y g++ gcc gdb 

# 6. 启动服务
sudo systemctl enable ssh
sudo systemctl start ssh
