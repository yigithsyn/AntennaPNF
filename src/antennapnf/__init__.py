# from . import AntennaPNF as AntennaPNF

C0 = 299792458  # m/s


class Utility:

    def freq2wlen(freq: float) -> float:
        return C0 / freq


class AntennaPNF:

    def __init__():
        pass

    def seperationDistance(coeff: float, frequency: float) -> float:
        r"""Seperation distance respect to wavelength coefficient for near-field antenna measurements in meters

        .. math::
        R_{nf} = k\times\lambda = k\times c_0/f

        :param float coeff: multiplication coefficient 
        :param float frequency: frequency of interest in Hertz [Hz]
        :return float: distance n meters [m]
        """
        return coeff * Utility.freq2wlen(frequency)



    def minSeperationDistance(frequency: float, three_lambda: bool = False) -> float:
        r"""Minimum recommended seperation distance between antena and probe aperture for near-field antenna measurements in meters

        .. math::R_{nf} = 5\times\lambda = 5\times c_0/f

        Standard suggests to choose between 3 or 5 wavelength.
        In order to ensure copuling effect, 5 wavelength distance is choosen and implemented. 3 wavelength is optional.

        .. [1] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.3.1.4, Page 27.

        :param float frequency: frequency of interest in Hertz [Hz]
        :param bool three_lambda: use 3 lambda criteria as minimum, defaults to False
        :return float: minimum distance in meters [m]
        """
        return 3*Utility.freq2wlen(frequency) if three_lambda else 3*Utility.freq2wlen(frequency)

