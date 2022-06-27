# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import teruel2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, teruel2018a, ref="Teruel, Milagro, Cristian Cardellino, Fernando Cardellino, Laura Alonso Alemany, and Serena Villata. 2018. “Legal Text Processing Within the MIREL Project.” In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018).",
    contexts=[],
))

