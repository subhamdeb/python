class Human:
  def __init__(self,first,last,age):
    self.first=first
    self.last = last
    self.age = age
  def __repr__(self):
    return f"Human name {self.first} {self.last}"
  def __len__(self):
    return self.age

j = Human("Jenny", "Larsen",47)

print(j)
print(len(j))