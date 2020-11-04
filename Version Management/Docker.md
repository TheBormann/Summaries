# Docker
Docker is a tool, that creates containers (You can imagine it as a virtual environment, but it really isn't), where you can develop and build applications.
Because you install and configure everything inside the container, you can ship this container to any other machine and 
it will perform exactly like on the previous machine.  

If you should use a VM or Docker to guaranty consistency, depends on the use cases. Try both out or decide with the following 
advantages and disadvantages:

## Advantages
1. **Reproducibility**: A Docker container will run the same on every operating system
2. **Isolation**: Installations or changes of libraries will only affect the inside of the container
3. **Security**: By separating Applications into different containers, will only the compromised container have a problem
4. **Docker Hub**: allows you to save images in the cloud
5. **Environment management**: You can build different environment for the same application (development, testing, production)
6. **Continuous Integration** You can automatically update your docker img with tools like Travis, Jenkins or Wercker

## When to use Docker
1. Learning new Technologies
2. Basic use cases
3. App isolation
4. Developer teams

## When NOT to use Docker
1. Your app is complicated and you are not/do not have a sysadmin
2. Performance is critical to your application
3. You don’t want upgrade hassles
4. Security is critical to your application (Even though Docker solves some security problems, they create new ones)
5. Multiple operating systems (Docker containers share the host computers operating system, if oyu want to run the same project on a different
    system, you need to switch to a virtual machine)
6. Clusters (When running Docker projects in cluster it can get complicated and you need to find a work around) 

## Process of a Docker project
1. Dockerfile:
    This text file stores all commands that are necessary to create the image

2. Image:
    The image contains the whole environment and applications. These are saved and can be shipped to others.
    When you want to use the img, you can build with that image the container, where everything will be run.
    
3. Container:
    The container is the actual running "environment", that runs the applications


## Example project
Even though docker containers are available for linux and windows, we will use Linux (Ubuntu to be exact) to create an container

###  [Install Docker](https://docs.docker.com/engine/install/#desktop)
After installing Docker correctly, you can check if it's working with the following command:
```
docker run hello-world
```
This will download an example docker file and the program in that file will print "Hello from Docker." in the terminal 
when it's working correctly.

### Now you can check docker-hub for specific containers to build your product onto or create a new container
1. Load container from docker-hub
    (If Docker doesn't has admin privileges right away you can add sudo to get permission you need)
    ```
    docker pull tensorflow/tensorflow
    ```
2. To create a Docker container we need to write a Dockerfile, which describes how to build the filesystem in the container, 
what metadata is needed and how to run the container.
How to write one will be covered later.  
If you have your Dockerfile, navigate to your working dir with the Dockerfile and create the image with the command
    ```
    docker build --tag container_name:1.0 .
    ```
3. Delete container
    ```
    docker rm --force bb
    ```

### Run the container
```
docker run -it --rm tensorflow/tensorflow bash
```
Note that there are multiple parameters that can be set for the run method, most important ones are:
* ``-d`` will detach the container from your terminal
* ``-p`` will assign container ports to random host ports
* ``-e`` will change environment variables
* ``--name`` will define the container name
* ``AUTHOR`` is an environment variable


To see on which ports an container is running use:
```
docker port static-siteS
```

### Stop container
1. See running containers
    ```
    docker ps
    ```
2. stop the container
    ```
     docker stop docker_id
    ```
3. Additional you can remove the container as well
    ```
     docker rm docker_id
    ```


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