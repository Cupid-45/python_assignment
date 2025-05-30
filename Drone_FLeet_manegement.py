class Device:
       def __init__(self,id):
              self.id=id

class Flyer:
       def fly(self):
              print("FLying.....")

class Drone(Device,Flyer):
       def __init__(self,id):
              Device.__init__(self,id)
                      
       def capture_image(self):
              print("Capturing image....")

d=Drone("g545")
print("Device id: ",d,id)
d.fly()
d.capture_image()



