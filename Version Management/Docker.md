# Docker

Docker is a tool, that creates containers (Virutal environments) where you can develop and build applications.
Because you install and configure everything inside the container, you can ship this container to any other machine and 
it will perform exactly like on the previous machine.

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

# UNDER CONSTRUCTION


## References

* https://www.youtube.com/watch?v=YFl2mCHdv24