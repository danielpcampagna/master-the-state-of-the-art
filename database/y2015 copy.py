# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

bartolini2015a = DB(WorkOk(
    2015, "Using ontologies to model data protection requirements in workflows",
    aliases=[  # List of aliases for the same work
        (
            2015, 
            "Reconciling data protection rights and obligations: An ontology of the forthcoming eu regulation",
            "Bartolini, Cesare and Muthuri, Robert"
        ),
    ]
    display="bartolini",
    authors="Bartolini, Cesare and Muthuri, Robert and Santos, Cristiana",
    place=JSAI,
    ID='bartolini2015using',
    category='ok',
    cluster_id='12787841822425963859',
    entrytype='inproceedings',
    link='https://orbilu.uni.lu/bitstream/10993/33856/1/main.pdf',
    organization='Springer',
    pp='233--248',
    scholar='https://scholar.google.com.br/scholar?cites=12787841822425963859&as_sdt=2005&sciodt=0,5&hl=en',
    scholar_id='U12VdWKKd7EJ',
    scholar_ok=True,
    provenance_related=True,
    summary="Data protection, currently under the limelight at the European level, is undergoing a long and complex reform that is finally approaching its completion. Consequently, there is an urgent need to customize semantic standards towards the prospective legal framework. The aim of this paper is to provide a bottom-up ontology describing the constituents of data protection domain and its relationships. Our contribution envisions a methodology to highlight the (new) duties of data controllers and foster the transition of IT-based systems, services, tools and businesses to comply with the new General Data Protection Regulation. This structure may serve as the foundation for the design of data protection compliant information systems.",
    due="related to GDPR",
    related="aimsTo (\"provide an ontology\", \"to assist data controllers in\", \"achieving compliance with GDPR\");\n\ncontext \"ontology\";\n\nscope \"entire law\";\n\nprovide (\"an ontology\", \"to model data protection requirements\"), (\"methodology\", \"a methodology\", \"for integrating it into a workflow to express the GDPR requirements within a business process by means of the ontology\");\n\nopenIssues \"Some of the concepts this ontology expresses appear to be generic, requiring coordination with knowledge from other domains\".",
))

bartolini2015b = DB(WorkUnrelated(
    2015, "Assessing IT security standards against the upcoming GDPR for cloud systems",
    due="File not found",
    display="bartolini",
    authors="Bartolini, Cesare and Gheorghe, Gabriela and Giurgiu, Andra and Sabetzadeh, Mehrdad and Sannier, Nicolas",
    place=GRSRD,
    ID='bartolini2015assessing',
    category='nofile',
    cluster_id='7377825825774535621',
    entrytype='article',
    link='https://orbilu.uni.lu/bitstream/10993/20791/2/abstract.pdf',
    scholar='https://scholar.google.com/scholar?cites=7377825825774535621&as_sdt=2005&sciodt=0,5&hl=en',
    scholar_id='xYP-x39NY2YJ',
    scholar_ok=True,
    provenance_related=True,
))

# bartolini2015c = DB(WorkUnrelated(
#     2015, "Reconciling data protection rights and obligations: An ontology of the forthcoming eu regulation",
#     due="Related to GDPR.",
#     display="bartolini",
#     authors="Bartolini, Cesare and Muthuri, Robert",
#     place=LST4LD,
#     ID='bartolini2015reconciling',
#     category='ok',
#     cluster_id='5773811276492389824',
#     entrytype='article',
#     link='https://orbilu.uni.lu/bitstream/10993/21969/1/main.pdf',
#     scholar='https://scholar.google.com/scholar?cites=5773811276492389824&as_sdt=2005&sciodt=0,5&hl=en',
#     scholar_id='wD1518OyIFAJ',
#     scholar_ok=True,
#     summary="Knowledge theory has made its way into modern computing, through the use of models and annotations to organize it. The bottom layer of knowledge organizations makes use of ontologies, which are models based on a formal language structure and designed to express the concepts pertaining to a domain and the relationships between them. The use of ontologies is popular also in the legal domain to organize legal documents and as a support to legal reasoning. A legal topic which is currently under the limelight at the European level is data protection. Under the pressure of the last years’ technological developments, the data protection legislation has shown its weaknesses, and is currently undergoing a long and complex reform that is finally approaching its completion. The reform will urge businesses dealing with personal data to comply with the new Regulation. The aim of the current paper is to provide a basic ontology for the upcoming data protection legislation, highlighting the duties of the data controller, to ease the transition of systems and services from the existing legislation to the new one.",
#     start_set=True,
# ))

bates2015a = DB(WorkUnrelated(
    2015, "Trustworthy whole-system provenance for the linux kernel",
    due="unrelated to GDPR",
    display="bates",
    authors="Bates, Adam and Tian, Dave Jing and Butler, Kevin RB and Moyer, Thomas",
    place=USENIX,
    ID='bates2015trustworthy',
    category='unrelated',
    cluster_id='14633765960424456584',
    entrytype='inproceedings',
    link='https://www.usenix.org/system/files/conference/usenixsecurity15/sec15-paper-bates.pdf',
    pp='319--334',
    scholar='https://scholar.google.com.br/scholar?cites=14633765960424456584&as_sdt=2005&sciodt=0,5&hl=en',
    scholar_id='iIFNpZuUFcsJ',
    scholar_ok=True,
))

robaldo2015a = DB(WorkUnrelated(
    2015, "Combining input/output logic and reification for representing real-world obligations",
    due="unrelated to GDPR",
    display="robaldo",
    authors="Robaldo, Livio and Humphreys, Llio and Sun, Xin and Cupi, Loredana and Santos, Cristiana and Muthuri, Robert",
    place=JSAI,
    ID='robaldo2015combining',
    category='unrelated',
    cluster_id='15417085231969935553',
    entrytype='inproceedings',
    link='https://orbilu.uni.lu/bitstream/10993/29526/1/RobaldoetalJURISIN2015.pdf',
    organization='Springer',
    pp='217--232',
    scholar='https://scholar.google.com/scholar?cites=15417085231969935553&as_sdt=2005&sciodt=0,5&hl=en',
    scholar_id='wSB901V99NUJ',
    scholar_ok=True,
))

robaldo2015b = DB(WorkUnrelated(
    2015, "The ProLeMAS project: representing natural language norms in Input/Output logic",
    due="unrelated to GDPR",
    display="robaldo",
    authors="Robaldo, Livio and Humphreys, Llio and Sun, Xin and Cupi, Loredana and Santos, Cristiana and Muthuri, Robert",
    place=CONF,
    ID='robaldo2015prolemas',
    category='unrelated',
    cluster_id='1546480202323185121',
    entrytype='article',
    link='https://orbilu.uni.lu/bitstream/10993/26571/1/RobaldoetalJURISIN2015.pdf',
    scholar='https://scholar.google.com/scholar?cites=1546480202323185121&as_sdt=2005&sciodt=0,5&hl=en',
    scholar_id='4c2l54wzdhUJ',
    scholar_ok=True,
))

rosing2015a = DB(WorkUnrelated(
    2015, "Business Process Model and Notation-BPMN.",
    due="Unrelated to GDPR",
    display="rosing",
    authors="von Rosing, Mark and White, Stephen and Cummins, Fred and de Man, Henk",
    place=Web,
    ID='von2015business',
    category='unrelated',
    cluster_id='8497807918410162033',
    entrytype='misc',
    link='https://it-cisq.net/news/whitepapers/Business_Process_Model_and_Notation.pdf',
    scholar='https://scholar.google.com/scholar?cites=8497807918410162033&as_sdt=2005&sciodt=0,5&hl=en',
    scholar_id='cd9WSkdH7nUJ',
    scholar_ok=True,
))
