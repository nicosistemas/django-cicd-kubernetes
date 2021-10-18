# django-cicd-kubernetes
django project pipeline cicd github actions to deploy on kubernetes cluster
# cicd
La aplicación de prueba escrita en Python/django es dockerizada, pusheada al registry de Docker y deployada en un cluster de Kubernetes mediante pipeline en Github Actions.

Mi Docker Hub: https://hub.docker.com/repository/docker/nicosistemas/probando-django/general

To Do on cluster:

kubectl apply -f deployment.yaml -n test-nico
