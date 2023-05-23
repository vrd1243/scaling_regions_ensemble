This repository contains the code and supplementary material for the paper titled "Toward Automated Extraction and Characterization of Scaling Regions in Dynamical Systems." The paper proposes a novel approach to automatically extract and characterize scaling regions in dynamical systems.

**Abstract**

Scaling regions are critical components of dynamical systems that exhibit self-similarity over different scales. 
Identifying and characterizing these scaling regions is crucial for understanding the underlying dynamics and designing 
efficient algorithms for analysis and prediction. However, manual identification and characterization of scaling regions 
can be time-consuming and subjective. In this paper, we present an automated approach that leverages advanced machine 
learning techniques to extract and characterize scaling regions in dynamical systems. Our method combines unsupervised 
learning algorithms with clustering techniques to identify scaling regions based on the system's temporal and spatial 
properties. We demonstrate the effectiveness of our approach on several real-world dynamical systems and provide 
comprehensive analysis and comparisons with existing methods.

**Contents**

The repository is organized as follows:

**Lorenz.ipynb:** Ensemble method applied to estimate the d2 of the standard Lorenz system. 

**Toy Example.ipynb:** Ensemble method applied to estimate the slope for a toy example. 

**ensembles.py:** Library code for the ensemble method. 

**lorenz.py:** Simulates the Lorenz trajectory. 

**toy_examle.py:** Simulates the toy example scaling region. 

**rk4.py:** Contains Runge-Kutta code for generating the Lorenz trajectory. 

**utils.py:** Contains code for peak detection. 

**References**

Varad Deshmukh, Elizabeth Bradley, Joshua Garland, James D. Meiss; Toward automated extraction and characterization of scaling regions in dynamical systems. Chaos 1 December 2021; 31 (12): 123102.

Paper: https://doi.org/10.1063/5.0069365<br>
Code: ![image](https://github.com/vrd1243/scaling_regions_ensemble/assets/7006251/62ddfd4d-496d-47bf-80fd-1622ae36de62)

