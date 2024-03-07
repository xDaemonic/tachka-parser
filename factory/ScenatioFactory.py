import sys, importlib

class ScenarioFactory():
  staticmethod
  def make(scenario, html):
    module = f"scenario.{scenario}"
    module =importlib.import_module(module, scenario) if module not in sys.modules else sys.modules[module]
    scenario_class = getattr(module, scenario)
    return scenario_class(html)