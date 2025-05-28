class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self .cuisine_type=cuisine_type
        self.number_served = 100
    def describe_restaurant(self):
        print("The name of my restaurant is "+ self.restaurant_name+". It is famous for its "+ self.cuisine_type )
    def open_restaurant(self):
        print("The " + self.restaurant_name + " is open!")
    def set_number_served(self,upd_number_served):
        self.number_served=upd_number_served
        print("A total of "+str(self.number_served)+" no of people have been served!")
    def increment_number_served(self,increm_no_of_cust):
        increm_no_of_cust+=self.number_served
        print("The latest incremented no of people served are: "+str(increm_no_of_cust))