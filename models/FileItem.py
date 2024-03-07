import os
from src.Model import Model

class FileItem (Model):
  name: str = ''
  url: str = ''
  ext: str = ''
  filepath: str = ''
  downloaded: bool = False
  processed: bool = False
  scenario: None

  def needDownload(self) -> bool: return not self.downloaded

  def hasScenario(self) -> bool: return self.scenario and self.scenario is not None

  def hasHtml(self) -> bool: return os.path.exists(self.filepath) and os.stat(self.filepath).st_size > 0

  def getHtml(self) -> str:
    with open(self.filepath, 'r+') as f:
      content = f.read()
      f.close()
      return content