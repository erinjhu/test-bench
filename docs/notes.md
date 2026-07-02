




## OOP Framework

Goals:
- Scalable framework for different devices
- OOP fundamentals
    - Encapsulation
    - Abstraction
    - Polymorphism
    - Inheritance

### Architecture

#### UML Diagram

![](test-framework.drawio.png)

#### Classes

General class for serial devices

### States

| State     | Description |
| --------- | ----------- |
| IDLE      |             |
| CONNECTED |             |
| TESTING   |             |
| ERROR     |             |
| FINISHED  |             |

### Logging

`[Timestamp][Test_Name][Status][Response]`

Output to CSV   

### FW Course

Technical Concepts
- Baremetal: firmware without OS

Development Process
- Debugging: instead of adding more code to fix it, find the root cause



## Testing Types

### Unit

- Tests for functions in isolation
- GTest for firmware
    - Since GTest can run in a C file and STM32 code is in C

### Functional

### Regression

### Integration

- Tests for systems interacting with each other
- 