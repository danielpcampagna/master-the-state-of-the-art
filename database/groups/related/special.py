from unicodedata import category
from snowballing.approaches import Group

from ..constants import *
from ...work.y2018 import kirrane2018a
from ...work.y2018 import bonatti2018a
from ...work.y2018 import bonatti2018b
from ...work.y2018 import bonatti2018d

approach = Group(
    kirrane2018a, bonatti2018a, bonatti2018b, bonatti2018d,
    display="SPECIAL",
    approach_name="SPECIAL",
    category='unrelated',
    useful=True,
    not_directly_related_to_provenance=True,
)
