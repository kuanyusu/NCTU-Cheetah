# NCTU-Cheetah

## Introduction
In this project, a compliant leg mechanism for low-cost quadruped pet robots had been studied and built. Inspired by the published literature from EPFL-Cheetah and Oncilla robots, a new quadruped robot NCTU-Cheetah based on the compliant leg mechanism mentioned above had been realized too. NCTU-Cheetah robot relies on the Central Pattern Generator (CPG) algorithm to control its 12 servo motors, including 4 tilt motors that allow hip adduction and abduction. The V-REP simulation model of NCTU-Cheetah robot, CPG program, and other helper utilities were open sourced here. 
 
![image](https://github.com/kuanyusu/NCTU-Cheetah/blob/master/fig.1.jpg)
Fig. 1 An NCTU-Cheetah robot model in V-REP.  

The dimensions of NCTU-Cheetah robot is about 18cm (W) x 24cm (H) x 30cm (L) when it stands still. The weight (including 12 servo motors) of a real NCTU-Cheetah robot is 1.6Kg. The detailed geometric information of every mechanical link can be checked by importing the open sourced V-REP scene file (*.ttt) into V-REP simulator by readers.

## Assembly & Testing
I printed all mechanical links using a low-cost 3D printer, and the type of 3D printing filament is ABS. The servo motors, motor controller board (Raspberry Pi 3) and other necessary parts (bolts, nuts, bearings, springs, batteries, etc.) were all bought from online hardware stores in Taiwan (Misumi, Ruten) or China (Taobao).

Fig. 2 shows four completely assembled ASLP legs ready to be installed on hip motors. The left two are forelegs, and the rest are hind legs.

![image](https://github.com/kuanyusu/NCTU-Cheetah/blob/master/fig.3.jpg)
Fig. 2 Four completely assembled ASLP legs

In the testing, an NCTU-Cheetah robot had equipped 12 SGS-215 servo motors. Each SGS-215 servo motor has 17 kg-cm peak stall torque and can be inter-connected (including power and data lines) in a daisy-chain style to up to theoretically 253 devices. This eases the assembly works significantly. 12 SGS-215 spend about 150 US$, and the full BOM of an NCTU-Cheetah robot costs about  260 US$.

The motor control software was programmed in Python language and running on the Raspberry Pi 3 module. A Python class encapsulating the details of low-level communication with the SGS215 servo motors had been designed to provide convenient high-level motor control commands. Another Python class based on scipy.integrate.odeint, an ordinary differential equations solver package, had been developed to realize the CPG algorithm. Since Raspberry Pi 3 is not capable to generate the CPG trajectories in real-time, in the testing all CPG trajectories would be generated in advance.


## Appendix - Testing Videos
(1)Trot gait moving test: https://reurl.cc/xD0564

(2)Turning test: https://reurl.cc/alvOLD

(3)Trot gait simulation: https://reurl.cc/rl8yry

(4)Bound gait simulation: https://reurl.cc/D16zjd
