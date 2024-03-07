import inspect
from src.Bag import Bag

class BagFactory:
  staticmethod
  def make(data: list, cls) -> Bag:
    if inspect.isclass(cls):
      data = [cls(item) for item in data]

    return Bag(data)
