# django-cicd-kubernetes
django project pipeline cicd github actions to deploy on kubernetes cluster
# cicd
La aplicación de prueba escrita en Python/django es dockerizada, pusheada al registry de Docker y deployada en un cluster de Kubernetes mediante pipeline en Github Actions.

Mi Docker Hub: https://hub.docker.com/repository/docker/nicosistemas/probando-django/general

Por el momento no es accedible a una url https poqrue no tengo Ingress ni dominio propio, lo que hago es emularlo con ngrok para ser consumida


To Do on cluster la primera vez:

kubectl apply -f deployment.yaml -n test-nico
