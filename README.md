# python_mongo_docker
#git status
#git add .
git commit -m "add arquivos do projeto"
git push -u origin main

##Iniciar projeto
git init
##Adicionar Repositórios Remotos
$ git remote add origin https://meu-endereco.com/meu-projeto.git

##Executar aplicacao pelo docker
docker build -t my-python-app .
$ docker run -it --rm --name my-running-app my-python-app
##Links de referencia
https://kb.objectrocket.com/mongo-db/use-docker-and-python-for-a-mongodb-application-1046

