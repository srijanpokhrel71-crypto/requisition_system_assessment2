#python  program assessment 

requisition_counter = 0

class Requisition:
    def __init__(self):
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.requisition_id = 0
        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available "


    def add_requisition(self):
            global requisition_counter


            print("\nEnter you Information")


            self.date = input("Date:   ")
            self.staff_id = input("Staff ID: ")
            self.staff_name = input("Staff Name: ")


            requisition_counter = requisition_counter +1
            self.requisition_id = 10000 + requisition_counter
            print("Requisition ID:", self.requisition_id)

            print("Add items")
            choice = "yes"

            while choice == "yes":
                item_name = input("Item name: ")
                price = int(input("Item Price ($):"))


                self.total = self.total + price 

                choice = input("Add another item ? (yes/no): ")

                print("Total: $", self.total)



    def approve_requisition(self):
                    if self.total < 500:
                        self.status = "Approved"
                        last_three = str(self.requisition_id) [-3:]
                        self.approval_ref = self.staff_id + last_three


                    else:
                        self.status = "Pending"
                        self.approval_ref = "Not available"







req = Requisition()
req.add_requisition()
req.approve_requisition()


print("Status:", req.status)
print("Approval Reference:" , req.approval_ref) 




    





        
    