class GrumpyDict(dict):
  def __repr__(self):
    print("NONE OF YOUR BUSINESS")
    return super().__repr__()

data = GrumpyDict({"first" : "Tom","animal" : "cat"})

print(data)