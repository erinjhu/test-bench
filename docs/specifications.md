## Table of Contents

1. **Overview**
- 1.1 Project Objectives
- 1.2 Target Hardware & Interface
- 1.3 Scope (What is tested, what is simulated)

2. **System Architecture**
- 2.1 High-Level Block Diagram
- 2.2 UML Class Diagram (The OOP Framework)
- 2.3 Component Responsibilities (STM32 vs. Python PC Side)

3. **Communication Protocol**
- 3.1 Transport Layer (UART Settings: Baud, Parity, Stop Bits)
- 3.2 Packet Structure (Header, Length, Payload, Checksum)
- 3.3 Command Set (Table of Commands the PC sends to the STM32)

4. **Operational Logic**
- 4.1 System State Machine (Diagram and Description)
- 4.2 Error Handling & Safety (Watchdog behavior, Timeout handling)
- 4.3 Sequence Diagram (The "PC asks, STM32 answers" flow)

5. **Data Handling**
- 5.1 Configuration File Format (JSON)
- 5.2 Log File Format (CSV Schema)

6. **Testing & Validation**
- 6.1 Test Suite Overview (What are we testing?)
- 6.2 CI/CD Integration Strategy (How do we run this automatically?)


## 1. Overview

### 1.1 Project Objectives

- Improve skills in Pytest, CI/CD, HIL, and testing for embedded systems by building a robust test bench
- Build a system to automate testing future projects

### 1.2 Target Hardware & Interface
   
STM32-F401RE

### 1.3 Scope

(In progress)

## 2. System Architecture
### 2.1 High-Level Block Diagram
### 2.2 UML Class Diagram (The OOP Framework)
### 2.3 Component Responsibilities (STM32 vs. Python PC Side)

## 3. Communication Protocol
### 3.1 Transport Layer (UART Settings: Baud, Parity, Stop Bits)
### 3.2 Packet Structure (Header, Length, Payload, Checksum)
### 3.3 Command Set (Table of Commands the PC sends to the STM32)

## 4. Operational Logic
### 4.1 System State Machine (Diagram and Description)
### 4.2 Error Handling & Safety (Watchdog behavior, Timeout handling)
### 4.3 Sequence Diagram (The "PC asks, STM32 answers" flow)

## 5. Data Handling
### 5.1 Configuration File Format (JSON)
### 5.2 Log File Format (CSV Schema)

## 6. Testing & Validation
### 6.1 Test Suite Overview (What are we testing?)
### 6.2 CI/CD Integration Strategy (How do we run this automatically?)