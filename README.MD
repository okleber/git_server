## How to build the image ?

docker build -t kleber/git_server:0.1 .

## How to run the container ?

docker run -ti -p 8080:80 -p 2222:22 kleber/git_server:0.1

## How to read/test/USE the REST API ?

Point your browser to http://localhost:8080/docs

## How to clone a repository named "test123" to your local machine ?

git clone ssh://root@localhost:2222/test123.git

Note: default password is root



