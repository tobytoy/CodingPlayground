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


