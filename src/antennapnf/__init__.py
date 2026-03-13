from math import atan2, degrees, tan, radians

C0 = 299792458  # m/s


class Utility:

    @staticmethod
    def frequencyToWavelength(freq: float) -> float:
        return C0 / freq


class AntennaPNF:

    @staticmethod
    def seperationDistance(frequency: float, coeff: float) -> float:
        r"""Seperation distance in terms of vavelength multiples for near-field antenna measurements in meters

        
        Parameters
        ----------
        coeff : float 
            multiplication coefficient 
        frequency : float
            frequency of interest in Hertz [Hz]

        Returns
        -------
        float
            seperation distance in meters [m]

        Formula
        -------
        .. math::
            R_{nf} = k\times\lambda = k\times c_0/f
        """
        return coeff*Utility.frequencyToWavelength(frequency)


    @staticmethod
    def minSeperationDistance(frequency: float, three_lambda: bool = False) -> float:
        r""" Minimum recommended seperation distance between antenna and probe for near-field antenna measurements

        Parameters
        ----------
        frequency : float
            frequency of interest in Hertz [Hz]

        closer : bool
            use 3 lambda criteria as minimum, defaults to False

        Returns
        -------
        float
            seperation distance in meters [m]

        Notes
        -----
        Standard suggests to choose between 3 or 5 wavelength.
        In order to ensure copuling effect, 5 wavelength distance is choosen and implemented. 3 wavelength is optional.

        References
        ----------
        .. [1] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.3.1.4, Page 27.

        Formula
        -------
        .. math::
            R_{nf} = 5\times\lambda = 5\times c_0/f
        """
        return 3*Utility.frequencyToWavelength(frequency) if three_lambda else 5*Utility.frequencyToWavelength(frequency)
    

    @staticmethod
    def angleOfView(a: float, d: float, L: float) -> float:
        r""" Reliable far-field angle-of-view in planar near-field antenna measurements

        Parameters
        ----------
        a : float
            antenna cross-section length [m]
        d : float
            seperation distance between antenna and probe [m]
        L : float
            scan length of region [m]

        Notes
        -----
        Calculation assumes a scanning region centered on the AUT.  

        References
        ----------
        .. [1] IEEE 149-2021 Recommended Practice for Antenna Measurements, Section 12.5, Page 135, Equation 99.
        .. [2] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.3.1.6, Page 28, Equation 27.

        Formula
        -------
        .. math::
            theta = \atan^{-1} \left \dfrac{L-a}{2d} \right
        """
        return degrees(atan2(L-a, 2*d))
    
    @staticmethod
    def samplingSpacing(frequency: float):
        r""" Maximum sampling length for near-field antenna measurements

        Parameters
        ----------
        frequency : float
            frequency of interest in Hertz [Hz]

        References
        -----
        .. [1] IEEE 149-2021 Recommended Practice for Antenna Measurements, Section 12.5, Page 135.
        .. [2] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.2.5, Page 23, Equation 25.

        Formula
        -------
        .. math::
            \Delta = \lambda / 2 = 0.5 \times (c_0 / f)
        """
        return 0.5*Utility.frequencyToWavelength(frequency)
    
    @staticmethod
    def scanLength(a: float, d: float, theta:float):
        r""" Required length of the scan for desired angle-of-view in planar near-field antenna measurements

        Parameters
        ----------
        a     : float
                antenna cross-section length [m]
        d     : float
                seperation distance between antenna and probe [m]
        theta : float
                desired pattern view angle along one side [deg]

        Notes
        -----
        Calculation assumes a scanning region centered on the AUT.
        Input distances are unitless so output is the same quantity of inputs.

        References
        ----------
        .. [1] IEEE 149-2021 Recommended Practice for Antenna Measurements, Section 12.5, Page 135, Equation 99.
        .. [2] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.3.1.6, Page 28, Equation 27.

        Formula
        -------
        .. math::
            L = 2d \cdot \tan\theta + a
        """
        
        return 2*d*tan(radians(theta))+a

