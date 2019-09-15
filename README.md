# NCTU-Cheetah

In this project, a compliant leg mechanism for low-cost quadruped pet robots had
been studied and built. Inspired by the published literature from EPFL-Cheetah and
Oncilla robots, a new quadruped robot NCTU-Cheetah based on the compliant leg
mechanism mentioned above had been realized too. NCTU-Cheetah robot relies on
the Central Pattern Generator (CPG) algorithm to control its 12 servo motors,
including 4 tilt motors that allow hip adduction and abduction. The V-REP simulation
model of NCTU-Cheetah robot, CPG program, and other helper utilities were open
sourced here. 

# Introduction
Legged robots have stronger abilities to move in non-flat terrain than the wheeled robots. The compliant leg mechanism has the following three superiorities with respect to the rigid leg mechanism in terms of robot motion:
●	Efficiency: Using mechanical energy storage/release to improve the energy efficiency of motion.
●	Simplification: Using the self-balanced relationship of overall geometry and dynamic structures between the compliant legs and torso to reduce the complexity of gait controller design.
●	Robustness: The compliant leg structure has a high tolerance to the motion disturbances imposed by the real world.
The superiorities mentioned above can be seen in many mammals, including humans. 
The motivation of this project is to design a compliant leg mechanism suitable for low-cost quadruped pet robots. With this compliant leg mechanism, it has the advantages of low complexity, easy assembly, and quick walking.
In this project, EPFL-Cheetah [1-3] robot, Oncilla [4] robot and other total eight compliant quadruped robots had been studied deeply at first to acquire enough technical background for the subsequent development of my own NCTU-Cheetah robot. The preliminary mechanical design of NCTU-Cheetah robot was mainly inspired by the published literature from EPFL-Cheetah and Oncilla robots. NCTU-Cheetah’s mechanical design was finished using SolidWorks, and the URDF-format robot description file about NCTU-Cheetah was then imported, modified and simulated in V-REP [7] robot simulator as Fig. 1.
 
![image](https://github.com/kuanyusu/NCTU-Cheetah/blob/master/fig.1.jpg)
Fig. 1 An NCTU-Cheetah robot model in V-REP.

After many iterations of trial-and-error, e.g. adjusting link dimensions/spring coefficients and validating the plausibility of the adopted CPG motor control algorithm, I started to print all mechanical links using a low-cost 3D printer. The servo motors and other necessary parts (bolts, nuts, bearings, springs, etc.) were all bought from online hardware stores in Taiwan (Misumi, Ruten) or China (Taobao).  The final assembled NCTU-Cheetah robot is shown in Fig. 2.

![image]
Fig. 2  The assembled NCTU-Cheetah robot.

This report contains 7 sections: Section 2 references the most important literature that influence this project. Section 3 illustrates the mechanical design of NCTU-Cheetah robot. Section 4 explains how to generate CPG motor control trajectories. Section 5 describes the strategies to correctly simulate a compliant robot like NCTU-Cheetah in V-REP. Section 6 demonstrates how to assemble a real NCTU-Cheetah robot. Section 7 gives some preliminary motion testings on the robot to confirm the plausibility of the current design.
