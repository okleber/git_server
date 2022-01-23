## How to build the image ?

docker build -t kleber/git_server .

## How to run the container ?

docker run -ti -p 8080:80 -p 2222:22 --name git_server kleber/git_server

## How to create repository named TEST123 using curl command line command ?

command: curl -X POST http://localhost:8080/createrepo/TEST123

result:  {"output":"Initialized empty Git repository in /TEST123.git/\n"}%   

## How to delete repository named TEST123 using curl command line command ?

command: curl -X POST http://localhost:8080/deleterepo/TEST123

result:  {"output":"Deleted TEST123"}%

## How to list all repository using curl command line command ?

command: curl http://localhost:8080/listrepo

result: {" ":["/TEST123.git"]}%

## How to clone a repository named "TEST123" to your local machine ?

command: git clone ssh://root@localhost:2222/TEST123.git

result: 

Cloning into 'TEST123'...
warning: You appear to have cloned an empty repository.

## Where to find the REST API documentation ?

Point your browser to http://localhost:8080/docs
