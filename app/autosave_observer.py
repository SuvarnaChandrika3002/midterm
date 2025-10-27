import pandas as pd
from app.observer import Observer
from app.calculator_config import HISTORY_CSV
from app.history import History

class AutoSaveObserver(Observer):
    def __init__(self, history: History):
        self.history = history

    def update(self, _):  
        df = self.history.to_dataframe()
        df.to_csv(HISTORY_CSV, index=False)