import json
from typing_extensions import Self

class Bag:
  __items: list

  def __init__(self, items: list = []) -> None:
    self.__items = items

  def getItems(self) -> list:
    return self.__items

  def isEmpty(self) -> bool:
    return not len(self.__items) > 0
  
  def isNotEmpty(self) -> bool:
    return not self.isEmpty()
  
  def map(self, fn: callable) -> Self:
    self.__items = list(map(lambda item: fn(item), self.__items))
    return self
  
  def filter(self, fn: callable) -> Self:
    self.__items = list(filter(lambda item: fn(item), self.__items))
    return self