## Table of Contents
-[About the Section](#about-the-section)
-[Chart Design](#chart-design)
-[Chart Explanation](#chart-explanation)
-[Requirements](#requirements)

<!-- ABOUT THE SECTION -->
## About The Section
Section 4: Charts and APIs
Your team decided to design a dashboard to display the statistic of COVID19 cases. You are tasked to display one of the components of the dashboard which is to display a visualisation representation of number of COVID19 cases in Singapore over time.

Your team decided to use the public data from https://documenter.getpostman.com/view/10808728/SzS8rjbc#b07f97ba-24f4-4ebe-ad71-97fa35f3b683.

Display a graph to show the number cases in Singapore over time using the APIs from https://covid19api.com/.

<!-- Chart Design -->
## Chart Design
![Alt text](https://github.com/darrenCWJ/dataeng_test/blob/master/Section%204/Chart.png)


<!-- Chart Explanation -->
## Chart Explanation
Since the task is to create a chart to visualise data over time, its best to use a line chart which is the best to show the flow of data over time. For the display of the chart, there will be option to filter the data to show daily or culmulative difference in cases and death over whichever period theres data for. Following that, if the user wants to analyse the data used, theres a download button to get a csv of the data shown below.

## Requirements
[Streamlit](https://streamlit.io/) will be needed to run this code. The bat file will have a pip install command to install streamlit.
