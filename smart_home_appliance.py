class Appliance:
          def status(self):
                 print("General appliance is working")

class Fan(Appliance):
          def status(self):
                 print("Fan is running")

class Light(Appliance):
          def status(self):
                  print("Light is on")

class AC(Appliance):
        def status(self):
                print("AC is cooling")

device=[Fan(),Light(),AC()]
for device in device:
      device.status()

