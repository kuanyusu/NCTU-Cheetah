# NCTU-Cheetah

## Abstract
In this project, a compliant leg mechanism for low-cost quadruped pet robots had been studied and built. Inspired by the published literature from EPFL-Cheetah and Oncilla robots, a new quadruped robot NCTU-Cheetah based on the compliant leg mechanism mentioned above had been realized too. NCTU-Cheetah robot relies on the Central Pattern Generator (CPG) algorithm to control its 12 servo motors, including 4 tilt motors that allow hip adduction and abduction. The V-REP simulation model of NCTU-Cheetah robot, CPG program, and other helper utilities were open sourced here. 

## Introduction
Legged robots have stronger abilities to move in non-flat terrain than the wheeled robots. The compliant leg mechanism has the following three superiorities with respect to the rigid leg mechanism in terms of robot motion:  

> ●	Efficiency: Using mechanical energy storage/release to improve the energy efficiency of motion.  

> ●	Simplification: Using the self-balanced relationship of overall geometry and dynamic structures between the compliant legs and torso to reduce the complexity of gait controller design.  

> ● Robustness: The compliant leg structure has a high tolerance to the motion disturbances imposed by the real world.  

The superiorities mentioned above can be seen in many mammals, including humans.

The motivation of this project is to design a compliant leg mechanism suitable for low-cost quadruped pet robots. With this compliant leg mechanism, it has the advantages of low complexity, easy assembly, and quick walking.  

In this project, EPFL-Cheetah robot, Oncilla robot and other total eight compliant quadruped robots had been studied deeply at first to acquire enough technical background for the subsequent development of my own NCTU-Cheetah robot. The preliminary mechanical design of NCTU-Cheetah robot was mainly inspired by the published literature from EPFL-Cheetah and Oncilla robots. NCTU-Cheetah’s mechanical design was finished using SolidWorks, and the URDF-format robot description file about NCTU-Cheetah was then imported, modified and simulated in V-REP robot simulator as Fig. 1.  
 
![image](https://github.com/kuanyusu/NCTU-Cheetah/blob/master/fig.1.jpg)
Fig. 1 An NCTU-Cheetah robot model in V-REP.  

After many iterations of trial-and-error, e.g. adjusting link dimensions/spring coefficients and validating the plausibility of the adopted CPG motor control algorithm, I started to print all mechanical links using a low-cost 3D printer. The servo motors and other necessary parts (bolts, nuts, bearings, springs, etc.) were all bought from online hardware stores in Taiwan (Misumi, Ruten) or China (Taobao).  The final assembled NCTU-Cheetah robot is shown in Fig. 2.  

![image](https://github.com/kuanyusu/NCTU-Cheetah/blob/master/fig.2.jpg)
Fig. 2  The assembled NCTU-Cheetah robot.  

## Mechanical Design
There are four main factors that lead NCTU-Cheetah robot’s mechanical design: (1) Make the limb ratio close to a real cheetah cub. (2)  Have an ASLP compliant leg mechanism like EPFL-CheetahCub robot. (3)  Have a turning mechanism similar to Oncilla Robot. (4) Enhance the structure strength of 3D printed links. Simply put, NCTU-Cheetah’s mechanical complexity and weight are between EPFL-CheetahCub and Oncilla.  

![image]
Fig. 6 illustrates the front view and the side view of NCTU-Cheetah robot. The dimensions of NCTU-Cheetah robot is about 18cm (W) x 24cm (H) x 30cm (L) when it stands still. The weight (including 12 servo motors) of a real NCTU-Cheetah robot is 1.6Kg. The detailed geometric information of every mechanical link can be checked by importing the open sourced V-REP scene file (*.ttt) into V-REP simulator by readers.
  
