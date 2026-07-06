## Daily Logs

### Next session

- Fix failing tests
- Send unsigned bytes, implement offset or cast with 2's complement
- add tests to validate payload parameter validation 

### 7/6

- Failed `test_encode_get_command` because there is no associated ID for any invalid commands (commands other than the ones in `COMMAND_IDS` of `constants.py`). Changed so that ID = 0 for invalid commands.
- `encode` method for set commands was not adding the data length
- validate payload input for `encode`
- Fixed `TypeError` by using `extend()` instead of `append()` to handle empty payloads
- [HIL Test Pipeline/lint-and-analyze]   🐳  docker exec cmd=[bash -e /var/run/act/workflow/3] user= workdir=
[HIL Test Pipeline/lint-and-analyze] [DEBUG] Exec command '[bash -e /var/run/act/workflow/3]'
[HIL Test Pipeline/lint-and-analyze] [DEBUG] Working directory '/mnt/c/Users/Hu/Desktop/projects/test-bench'
- Error ```
| cppcheck: error: could not find or open any of the paths given.
[HIL Test Pipeline/lint-and-analyze]   ❌  Failure - Main Run cppcheck [3.319853458s]
``` Issue was because cppcheck was looking for c files but I only had a .h file. Fixed by only running cppcheck if there are c files.

### 7/5

- Wrote new tests but forgot to name them test_{test_name} so they weren't even running
- Added tests for payload length and payloads to accomodate read and write commands
- Parametrize data for set commands was not matching the expected parameters, was leading to error
- Added separate file for command IDs

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