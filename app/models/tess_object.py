from datetime import datetime
from pydantic import BaseModel


class TESSObject(BaseModel):
    # IDENTIFICATION
    tid: str  # TESS ID
    toi: str  # TESS object of interest
    ctoi: float  # Number to track and identify objects of interest
    classification: str  # Category of the observation

    # POSITION
    rastr: str  # Right ascension of the planetary system in sexagesimal
    ra: float  # Right Ascension of the planetary system in decimal degrees
    decstr: str  # Declination of the planetary system in sexagesimal
    dec: int  # Declination of the planetary system in decimal degrees
    st_pmra: float  # Angular change in right ascension over time as seen from the center of mass of the Solar System
    st_pmdec: float  # Angular change in declination over time as seen from the center of mass of the Solar System

    # PLANET PROPERTIES
    pl_tranmid: float  # The time given by the average of the time the planet begins to cross the stellar limb and the time the planet finishes crossing the stellar limb
    pl_orbper: float  # Time the planet takes to make a complete orbit around the host star or system
    pl_trandurh: float  # The length of time from the moment the planet begins to cross the stellar limb to the moment the planet finishes crossing the stellar limb
    pl_trandep: float  # The size of the relative flux decrement caused by the orbiting body transiting in front of the star
    pl_rade: float  # Length of a line segment from the center of the planet to its surface, measured in units of radius of the Earth
    pl_insol: float  # Insolation flux is the measure of the amount of stellar radiation received by the planet in units relative to that measured from the Earth from the Sun
    pl_eqt: float  # The equilibrium temperature of the planet as modeled by a black body heated only by its host star

    # STELLAR PROPERTIES
    st_tmag: float  # Brightness of the host star as measured using the TESS-band in units of magnitudes as reported in the TESS Input Catalog
    st_dist: float  # Distance to the planetary system in units of parsecs as reported in the TESS Input Catalog
    st_teff: float  # Stellar effective temperature value as reported in the TESS Input Catalog
    st_logg: float  # Gravitational acceleration experienced at the stellar surface as reported in the TESS Input Catalog
    st_rad: float  # Length of a line segment from the center of the star to its surface, measured in units of radius of the Sun as reported in the TESS Input Catalog

    # DATE
    toi_created: datetime  # Date on which the TESS Project identified the Object of Interest
    rowupdate: datetime  # Date of last update of the planet parameters
