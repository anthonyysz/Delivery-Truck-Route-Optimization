#Student ID: 011239490
#Name: Anthony Szabo

import csv  #CSV for package data
from hashtable import HashTable 
from package import Package #Bringing in our hashtable, truck, and package classes
from truck import Truck
from datetime import datetime   #Datetime for all of our datetime telling needs
#Necessary imports for our main function


def packagelist_remover(list1, list2):  #Will be used later to indicate that a package has been assigned a truck
    for each in list1:
        if each in list2:
            list1.remove(each)
    return list1

def load_distance_file(file):   #Used only to load the distance table
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        header = next(reader)
        rows = []
        for each in reader:
            rows.append(each)
        return [header, rows]

distancefile = 'distancetable.csv'  #Our CSV files
packagefile = 'packagetable.csv'
distancetable = load_distance_file(distancefile)    #Loading the distance table

packagelist = list(range(1, 41))    #A list of all packages 1 through 40, and packages that need to be on certain trucks because of time constraints placed there
truck1needs = [14, 15, 16, 34, 29, 20, 1, 13]
truck2needs = [31, 6, 40, 25, 30, 37, 3, 18, 36, 38]
truck3needs = [9, 28, 32]

packagelist = packagelist_remover(packagelist, truck1needs) #Removing the 'needs' from the package list (they have been assigned to trucks)
packagelist = packagelist_remover(packagelist, truck2needs)
packagelist = packagelist_remover(packagelist, truck3needs)     

def load_package_data(file):    #Loading our package table
    hashtable = HashTable()
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        next(reader)
        for each in reader:
            idnum = int(each[0])
            address = each[1]
            city = each[2]
            state = each[3]
            zipcode = each[4]
            deadline = each[5]
            weight = int(each[6])
            notes = each[7]
            
            package = Package(idnum, address, city, state, zipcode, deadline, weight, notes)
            hashtable.insert(idnum, package)    #Putting the package data into a hash table
    return hashtable
           
def find_nearest_package(current, ht):  
    best = 100  #100 would be further than any packages, so we start here
    k = 0   #there is no package with id 0, so we start here
    for each in range(1, 40):
        i = ht.return_package(each)
        if i.truck == None:
            for row in distancetable[1]:
                if row[0] == current:
                    distance = float(row[distancetable[0].index(i.address)+1]) #Getting the distance to the next package
                    if distance < best:  #Finding the nearest delivery to the current address
                        best = distance  #If we have a new best, make it best
                        k = ht.return_package(each).idnum   #Assign the best's id to k
    return k  

def load_needs(ht, truck, needs):   #Loading the needed packages directly from a list
    for each in needs:
        truck.add(ht.return_package(each))

def load_truck(ht, truck):  #Loading a truck, up 16 packages
    while len(truck.packages) < 16:
        address = ht.lookup(truck.packages[-1])[1]
        next = find_nearest_package(address, ht)    #Finding the nearest package to the current address
        if next != 0:   #If find nearest package returns 0, that means that all the packages were assigned to a truck
            truck.add(ht.return_package(next))
        else:
            break   #If there are no available packages, we break the loop
  
def deliver_packages(ht, truck):
    for package in truck.packages: #Setting our packages that are being delivered to en route
        ht.return_package(package).status = 'En Route'
    for each in truck.packages: 
        next_address = ht.lookup(each)[1]   #Getting the address of the next package
        for row in distancetable[1]:
            if row[0] == truck.address:
                distance = float(row[distancetable[0].index(next_address)+1]) #Getting the distance to the next package
        truck.packages_deliver(ht, each, distance)  #Delivering each package, adding the distance that will be needed to travel the truck
        truck.address = next_address    #Setting the trucks address to the next_address variable
        
def get_all_status_at_time(trucks, time, ht):   #This function is majorly used to get what we need for our menu
    status_at_time = [] #Starting this with a list makes things much easier when returning all package data
    for truck in trucks:
        for package in truck.packages:  #For each package in each truck
            package_item = ht.return_package(package)
            if package_item.delivery_time <= time:  #If the delivery time is less than the time inputted, then the package has already been delivered
                status = "Delivered"
                deliverytime = package_item.delivery_time
            elif package_item.delivery_time > time and truck.departure_time <= time:    #If the delivery time is less by the departure time is more, then the package is 'en route'
                status = "En Route"
                deliverytime = 'Not yet Delivered'
            else:   #Otherwise, the package as yet to leave the HUB
                status = "At Hub"
                deliverytime = 'Not yet Delivered'
            status_at_time.append({
                'package_id': package_item.idnum,
                'truck': package_item.truck,
                'address': package_item.address,
                'deadline': package_item.deadline,
                'city': package_item.city,
                'zipcode': package_item.zipcode,
                'weight': package_item.weight,
                'status': status,
                'delivery_time': deliverytime
            })
    return status_at_time
    
     


def main():
    Truck1 = Truck(1, '8:00 AM')    #Initializing our three trucks with proper departure times to reflect the special notes
    Truck2 = Truck(2, '9:05 AM')
    Truck3 = Truck(3, '10:20 AM')
    trucks = [Truck1, Truck2, Truck3]
    hashtable = load_package_data(packagefile)  #Loading our package information into a hash table

    load_needs(hashtable, Truck1, truck1needs)  #Getting our needs in their proper trucks
    load_needs(hashtable, Truck2, truck2needs)
    load_needs(hashtable, Truck3, truck3needs)
    
    for truck in trucks:    #Loading each of our trucks
        load_truck(hashtable, truck)
     
    for truck in trucks:    #Delivering all of our packages
        deliver_packages(hashtable, truck)

    while True:
        print("Menu")
        print("1: Check Package Status")
        print("2: Show all Packages Status")
        print("3: Check Truck Mileage")
        print("4: See a truck's information")
        print("5: Exit")
        selection = input("Enter the number of your selection: ")
        print("\n")
        
        if selection == "1":
            id = int(input("Enter Package ID: "))       #We need a certain package
            timetext = input("Enter time of day in HH:DD AM/PM: ")  #And a certain time
            try:    #This will try to print our information
                time = datetime.strptime(timetext, '%I:%M %p')  #Getting the inputted time into the right object type
                statuses = get_all_status_at_time(trucks, time, hashtable)  #Using this function because I had written it first
                status = None
                for each in statuses:
                    if each['package_id'] == id:
                        status = each   #Picking out the status of the package that we need
                if status['package_id'] == 9 and time <= datetime.strptime('10:20 AM', '%I:%M %p'):
                    status['address'] = "300 State St"
                    status['zipcode'] = 84103
                if status:
                    print(f"Package ID: {status['package_id']}, Truck: {status['truck']}, Address: {status['address']}")#And printing out all of the information about that package
                    print(f"Deadline: {status['deadline']}, City: {status['city']}, Zip Code: {status['zipcode']}, Weight: {status['weight']}")
                    print(f"Status: {status['status']}, Delivery Time: {status['delivery_time']}")
                else:
                    print("Package ID not found. Please try again.")    #And if there is an error with the package id, there will be an error that says so
            except:
                print('Incorrect time entered. Please check the format and try again.') #Also, if there is an error with the time that is inputted, we will say so
            print("---------------------------------------------------------------")    #For easier visibility
            print("\n")
            print("\n")
                
        elif selection == "2":
            timetext = input("Enter time of day in HH:MM AM/PM format: ")   #Using the same time getting, error throwing format as last time
            try:
                time = datetime.strptime(timetext, '%I:%M %p')
                statuses = get_all_status_at_time(trucks, time, hashtable)
                for each in statuses:   #Except this time, we will be printing out every package
                    if each['package_id'] == 9 and time <= datetime.strptime('10:20 AM', '%I:%M %p'):
                        status['address'] = "300 State St"
                        status['zipcode'] = 84103
                    print(f"Package ID: {each['package_id']}, Status: {each['status']}, Delivery Time: {each['delivery_time']}")
                    
            except:
                print('Incorrect time. Please check the format and try again.')  
            print("---------------------------------------------------------------")
            print("\n")
            print("\n")
                
        elif selection == "3":
            total_miles = 0
            for each in trucks:
                total_miles += each.total_miles_traveled    #Adding the miles of all the trucks
            print(f"Total Miles Traveled: {total_miles} miles.")
            print("---------------------------------------------------------------")
            print("\n")
            print("\n")
            
        elif selection == "4":
            truckint = int(input('Please enter which truck you would like to see (1, 2 or 3): '))   #Taking an input of one of the trucks
            if truckint in [1, 2, 3]:
                truckinput = [trucks[truckint - 1]] #Callin that truck into a list item
                timetext = input("Enter time of day in HH:MM AM/PM format: ")   #Same time getting format
                try:
                    time = datetime.strptime(timetext, '%I:%M %p')
                    statuses = get_all_status_at_time(truckinput, time, hashtable)      #Passing the one truck into the get all status function, so we only return the info from that one truck
                    for each in statuses:
                        if each['package_id'] == 9 and time <= datetime.strptime('10:20 AM', '%I:%M %p'):
                            each['address'] = "300 State St"
                            each['zipcode'] = 84103
                        print(f"Package ID: {each['package_id']}, Status: {each['status']}, Delivery Time: {each['delivery_time']}")
                except:
                    print('Incorrect time. Please check the format and try again.')     #Same
            else:
                print("Please enter a proper truck number (1, 2, or 3).")   #Same
            print("---------------------------------------------------------------")
            print("\n")
            print("\n")
                
        elif selection == "5":  #Ending the session
            break
        
        else:
            print("Invalid Choice, please enter a number 1 through 5.") #Throwing an error if someone doesn't put in one of the right numbers
            print("---------------------------------------------------------------")
            print("\n") 
            print("\n")
            
            
      
if __name__ == "__main__":
    main() 