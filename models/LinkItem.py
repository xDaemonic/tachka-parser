from src.Model import Model

class LinkItem(Model):
  __core: str = 'https://tachka.ru'
  __path: str = ''
  scenario: str
  
  def __init__(self, attributes: dict):
    if 'path' not in attributes and 'href' not in attributes:
      raise Exception('path or href attribute is required')
    
    self.__path = attributes['path'] if 'path' in attributes else attributes['href']
    super().__init__(attributes)
    
  def getRoute(self) -> str:
    return f"{self.__core}{self.__path}"
  
  def getPath(self) -> str:
    return self.__path