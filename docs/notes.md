




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