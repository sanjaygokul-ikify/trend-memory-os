class Metrics:
    def __init__(self):
        self.metrics = {}

    def add_metric(self, name: str, value: int) -> None:
        self.metrics[name] = value

    def get_metric(self, name: str) -> int:
        return self.metrics.get(name, 0)