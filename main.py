#python  program assessment 


#I am starting requisition counter from 0


requisition_counter = 0
#This class is used to store requisition information 

class Requisition:
    # I USED  CONSTRUCTOR METHOD TO CREATE REQUISITION ATTRIBUTES
    def __init__(self):
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.requisition_id = 0
        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available "

# I used this method to add new requisition
    def add_requisition(self):
            global requisition_counter   # it is used for counter value to increase every time  a new requisition is created


            print("\nEnter you Information") # enter the staff information


            self.date = input("Date:   ")      #THIS TAKES DATE, ID, NAME OF STAFFF
            self.staff_id = input("Staff ID: ")
            self.staff_name = input("Staff Name: ")


            requisition_counter = requisition_counter +1 #I AM increasing counter by 1 every new requisition
            self.requisition_id = 10000 + requisition_counter # thsi help to create a unique requisition id
            print("Requisition ID:", self.requisition_id)

            print("Add items")
            choice = "yes" # here i am setting yes so the loop runs at least once 
              #this loop allows user to enter multiple items 
            while choice == "yes":
                item_name = input("Item name: ") # i am taking item name and price here
                price = int(input("Item Price ($):"))


                self.total = self.total + price 

                choice = input("Add another item ? (yes/no): ")

                print("Total: $", self.total)


# This method checks whether requisition can be approved automatically
    def approve_requisition(self):
                    #if total amount is less that 500 it will be approved
                    if self.total < 500:
                        self.status = "Approved"
                        last_three = str(self.requisition_id) [-3:] #Taking last 3 digits form requisition ID
                        self.approval_ref = self.staff_id + last_three # it combines staff if and last 3 digits  to create approval reference


                    else:
                        self.status = "Pending"
                        self.approval_ref = "Not available"
    

# this method display all the requisition details 
    def display_requisition(self):
          print("\n Requisition Details")
          print("Date:", self.date)
          print("Staff Id:", self.staff_id)
          print("Staff Name:", self.staff_name)
          print("Requisition ID:", self.requisition_id)
          print("Total: $", self.total)
          print("Status:", self.status)
          print("Approval Reference Number:", self.approval_ref)

#this method allows manager to respond to pending requisitions
    def respond_requisition(self):
          if self.status == "Pending":
                print("Manager response required for Requisition ID:", self.requisition_id," and Staff Name:", self.staff_name)
                print("1. Approved")
                print("2. Not Approved")
                print("3. Pending")

                choice = input("Enter manager choice: ") # this alows the manager  to choose options like approved , not approved or pending 

                if choice == "1":
                      self.status = "Approved"
                      last_three = str(self.requisition_id)[-3:]
                      self.approval_ref = self.staff_id + last_three


                elif choice =="2":
                      self.status = "Not Approved"
                      self.approval_ref = "Not available"



                elif choice == "3":
                      self.status = "Pending"


                else:
                      print("Invalid choice")
                    




#this function display requisition statistics
def requisition_statistics(requisitions):
      total = len(requisitions)

      approved = 0
      pending = 0
      not_approved = 0


      for req in requisitions:
            if req.status == "Approved":
                  approved +=1

            elif req.status == "Pending":
                  pending +=1


                

            elif req.status == "Not Approved":
                  not_approved +=1
                  

      print("\n Displaying the Requisition Statistics")
      print(" The Total Number of  Requistations Submitted:", total)
      print(" The Total Number of Approved Requistations  :", approved)
      print("The Total number of Pending Requistations :", pending)
      print("The Total Number of Not Approved Requistations :", not_approved)


      #main program

requisitions = []

request_number =1
choice = "yes"

#This loop allows user to create multiple requisitions

while choice == "yes":
      print("\nRequisitions", request_number)
      
      req = Requisition()
      req.add_requisition()
      req.approve_requisition()

# i am adding each requisition object into the requisition list
      requisitions.append(req)
      choice = input("Do you want to add another requisition? (yes/no):")
      request_number = request_number +1

print("\nRequisitions Information Before Manager Response")
for req in requisitions:
      req.display_requisition()

requisition_statistics(requisitions)

print("\nManager Response Section")
for req in requisitions:
      req.respond_requisition()

print("\n Updated Requisition Information After manager Response") # displaying upated information
for req in requisitions:
      req.display_requisition()
      

requisition_statistics(requisitions)
      

















    





        
    