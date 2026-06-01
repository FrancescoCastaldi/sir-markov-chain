import sys
sys.path.insert(0, "../src")
import numpy as np
from model import next_state, transition_probs

def test_conservation():
    for _ in range(100):
        s, i = np.random.randint(1, 50), np.random.randint(1, 20)
        r = 100 - s - i
        sn, in_, rn = next_state(s, i, r)
        assert sn + in_ + rn == 100, "Violazione conservazione N"

def test_absorbing_state():
    s, i, r = 60, 0, 40
    sn, in_, rn = next_state(s, i, r)
    assert in_ == 0, "R non è assorbente"

def test_non_negative():
    for _ in range(100):
        s, i = np.random.randint(1, 50), np.random.randint(1, 20)
        r = 100 - s - i
        sn, in_, rn = next_state(s, i, r)
        assert sn >= 0 and in_ >= 0 and rn >= 0

if __name__ == "__main__":
    test_conservation()
    test_absorbing_state()
    test_non_negative()
    print("Tutti i test passati.")
