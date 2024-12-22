# L293D Motor Driver IC Datasheet

#### **General Description**


The L293D is a quadruple high-current half-H-Bridge motor driver integrated circuit (IC). It is designed for driving DC motors, stepper motors, and other inductive loads in both directions.

---


#### **Pin Configuration (16-Pin Dual In-line Package)**
| Pin | Name              | Function                               |
|-----|-------------------|----------------------------------------|
| 1   | IN1               | Input for Motor 1 direction control   |
| 2   | IN2               | Input for Motor 1 direction control   |
| 3   | IN3               | Input for Motor 2 direction control   |
| 4   | IN4               | Input for Motor 2 direction control   |
| 5   | Ground (GND)      | Ground pin                            |
| 6   | Ground (GND)      | Ground pin                            |
| 7   | Vcc2              | Motor supply voltage                  |
| 8   | Vcc1              | Logic supply voltage (typically 5V)   |
| 9   | OUT1              | Motor 1 output (connected to motor terminal) |
| 10  | OUT2              | Motor 1 output (connected to motor terminal) |
| 11  | Ground (GND)      | Ground pin                            |
| 12  | Ground (GND)      | Ground pin                            |
| 13  | OUT3              | Motor 2 output (connected to motor terminal) |
| 14  | OUT4              | Motor 2 output (connected to motor terminal) |
| 15  | Vcc2              | Motor supply voltage                  |
| 16  | Vcc1              | Logic supply voltage (typically 5V)   |


 ![](https://lastminuteengineers.com/wp-content/uploads/arduino/L293D-Dual-H-Bridge-Motor-Driver-IC-Pinout.png)

---
####  **H-Bridge Configuration**
The L293D uses an H-Bridge circuit to allow bidirectional control of motors. The H-Bridge consists of four switches (transistors) that control the direction of current flowing through the motor. By switching these transistors on and off, the L293D can reverse the motor's direction.

- **Forward Motion:** To drive the motor forward, one pair of transistors (one on each side of the H-Bridge) is turned on, allowing current to flow in one direction.
- **Reverse Motion:** Reversing the transistors allows current to flow in the opposite direction, making the motor rotate in reverse.
- **Braking and Coasting:** The IC can also perform motor braking by shorting the motor terminals or allow it to coast to a stop by leaving the transistors open.

---

#### **Pulse Width Modulation (PWM) for Speed Control**
PWM is used in the L293D to control the speed of motors. By adjusting the duty cycle of the PWM signal, the average voltage applied to the motor can be varied, thereby controlling the motor's speed.

- **Duty Cycle Control:** The higher the duty cycle, the faster the motor spins. A lower duty cycle results in slower motor speed.
- **Efficient Motor Control:** PWM offers energy-efficient motor speed control by switching the transistors on and off at high frequencies, reducing power dissipation.

---
                                     _/\_ Thanks for Reading _/\_
 
 ---


