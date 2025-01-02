# CLI (Command line interface)



By default, Docker can be accessed from the CLI. Using CLI commands will help you gain an initial understanding of how Docker operates, and these commands will be invaluable as you continue to use Docker.

Let's start by exploring some basic CLI commands:

```bash
docker --help
```



You will see various sections, such as Common, Management, and Swarm Commands.

In this tutorial, you will use some of these commands:

**Common Commands**

```bash
  run         Create and run a new container from an image
  exec        Execute a command in a running container

  build       Build an image from a Dockerfile
  pull        Download an image from a registry
  
  ps          List containers
  images      List images
```



You can also explore additional options for Common Commands. Let's try running:

```bash
docker run --help
```

You will see many options for the `run` command. The most important ones for us are:

```bash
-it
  -i, --interactive   Keep STDIN open even if not attached
  -t, --tty           Allocate a pseudo-TTY

-p                    Publish a container's port(s) to the host
--rm                  Automatically remove the container and its associated anonymous volumes when it exits
-v                    Bind mount a volume
```

Did you remember test docker command?

```bash
docker run hello-world
```

You use command `run` and `hello-world` image

Another example:

```bash
docker run --name myng --rm -p 8080:80 -v ./:/data -d nginx
```

- I will run `docker`: This is the main command to interact with Docker.

- With the `run` command: This creates and starts a new container.

- Set the container name to `myng`: Using the option `--name myng`.

- Automatically delete the container after stopping it: Achieved using the `--rm` option.

- Publish a port to the host:

  - Nginx listens on port `80` inside the container.
  - Since containers are isolated, I will publish the container's port `80` to the host's port `8080` using `-p 8080:80`.
  - This allows access to Nginx on the host machine via `127.0.0.1:8080`.

- Share the current folder (`./`) with the container:

  - The current folder is mounted to `/data` in the container using the `-v ./:/data` option.
  - Docker will create the `/data` folder inside the container if it doesn’t already exist.

- Run the container as a daemon (**optional**):

  - By using the `-d` option, the container runs in the background.
  - If I want to see the logs in the terminal in real-time, I can omit the `-d` option.



To see all running containers, use the `ps` command:

```bash
docker ps
```

Example output:

```bash
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                     NAMES
4a433f297731   nginx     "/docker-entrypoint.…"   8 minutes ago   Up 8 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   myng
```

In the output, you can see the `myng` container is running.

Open your browser and navigate to http://127.0.0.1:8080/. You should see the Nginx welcome screen.

To stop the `myng` container, run:

```bash
docker stop myng
```

If you run `docker ps` again, you will notice that the `myng` container has disappeared because it was automatically removed due to the `--rm` option used earlier.

