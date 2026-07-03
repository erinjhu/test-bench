



## Roadmap

1. TDD: ADC, UART, watchdog, JTAG
2. FreeRTOS
3. SPI

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

To perform TDD on ADC and UART, you must keep your **hardware access** separated from your **data logic**. Here is the strategy:

### 1. UART TDD (Focus: Packet Parsing)

* **Goal:** You want to ensure your system correctly handles incoming commands and outgoing responses.
* **Test (Red):** Write a Pytest that passes a raw byte string `b"\xAA\x05\x00\x00\xAF"` to your `Parser` class and asserts it returns a `READ_VOLTAGE` object.
* **Code (Green):** Write the minimal `Parser.parse()` method to make that test pass.
* **Refactor:** Clean up the logic so it can handle different command lengths.
* **Why:** You are testing the *logic* of the communication protocol without ever touching the actual UART pins.

### 2. ADC TDD (Focus: Data Conversion)

* **Goal:** You want to ensure the raw integer value from the ADC registers correctly converts to a physical voltage.
* **Test (Red):** Write a GTest (C) that feeds the raw value `2048` into your conversion function and asserts the result is `1.65` (assuming a 3.3V range).
* **Code (Green):** Write the math logic: $Voltage = (Raw / Max) * Reference$.
* **Refactor:** Use named constants for `MAX_ADC_VALUE` and `V_REF`.
* **Why:** The hardware (ADC) provides the number, but the *conversion logic* is where bugs hide.

### 3. The "Seam" Pattern (Crucial for HIL)

* Create an interface (or function pointers) for your drivers:
* `uint16_t adc_read_raw(void);`
* `void uart_transmit(uint8_t *data, size_t len);`


* **During Unit Tests (PC):** You replace these functions with "Mocks" that return fixed values.
* **During HIL (STM32):** You link these functions to the actual HAL or register-writing code.

### Summary of Workflow

* **Step 1:** Write the test on your PC (GTest for C logic, Pytest for Python parsing).
* **Step 2:** Ensure the test fails because the code doesn't exist.
* **Step 3:** Implement the math/logic functions.
* **Step 4:** Run the test. Once green, integrate it with the actual ADC/UART drivers.
* **Step 5:** Run your Pytest functional test (Phase 4 of `test_plan.md`) to verify the physical hardware integration.