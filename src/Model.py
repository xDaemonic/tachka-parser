class Model:
  def __init__(
      self,
      attributes: dict
      ) -> None:
    

    print(attributes)
    for key, val in attributes.items():
      if key in self.__annotations__:
        self.setAttribute(key, val)
        
  def getAttibutes(self) -> list: return vars(self)

  def setAttribute(self, key, value) -> None: self.__setattr__(key, value)