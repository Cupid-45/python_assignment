class Appliance:
          def status(self):
                 print("General appliance is working")

class Fan(Appliance)
          def status(self):
                 print("Fan is running")

class Light(Appliance):
          def status(self):
                  print("Ac is cooling")

device=[Fan(),Light(),AC()]
for device in devices:
      device.status()

