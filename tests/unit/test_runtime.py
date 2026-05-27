import unittest
from packages.utils import MetricCollector

class TestRuntime(unittest.TestCase):
    def test_metric_collection(self):
        collector = MetricCollector()
        collector.add_metric('metric-1', 10)
        self.assertEqual(collector.metrics['metric-1'], 10)