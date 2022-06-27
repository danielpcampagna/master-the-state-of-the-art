# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import tom2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, tom2018a, ref="Tom, Jake, Eduard Sing, and Raimundas Matulevičius. 2018. “Conceptual Representation of the GDPR: Model and Application Directions.” In International Conference on Business Informatics Research, 18–28. Lecture Notes in Business Information Processing. Springer. https://doi.org/10/gft37v.",
    contexts=[],
))

