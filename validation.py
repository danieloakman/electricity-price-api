from enum import Enum


class AustralianState(str, Enum):
    """Enum representing Australian states and territories."""

    NEW_SOUTH_WALES = "NSW"
    VICTORIA = "VIC"
    QUEENSLAND = "QLD"
    WESTERN_AUSTRALIA = "WA"
    SOUTH_AUSTRALIA = "SA"
    TASMANIA = "TAS"
    AUSTRALIAN_CAPITAL_TERRITORY = "ACT"
    NORTHERN_TERRITORY = "NT"
