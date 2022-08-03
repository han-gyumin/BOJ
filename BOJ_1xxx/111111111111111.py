# your code here
#################################
class Phone:
  def __init__(self,brand,color,year):
    self.brand=brand
    self.color=color
    self.year=year

  
  def print_info(self):
    print(f'Brand: {self.brand}, Color: {self.color}, Released year:{self.year}')


  def simple_name_generator(self):
    print(f'Abbreviated name of this phone is {self.brand[0].upper()+self.color[0].upper()+self.year}')

    # Test your code here
p1=Phone('galaxy','red',2020)
p2=Phone('apple','blue',2021)
p3=Phone('galaxy','white',2022)
p4=Phone('apple','gray',2020)
p1.print_info()