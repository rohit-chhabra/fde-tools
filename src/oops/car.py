class Car:
    
    def __init__(self):
        self.top_speed = 300
        self.warnings = []


    def drive(self):
        print("I am driving but not faster than {}".format(self.top_speed))

    def __repr__(self):
        return 'Top speed: {}. Warnings {}'.format(self.top_speed, self.warnings)

car1 = Car()
car1.drive()

car1.warnings.append('New warning on car 1')

car1.warnings = list(car1.warnings)
car1.warnings.append('Newer warning on car 1')



print(car1)

car1.top_speed += 500
print(car1.__dict__)

car2 = Car()
car2.drive()
print(car2.__dict__)

car3 = Car()
car3.drive()

print(car3.__dict__)


Car.top_speed = 400

car1.top_speeds = None

car1.drive()
car2.drive()
car3.drive()
