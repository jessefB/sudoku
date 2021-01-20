class Coordinate:
   def __init__(self, x, y):
      self.x = x
      self.y = y
      return None
   def build(self, x, y):
      self.__init__(self, x, y)
      return self