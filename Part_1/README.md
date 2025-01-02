# Install Docker

More information regarding docker installation in official Docker webpage: https://docs.docker.com/engine/install/



## Linux

#### Set up the repository

1.  Update the `apt` package index and install packages to allow `apt` to use a repository over HTTPS:

```bash
sudo apt update
sudo apt install ca-certificates curl gnupg
```

2.  Add Docker’s official GPG key:

```bash
# Add Docker's official GPG key:
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /usr/share/keyrings/docker.asc
sudo chmod a+r /usr/share/keyrings/docker.asc
```

3.  Use the following command to set up the repository:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
```

#### Install Docker Engine

1.  Install Docker Engine, containerd, and Docker Compose.

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



## Windows



1. **Download the Installer**
   Use the download button at the top of the page or visit the [Docker Desktop release notes](https://docs.docker.com/desktop/release-notes/) to download the installer.
2. **Run the Installer**
   Double-click `Docker Desktop Installer.exe` to launch the installation process. By default, Docker Desktop is installed in `C:\Program Files\Docker\Docker`.
3. **Select Configuration Options**
   On the Configuration page, decide whether to enable the **Use WSL 2 instead of Hyper-V** option based on your choice of backend.
   - If your system supports only one of these options, you won’t be able to choose.
4. **Complete the Installation Wizard**
   Follow the instructions in the installation wizard to authorize and proceed with the installation.
5. **Finish Installation**
   Once the installation is complete, click **Close** to exit the installer.
6. **Start Docker Desktop**
   [Launch Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/#start-docker-desktop) to begin using it.

**Additional Resource:**
Check out this helpful YouTube video: [How to Install Docker on Windows](https://www.youtube.com/watch?v=ZyBBv1JmnWQ).

---

# Test

After installing Docker, run the following command:

```bash
docker run hello-world
```

If you see an output similar to this, Docker is functioning correctly.

```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```