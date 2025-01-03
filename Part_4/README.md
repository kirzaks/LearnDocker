# Docker build

## Intro

In all the previous examples, we used pre-compiled Docker images such as Nginx, WordPress, and MySQL.

However, there is an option to build a Docker image yourself. This is essential when you need a custom image tailored to your specific requirements.

In this lesson, you will learn why building Docker images is important and how to create a configuration build file called a `Dockerfile`.

:exclamation: :warning: Please, use `Part_4` as current folder during this chapter practical tasks. Or copy `calc.py` python script to your favorite destination.



## Your own project

Let's create a custom Docker container using the Python image

The container will run a Python script, `calc.py`, which multiplies the number you provide via a REST API built with Flask. To achieve this, the Flask library needs to be installed.

First, try to run python script in python docker container without Flask library. You will see error.

```bash
docker run --rm -it -p 8080:8080 -v ./:/data python /bin/bash
```

> docker run - Create and run a new container from an image
> --rm - Automatically removes the container when it stops.
> -it - Runs the container interactively.
> -p 8080:8080 - Maps port 8080 of the container to port 8080 on the host.
> -v ./:/data - Mounts the current directory (./) to /data in the container.
> python - use Python base image. I you dont have python image on your computer it will be downloaded from dockerhub registry
> /bin/bash - Opens a Bash shell inside the container.

You will see something like this:

```bash
root@e44e09bc4c6c:/# 
```

And now try to run python script:

```bash
root@e44e09bc4c6c:/# cd /data/
root@e44e09bc4c6c:/data# python calc.py 
Traceback (most recent call last):
  File "/data/calc.py", line 1, in <module>
    from flask import Flask, request
ModuleNotFoundError: No module named 'flask'
```

This is flask module error. This is because the Python image doesn’t include Flask by default.
Now install it.

```bash
root@e44e09bc4c6c:/data# pip3 install flask
```

and run it again. 

```bash
root@e44e09bc4c6c:/data# python calc.py 
Traceback (most recent call last):
  File "/data/calc.py", line 2, in <module>
    import redis
ModuleNotFoundError: No module named 'redis'
```

Redis module error. Install Redis module also.

```bash
root@e44e09bc4c6c:/data# pip3 install redis
```
Run script again.

```bash
root@e44e09bc4c6c:/data# python calc.py 
 * Serving Flask app 'calc'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://172.17.0.2:8080
Press CTRL+C to quit
```

Now script is running and you are able to open URL: http://127.0.0.1:8080/?x=4
You will see result.

```bash
Result: 4+4=8 [ERR] No connection to redis... 
```

## Dockerfile

Let's be honest. It is not very comfortable to every time install Flask and Redis. The solution is to build your own Docker image with these libraries pre-installed.

Here’s how you can create a Dockerfile for building your own Docker image:

```yaml
FROM python
COPY calc.py /data/
RUN pip3 install flask redis
CMD ["python", "/data/calc.py"]
```

More instruction you can finde here: https://docs.docker.com/reference/dockerfile/

> FROM - Create a new build stage from a base image.
> 
> COPY calc.py /data/ - Copy file calc.py from current directory to /data
> 
> RUN pip3 install flask redis - Execute command pip3 install flask redis
> 
> CMD ["python", "/data/calc.py"] - Run python /data/calc.py after on container start
> 

And build with command:

```yaml
docker build -t myproj ./
```
> docker build - Build an image from a Dockerfile
> -t myproj - set image name to myproj
> ./ - use Dockerfile file from current location

And now you can run new created docker image

```bash
docker run --rm -p 8080:8080 myproj
 * Serving Flask app 'calc'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://172.17.0.2:8080
Press CTRL+C to quit
```
> from CLI is removed:
>  -v ./:/data as python script is already installed. But you can also use it as before
>  No need more run interactivity. There is already command defineded by CMD in Dockerfile
>  -it - No need more run interactivity.



## Docker compose 

We have already `myproj` image. Let's convert CLI (`docker run --rm -p 8080:8080 myproj`) to docker compose file



**docker-compose.yaml**

```yaml
services:

  calc:
    image: myproj
    ports:
      - 8080:8080
```



And now - it is possible to run docker compose file by command:

```
docker compose up
```



## Redis

Do you remember the `redis` library?

Redis is an in-memory database. The Python script uses Redis to store information.

Press `Ctrl+C` to stop the container  or run `docker compose down` if you running in detached mode`-d`

Add the Redis Docker image into a Docker Compose file

```yaml
services:

  calc:
    image: myproj
    ports:
      - 8080:8080

  iamredis:
    image: redis
```

Run docker compose again and open URL: http://127.0.0.1:8080/?x=5

You will see different output. Open the same URL again...



