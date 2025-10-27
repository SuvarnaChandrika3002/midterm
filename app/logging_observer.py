from app.observer import Observer
from app.logger import log

class LoggingObserver(Observer):
    def update(self, calculation):
        log.info(
            f"{calculation.operation}: {calculation.a}, {calculation.b} = {calculation.result}"
        )




