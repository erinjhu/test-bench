# lightweight base image
FROM python:3.10-slim 
# /app is the working directory in the docker ontainer
WORKDIR /app 
# copy the requirements.txt file into /app
COPY requirements.txt . 
# --no-cache-dir: prevent from writing packages to local cache to minimize the size
# -r: tell pip to read requirements.txt for packages to install
RUN pip install --no-cache-dir -r requirements.txt
# copy code from current host directory into /app in container
COPY . . 
# will run "pytest tests/" in the container
CMD ["pytest", "tests/"]
