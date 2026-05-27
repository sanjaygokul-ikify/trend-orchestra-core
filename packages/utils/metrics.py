class MetricCollector:
    def __init__(self):
        self.metrics = {}

    def add_metric(self, name, value):
        self.metrics[name] = value