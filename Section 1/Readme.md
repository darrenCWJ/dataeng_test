## Table of Contents
-[About the Section](#about-the-section)
-[Thought Processes on codes](#thought-process-on-codes)
-[AutoRun Commands](#autorun-commands)


<!-- ABOUT THE SECTION -->
## About The Section
Section 1: Data Pipelines

The objective of this section is to design and implement a solution to process a data file on a regular interval (e.g. daily). Assume that there are 2 data files dataset1.csv and dataset2.csv, design a solution to process these files, along with the scheduling component. The expected output of the processing task is a CSV file including a header containing the field names.

You can use common scheduling solutions such as cron or airflow to implement the scheduling component. You may assume that the data file will be available at 1am everyday. Please provide documentation (a markdown file will help) to explain your solution.

Processing tasks:

Split the name field into first_name, and last_name
Remove any zeros prepended to the price field
Delete any rows which do not have a name
Create a new field named above_100, which is true if the price is strictly greater than 100
Note: please submit the processed dataset too.

<!-- Thought Processes on codes -->
## Thought Process on Codes
Dataset 1 and Dataset 2 comes with errors in their names and price fields.

First we can just drop the names that are blank as long as it is missing as the data is just keyed wrongly resulting in incomplete data.

The next step of the cleaning process will be their name.
There are 4 different scenarios that the name field can fall into
First, is the normal name which contains just 2 parts which can be split properly into the firstname and lastname category.
Secondly, theres names that have a prefix and a suffix. This means that the code will need to identify those names that contains both a prefix and a suffix and remove it accordingly by just removing the front most and back most part of the name
The third and fourth groups contains names that have either a prefix or a suffix. Therefore the code will need to correctly identify which one is prefix and which one is suffix and properly remove it.
For Names with prefix, it can be easily identtified with a '.' in the name field apart from 'Miss' therefore the code will need to search the Prefix based on this 2 categories and drop it.
For Names with suffix, after dropping the prefix, it will be the only name left with 3 parts to it therefore it could be very easily drop off at the end.

For the price field,
Due to the wrongly keyed data, the names moved into this field will affect the price column. Since the codes already drop incomplete data, those wrongly keyed data will be dropped automatically.
After which to ensure that the price field is clean, we remove any letters and leading 0s from the dataset by using the replace function.

Once data is clean, we can combine them together to form a single dataframe
Lastly, to get the price that is more than 100, we can easily find it by converting the cleaned price to float variable and take those that are more than 100.

## Autorun commands
To schedule cron job, simply run the sh file on linux, that is set as 0 1 * * * which translate to 1am to run the python file. Also the command will check if python is installed first to make sure it contains the software needed to run the script.

For Windows, running the bat file will open CLI and setup the task schedule to run the python file at 1am using the command daily 1am
