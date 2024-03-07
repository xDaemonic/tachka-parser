from src.Scenario import Scenario

from models.FileItem import FileItem
from models.LinkItem import LinkItem

from src.Plan import Plan
from src.FileScrapper import FileScraper

class GlobalCategoriesScenario(Scenario):
  def __init__(self) -> None:
    super().__init__()
    self._plan = Plan()
  
  def run(self, object: FileItem) -> list:
    if object.needDownload():
      scrapper = FileScraper()
      object.setAttribute('filepath', scrapper.download_file(object))
      object.setAttribute('downloaded', True)
      
    self._initSoup(object.getHtml())
    fresh = self._soup.find('ul', class_='more-items__list').find_all('a')
    links = [LinkItem({'path': item['href']}) for item in fresh]
    formatted = list(map(lambda item: self._formatLinkItem(item, 'CategoryBrandScenario'), links))
  
    if len(formatted) > 0:
      self._plan.addList(formatted)
      
    object.setAttribute('processed', True)
      
    self._plan.updateFileItem(object)