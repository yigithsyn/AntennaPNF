from math import atan, degrees, radians, tan, floor, ceil

from ._utility import frequency_to_wavelength

__all__ = [
    "separation_distance",
    "min_separation_distance",
    "angle_of_view",
    "sampling_spacing",
    "scan_length",
]

def separation_distance(frequency: float, coeff: float) -> float:
    r"""Separation distance in terms of wavelength multiples for near-field antenna measurements in meters

    Parameters
    ----------
    frequency : float
        frequency of interest in Hertz [Hz]
    coeff : float
        multiplication coefficient

    Returns
    -------
    float
        separation distance in meters [m]

    Formula
    -------
    .. math::
        R_{nf} = k\times\lambda = k\times c_0/f
    """
    return coeff * frequency_to_wavelength(frequency)


def min_separation_distance(frequency: float, three_lambda: bool = False) -> float:
    r"""Minimum recommended separation distance between antenna and probe for near-field antenna measurements

    Parameters
    ----------
    frequency : float
        frequency of interest in Hertz [Hz]
    three_lambda : bool
        use 3 lambda criteria as minimum, defaults to False

    Returns
    -------
    float
        separation distance in meters [m]

    Notes
    -----
    Standard suggests to choose between 3 or 5 wavelengths.
    In order to ensure coupling effect, 5 wavelength distance is chosen and implemented.
    3 wavelength is optional.

    References
    ----------
    .. [1] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements,
            Section 5.3.1.4, Page 27.

    Formula
    -------
    .. math::
        R_{nf} = 5\times\lambda = 5\times c_0/f
    """
    return 3 * frequency_to_wavelength(frequency) if three_lambda else 5 * frequency_to_wavelength(frequency)


def angle_of_view(a: float, d: float, L: float) -> float:
    r"""Reliable far-field angle-of-view in planar near-field antenna measurements

    Parameters
    ----------
    a : float
        antenna cross-section length [m]
    d : float
        separation distance between antenna and probe [m]
    L : float
        scan length of region [m]

    Returns
    -------
    float
        angle of view in degrees [deg]

    Notes
    -----
    Calculation assumes a scanning region centered on the AUT.
    The scan length L must be greater than the antenna length a (i.e., L > a).

    References
    ----------
    .. [1] IEEE 149-2021 Recommended Practice for Antenna Measurements,
            Section 12.5, Page 135, Equation 99.
    .. [2] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements,
            Section 5.3.1.6, Page 28, Equation 27.

    Formula
    -------
    .. math::
        \theta = \arctan\left(\dfrac{L - a}{2d}\right)
    """
    if L <= a:
        raise ValueError(f"Scan length L ({L}) must be greater than antenna length a ({a}).")
    return degrees(atan((L - a) / (2 * d)))


def sampling_spacing(frequency: float) -> float:
    r"""Maximum sampling spacing for near-field antenna measurements

    Parameters
    ----------
    frequency : float
        frequency of interest in Hertz [Hz]

    Returns
    -------
    float
        sampling spacing in meters [m]

    References
    ----------
    .. [1] IEEE 149-2021 Recommended Practice for Antenna Measurements,
            Section 12.5, Page 135.
    .. [2] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements,
            Section 5.2.5, Page 23, Equation 25.

    Formula
    -------
    .. math::
        \Delta = \lambda / 2 = 0.5 \times (c_0 / f)
    """
    return 0.5 * frequency_to_wavelength(frequency)


def scan_length(a: float, d: float, theta: float) -> float:
    r"""Required length of the scan for desired angle-of-view in planar near-field antenna measurements

    Parameters
    ----------
    a : float
        antenna cross-section length [m]
    d : float
        separation distance between antenna and probe [m]
    theta : float
        desired pattern view angle along one side [deg]

    Returns
    -------
    float
        required scan length in the same unit as inputs [m]

    Notes
    -----
    Calculation assumes a scanning region centered on the AUT.
    Input distances and output are in the same physical unit.

    References
    ----------
    .. [1] IEEE 149-2021 Recommended Practice for Antenna Measurements,
            Section 12.5, Page 135, Equation 99.
    .. [2] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements,
            Section 5.3.1.6, Page 28, Equation 27.

    Formula
    -------
    .. math::
        L = 2d \cdot \tan\theta + a
    """
    return 2 * d * tan(radians(theta)) + a


def sampling_parameters_for_length(frequency: float, L: float) -> tuple:
    r""" Planar near-field antenna measurement sampling count according to frequency and desired minimum length
    
    Parameters
    ----------
    frequency : float
                frequency of interest in Hertz [Hz]
    L         : float
                desired minimum scan length [m]

    Returns
    -------
    Lm    : float
            sampling start position [m]
    Lp    : float
            sampling stop position [m] (equals to negative of Lp)
    N     : float
            samplng count
    Delta : float
            spatial samplng length [mm]

    Notes
    -----
    Calculation assumes a scanning region centered on the AUT.  

    Formula
    -------
    .. math::
    """
    
    d_mm = floor(sampling_spacing(frequency)*1E3)
    L_mm = ceil(L*1E3)
    L_mm_half = L_mm/2 if L_mm%2 ==0 else (L_mm+1)/2
    if L_mm_half%d_mm > 0:
        L_mm_half = L_mm_half + (d_mm-L_mm_half%d_mm)
    
    N  = 2*(L_mm_half/d_mm)+1
    Lm = -L_mm_half/1E3
    Lp = +L_mm_half/1E3
    
    return ( Lm, Lp, int(N), int(d_mm) )

def sampling_parameters_for_angle(frequency: float, a: float, d: float, theta: float) -> tuple:
    r""" Planar near-field antenna measurement sampling count according to frequency and angle-of-view

    Parameters
    ----------
    frequency : float
                frequency of interest in Hertz [Hz]
    a         : float
                antenna cross-section length [m]
    d         : float
                separation distance between antenna and probe [m]
    theta     : float
                desired pattern view angle along one side [deg]

    Returns
    -------
    Lm    : float
            sampling start position [m]
    Lp    : float
            sampling stop position [m] (equals to negative of Lp)
    N     : float
            samplng count
    Delta : float
            spatial samplng length [mm]

    Notes
    -----
    Calculation assumes a scanning region centered on the AUT.  

    Formula
    -------
    .. math::
    """
    L = scan_length(a, d, theta)
    return sampling_parameters_for_length(frequency, L)