# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

# class parent
class device:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

  def device_info(self):
    return f"{self.brand} {self.model}"

# d = device('samsung','Galaxy S20')
# print(d.device_info())

# class child1
class smartPhone(device):
  def __init__(self,brand,model,sim_cards,fingerprint_unlock,camera_megapixels):
    super().__init__(brand,model)
    self.sim_cards = sim_cards
    self.fingerprint_unlock = fingerprint_unlock
    self.camera_megapixels = camera_megapixels

  def calling(self,number,sim_slot = 2):
    if self.sim_cards > sim_slot or sim_slot < 1:
      return f"Invalid SIM slot, this phone supports {self.sim_cards} SIM card(s)."
    else:
      return f"Calling {number} using SIM{sim_slot} on {self.brand} {self.model}" 
    
  def unlock(self):
    if self.fingerprint_unlock:
      return f"{self.brand} {self.model} unlocked with fingerprint"
    else:
      return f"{self.brand} {self.model} unlocked with passcode"
    
  def taking_photos(self):
    return f"Taking a photo with {self.camera_megapixels}MP camera!"  

s = smartPhone('Samsung','Galaxy S25',1, True, 200)
print(s.calling(+25471234567))
print(s.unlock())
print(s.taking_photos())

# class child2
class tablet(device):
  def __init__(self, brand, model, screen_size):
    super().__init__(brand, model)
    self.screen_size = screen_size

  def multi_window_mode(self):
    if self.screen_size >= 576:
      return f"Split screen enabled on {self.brand} {self.model}"
    else:
      return f"screen too small for splitting"
    
t = tablet('Apple','iPad mini',320)
t = tablet('Apple','iPad mini',768)
print(t.multi_window_mode())    

# child 3 
class laptop(device):
  def __init__(self, brand, model,keyboard_backlight, ram_size,gpu_model):
    super().__init__(brand, model)
    self.keyboard_backlight = keyboard_backlight
    self.ram_size = ram_size
    self.gpu_model = gpu_model

  def compile_code(self):
    return f"Compiling code on {self.brand} {self.model} with {self.ram_size}GB RAM" 

  def play_game(self):
    ram_number = self.ram_size
    ideal_gpus = ["RTX 4070", "RTX 4080", "RTX 4090", "RX 7600", "RX 7700", "RX 7900"]
    gpu_ok = any(gpu in self.gpu_model.upper() for gpu in ideal_gpus)

    if ram_number >= 16 and gpu_ok:
      return f"{self.brand} {self.model} with {self.ram_size}GB RAM and {self.gpu_model} is game ready"
    else:
      return f"{self.brand} {self.model} with {self.ram_size}GB RAM and {self.gpu_model} is NOT game ready"

l = laptop('HP','SPECTRE 360', True, 16,'UHD 620' )
print(l.compile_code())
print(l.play_game())
l1 = laptop('HP','PAVILLION', True, 32,'RX 7600' )
print(l1.compile_code())
print(l1.play_game())


# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, 
# Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Animals:
  def sound(self):
    raise NotImplementedError("subclass must implement this method")
  
class dog(Animals):
  def sound(self):
    return f"dog says Woof!"
  
d = dog()
print(d.sound())  

class cat(Animals):
  def sound(self):
    return f"cat says MEOW!"
  
c = cat()
print(c.sound())

class cow(Animals):
  def sound(self):
    return f"cow says MOO!"
  
C = cow()
print(C.sound())