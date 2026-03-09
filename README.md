# Delivery Truck Route Optimization

## 1. Introduction
&nbsp;&nbsp;&nbsp;&nbsp;For this WGU project, I was tasked with finding the optimal route to send 3 delivery truck on when delivering packages around the greater Salt Lake City area. There are 3 trucks and 2 drivers, and the combined total distance traveled for all 3 trucks must be below 140 miles. There was a list of assimptions provided to outline:
* Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
* The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
* There are no collisions.
* Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
* Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
* The delivery and loading times are instantaneous (i.e., no time passes while at a delivery or when moving packages to a truck at the hub). This time is factored into the calculation of the average speed of the trucks.
* There is up to one special note associated with a package.
* The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. The delivery service is aware that the address is incorrect and will be updated at 10:20 a.m. However, The service does not know the correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.
* The distances between locations are equal regardless of the direction traveled.
* The day ends when all 40 packages have been delivered.\

## 2. My Task
&nbsp;&nbsp;&nbsp;&nbsp;When developing my solution, I was given a few constraints on how I did it. I had to make a hash table with no additional libraries or classes that includes an insert function that takes the package ID as input and inserts the package's data into the hash table. I also needed to develop a look-up function that takes the package ID as input and returns all of the package's data.

&nbsp;&nbsp;&nbsp;&nbsp;In [the hashtable class](https://github.com/anthonyysz/Data-Structures-and-Algorithms-II/blob/main/code/hashtable.py), both of those are included. The necessary insert function was provided to me, so I edited it to support lookup as well. I also added a function that would return the package item if needed. 

## 3. My solution
&nbsp;&nbsp;&nbsp;&nbsp;In my [main.py](https://github.com/anthonyysz/Data-Structures-and-Algorithms-II/blob/main/code/main.py) file, my truck accurately loads the packages that need to be delivered the soonest onto the first two trucks, sorts those packages to optimize the route, then loads the rest of the packages. A few of the functions I added include one to see the status of a package at a certain time, a function to have the truck deliver the packages, and function to find the nearest package to another one so that the packages are loaded to the right trucks and delivered in the right order.

&nbsp;&nbsp;&nbsp;&nbsp;When my main function is run, a menu appears. The menu's options include Checking a package's status, showing the status of all packages, checking a truck's mileage, and seeing a truck's information. I provided a few [screenshots](https://github.com/anthonyysz/Delivery-Truck-Route-Optimization/tree/main/screenshots) to demonstrate my program in use. 

## 4. Looking forward
&nbsp;&nbsp;&nbsp;&nbsp;In the future, I'd like to be able to create a program that can sort the packages with special conditions without the need for a special addition step. I would have to transcribe those special requests into a 'deliver-by' column and have those packages sorted and delivered first. I would do something similar with the packages that needed to be on trucks 2 and 3. I did not do that for this project because I was instructed not to, as changing the dataset can affect the project's grading.
