# BergelsonLab_lena5min

#### Extract the first value in the "Timestamp" column, and place it into a new csv. 

### Usage:

In command line/terminal:
 * move to the BergelsonLab_lena5min directory
 * run the "first_timestamp.py" file as follows:
 
 $python first_timestamp.py "the path of your lena5min folder" "the path where you want to save the csv output"
 
 For example:
 
 $python first_timestamp.py "/home/jovyan/work/BergelsonLab/lena5min" "/home/jovyan/work/BergelsonLab/Bergelsonlab_lena5min"
 
### Dependency:
 
This script depends on pandas. To install it, you can simply enter "pip install pandas" in the command line. If you don't have pip, put the following in the command line:
 
 $conda install pip
 
 $pip install pandas