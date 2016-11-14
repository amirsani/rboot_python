# Replacement Bootstrap version 0.01
An implementation of the replacement bootstrap algorithm for dependent data with modifications to support real-numbered series (up to 64 bits) and accelerations to improve compute performance.  

If you use this code or a modification of this code, please reference:
@inproceedings{sani2015replacement,
  title={The replacement bootstrap for dependent data},
  author={Sani, Amir and Lazaric, Alessandro and Ryabko, Daniil},
  booktitle={2015 IEEE International Symposium on Information Theory (ISIT)},
  pages={1194--1198},
  year={2015},
  organization={IEEE}
}

## Parameters:
series - Real or integer series  
bootstraps - Number of Bootstraps  
seed - Random number seed  
replacement_percentage - The percentage of the original series to replace max(1, 0.01 <= replacement_percentage).  
replace - Sample with or without replacement [True, False]  
rho - Concentration control. rho closer to 0 concentrates bootstraps towards the mean, while rho closer to 1 maximizes variability.  

Copyright Amir Sani 2016
