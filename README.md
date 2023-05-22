This repository contains the code and supplementary material for the paper titled "Toward Automated Extraction and Characterization of Scaling Regions in Dynamical Systems."
(https://doi.org/10.1063/5.0069365) The paper proposes a novel approach to automatically extract and characterize scaling regions in dynamical systems.

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

**rk4.py:** Contains Runge-Kutta code for generating the Lorenz trajectory. 

**utils.py:** Contains code for peak detection. 
