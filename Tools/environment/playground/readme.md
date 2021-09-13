# Docker part:
## build image:
    docker build -t toby-playground:v1 .

## run container:
    docker-compose up -d
    docker-compose build
    docker-compose restart playground
    (docker-compose down)
    docker network create toby-network

## common check
    docker-compose logs

## kill
    docker image prune
    docker rmi $(docker images -f “dangling=true” -q)
    docker container prune

# rabbitMQ
    port: 5672, 15672

# redis
    port: 6379

# connect ssh:
    ssh -p 8822 toby@127.0.0.1

# run code:
    python3 hello.py
    js hello.js
    kotlinc hello.kt -include-runtime -d hello.jar
    java -jar hello.jar
    g++ hello.cpp
    ./a.out

# add path
    PATH=$PATH:/sbin

# vscode issue:
    .ssh -> known_hosts ( may kill reapeat part)

# init:
    sudo chown -R toby:toby document/

# git:
## init:
    git config --global user.name "toby"
    git config --global user.email tobywang2021@gmail.com
    git clone https://github.com/tobytoy/CodingPlayground.git

## easy work loop:
    git pull 
    git add .
    git commit 
    git push

## common check:
    git config --list
    git status
    git log

# Jupyter:
    jupyter lab --ip=*.*.*.* --no-browser --allow-root --NotebookApp.token='jupyter' --port=8888


