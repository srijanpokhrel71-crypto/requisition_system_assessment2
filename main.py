#python  program assessment 

requisition_counter = 0

class Requisition:
    def __init__(self):
        self.data = ""
        self.staff_id = ""
        self.staff_name = ""
        self.requisition_id = 0
        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available "

        