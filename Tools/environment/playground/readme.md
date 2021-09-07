# build image:
    docker build -t toby-playground:v1 .

# run container:
    docker-compose up -d

# connect ssh:
    ssh -p 8822 toby@127.0.0.1

# run code:
    python3 hello.py
    js hello.js
    kotlinc hello.kt -include-runtime -d hello.jar
    java -jar hello.jar

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

# Jupyter:
    jupyter lab --ip=*.*.*.* --no-browser --allow-root --NotebookApp.token='jupyter' --port=8888


