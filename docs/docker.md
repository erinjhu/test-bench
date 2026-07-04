## Docker

### Dockerfile

```Dockerfile
# lightweight base image
FROM python:3.10-slim 
# /app is the working directory in the docker ontainer
WORKDIR /app 
# copy the requirements.txt file into /app
COPY requirements.txt . 
# --no-cache-dir: prevent from writing packages to local cache to minimize the size
# -r: 
RUN pip install --no-cache-dir -r requirements.txt
# copy code from host directory into /app in container
COPY . . 
# will run "pytest tests/" in the container
CMD ["pytest", "tests/"]
```

### Building and Running Docker Container

I added a script in [run.sh](../run.sh) that lets you build and run in one command.

Here is what that script does, assuming that the Docker desktop app is already installed.

1. Build and run the Docker container. 

    Notes:
    - `-t`: shows container's output in the host terminal
    - After making changes, rebuild the container before running it

    ```
    docker build -t test-bench .
    ```

2. Run container.

    **Option 1: Container automatically stops when the tests are done running**

    Notes:
    - `-rm`: automatically delete the container when it is done running
    - `--device=/dev/ttyUSB0:/dev/ttyUSB0`: let the container access the hardware port 

    ```
    docker run --device=/dev/ttyUSB0:/dev/ttyUSB0 --rm test-bench
    ```

    **Option 2: Do development inside the container**

    Notes:
    - `-it`: interactive terminal; can type commands
    - `--rm`: automatically delete container when exiting
    - `/bin/bash`: the command prompt program to run inside the container

    ```
    docker run -it --rm python:3.12-slim /bin/bash
    ```