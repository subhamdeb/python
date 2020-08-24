class GrumpyDict(dict):
  def __repr__(self):
    print("NONE OF YOUR BUSINESS")
    return super().__repr__()
  def __missing__(self,key):
    print(f"ypun want {key}? well it aint here!")
  def __setitem__(self,key,value):
    super().__setitem__(key,value)



data = GrumpyDict({"first" : "Tom","animal" : "cat"})

print(data)

data["animal"] = "Dog"
print(data)


data2 = dict({"name" : "Subham"})
print(data2)