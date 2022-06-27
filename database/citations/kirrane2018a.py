# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import kirrane2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, kirrane2018a, ref="Kirrane, Sabrina, Javier D. Fernández, Wouter Dullaert, Uros Milosevic, Axel Polleres, Piero Bonatti, Rigo Wenning, Olha Drozd, and Philip Raschke. 2018. “A Scalable Consent, Transparency and Compliance Architecture.” In Proceedings of the Posters and Demos Track of the Extended Semantic Web Conference (ESWC 2018). https://doi.org/10/gfxvsf.",
    contexts=[],
))

