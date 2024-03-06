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

  def hasScenario(self) -> bool: return bool(self.scenario and self.scenario is not None)