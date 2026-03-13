import sys
import pytest
# setting path
sys.path.append('./src/')

from antennapnf import AntennaPNF

def test_minSeperationDistance():
    frequency = 3E9

    assert round(AntennaPNF.minSeperationDistance(frequency),3) == pytest.approx(0.3)
    print(f"- Minimum seperation distance at {frequency/1E6}MHz is {AntennaPNF.minSeperationDistance(frequency):.3f}")
    # assert print(AntennaPNF.minSeperationDistance(frequency))


