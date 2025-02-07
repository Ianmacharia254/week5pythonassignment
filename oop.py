class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_capacity = battery_capacity
        self.battery_level = 100  # Initially, battery is full

    def power_on(self):
        print(f"{self.brand} {self.model} is now powered on.")
    
    def power_off(self):
        print(f"{self.brand} {self.model} is now powered off.")
    
    def check_battery(self):
        print(f"Battery level: {self.battery_level}%")
    
    def use_app(self, app_name, usage_time):
        battery_drain = usage_time * 0.5  # Assume each minute of app use drains 0.5% battery
        self.battery_level -= battery_drain
        self.battery_level = max(self.battery_level, 0)  # Battery cannot go below 0%
        print(f"Used {app_name} for {usage_time} minutes. Battery is now at {self.battery_level}%.")

    def charge_phone(self):
        self.battery_level = 100
        print(f"{self.brand} {self.model} is now fully charged.")


class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, camera_quality):
        # Call the constructor of the parent class
        super().__init__(brand, model, storage, battery_capacity)
        self.camera_quality = camera_quality  # In Megapixels

    def take_photo(self):
        print(f"Taking a photo with the {self.camera_quality} MP camera on {self.brand} {self.model}.")
    
    def record_video(self):
        print(f"Recording video with the {self.camera_quality} MP camera on {self.brand} {self.model}.")


# Creating a basic smartphone object
phone1 = Smartphone("BrandX", "ModelY", 128, 4000)
phone1.power_on()
phone1.use_app("Twitter", 30)
phone1.check_battery()
phone1.charge_phone()

print("\n")

# Creating a smartphone with a camera object
phone2 = SmartphoneWithCamera("BrandA", "ModelZ", 256, 5000, 48)
phone2.power_on()
phone2.use_app("Instagram", 20)
phone2.take_photo()
phone2.record_video()
phone2.check_battery()
phone2.charge_phone()
