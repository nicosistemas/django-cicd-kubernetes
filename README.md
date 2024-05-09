# Challenge DevOps
## django-cicd-kubernetes
django project pipeline cicd github actions to deploy on kubernetes cluster

## CICD TEST
La aplicación de prueba escrita en Python/django es dockerizada, pusheada al registry de Docker y deployada en un cluster de Kubernetes. 
Con solo realizar un push a Master se ejecutan los jobs del pipeline.

Github Actions Pipeline: https://github.com/nicosistemas/django-cicd-kubernetes/blob/a3058398737aade80650d505b133327954e9a09b/.github/workflows/django.yml

App: es una simple aplicacion tipo "hola mundo" en Django que se consume en /hola por el puesto 8000
https://github.com/nicosistemas/django-cicd-kubernetes/tree/master/docker_django/hola_docker

Mi Docker Hub: https://hub.docker.com/repository/docker/nicosistemas/probando-django/general

Por el momento no es accedible a una url https poqrue no tengo Ingress ni dominio propio, lo que hago es emularlo con ngrok para ser consumida,
ej:https://c116-2803-9800-98c4-8511-3c4-7187-7855-f2ea.ngrok.io/hola/   (local command ./ngrok http 8000)


To Do on cluster la primera vez (el pipeline no crea los pods, si los "updatea/deploya"):

kubectl apply -f deployment.yaml -n test-nico


## Contiene pruebas para Github Fundations (UPDATE)
* Templates de PR
* Templates de Issues
* Labels
* Diferentes Markdowns
* Tags y Releases
* prioridad de Readme.md
  - .github
  - root
  - docs
