

# Docker

Docker is a tool, that creates containers (You can imagine it as a virtual environment, but it really isn't), where you can develop and build applications.
Because you install and configure everything inside the container, you can ship this container to any other machine and 
it will perform exactly like on the previous machine.  

[Install Docker](https://docs.docker.com/engine/install/#desktop)

If you should use a VM or Docker to guaranty consistency, depends on the use cases. Try both out or decide with the following 
advantages and disadvantages:

## Advantages
1. **Reproducibility**: A Docker container will run the same on every operating system
2. **Isolation**: Installations or changes of libraries will only affect the inside of the container
4. **Docker Hub**: allows you to save images in the cloud
5. **Environment management**: You can build different environment for the same application (development, testing, production)
6. **Continuous Integration** You can automatically update your docker img with tools like Travis, Jenkins or Wercker

## When NOT to use Docker
1. Your app is complicated and you are not/do not have a sysadmin
2. Performance is critical to your application
3. You don’t want upgrade hassles
4. **Security is critical to your application** (Even though Docker solves some security problems, they create new ones)
5. **Multiple operating systems** (Docker containers share the host computers operating system, if you want to run the same project on a different
    system, you need to switch to a virtual machine)
6. **Clusters** (When running Docker projects in cluster it can get complicated and you need to find a work around) 

## Security Issue

1. **Unsecured communication and unrestricted network traffic**
   In some versions of Docker, all network traffic is allowed between containers in the same host.
   Developers should only allow intercommunication that is necessary by linking specific containers.
   In addition communication with Docker registries should be encrypted through TLS security protocol
2. **Unrestricted access of Process and files**
   An attacker that gains access to one container may have the capability to gain access to other containers or the host. (via remouting)
   To avoid this, the user namespace feature in Linux containers will allow developers to avoid root access by giving isolated containers separate user accounts, and mandate resource constrains, so users from one container do not have the capability to access other containers or their resources.
   This feature is not enabled by default
3. **Kernel level threats**
   All containers share the same kernel and the host.
   This means the host should be updated and hardened to reduce kernel threats.
   In addition, only necessary privileged ports should be accessible trough a container
4. **Inconsistent update and patching of docker containers**
5. **Unverified docker images**



## Process of a Docker project
1. Dockerfile:
    This text file stores all commands that are necessary to create the image
2. Image:
    The image contains the whole environment and applications. These are saved and can be shipped to others.
    When you want to use the image, you can build with that image the container, where everything will be run.
3. Container:
    The container is the actual running "environment", that runs the applications

## Commands

### Build

Build from dockerfile

```
docker build -t myimgae:1.0 .
```

list all images that are locally stored

```
docker image ls
```

delete an image from local image store

```
docker image rm myImage
```

### Share

Pull an image

```
docker pull myimage:1.0
```

Retag a local image with new image name and tag

```
docker tag myimage:1.0 myrepo myimage:2.0
```

Push an image to a registry

```
docker push myrepo/myimage:2.0
```

### Run

Note that there are multiple parameters that can be set for the run method, most important ones are:

* ``-a`` will connect the container to your terminal

* ``-d`` will detach the container from your terminal
* ``-p`` will assign container ports to specific ports
* ``-e`` will change environment variables
* ``--name`` will define the container name
* ``AUTHOR`` is an environment variable

Run a container from an image (if the image not available locally, docker searches for it on docker hub)

```
docker container run --name nameOfContainer -p 8888:8888 imageName
```

List the running containers (add --all to include stopped containers)

```
docker container ls
```

Print the last 100 lines of a container’s logs

```
docker container logs --tail 100 nameOfContainer
```

Stop a running container through SIGTERM

```
docker container stop nameOfContainer
```

Stop a running container through SIGKILL

``````
docker container kill nameOfContainer
``````

List the networks

``````
docker network ls
``````

Delete container

``````
docker rm --force nameOfContainer
``````

To see on which ports an container is running use

``````
docker port static-sites
``````


### Saving Docker image locally
The easiest way to distribute your docker file is with the docker-hub, but if you don't want to get pay for an subscription
or don't want to share the product on a third party server, you can do the following:

Save the docker image as tar file
```
docker save --output saved-image.tar my-image:1.0.0

# or

docker save my-image:1.0.0 > saved-image.tar
```
And load the file with
```
docker load --input saved-image.tar

# or 

docker load < saved-image.tar
```
To check if the image is loaded correctly you can list all images
```
docker images
```

## Create own Dockerfile
More about that [here](https://docs.docker.com/get-started/part2/#sample-dockerfile) 

## References
* https://docs.docker.com/samples/
* https://github.com/docker/labs/blob/master/beginner/chapters/setup.md
* https://www.youtube.com/watch?v=YFl2mCHdv24
* https://medium.com/@sanketmeghani/docker-transferring-docker-images-without-registry-2ed50726495f