# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2015 import bartolini2015b
from ..work.y2018 import ujcich2018a
from ..work.y2019 import besik2019a
from ..work.y2020 import campagna2020a
from ..work.y2020 import pandit2020a


DB(Citation(
    ujcich2018a, bartolini2015b, ref="3. C. Bartolini, R. Muthuri, and C. Santos, “Using ontologies to model data protection requirements in workflows,” in Proceedings of New Frontiers in Artificial Intelligence. Springer, 2017, pp. 233–248.",
    contexts=[],
))

DB(Citation(
    besik2019a, bartolini2015b, ref="5. Cesare Bartolini, Robert Muthuri, and Cristiana Santos. Using ontologies to modeldata protection requirements in workﬂows. In JSAI Int. Symposium on ArtiﬁcialIntelligence, pages 233–248. Springer, 2015.",
    contexts=[],
))

DB(Citation(
    campagna2020a, bartolini2015b, ref="Bartolini, C., Muthuri, R., and Santos, C. (2015). Using ontologies to model data protection requirements in workflows. In JSAI International Symposium on Artificial Intelligence, pages 233–248. Springer",
    contexts=[],
))


DB(Citation(
    pandit2020a, bartolini2015b, ref="Bartolini, Cesare, Robert Muthuri, and Cristiana Santos. 2017. “Using Ontologies to Model Data Protection Requirements in Workflows.” In New Frontiers in Artificial Intelligence, edited by Mihoko Otake, Setsuya Kurahashi, Yuiko Ota, Ken Satoh, and Daisuke Bekki, 10091:233–48. Cham: Springer International Publishing. https://doi.org/10.1007/978-3-319-50953-2_17.",
    contexts=[],
))

