
from datetime import datetime
from datetime import timedelta #datetime and timedelta will be necessary for finding information by time

class Truck:
    def __init__(self, id, departure_time):
        self.id = id
        self.packages = []
        self.driver = None
        self.address = 'HUB'
        self.total_miles_traveled = 0
        self.speed = 18
        self.max_space = 16
        self.departure_time = datetime.strptime(departure_time, '%I:%M %p') #This will stay constant, not changing ever
        self.time = datetime.strptime(departure_time, '%I:%M %p') #This will change when we want to see what a truck was doing at a certain time
        
    def add(self, package): #Adding a package, as long as truck isn't full
        if len(self.packages) < 16:
            self.packages.append(package.idnum)
            package.truck = self.id
        
    def packages_en_route(self, hashtable): #Setting the package to en route once it has left the HUB
        for each in self.packages:
            package = hashtable.return_package(each)
            package.status = "En Route"
            
    def travel(self, miles):    
        self.total_miles_traveled += miles #Here, we can increase the number of miles the truck has traveled based on the distances between 2 packages
        self.time += timedelta(hours = (miles/self.speed))  #Here we change the time of the truck, as is necessary for delivery times
            
    def packages_deliver(self, hashtable, package_id, miles_traveled):  
        package = hashtable.return_package(package_id)  #Getting the package item
        self.travel(miles_traveled) #Traveling from the current address to the next
        
        package.status = "Delivered"    #Setting the current package to 'delivered'
        package.delivery_time = self.time   #Setting the package delivery time to whatever time it is delivered at; see Truck.travel()
        package.truck = None    #Removing the package from the truck
        
    def to_hub(self, distance_to_hub):  #Sending the truck back to the hub
        self.travel(distance_to_hub)
        self.at_hub = True
          
