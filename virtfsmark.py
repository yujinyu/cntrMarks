# -*- coding: UTF-8 -*-
import os, docker
from configs.container import *
from configs.cpus import *

image = "virtfsmark:f25"

if __name__ == "__main__":
    dockerfile = os.path.join(os.getcwd(),"image_built/")
    print(dockerfile)

    client = docker.from_env()
    pre_work_for_docker(client, dockerfile, image)



    # todo
