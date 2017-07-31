from fabric.api import local


def bootstrap():
    local('pip install -r requirements.txt')
