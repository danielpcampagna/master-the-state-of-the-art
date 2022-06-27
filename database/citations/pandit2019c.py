# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import pandit2019c
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pandit2019c, ref="Pandit, Harshvardhan J., Axel Polleres, Bert Bos, Rob Brennan, Bud Bruegger, Fajar J Ekaputra, Javier D Fernández, et al. 2019. “Creating A Vocabulary for Data Privacy.” In The 18th International Conference on Ontologies, DataBases, and Applications of Semantics (ODBASE2019), 17. Rhodes, Greece.",
    contexts=[],
))

