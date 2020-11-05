class car:
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
    
    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerate")
    
    def change_gear(self, gear_type):
        self.gear_type = gear_type
        print("gear changed", self.gear_type)


lexus = car("lexus", "black", "lexus", "2")

lexus.start()
lexus.change_gear("5")


