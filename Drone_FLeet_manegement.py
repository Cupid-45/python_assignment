class Device:
         def __init__(self,id)
         self.id=id

class Flyer:
          def fly(self):
                 print("FLying.....")

class Drone(Device,flyer):
          def __init__(self,id)

          def capture_image(self):
                 print("Capturing image....")

d=drone
print("Device id: ",d,device_id)
d.fly()
d.capture_image()



