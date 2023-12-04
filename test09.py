from random import random

import pytest


@pytest.mark.flaky(reruns=6, reruns_delay=2)
def test_example(self):
    print(3)
    assert random.choice([True, False])

# pytest 09.py --reruns=3
