import sys
import pytest
# setting path
sys.path.append('./src/')

from antennapnf import AntennaPNF

def test_seperationDistance():
    frequency = 10E9
    coeff = 10

    print()
    assert round(AntennaPNF.seperationDistance(frequency, coeff),3) == pytest.approx(0.3)
    print(f"- Seperation distance at {frequency/1E6}MHz is {AntennaPNF.seperationDistance(frequency,coeff):.3f} meters with coefficient={coeff}")


def test_minSeperationDistance():
    frequency = 3E9

    print()
    assert round(AntennaPNF.minSeperationDistance(frequency),3) == pytest.approx(0.5)
    print(f"- Minimum seperation distance at {frequency/1E6}MHz is {AntennaPNF.minSeperationDistance(frequency):.3f} meters")
    assert round(AntennaPNF.minSeperationDistance(frequency, True),3) == pytest.approx(0.3)
    print(f"- Minimum seperation distance at {frequency/1E6}MHz is {AntennaPNF.minSeperationDistance(frequency, True):.3f} meters (3 lambda crtieria)")


def test_angleOfView():
    a = 0.15
    d = 0.05
    L = 1.00

    result = 83.290

    print()
    assert round(AntennaPNF.angleOfView(a,d,L),3) == pytest.approx(result)
    print(f"- Angle of view (d={a}, d={d}, L={L}) is {AntennaPNF.angleOfView(a,d,L):.3f}")

def test_samplingSpacing():
    freq = 5E9

    result = 0.030

    print()
    assert round(AntennaPNF.samplingSpacing(freq),3) == pytest.approx(result)
    print(f"- Sampling spacing (frequency={freq/1e6}MHz) is {AntennaPNF.samplingSpacing(freq):.3f}")

def test_scanLength():
    a = 0.15
    d = 0.05
    theta = 83.290

    result = 1.000

    print()
    assert round(AntennaPNF.scanLength(a,d,theta),3) == pytest.approx(result)
    print(f"- Scan length (d={a}, d={d}, theta={theta}) is {AntennaPNF.scanLength(a,d,theta):.3f}")


