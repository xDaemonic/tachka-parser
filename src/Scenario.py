import lxml, re
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod 
from models.LinkItem import LinkItem

class Scenario(ABC):
  _soup: BeautifulSoup
  
  _link_template: dict = {
    "name": "",
    "url": "",
    "ext": "html",
    "downloaded": False,
    "processed": False,
    "scenario": None,
    "filepath": ""
  }

  def __init__(self) -> None:
    pass
  
  @abstractmethod
  def run(self, object: object) -> list:
    pass

  def _formatLinkItem(self, link: LinkItem, scenario: str = None) -> dict:
    formatted = self._link_template.copy()
    formatted['name'] = re.sub(r"[\/]", '', link.getPath())
    formatted['url'] = link.getRoute()
    formatted['scenario'] = scenario
    
    return formatted
  
  def _initSoup(self, html):
    self._soup = BeautifulSoup(html, 'lxml')
