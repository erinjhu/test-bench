set -e # stop script if any command fails
docker build -t test-bench .
docker run --rm test-bench