# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import bonatti2018b
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, bonatti2018b, ref="Bonatti, Piero A, Bert Bos, Stefan Decker, Javier D Fernandez, Vassilios Peristeras, Axel Polleres, and Rigo Wenning. 2018. “Data Privacy Vocabularies and Controls: Semantic Web for Transparency and Privacy.” In Proceedings of the Workshop on Semantic Web for Social Good Co-Located with 17th International Semantic Web Conference (ISWC 2018), 4. Monterey, California, USA. http://ceur-ws.org/Vol-2182/paper_3.pdf.",
    contexts=[],
))

