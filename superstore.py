class House: 
    has_basement = False
    has_garage = False 

    def __init__ (self, squarefootage:int, flooring):
        self.squarefootage = squarefootage 
        self.flooring = flooring
    
    @classmethod 
    def update_has_basement(cls, has_basement):
        cls.has_basement = has_basement 
        if cls.has_basement == True: 
            print("This house has a basement.")
        else: 
            print("This house lacks a basement.")
    
    @classmethod 
    def update_has_garage(cls, has_garage): 
        cls.has_garage = has_garage 
        if cls.has_garage == True: 
            print("This house has a garage.")
        else: 
            print("This house lacks a garage.")

class Bedroom(House): 
    has_bed = False 
    has_dresser = False

    def __init__ (self, has_lamp: bool, has_closet: bool):
        self.has_lamp = has_lamp
        self.has_closet = has_closet
    
    @classmethod 
    def update_has_bed(cls, has_bed): 
        cls.has_bed = has_bed 
        if cls.has_bed == True: 
            print("This bedroom has a bed.")
        else: 
            print("This bedroom lacks a bed.")
    
    @classmethod 
    def update_has_dresser(cls, has_dresser): 
        cls.has_dresser = has_dresser 
        if cls.has_dresser == True: 
            print("This bedroom has a dresser.")
        else: 
            print("This bedroom lacks a dresser.")
    


test_bedroom = Bedroom 
print(test_bedroom.)

class LivingRoom(House): 
    has_couch = False 
    has_fireplace = False

    def __init__ (self, television, coffee_table): 
        self.television = television
        self.coffee_table = coffee_table 

