## Table of Contents
-[About the Section](#about-the-section)
-[Design Layout](#design-layout)
-[Explanation of Design](#explanation-of-design)
-[Assumptions](#assumptions)
<!-- ABOUT THE SECTION -->
## About The Section
Section 3: System Design
You are designing data infrastructure on the cloud for a company whose main business is in processing images.

The company has a web application which collects images uploaded by customers. The company also has a separate web application which provides a stream of images using a Kafka stream. The company’s software engineers have already some code written to process the images. The company would like to save processed images for a minimum of 7 days for archival purposes. Ideally, the company would also want to be able to have some Business Intelligence (BI) on key statistics including number and type of images processed, and by which customers.

Produce a system architecture diagram (e.g. Visio, Powerpoint) using any of the commercial cloud providers' ecosystem to explain your design. Please also indicate clearly if you have made any assumptions at any point.

<!-- Design Layout -->
# Design Layout
![Alt text](https://github.com/darrenCWJ/dataeng_test/blob/master/Section%203/Section%203_System%20Design.png)


<!-- Explanation of Design -->
# Explanation of Design
When Users connect to the application, the information will be screen through the DNS protection and firewall before allowing them to access the application. This process helps to prevent DDOS attack onto the server. As Users may have a wave of login at the same time, a load balancer will be used to diverse out the users such that the system will still be able to take in the information. In the application, users will be able to upload image to the cloud which will then enter a kafka stream which will process the images in the ML model. After image is process, it will be sent to an Amazon RDS system which will have store the key statistic and image. The Analyst will have access to the data stored in the RDS for analytical purposes.

<!-- Assumptions -->
# Assumptions
-Applications are hosted on AWS cloud

-Firewall is used for security check and DDOS protection and blacklist IP address of illegal users.

-The cloud is hosted on a single region: Singapore but if demand increases based on demand, might expand to other region to meet demands increase.

-Application load balance has auto scalling to meet demand of application. 

-Each Application has clearly defined ingress rules in its security groups

-For public facing application the ingress rules:
	- HTTP port 80 and HTTPS 443

-For private facing application the ingress rules:
	- The ingress rules allows for it to talk to each other only in the private subnet
