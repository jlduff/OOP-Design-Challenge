class House: 
    has_basement = False
    has_garage = False 

    def __init__(self, squarefootage:int, flooring):
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

    def __init__(self, lamp, closet, rug:str):
        self.lamp = lamp
        self.closet = closet
        self.rug = rug

    def add_lamp(self): 
        print("A lamp has been added to the bedroom.")

    def add_rug (self): 
        print("A rug has been added to the bedroom.")

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

test_bedroom = Bedroom("str", "sks", "rug")
print(test_bedroom.add_rug())

class LivingRoom(House): 
    has_couch = False 
    has_fireplace = False

    def __init__(self, television:str, coffee_table): 
        self.television = television
        self.coffee_table = coffee_table 
    
    def add_television(self): 
        print("You now have a television in your living room.")

    @classmethod 
    def update_has_couch(cls, has_couch): 
        cls.has_couch = has_couch
        if cls.has_couch == True: 
            print("This living room has a couch.")
        else: 
            print("This living room lacks a couch.")
    
    @classmethod 
    def update_has_fireplace(cls, has_fireplace):
        cls.has_fireplace = has_fireplace
        if cls.has_fireplace == True: 
            print("This living room has a fireplace.")
        else: 
            print("This living room lacks a fireplace.") 

test_LivingRoom = LivingRoom("str", "sks", "television")
print(test_bedroom.add_television())

class Kitchen(House): 
    has_cupboards = False 
    has_pantry = False 

    def __init__(self, utensils, fridge):
        self.utensils = utensils
        self.fridge = fridge 

