## Daily Logs

### Next session

- Implement the test in the UML


### 7/4

- Script to build and run Docker container in one command
- Refactor [parser](../src/parser.py) to use hash map instead of if statements for command ids
- Was failing the workflow because it was trying to run cppcheck but I didn't add any C files yet. Fixed by adding condition to yml
- Test for validating the checksum was returning Index error because it was trying to calculate the checksum for the case where the command is invalid and there are no bytes to make the checksum out of, so the checksum is empty. Fixed by adding a separate if statement.

### 7/3

- Parser class
    - Decided on protocol for human commands, added to [specifications](docs\specifications.md)
    - Translate human commands into bytes (e.g. PING, GET_VOLTAGE)
    - Started test-driven development; wrote test for encoding PING command to bytes
- Install act on host machine
    - To run workflow locally before pushing it
- Obstacles
    - act was getting stuck. Fixed by installing dependencies in the Docker container (configured in the Dockerfile instead) of installing it at runtime (configured in the test.yml). Also updated test.yml to point to the container image to test it there instead of on the host.

### 7/2

- Planning structure for test bench; deciding on what tools to use for unit, regression, functional, integration tests

### 7/1

- Outline specifications document

### 6/28

- High-level planning
- UML diagram for Pytest framework
- Set up Docker
- Configure GitHub Actions