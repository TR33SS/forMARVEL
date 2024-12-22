# L293D Motor Driver IC Datasheet
---
#### **1. General Description**

The L293D is a quadruple high-current half-H-Bridge motor driver integrated circuit (IC). It is designed for driving DC motors, stepper motors, and other inductive loads in both directions. The IC provides bidirectional control for two DC motors or a single stepper motor. It has integrated thermal shutdown, overload protection, and built-in flyback diodes for protection against inductive loads.
the L293D motor driver IC is a versatile and efficient solution for controlling DC motors and stepper motors. With features such as bidirectional motor control via an H-Bridge, speed control using PWM, and built-in protection mechanisms, the L293D is widely used in robotics, automation, and embedded systems. Its ease of use and ability to drive motors in both directions with speed control make it an excellent choice for motor control applications.

---

#### **2. Key Features of L293D**
- **Motor Driving Capability:** Can drive up to two DC motors or one stepper motor.
- **Voltage Range:** Operates with a motor voltage supply (Vcc2) from 4.5V to 36V.
- **Current Rating:** Capable of outputting a continuous current of up to 600 mA per motor channel, with a peak current of 1.2 A.
- **Thermal and Overload Protection:** Includes internal thermal shutdown and overload protection to safeguard against excessive heat and current.
- **Logic Voltage:** Operates with a 5V logic supply (Vcc1) for control inputs.
- **H-Bridge Configuration:** Uses two H-Bridge circuits to control motor direction.
- **PWM Capability:** Supports Pulse Width Modulation (PWM) for motor speed control.
---



#### **3. Pin Configuration (16-Pin Dual In-line Package)**
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


---
 ![](https://lastminuteengineers.com/wp-content/uploads/arduino/L293D-Dual-H-Bridge-Motor-Driver-IC-Pinout.png)

---


#### **4. Electrical Characteristics**
- **Operating Voltage (Vcc1):** 4.5V to 5.5V (logic supply voltage)
- **Motor Voltage (Vcc2):** 4.5V to 36V (motor supply voltage)
- **Continuous Output Current:** 600 mA per channel
- **Peak Output Current:** 1.2A per channel (for brief periods)
- **Power Dissipation:** 1W maximum
- **Operating Temperature Range:** -40°C to +85°C
- **Thermal Shutdown:** Yes, at 150°C
- **Overcurrent Protection:** Yes, automatically disables output if current exceeds limit 

---

#### **5. H-Bridge Configuration**
The L293D uses an H-Bridge circuit to allow bidirectional control of motors. The H-Bridge consists of four switches (transistors) that control the direction of current flowing through the motor. By switching these transistors on and off, the L293D can reverse the motor's direction.

- **Forward Motion:** To drive the motor forward, one pair of transistors (one on each side of the H-Bridge) is turned on, allowing current to flow in one direction.
- **Reverse Motion:** Reversing the transistors allows current to flow in the opposite direction, making the motor rotate in reverse.
- **Braking and Coasting:** The IC can also perform motor braking by shorting the motor terminals or allow it to coast to a stop by leaving the transistors open.

---

#### **6. Pulse Width Modulation (PWM) for Speed Control**
PWM is used in the L293D to control the speed of motors. By adjusting the duty cycle of the PWM signal, the average voltage applied to the motor can be varied, thereby controlling the motor's speed.

- **Duty Cycle Control:** The higher the duty cycle, the faster the motor spins. A lower duty cycle results in slower motor speed.
- **Efficient Motor Control:** PWM offers energy-efficient motor speed control by switching the transistors on and off at high frequencies, reducing power dissipation.

---

#### **7. Internal Protection Mechanisms**
- **Thermal Shutdown:** The L293D includes a thermal shutdown feature that turns off the motor outputs if the internal temperature exceeds a predefined threshold (typically 150°C) to prevent damage from overheating.
- **Overload Protection:** The IC also features overload protection to prevent damage if the motor draws too much current.
- **Flyback Diodes:** Built-in diodes protect the IC from voltage spikes caused by inductive loads, such as motors.


---

#### **8. Applications**
- **Robotics:** Control DC motors or stepper motors in robots for movement and manipulation tasks.
- **Arduino Projects:** Used in various Arduino-based motor control projects, such as controlling the movement of robotic vehicles.
- **Toys and Hobby Projects:** Commonly found in motorized toys and hobbyist vehicles requiring motor direction and speed control.
- **Automation Systems:** Can be used in automated systems to drive actuators, conveyors, and other motorized components.

---

#### **9. Typical Application Circuit**
A typical application circuit involves connecting the L293D’s input pins (IN1, IN2, IN3, IN4) to a microcontroller (such as an Arduino) and using PWM signals to control the speed of the motors. The motor is connected to the output pins (OUT1, OUT2 for Motor 1, and OUT3, OUT4 for Motor 2), and the motor supply (Vcc2) is connected to a suitable motor voltage source (usually 12V or 24V for DC motors).

---
                                     _/\_ Thanks for Reading _/\_
 
 ---


