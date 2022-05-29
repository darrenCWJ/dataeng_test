## Table of Contents
-[About the Section](#about-the-section)
-[Thought Process](#thought-process)

<!-- ABOUT THE SECTION -->
## About The Section
Section 5: Machine Learning
Using the dataset from https://archive.ics.uci.edu/ml/datasets/Car+Evaluation, create a machine learning model to predict the buying price given the following parameters:

Maintenance = High Number of doors = 4 Lug Boot Size = Big Safety = High Class Value = Good

<!-- Thought Process -->
## Thought Process
Looking at the variables in the groups below, we can conclude that all the variables are categorical. However, we do not know if they are ordinal or nominal therefore we will need to try out on both formats. Following up, we will test on multiple different models to find out which models works best with the data provided. However after going through all the model, we realise that the highest possible accuracy is only 30%. This could be due to low sample size of data at only 1728 observations. Possible ways on increasing accuracy could be to do more bagging to increase sample accuracy. However, as seen from random forest accuracy result compared to decision tree result, there isn't a significant increase in accuracy. This may probably mean that the variables do not  fully explain the dependent variable or it may be due to the sampe size that we have.

---
**NOTE**
Attribute Values:

   buying:       v-high, high, med, low\
   maint :       v-high, high, med, low\
   doors   :     2, 3, 4, 5-more\
   persons  :    2, 4, more\
   lug_boot  :   small, med, big\
   safety    :   low, med, high
   
---
