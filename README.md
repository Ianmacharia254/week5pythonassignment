# week5pythonassignment
Explanation
Attributes:

Smartphone has basic attributes like brand, model, storage, and battery_capacity.
SmartphoneWithCamera adds a camera_quality attribute to capture the camera specs (e.g., 48 MP).
Methods:

Common methods such as power_on(), power_off(), and check_battery() are part of the base Smartphone class.
The use_app() method simulates using an app and drains the battery.
charge_phone() restores the battery to 100%.
SmartphoneWithCamera has specialized methods like take_photo() and record_video() that enhance the functionality of the smartphone.
Inheritance and Polymorphism:

SmartphoneWithCamera inherits from Smartphone, adding more functionality without changing the base behavior.
Polymorphism is demonstrated in the ability to create a general Smartphone object or a more specific SmartphoneWithCamera object, where both share common behavior but also have unique methods.
Encapsulation:

Internal attributes like battery_level are encapsulated within the class. The user interacts with public methods rather than accessing these variables directly.
