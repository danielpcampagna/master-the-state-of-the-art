---
ID: pandit2020representing
authors: PANDIT, HARSHVARDHAN JITENDRA
category: ok
cluster_id: "7232081120271493220"
display: pandit [TODO DUE]
due: |-
  Related to GDPR. [TODO] This thesis presents a large and useful review of the state of the art about approaches related to GDPR. Additionally, this Pandit's contribution includes:

  (1) 120 questions, encompassed into 15 use-cases, elaborated from 7 reliable resources, in addition to the text of GDPR, to assist the endeavor of achieving GDPR compliance; (1a) he also elicits assumptions and constraints associated to those questions (p. 110)

  (2) 3 ontologies for representing: (2a) the GDPR text into a glossary of GDPR compliance concepts as a linked data (GDPRtext); (2b) the provenance of activities associated with personal data and consent in ex-ante and ex-post phases (GDPRov); (2c) information regarding consent (GConsent).

  # The State of the Art

  ## 3.2 APPROACHES FOR GDPR COMPLIANCE UTILISING SEMANTIC WEB

  1. SPECIAL (Scalable Policy-aware Linked Data Architecture For Privacy, Transparency and Compliance)

  2. SERAMIS

  3. Vos et al.

  4. CitySPIN

  5. MIREL

  6. DAPRECO

  7. BPR4GDPR

  8. Elluri et al.

  9. Ujcich et al

  10. Personal Information Controller Service (PICS)

  11. ADvoCATE

  12. Ontology by Geko & Tjoa

  ## APPROACHES ADDRESSING GDPR COMPLIANCE

  13. Layered Privacy Language (LPL)

  14. Lodge et al.

  15. Consent and Data Management Model by Peras

  16. Tom et al.

  17. Coletti et al.

  18. Corrales et al.

  19. LUCE

  20. Decision Provenance by Singh et al.

  21. Sion et al.

  22. privacyTracker

  23. Metrics for Transparency by Spagnuelo et al.

  24. meta-model for PLA by Diamantopoulou et al.

  25. Robol et al.

  26. Basin et al.

  27. RestAssured

  28. OPERANDO

  29. My Health My Data (MHMD)

  ## 3.4 APPROACHES INVOLVING PRIVACY POLICIES

  30. Usable Privacy Project

  31. Polisis and other approaches based on Usable Privacy Project

  32. PrivacyGuide

  ## 3.5 APPROACHES RELATED TO CONSENT

  33. Grando et al.

  34. Consent Receipt Specification

  ## 3.6 UPCOMING RESEARCH PROJECTS ADDRESSING GDPR

  35. PDP4E

  36. DEFeND

  37. PAPAYA

  38. SMOOTH

  39. SODA

  40. DECODE

  41. MOSAICrOWN

  42. PoSEID-on

  # Contribution
entrytype: phdthesis
link: https://harshp.com/research/publications/035-representing-activities-processing-personal-data-consent-semweb-gdpr-compliance
name: Representing Activities associated with Processing of Personal Data and Consent using Semantic Web for GDPR Compliance
place: arXiv
scholar: https://scholar.google.com.br/scholar?cites=7232081120271493220&as_sdt=2005&sciodt=0,5&hl=en
scholar_id: ZGiXMHaDXWQJ
scholar_ok: true
start_set: true
year: 2020
---
# PANDIT, HARSHVARDHAN JITENDRA. Representing Activities associated with Processing of Personal Data and Consent using Semantic Web for GDPR Compliance. 2020.

> https://w3id.org/GDPRov/

## Approach and Motivations

The approach presented in this publication focuses on the GDPRov (GDPR Provenance Ontology), which is designed to represent activities and consent information related to the processing of personal data in compliance with the General Data Protection Regulation (GDPR). The primary motivation behind this approach is to provide a structured and comprehensive way to document both planned (ex-ante) and executed (ex-post) activities to demonstrate GDPR compliance.

The ontology builds on existing standards like PROV-O and P-Plan, extending them to cover specific GDPR compliance requirements. GDPRov uses GDPRtEXT to define the origin and relevance of its concepts within the GDPR, ensuring that all represented activities are traceable back to the regulation's text. The model was created, documented, and published using a rigorous methodology, and it aims to assist controllers in tracking activities and consent information associated with personal data processing.

The structure of the paper includes an introduction to the need for such an ontology, a detailed description of the GDPRov model, its components (such as `p-plan:Plan`, `p-plan:Step`, and properties like `p-plan:isStepOfPlan`), and an evaluation of its effectiveness using competency questions derived from GDPR compliance requirements.

## Approach Contribution For The Compliance Questions

### Question 28

The approach described in the publication indirectly contributes to answering this question. GDPRov's focus on documenting activities and consent information could be extended to include procedures for updating and correcting personal data. By using concepts and relationships to represent these activities, it could potentially ensure that personal data is kept up to date and accurate (e.g., using `p-plan:Step` to represent data correction actions).

### Question 29

GDPRov can be extended to document retention policies and procedures by leveraging its existing framework for representing processes. The ontology can be adapted to include specific processes for data retention and deletion, ensuring data is held only as long as necessary. However, this is not explicitly covered in the current model.

### Question 63

GDPRov's use of GDPRtEXT to define the origin and relevance of concepts within GDPR can be employed to list all transfers, including the nature of the data, purpose of processing, and transfer details. However, the model would need to be extended to fully capture and represent all aspects of data transfers comprehensively.

### Question 64

The current model's ability to document planned and executed activities could be extended to include the legal basis for data transfers. By representing these legal bases as part of the compliance processes, GDPRov could help in documenting and tracking compliance with GDPR requirements related to data transfers.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8

The GDPRov model does not currently include components for specifying retention periods for different categories of personal data. This would require additional properties or extensions to represent data retention schedules explicitly.

### Question 28

While GDPRov can document activities, it lacks specific components to ensure that data is kept up to date and accurate. This would require additional properties or mechanisms to track data updates and corrections systematically.

### Question 29

The model does not explicitly cover retention policies and procedures. Extending the ontology to include these aspects would be necessary to fully address this compliance question.

### Question 51

GDPRov does not include specific components for systematically destroying, erasing, or anonymizing personal data. This would require additional extensions to represent these actions within the ontology.

### Question 63

The current model does not comprehensively cover all aspects of data transfers, such as the details of the transfer process, the nature of the data, and the recipient information. These would need to be explicitly included in the ontology.

### Question 64

The legal basis for data transfers is not currently documented within GDPRov. Extending the model to represent these legal bases and their documentation would be necessary to answer this question fully.

## Key Contributions

- **Extension of PROV-O and P-Plan** to represent GDPR compliance activities.

  - **Components**: `p-plan:Plan`, `p-plan:Step`, `p-plan:isStepOfPlan`, and others.

- **Use of GDPRtEXT** to define the origin and relevance of concepts within GDPR.

- **Documentation of both ex-ante and ex-post activities** to demonstrate GDPR compliance.

- **Evaluation using competency questions** derived from GDPR compliance requirements.

## State-of-the-Art

The GDPRov model advances the state-of-the-art by providing a structured and comprehensive way to document GDPR compliance activities using semantic web technologies. Unlike other approaches that emerged later, GDPRov uniquely integrates PROV-O and P-Plan to represent both planned and executed activities, ensuring a complete documentation of compliance processes.

The model also differentiates itself by using GDPRtEXT to link concepts directly to the GDPR text, ensuring traceability and relevance. While there are other approaches, such as SPECIAL, that use provenance vocabularies for GDPR compliance, GDPRov expands on these by including representations of plans or templates to indicate the association between ex-ante and ex-post phases.

Overall, GDPRov provides a novel and robust framework for documenting GDPR compliance activities, contributing significantly to the field of GDPR compliance and semantic web technologies.

---
# Resumo

A tese de Harshvardhan J. Pandit investiga a aplicação de tecnologias da Web Semântica para representar e associar informações sobre o processamento de dados pessoais e consentimento, com o objetivo de auxiliar na conformidade com o Regulamento Geral de Proteção de Dados (GDPR).

# Contribuições Principais:

1. **GDPRtEXT:** Recurso de dados abertos vinculados que representa o texto do GDPR e um glossário de conceitos relevantes para conformidade.

2. **GDPRov:** Ontologia baseada no PROV-O para modelar atividades associadas a dados pessoais e consentimento, abrangendo fases de planejamento (ex-ante) e execução (ex-post).

3. **GConsent:** Ontologia para representar informações sobre consentimento no contexto da conformidade com o GDPR.

4. **Aplicação de Tecnologias da Web Semântica:** Demonstrações de como utilizar SPARQL para consultas e SHACL para validação de informações relacionadas à conformidade com o GDPR.

# Avaliação das Contribuições

As ontologias e recursos desenvolvidos foram avaliados quanto à sua capacidade de representar com precisão os requisitos do GDPR e sua aplicabilidade na automação de processos de conformidade. Foram realizados estudos de caso e implementações de prova de conceito para demonstrar a eficácia das soluções propostas.

# Tópicos Abordados

1. **Introdução:**
   - **Motivação:** Necessidade de ferramentas automatizadas para auxiliar organizações na conformidade com o GDPR.
   - **Questão de Pesquisa:** Aplicação da Web Semântica na representação de atividades de processamento de dados pessoais e consentimento para conformidade com o GDPR.

2. **Fundamentação Teórica:**
   - **GDPR:** Descrição dos principais requisitos e terminologias do regulamento.
   - **Tecnologias da Web Semântica:** Exploração de RDF, OWL, SPARQL e SHACL como ferramentas para modelagem de informações.

3. **Estado da Arte:**
   - **Abordagens Existentes:** Análise de projetos e pesquisas que utilizam a Web Semântica para conformidade com o GDPR.
   - **Lacunas Identificadas:** Deficiências nas representações atuais de atividades de processamento e consentimento.

4. **Análise dos Requisitos de Conformidade:**
   - **Modelo de Interoperabilidade:** Desenvolvimento de um modelo para categorizar informações baseadas no GDPR.
   - **Questões de Conformidade:** Elaboração de perguntas para avaliar a aderência às exigências do GDPR.

5. **Representação de Informações para Conformidade:**
   - **Metodologia de Engenharia de Ontologias:** Processo de desenvolvimento das ontologias GDPRtEXT, GDPRov e GConsent.
   - **Descrição das Ontologias:** Detalhamento de como cada ontologia representa aspectos específicos do GDPR.

6. **Consulta e Validação de Informações:**
   - **Consultas com SPARQL:** Demonstração de como realizar consultas para extrair informações relevantes para conformidade.
   - **Validação com SHACL:** Aplicação de SHACL para verificar a conformidade das informações com os requisitos do GDPR.

7. **Conclusão:**
   - **Síntese dos Resultados:** Resumo das contribuições e sua relevância para a conformidade com o GDPR.
   - **Trabalhos Futuros:** Sugestões para expandir e aprimorar as abordagens propostas.

# Observações

A tese oferece uma abordagem abrangente para a aplicação de tecnologias da Web Semântica na representação e gestão de informações relacionadas ao processamento de dados pessoais e consentimento, proporcionando ferramentas valiosas para auxiliar organizações na conformidade com o GDPR.
# References

[[piras2019a|Piras, Luca, Mohammed Ghazi Al-Obeidallah, Andrea Praitano, Aggeliki Tsohou, Haralambos Mouratidis, Beatriz Gallego-Nicasio Crespo, Jean Baptiste Bernard, et al. 2019. “DEFeND Architecture: A Privacy by Design Platform for GDPR Compliance.” In Trust, Privacy and Security in Digital Business, edited by Stefanos Gritzalis, Edgar R. Weippl, Sokratis K. Katsikas, Gabriele Anderst-Kotsis, A Min Tjoa, and Ismail Khalil, 78–93. Lecture Notes in Computer Science. Springer International Publishing.]]
[[tesfay2018a|Tesfay, Welderufael B., Peter Hofmann, Toru Nakamura, Shinsaku Kiyomoto, and Jetzabel Serna. 2018. “PrivacyGuide: Towards an Implementation of the EU GDPR on Internet Privacy Policy Evaluation.” In Proceedings of the Fourth ACM International Workshop on Security and Privacy Analytics, 15–21. IWSPA ’18. New York, NY, USA: ACM. https://doi.org/10/gfxvsx.]]
[[pandit2018g|Pandit, Harshvardhan Jitendra, Declan O’Sullivan, and Dave Lewis. 2018a. “Extracting Provenance Metadata from Privacy Policies.” In Provenance and Annotation of Data and Processes, edited by Khalid Belhajjame, Ashish Gehani, and Pinar Alper, 262–65. Lecture Notes in Computer Science. Springer International Publishing. https://doi.org/10/gfxgwm.]]
[[garijo2017a|Garijo, Daniel. 2017. “WIDOCO: A Wizard for Documenting Ontologies.” In International Semantic Web Conference, 94–102. Springer. https://doi.org/10/gfxvtk.]]
[[elgammal2016a|Elgammal, Amal, Oktay Turetken, Willem-Jan van den Heuvel, and Mike Papazoglou. 2016. “Formalizing and Appling Compliance Patterns for Business Process Compliance.” Software & Systems Modeling 15 (1): 119–46. https://doi.org/10/gfzrgw.]]
[[fernández2020a|Fernandez, Javier D, Marta Sabou, Elmar Kiesling, Fajar J Ekaputra, Amr Azzam, and Rigo Wenning. 2019. “User Consent Modeling for Ensuring Transparency and Compliance in Smart Cities.” Personal and Ubiquitous Computing Journal, 34.]]
[[palm2018a|Palm, Alexander. 2018. “Modelling Data Protection Vulnerabilities of Cloud Systems Using Risk Patterns.” Technical Report. RestAssured.]]
[[sion2019a|Sion, L., P. Dewitte, D. Van Landuyt, K. Wuyts, I. Emanuilov, P. Valcke, and W. Joosen. 2019. “An Architectural View for Data Protection by Design.” In 2019 IEEE International Conference on Software Architecture (ICSA), 11–20. https://doi.org/10/gf3czd.]]
[[harris2013a|“SPARQL 1.1 Query Language.” 2013. 2013. https://www.w3.org/TR/sparql11-query/.]]
[[pellegrini2018a|Pellegrini, Tassilo, Andrea Schönhofer, Sabrina Kirrane, Anna Fensel, Oleksandra Panasiuk, Victor Mireles, Thomas Thurner, Axel Polleres, and Markus Dörfler. 2018. “A Genealogy and Classification of Rights Expression Languages-Preliminary Results.” In Data Protection/LegalTech-Proceedings of the 21st International Legal Informatics Symposium IRIS, 243–50.]]
[[westphal2018a|Westphal, Patrick, Javier D Fernandez, and Sabrina Kirrane. 2018. “SPIRIT: A Semantic Transparency and Compliance Stack.” In Proceedings of the 14th International Conference on Semantic Systems (SEMANTiCS), 4.]]
[[pullonen2019a|Pullonen, Pille, Jake Tom, Raimundas Matulevičius, and Aivo Toots. 2019. “Privacy-Enhanced BPMN: Enabling Data Privacy Analysis in Business Processes Models.” Software & Systems Modeling, January. https://doi.org/10/gfv5x7.]]
[[legislature2018a|“Assembly Bill No. 375 Chapter 55: An Act to Add Title 1.81.5 (Commencing with Section 1798.100) to Part 4 of Division 3 of the Civil Code, Relating to Privacy.” 2018. California State Legislature, June. https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201720180AB375.]]
[[urm2019a|Dellas, Nikolaos. 2019. “D2.3 Initial Specification of BPR4GDPR Architecture.” BPR4GDPR.]]
[[ujcich2018a|[50] B. E. Ujcich, A. Bates, and W. H. Sanders, “A Provenance Model for the European Union General Data Protection Regulation”, in Provenance and Annotation of Data and Processes, K. Belhajjame, A. Gehani, and P. Alper, Eds., vol. 11017, Cham: Springer International Publishing, 2018, pp. 45–57, ISBN: 978-3-319-98378-3 978-3-319-98379-0. DOI: 10.1007/978-3-319-98379-0_4. [Online]. Available: http://link.springer.com/ 10.1007/978-3-319-98379-0_4 (visited on 09/10/2018).]]
[[regulation2016a|“Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the Protection of Natural Persons with Regard to the Processing of Personal Data and on the Free Movement of Such Data, and Repealing Directive 95/46/EC (General Data Protection Regulation).” 2016. Official Journal of the European Union L119 (May). http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L:2016:119:TOC.]]
[[lebo2013a|Lebo, Timothy, Satya Sahoo, Deborah McGuinness, Khalid Belhajjame, James Cheney, David Corsar, Daniel Garijo, Stian Soiland-Reyes, Stephan Zednik, and Jun Zhao. 2013. “PROV-O: The PROV Ontology.” 2013.]]
[[agarwal2018a|Agarwal, Sushant, Simon Steyskal, Franjo Antunovic, and Sabrina Kirrane. 2018. “Legislative Compliance Assessment: Framework, Model and GDPR Instantiation.” In Privacy Technologies and Policy, edited by Manel Medina, Andreas Mitrakas, Kai Rannenberg, Erich Schweighofer, and Nikolaos Tsouroulas, 131–49. Lecture Notes in Computer Science. Springer International Publishing.]]
[[leone2018a|Leone, Valentina, Luigi Di Caro, and Serena Villata. 2018. “Legal Ontologies and How to Choose Them: The InvestigatiOnt Tool.” In Proceedings of the ISWC 2018 Posters & Demonstrations, Industry and Blue Sky Ideas Tracks Co-Located with 17th International Semantic Web Conference (ISWC 2018), Monterey, USA, October 8th - to - 12th, 2018. http://ceur-ws.org/Vol-2180/paper-36.pdf.]]
[[peras2018a|Peras, Dijana. 2018. “Guidelines for GDPR Compliant Consent and Data Management Model in ICT Businesses.” In 29th International Conference of Central European Conference on Information and Intelligent Systems, 9.]]
[[gharib2016a|Gharib, Mohamad, Paolo Giorgini, and John Mylopoulos. 2016. “Ontologies for Privacy Requirements Engineering: A Systematic Literature Review,” November. http://arxiv.org/abs/1611.10097.]]
[[schoenen2017a|Schoenen, Stefan, Zoltán Ádám Mann, and Andreas Metzger. 2018. “Using Risk Patterns to Identify Violations of Data Protection Policies in Cloud Systems.” In Service-Oriented Computing – ICSOC 2017 Workshops, edited by Lars Braubach, Juan M. Murillo, Nima Kaviani, Manuel Lama, Loli Burgueño, Naouel Moha, and Marc Oriol, 10797:296–307. Cham: Springer International Publishing. https://doi.org/10.1007/978-3-319-91764-1_24.]]
[[curia2019a|“Opinion of Advocate General - Case C‑673/17.” 2019. March 21, 2019. http://curia.europa.eu/juris/document/document.jsf?docid=212023&mode=req&pageIndex=1&dir=&occ=first&part=1&text=&doclang=EN&cid=5704393.]]
[[pandit9999a|Pandit, Harshvardhan J., and Axel Polleres. 2019. “DPV.” Data Privacy Vocabulary V0.1. July 26, 2019. https://www.w3.org/ns/dpv.]]
[[gurk2017a|Gurk, Silvio Mc, Charlie Abela, and Jeremy Debattista. 2017. “Towards Ontology Quality Assessment.” Joint Proceedings of the MEPDaW, 12.]]
[[mehr2019a|Mehr, Azadeh Sadat Mozafari. 2019. “Compliance to Data Protection and Purpose Control Using Process Mining Technique.” In Proceedings of the Dissertation Award, Doctoral Consortium, and Demonstration Track at BPM 2019 Co-Located with 17th International Conference on Business Process Management (BPM 2019), 6. Vienna, Austria.]]
[[schreiber2014a|“RDF 1.1 Primer.” 2014. June 24, 2014. https://www.w3.org/TR/rdf11-primer/.]]
[[palmirani2018c|Palmirani, Monica, Michele Martoni, Arianna Rossi, Cesare Bartolini, and Livio Robaldo. 2018a. “PrOnto: Privacy Ontology for Legal Compliance.” In Proceedings of the 18th European Conference on Digital Government ECDG 2018, 10.]]
[[bayle2018a|Bayle, Aurelie, Mirko Koscina, David Manset, and Octavio Perez-Kempner. 2018. “When Blockchain Meets the Right to Be Forgotten: Technology Versus Law in the Healthcare Industry.” In 2018 IEEE/WIC/ACM International Conference on Web Intelligence (WI), 788–92. Santiago: IEEE. https://doi.org/10/gf9jn7.]]
[[kirrane2018a|Kirrane, Sabrina, Javier D. Fernández, Wouter Dullaert, Uros Milosevic, Axel Polleres, Piero Bonatti, Rigo Wenning, Olha Drozd, and Philip Raschke. 2018. “A Scalable Consent, Transparency and Compliance Architecture.” In Proceedings of the Posters and Demos Track of the Extended Semantic Web Conference (ESWC 2018). https://doi.org/10/gfxvsf.]]
[[bonatti2018b|Bonatti, Piero A, Bert Bos, Stefan Decker, Javier D Fernandez, Vassilios Peristeras, Axel Polleres, and Rigo Wenning. 2018. “Data Privacy Vocabularies and Controls: Semantic Web for Transparency and Privacy.” In Proceedings of the Workshop on Semantic Web for Social Good Co-Located with 17th International Semantic Web Conference (ISWC 2018), 4. Monterey, California, USA. http://ceur-ws.org/Vol-2182/paper_3.pdf.]]
[[basin2018a|Basin, David, Søren Debois, and Thomas Hildebrandt. 2018. “On Purpose and by Necessity: Compliance Under the GDPR.” In Proceedings of Financial Cryptography and Data Security 2018, 18.]]
[[joshi2019a|Joshi, Karuna Pande, and Agniva Banerjee. 2019. “Automating Privacy Compliance Using Policy Integrated Blockchain.” Cryptography 3 (1): 7. https://doi.org/10/gf6rvc.]]
[[bartolini2015b|Bartolini, Cesare, Robert Muthuri, and Cristiana Santos. 2017. “Using Ontologies to Model Data Protection Requirements in Workflows.” In New Frontiers in Artificial Intelligence, edited by Mihoko Otake, Setsuya Kurahashi, Yuiko Ota, Ken Satoh, and Daisuke Bekki, 10091:233–48. Cham: Springer International Publishing. https://doi.org/10.1007/978-3-319-50953-2_17.]]
[[robol2017a|Robol, Marco, Mattia Salnitri, and Paolo Giorgini. 2017. “Toward GDPR-Compliant Socio-Technical Systems: Modeling Language and Reasoning Framework.” In The Practice of Enterprise Modeling, 236–50. Lecture Notes in Business Information Processing. Springer, Cham. https://doi.org/10/gfxvs7.]]
[[suárez2012a|Suárez-Figueroa, Mari Carmen, Asunción Gómez-Pérez, and Mariano Fernández-López. 2012. “The NeOn Methodology for Ontology Engineering.” In Ontology Engineering in a Networked World, edited by Mari Carmen Suárez-Figueroa, Asunción Gómez-Pérez, Enrico Motta, and Aldo Gangemi, 9–34. Berlin, Heidelberg: Springer Berlin Heidelberg. https://doi.org/10.1007/978-3-642-24794-1_2.]]
[[raschke2017a|Raschke, Philip, Olha Drozd, Bert Bos, Rudy Jacob, and Ben Whittamsmith. 2019. “D4.3 Transparency Dashboard and Control Panel Release V2.” Scalable Policy-awarE Linked Data arChitecture for prIvacy, trAnsparency and compLiance (SPECIAL).]]
[[gandon2017a|Gandon, Fabien, Guido Governatori, and Serena Villata. 2017. “Normative Requirements as Linked Data.” In 30th International Conference on Legal Knowledge and Information Systems (JURIX), 11. Luxembourg.]]
[[pandit2019b|Pandit, Harshvardhan J, Declan O’Sullivan, and Dave Lewis. 2019. “Test-Driven Approach Towards GDPR Compliance.” In 15th International Conference on Semantic Systems (SEMANTiCS2019). Karlsruhe, Germany.]]
[[pandit2018a|Pandit, Harshvardhan J, Declan O’Sullivan, and Dave Lewis. 2018d. “Queryable Provenance Metadata for GDPR Compliance.” In Procedia Computer Science, 137:262–68. Proceedings of the 14th International Conference on Semantic Systems 10th – 13th of September 2018 Vienna, Austria. https://doi.org/10/gfdc6r.]]
[[governatori2016a|Governatori, Guido, Mustafa Hashmi, Ho-Pun Lam, Serena Villata, and Monica Palmirani. 2016. “Semantic Business Process Regulatory Compliance Checking Using LegalRuleML.” In Knowledge Engineering and Knowledge Management, edited by Eva Blomqvist, Paolo Ciancarini, Francesco Poggi, and Fabio Vitali, 746–61. Lecture Notes in Computer Science. Springer International Publishing.]]
[[palmirani2018a|Monica, Palmirani, Martoni Michele, Rossi Arianna, Bartolini Cesare, and Robaldo Livio. 2018. “Legal Ontology for Modelling GDPR Concepts and Norms.” Frontiers in Artificial Intelligence and Applications, 91–100. https://doi.org/10/gfr9qd.]]
[[pandit2019a|Pandit, Harshvardhan J., Christophe Debruyne, Declan O’Sullivan, and Dave Lewis. 2019. “GConsent - A Consent Ontology Based on the GDPR.” In The Semantic Web, edited by Pascal Hitzler, Miriam Fernández, Krzysztof Janowicz, Amrapali Zaveri, Alasdair J. G. Gray, Vanessa Lopez, Armin Haller, and Karl Hammar, 270–82. Lecture Notes in Computer Science. Springer International Publishing. https://w3id.org/GConsent.]]
[[bonatti2018a|Bonatti, Piero A, Sabrina Kirrane, Illiana M. Petrova, Luigi Sauro, and Eva Schlehahn. 2018a. “The SPECIAL Usage Policy Language V0.1.” http://purl.org/specialprivacy/policylanguage.]]
[[pandit2017a|Pandit, Harshvardhan J., and Dave Lewis. 2017. “Modelling Provenance for GDPR Compliance Using Linked Open Data Vocabularies.” In Proceedings of the 5th Workshop on Society, Privacy and the Semantic Web - Policy and Technology (PrivOn2017) (PrivOn). http://ceur-ws.org/Vol-1951/PrivOn2017_paper_6.pdf.]]
[[pandit2018i|Pandit, Harshvardhan J., Christophe Debruyne, Declan O’Sullivan, and Dave Lewis. 2018. “An Exploration of Data Interoperability for GDPR.” International Journal of Standardization Research (IJSR) 16 (1): 1–21. https://doi.org/10/gfsn52.]]
[[robaldo2017a|Robaldo, Livio, and Xin Sun. 2017. “Reified Input/Output Logic: Combining Input/Output Logic and Reification to Represent Norms Coming from Existing Legislation.” Journal of Logic and Computation 27 (8): 2471–2503. https://doi.org/10/gf9jmn.]]
[[diamantopoulou2017a|Diamantopoulou, Vasiliki, Konstantinos Angelopoulos, Michalis Pavlidis, and Haralambos Mouratidis. 2017. “A Metamodel for GDPR-Based Privacy Level Agreements.” In Proceedings of the ER Forum 2017 and the ER 2017 Demo Track Co-Located with the 36th International Conference on Conceptual Modelling (ER 2017), Valencia, Spain, - November 6-9, 2017., 285–91. http://ceur-ws.org/Vol-1979/paper-08.pdf.]]
[[marini2018a|Marini, Alice, Alexis Kateifides, Joel Bates, Gabriela Zanfir-Fortuna, Michelle Bae, Stacey Gray, and Gargi Sen. 2018. “GDPR CCPA Comparison Guide.” DataGuidance and Future of Privacy Forum. https://fpf.org/wp-content/uploads/2018/11/GDPR_CCPA_Comparison-Guide.pdf.]]
[[coleti2019a|Coleti, Thiago Adriano, Marcelo Morandini, Lucia Vilela Leite Filgueiras, Pedro Luiz Pizzigatti Correa, Igor Goulart de Oliveira, and Cinthyan Renata Sachs Camerlengo de Barbosa. 2019. “Design Patterns to Support Personal Data Transparency Visualization in Mobile Applications.” In Human-Computer Interaction. Perspectives on Design, edited by Masaaki Kurosu, 11566:46–62. Cham: Springer International Publishing. https://doi.org/10.1007/978-3-030-22646-6_4.]]
[[bartolini2019a|Bartolini, Cesare, Antonello Calabró, and Eda Marchetti. 2019. “Enhancing Business Process Modelling with Data Protection Compliance: An Ontology-Based Proposal:” In Proceedings of the 5th International Conference on Information Systems Security and Privacy, 421–28. Prague, Czech Republic: SCITEPRESS - Science and Technology Publications. https://doi.org/10/gf3czj.]]
[[christl2016a|Christl, Wolfie, and Sarah Spiekermann. 2016. Networks of Control: A Report on Corporate Surveillance, Digital Tracking, Big Data & Privacy. Wien: Facultas.]]
[[debruyne2019a|Debruyne, C., H. J. Pandit, D. Lewis, and D. O’Sullivan. 2019. “Towards Generating Policy-Compliant Datasets.” In 2019 IEEE 13th International Conference on Semantic Computing (ICSC), 199–203. https://doi.org/10/gfxgwx.]]
[[w3c22012a|“OWL 2.” 2012. OWL 2 Web Ontology Language Document Overview (Second Edition). December 11, 2012. https://www.w3.org/TR/owl2-overview/.]]
[[pandit2018c|Pandit, Harshvardhan J., Declan O’Sullivan, and Dave Lewis. 2018a. “An Ontology Design Pattern for Describing Personal Data in Privacy Policies.” In Proceedings of the 9th Workshop on Ontology Design and Patterns (WOP 2018) Co-Located with 17th International Semantic Web Conference (ISWC 2018). Monterey, California, USA. http://ceur-ws.org/Vol-2195/pattern_paper_3.pdf.]]
[[gallé2019a|Galle, Matthias, Athena Christofi, and Hady Elsahar. 2019. “The Case for a GDPR-Specific Annotated Dataset of Privacy Policies.” In Proceedings of the PAL: Privacy-Enhancing Artificial Intelligence and Language Technologies as Part of the AAAI Spring Symposium Series (AAAI-SSS 2019), 3. http://ceur-ws.org/Vol-2335/1st_PAL_paper_5.pdf.]]
[[pandit2020b|Pandit, Harshvardhan Jitendra, Christophe Debruyne, Declan O’Sullivan, and Dave Lewis. 2020. “Standardisation, Data Interoperability, and GDPR.” Chapter. Shaping the Future Through Standardization. 2020. https://doi.org/10.4018/978-1-7998-2181-6.ch008.]]
[[pocs2016a|“D3.1 Guidelines on Legal Aspects.” 2016. OPERANDO. http://www.operando.eu/upload/operando/moduli/D3.1-Guidelinesonlegalaspectsv2.0_77_289.pdf.]]
[[tambou2019a|McCullagh, Karen, Olivia Tambou, and Sam Bourton. 2019. “National Adaptations of the GDPR.” Blog Droit Europeen. https://wp.me/p6OBGR-3dP.]]
[[fellmann2016a|Fellmann, Michael, and Andrea Zasada. 2014. “STATE-OF-THE-ART OF BUSINESS PROCESS COMPLIANCE APPROACHES.” Tel Aviv, 18.]]
[[peroni2013a|Peroni, Silvio, David Shotton, and Fabio Vitali. 2013. “Tools for the Automatic Generation of Ontology Documentation: A Task-Based Evaluation.” International Journal on Semantic Web and Information Systems (IJSWIS) 9 (1): 21–44. https://doi.org/10/f47ncz.]]
[[harkous2018a|Harkous, Hamza, Kassem Fawaz, Rémi Lebret, Florian Schaub, Kang G Shin, and Karl Aberer. 2018. “Polisis: Automated Analysis and Presentation of Privacy Policies Using Deep Learning.” In 27th USENIX Security Symposium (USENIX Security 18), 531–48.]]
[[kung2016a|“Privacy and Security by Design Methodology Handbook.” 2015. PRIPARE. http://pripareproject.eu/wp-content/uploads/2013/11/PRIPARE-Methodology-Handbook-Final-Feb-24-2016.pdf.]]
[[cardellino2017a|Cardellino, Cristian, Milagro Teruel, Laura Alonso Alemany, and Serena Villata. 2017. “Legal NERC with Ontologies, Wikipedia and Curriculum Learning.” In 15th European Chapter of the Association for Computational Linguistics (EACL 2017), 254–59. Valencia, Spain. https://doi.org/10/gf6rvp.]]
[[politou2018a|Politou, Eugenia, Efthimios Alepis, and Constantinos Patsakis. 2018. “Forgetting Personal Data and Revoking Consent Under the GDPR: Challenges and Proposed Solutions.” Journal of Cybersecurity 4 (1). https://doi.org/10/gfsqrg.]]
[[utz2019a|Utz, Christine, Martin Degeling, Sascha Fahl, Florian Schaub, and Thorsten Holz. 2019. “(Un)Informed Consent: Studying GDPR Consent Notices in the Field.” In ACM SIGSAC Conference on Computer and Communications Security (CCS’19), 18. London, United Kingdom.]]
[[oltramari2018a|Oltramari, Alessandro, Dhivya Piraviperumal, Florian Schaub, Shomir Wilson, Sushain Cherivirala, Thomas B. Norton, N. Cameron Russell, Peter Story, Joel Reidenberg, and Norman Sadeh. 2018. “PrivOnto: A Semantic Framework for the Analysis of Privacy Policies.” Edited by Mathieu d’Aquin, Sabrina Kirrane, Serena Villata, Mathieu d’Aquin, Sabrina Kirrane, and Serena Villata. Semantic Web 9 (2): 185–203. https://doi.org/10/gdfqnk.]]
[[pandit2018b|Pandit, Harshvardhan J, Declan O’Sullivan, and Dave Lewis. 2018b. “Exploring GDPR Compliance over Provenance Graphs Using SHACL.” In Proceedings of the Posters and Demos Track of the 14th International Conference on Semantic Systems Co-Located with the 14th International Conference on Semantic Systems (SEMANTiCS 2018). Vienna, Austria. http://ceur-ws.org/Vol-2198/paper_120.pdf.]]
[[abdullah2012a|Syed Abdullah, Norris, Shazia Sadiq, and Marta Indulska. 2012. “A Compliance Management Ontology: Developing Shared Understanding Through Models.” In Advanced Information Systems Engineering, edited by Jolita Ralyté, Xavier Franch, Sjaak Brinkkemper, and Stanislaw Wrycza, 429–44. Lecture Notes in Computer Science. Springer Berlin Heidelberg.]]
[[palmirani2018d|Monica, Palmirani, and Governatori Guido. 2018. “Modelling Legal Knowledge for GDPR Compliance Checking.” Frontiers in Artificial Intelligence and Applications, 101–10. https://doi.org/10/gfr9qc.]]
[[hadziselimovic2017a|Hadziselimovic, Ensar, Kaniz Fatema, Harshvardhan J. Pandit, and Dave Lewis. 2017. “Linked Data Contracts to Support Data Protection and Data Ethics in the Sharing of Scientific Data.” In Proceedings of the First Workshop on Enabling Open Semantic Science (SemSci), 55–62. http://ceur-ws.org/Vol-1931/paper-08.pdf.]]
[[bartolini2016a|Bartolini, Cesare, Gabriele Lenzini, and Livio Robaldo. 2016. “Towards Legal Compliance by Correlating Standards and Laws with a Semi-Automated Methodology.” In Proceedings of the 28 Benelux Conference on Artificial Intelligence (BNAIC). http://orbilu.uni.lu/handle/10993/28957.]]
[[hoekstra2007a|Hoekstra, Rinke, Joost Breuker, Marcello Di Bello, Alexander Boer, and others. 2007. “The LKIF Core Ontology of Basic Legal Concepts.” LOAIT 321: 43–63.]]
[[pasquier2018a|Pasquier, Thomas, Jatinder Singh, Julia Powles, David Eyers, Margo Seltzer, and Jean Bacon. 2018. “Data Provenance to Audit Compliance with Privacy Policy in the Internet of Things.” Personal and Ubiquitous Computing 22 (2): 333–44. https://doi.org/10/gdcvmb.]]
[[cox2020a|Cox, S, and C Little. 2017. “Time Ontology in OWL.” World Wide Web Consortium. Retrieved from Https://Www. W3. Org/TR/Owl-Time.]]
[[drozd2019b|Drozd, Olha, and Sabrina Kirrane. 2019b. “I Agree: Customize Your Personal Data Processing with the CoRe User Interface.” In Trust, Privacy and Security in Digital Business, edited by Stefanos Gritzalis, Edgar R. Weippl, Sokratis K. Katsikas, Gabriele Anderst-Kotsis, A Min Tjoa, and Ismail Khalil, 11711:17–32. Cham: Springer International Publishing. https://doi.org/10.1007/978-3-030-27813-7_2.]]
[[kirrane2017a|Kirrane, Sabrina, Alessandra Mileo, and Stefan Decker. 2016. “Access Control and the Resource Description Framework: A Survey.” Edited by Bernardo Cuenca Grau. Semantic Web 8 (2): 311–52. https://doi.org/10/gfxvr7.]]
[[wilson2016a|Wilson, Shomir, Florian Schaub, Aswarth Abhilash Dara, Frederick Liu, Sushain Cherivirala, Pedro Giovanni Leon, Mads Schaarup Andersen, et al. 2016. “The Creation and Analysis of a Website Privacy Policy Corpus.” In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 1330–40. Berlin, Germany: Association for Computational Linguistics. https://doi.org/10/gf9t98.]]
[[bartolini2018b|Bartolini, Cesare, Gabriele Lenzini, and Cristiana Santos. 2019. “An Agile Approach to Validate a Formal Representation of the GDPR.” New Frontiers in Artificial Intelligence, 16.]]
[[echevarria2017a|“D6.7 Final (Product) Version of Security Aware Tools.” 2017. OPERANDO. http://www.operando.eu/upload/operando/moduli/D6.7FinalProductVersionofSecurityAwareToolsv1.0_77_378.pdf.]]
[[bartolini2018a|Bartolini, Cesare, Gabriele Lenzini, and Cristiana Santos. 2018. “A Legal Validation of a Formal Representation of GDPR Articles.” In Proceedings of the 2nd Workshop on Technologies for Regulatory Compliance Co-Located with the 31st International Conference on Legal Knowledge and Information Systems (JURIX 2018), 14. Groningen, Netherlands.]]
[[casanovasabc2017a|Casanovas, Pompeu, Jorge González-Conejero, and Louis de Koker. 2017. “Legal Compliance by Design (LCbD) and Through Design (LCtD): Preliminary Survey.” In Proceedings of the 1st Workshop on Technologies for Regulatory Compliance Co-Located with the 3]]
[[tom2018a|Tom, Jake, Eduard Sing, and Raimundas Matulevičius. 2018. “Conceptual Representation of the GDPR: Model and Application Directions.” In International Conference on Business Informatics Research, 18–28. Lecture Notes in Business Information Processing. Springer. https://doi.org/10/gft37v.]]
[[drozd2019a|Drozd, Olha, and Sabrina Kirrane. 2019a. “Consent Comprehension Made Easy Demo.” In 19th Privacy Enhancing Technologies Symposium (PETS), 1.]]
[[libertés2019a|“The CNIL’s Restricted Committee Imposes a Financial Penalty of 50 Million Euros Against GOOGLE LLC | CNIL.” 2019. January 21, 2019. https://www.cnil.fr/en/cnils-restricted-committee-imposes-financial-penalty-50-million-euros-against-google-llc.]]
[[geko2018a|Geko, Melisa, and Simon Tjoa. 2018. “An Ontology Capturing the Interdependence of the General Data Protection Regulation (GDPR) and Information Security.” In Proceedings of the Central European Cybersecurity Conference 2018 on - CECC 2018, 1–6. Ljubljana, Slovenia: ACM Press. https://doi.org/10/gfxqw4.]]
[[teruel2018a|Teruel, Milagro, Cristian Cardellino, Fernando Cardellino, Laura Alonso Alemany, and Serena Villata. 2018. “Legal Text Processing Within the MIREL Project.” In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018).]]
[[alexakis2018a|“BPR4GDPR.” 2019. Business Process Re-Engineering and Functional Toolkit for GDPR Compliance (BPR4GDPR. 2019. http://www.bpr4gdpr.eu/.]]
[[directive1995a|“Directive 95/46/EC of the European Parliament and of the Council on the Protection of Individuals with Regard to the Processing of Personal Data and on the Free Movement of Such Data.” 1995. Official Journal of the European Union L281 (November): 31–50. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:31995L0046.]]
[[winckler2019a|Winckler, Marco, Laurent Goncalves, Olivier Nicolas, Frédérique Biennier, Hind Benfenatki, Thierry Despeyroux, Nourhène Alaya, et al. 2019. “Personal Information Controller Service (PICS).” In Web Engineering, edited by Maxim Bakaev, Flavius Frasincar, and In-Young Ko, 530–33. Lecture Notes in Computer Science. Springer International Publishing.]]
[[cms9999a|“GDPR Enforcement Tracker - List of GDPR Fines.” 2019. 2019. http://www.enforcementtracker.com.]]
[[palmirani2011a|Palmirani, Monica, Guido Governatori, Antonino Rotolo, Said Tabet, Harold Boley, and Adrian Paschke. 2011. “LegalRuleML: XML-Based Rules and Norms.” In Rule-Based Modeling and Computing on the Semantic Web, edited by Frank Olken, Monica Palmirani, and ]]
[[pandit2019c|Pandit, Harshvardhan J., Axel Polleres, Bert Bos, Rob Brennan, Bud Bruegger, Fajar J Ekaputra, Javier D Fernández, et al. 2019. “Creating A Vocabulary for Data Privacy.” In The 18th International Conference on Ontologies, DataBases, and Applications of Semantics (ODBASE2019), 17. Rhodes, Greece.]]
[[fernández2018a|Milošević, Uroš, Philip Raschke, Olha Drozd, Sabrina Kirrane, Freddy De Meersman, and Rudy Jacob. 2019. “D4.4 Usability Testing Report V2.” Scalable Policy-awarE Linked Data arChitecture for prIvacy, trAnsparency and compLiance (SPECIAL).]]
[[linden2018a|Linden, Thomas, Rishabh Khandelwal, Hamza Harkous, and Kassem Fawaz. 2018. “The Privacy Policy Landscape After the GDPR,” September. http://arxiv.org/abs/1809.08396.]]
[[elluri2018b|Elluri, Lavanya, and Karuna Pande Joshi. 2018. “A Knowledge Representation of Cloud Data Controls for EU GDPR Compliance.” In 2018 IEEE World Congress on Services, SERVICES 2018, San Francisco, CA, USA, July 2-7, 2018, 45–46. https://doi.org/10/gft38j.]]
[[opijnen2011a|Opijnen, Marc van. 2011. “European Case Law Identifier: Indispensable Asset for Legal Information Retrieval.” From Information to Knowledge – Online Access to Legal Information: Methodologies, Trends and Perspectives, December, 12.]]
[[restassured9999a|“RestAssured.” 2019. 2019. https://restassuredh2020.eu/.]]
[[union2012a|“Council Conclusions Inviting the Introduction of the European Legislation Identifier (ELI).” 2012. Official Journal of the European Union 325 (3): 3–11. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52012XG1026(01).]]
[[bonatti2018d|Bonatti, Piero A, Wouter Dullaert, Javier D Fernandez, Sabrina Kirrane, Uros Milosevic, and Axel Polleres. 2018. “The SPECIAL Policy Log Vocabulary V0.5.” https://aic.ai.wu.ac.at/qadlod/policyLog/.]]
[[rantos2018a|Rantos, Konstantinos, George Drosatos, Konstantinos Demertzis, Christos Ilioudis, Alexandros Papanikolaou, and Antonios Kritsas. 2019. “ADvoCATE: A Consent Management Platform for Personal Data Processing in the IoT Using Blockchain Technology.” In Innovative Security Solutions for Information Technology and Communications, edited by Jean-Louis Lanet and Cristian Toma, 300–313. Lecture Notes in Computer Science. Springer International Publishing.]]
[[lodge2018a|Lodge, Tom, Andy Crabtree, and Anthony Brown. 2018. “Developing GDPR Compliant Apps for the Edge.” In Data Privacy Management, Cryptocurrencies and Blockchain Technology, edited by Joaquin Garcia-Alfaro, Jordi Herrera-Joancomartí, Giovanni Livraga, and Ruben Rios, 11025:313–28. Cham: Springer International Publishing. https://doi.org/10.1007/978-3-030-00305-0_22.]]
[[elluri2018a|Elluri, L., A. Nagar, and K. P. Joshi. 2018. “An Integrated Knowledge Graph to Automate GDPR and PCI DSS Compliance.” In 2018 IEEE International Conference on Big Data (Big Data), 1266–71. https://doi.org/10/gf3cx9.]]
[[havelange2019a|Havelange, Nadine, Michel Dumontier, Birgit Wouters, Jona Linde, David Townend, Arno Riedl, and Visara Urovi. 2019. “LUCE: A Blockchain Solution for Monitoring Data License accoUntability and CompliancE,” August. http://arxiv.org/abs/1908.02287.]]
[[mohammadi2019a|Gol Mohammadi, Nazila, Jens Leicht, Nelufar Ulfat-Bunyadi, and Maritta Heisel. 2019. “Privacy Policy Specification Framework for Addressing End-Users’ Privacy Requirements.” In Trust, Privacy and Security in Digital Business, edited by Stefanos Gritzalis, Edgar R. Weippl, Sokratis K. Katsikas, Gabriele Anderst-Kotsis, A Min Tjoa, and Ismail Khalil, 11711:46–62. Cham: Springer International Publishing. https://doi.org/10.1007/978-3-030-27813-7_4.]]
[[poveda2014a|International Journal on Semantic Web and Information Systems (IJSWIS)]]
[[lioudakis2019a|Lioudakis, Georgios, and Davide Cascone. 2019. “D3.1 Compliance Ontology.” BPR4GDPR.]]
[[lieber2019a|Lieber, Sven. 2019. “Policy-Compliant Data Processing: RDF-Based Restrictions for Data-Protection.” In Doctoral Track - 18th International Semantic Web Conference (ISWC), 12. Auckland, New Zealand.]]
[[machuletz2019a|Machuletz, Dominique, and Rainer Böhme. 2019. “Multiple Purposes, Multiple Problems: A User Study of Consent Dialogs After GDPR,” August. http://arxiv.org/abs/1908.10048.]]
[[akhigbe2015a|Akhigbe, Okhaide, Daniel Amyot, and Gregory Richards. 2015. “Information Technology Artifacts in the Regulatory Compliance of Business Processes: A Meta-Analysis.” In E-Technologies, edited by Morad Benyoucef, Michael Weiss, and Hafedh Mili, 209:89–104. Cham: Springer International Publishing. https://doi.org/10.1007/978-3-319-17957-5_6.]]
[[gjermundrød2016a|Gjermundrød, Harald, Ioanna Dionysiou, and Kyriakos Costa. 2016. “privacyTracker: A Privacy-by-Design GDPR-Compliant Framework with Verifiable Data Traceability Controls.” In Current Trends in Web Engineering, 3–15. Lecture Notes in Computer Science. Springer, Cham. https://doi.org/10/gfxvs2.]]
[[sadiq2007a|Sadiq, Shazia, Guido Governatori, and Kioumars Namiri. 2007. “Modeling Control Objectives for Business Process Compliance.” In Business Process Management, edited by Gustavo Alonso, Peter Dadam, and Michael Rosemann, 149–64. Lecture Notes in Computer Science. Springer Berlin Heidelberg.]]
[[bizer2011a|Bizer, Christian, Tom Heath, and Tim Berners-Lee. 2011. “Linked Data: The Story so Far.” Semantic Services, Interoperability and Web Applications: Emerging Concepts, 205–27. https://doi.org/10/dh8v52.]]
[[hintze2017a|Hintze, Mike, and Gary LaFever. 2017. “Meeting Upcoming GDPR Requirements While Maximizing the Full Value of Data Analytics.” SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2927540.]]
[[corrales2019a|Corrales, Marcelo, Paulius Jurčys, and George Kousiouris. 2019. “Smart Contracts and Smart Disclosure: Coding a GDPR Compliance Framework.” In Legal Tech, Smart Contracts and Blockchain, 189–220. Springer.]]
[[pandit2018f|Pandit, Harshvardhan J, Declan O’Sullivan, and Dave Lewis. 2018. “GDPR-Driven Change Detection in Consent and Activity Metadata.” In Joint Proceedings of the 4th Workshop on Managing the Evolution and Preservation of the Data Web (MEPDaW), the 2nd Workshop on Semantic Web Solutions for Large-Scale Biomedical Data Analytics (SeWeBMeDA), and the Workshop on Semantic Web of Things for Industry 4.0 (SWeTI) Co-Located with 15th European Semantic Web Conference (ESWC 2018), 5. Heraklion, Crete, Greece. http://ceur-ws.org/Vol-2112/mepdaw_paper_2.pdf.]]
[[pereira2021a|Fernández, Javier D, Fajar J Ekaputra, Peb Ruswono, Elmar Kiesling, and Amr Azzam. 2019. “Privacy-Aware Linked Widgets.” In 1st Workshop on Fairness, Accountability, Transparency, Ethics, and Society on the Web. In Conjunction with the Web Conference 2019, 8. https://doi.org/10/gf2599.]]
[[privacy9999a|“Scalable Policy-Aware Linked Data Architecture for Privacy, Transparency and Compliance (SPECIAL).” 2019. 2019. https://www.specialprivacy.eu/.]]
[[gutierrez2017a|“D3.1 PoSeID-on Blockchain - Interim Implementation.” 2019. POSEIDON. https://www.poseidon-h2020.eu/wp-content/uploads/2019/08/D3.1_final-version_POSEIDON_v10.pdf.]]
[[otto2007a|Otto, Paul N., and Annie I. Anton. 2007. “Addressing Legal Requirements in Requirements Engineering.” In 15th IEEE International Requirements Engineering Conference (RE 2007), 5–14. IEEE. https://doi.org/10/d4rpf3.]]
[[hoppe2018a|Wenning, Rigo, and Sabrina Kirrane. 2018. “Compliance Using Metadata.” In Semantic Applications: Methodology, Technology, Corporate Use, edited by Thomas Hoppe, Bernhard Humm, and Anatol Reibold, 31–45. Berlin, Heidelberg: Springer Berlin Heidelberg. https://doi.org/10.1007/978-3-662-55433-3_3.]]
[[rodrigues2019a|Rodrigues, Cleyton Mário de Oliveira, Frederico Luiz Gonçalves de Freitas, Emanoel Francisco Spósito Barreiros, Ryan Ribeiro de Azevedo, and Adauto Trigueiro de Almeida Filho. 2019. “Legal Ontologies over Time: A Systematic Mapping Study.” Expert Systems with Applications 130 (September): 12–30. https://doi.org/10/gf223z.]]
[[grando2012a|Grando, Maria Adela, Aziz Boxwala, Richard Schwab, and Neda Alipanah. 2012. “Ontological Approach for the Management of Informed Consent Permissions.” In 2nd International Conference on Healthcare Informatics, Imaging and Systems Biology, 51–60. IEEE. https://doi.org/10/gfxvsr.]]
[[gu2017a|Spindler, Gerald, Anna Zsófia Horváth, and Lukas Dalby. 2017. “D3.1 General Legal Aspects.”]]
[[vos2019a|Vos, Marina De, Sabrina Kirrane, Julian Padget, and Ken Satoh. 2019. “ODRL Policy Modelling and Compliance]]
[[dalpiaz2016a|Dalpiaz, Fabiano, Elda Paja, and Paolo Giorgini. 2016. Security Requirements Engineering: Designing Secure Socio-Technical Systems. MIT Press.]]
[[nicoletti2017a|“D2.1 - Use Cases Analysis and User Scenarios.” 2018. POSEIDON. https://www.poseidon-h2020.eu/wp-content/uploads/2019/08/PoSeID-on_D2.1-Use-cases-analysis-and-user-scenarios-v1.00.pdf.]]
[[nicola2016a|De Nicola, Antonio, and Michele Missikoff. 2016. “A Lightweight Methodology for Rapid Ontology Engineering.” Communications of the ACM 59 (3): 79–86. https://doi.org/10/gftgpt.]]
[[pandit2018e|Pandit, Harshvardhan J., Kaniz Fatema, Declan O’Sullivan, and Dave Lewis. 2018. “GDPRtEXT - GDPR as a Linked Data Resource.” In The Semantic Web - European Semantic Web Conference, 481–95. Lecture Notes in Computer Science. Springer, Cham. https://doi.org/10/c3n4.]]
- [[fatema2017a|Fatema, Kaniz, Ensar Hadziselimovic, Harshvardhan J. Pandit, Christophe Debruyne, Dave Lewis, and Declan O’Sullivan. 2017. “Compliance Through Informed Consent: Semantic Based Consent Permission and Data Management Model.” In Proceedings of the 5th Workshop on Society, Privacy and the Semantic Web - Policy and Technology (PrivOn2017) (PrivOn). http://ceur-ws.org/Vol-1951/PrivOn2017_paper_5.pdf.]]
[[w3c2015a|“Semantic Web - W3C.” 2015. 2015. https://www.w3.org/standards/semanticweb/.]]
[[pandit2018h|Pandit, Harshvardhan Jitendra, Declan O’Sullivan, and Dave Lewis. 2018b. “Personalised Privacy Policies.” In New Trends in Databases and Information Systems, edited by András Benczúr, Bernhard Thalheim, Tomáš Horváth, Silvia Chiusano, Tania Cerquitelli, Csaba Sidló, and Peter Z. Revesz, 127–37. Communications in Computer and Information Science. Springer International Publishing. https://doi.org/10/gfxgwn.]]
[[silva2017a|“D4.3 Risk Management Module & Personal Data Analyser - Interim Implementation.” 2019. POSEIDON. https://www.poseidon-h2020.eu/wp-content/uploads/2019/08/D4.3-RMM-and-PDA-V1.0-Final.pdf.]]
[[noy2001a|Noy, Natalya F, Deborah L McGuinness, and others. 2001. “Ontology Development 101: A Guide to Creating Your First Ontology.” Stanford knowledge systems laboratory technical report KSL-01-05 and ….]]
[[pandit2018d|Pandit, Harshvardhan J, Declan O’Sullivan, and Dave Lewis. 2018c. “Towards Knowledge-Based Systems for GDPR Compliance.” In Proceedings of the Joint Proceedings of the International Workshops on Contextualized Knowledge Graphs, and Semantic Statistics (CKGSemStats). Monterey, California, USA. http://ceur-ws.org/Vol-2317/article-09.pdf.]]
[[gerl2018b|Gerl, Armin, Nadia Bennani, Harald Kosch, and Lionel Brunie. 2018. “LPL, Towards a GDPR-Compliant Privacy Language: Formal Definition and Usage.” In Transactions on Large-Scale Data- and Knowledge-Centered Systems XXXVII, edited by Abdelkader Hameurlain and Roland Wagner, 41–80. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer Berlin Heidelberg. https://doi.org/10.1007/978-3-662-57932-9_2.]]
[[gerl2018a|Gerl, Armin, and Dirk Pohl. 2018. “Critical Analysis of LPL According to Articles 12 - 14 of the GDPR.” In Proceedings of the 13th International Conference on Availability, Reliability and Security - ARES 2018, 1–9. Hamburg, Germany: ACM Press. https]]
[[sadeh2013a|Sadeh, Norman, Alessandro Acquisti, Travis D. Breaux, Lorrie Faith Cranor, Aleecia M. McDonald, Joel R. Reidenberg, Noah A. Smith, et al. 2013. “The Usable Privacy Policy Project.” Technical Report, CMU-ISR-13-119, Carnegie Mellon University. http://ra.adm.cs.cmu.edu/anon/usr0/ftp/home/anon/isr2013/CMU-ISR-13-119.pdf.]]
[[garijo2014a|Garijo, Daniel, and Yolanda Gil. 2014. “The P-PLAN Ontology.” March 12, 2014. http://vocab.linkeddata.es/p-plan/.]]
[[bonatti2019a|Bonatti, Piero A, Iliana M Petrova, and Luigi Sauro. 2019. “A Richer Policy Language for GDPR Compliance.” In Proceedings of the 32nd International Workshop on Description Logics, 12. Oslo, Norway.]]
[[knublauch2017a|Knublauch, Holger, and Dimitris Kontokostas. 2017. “Shapes Constraint Language (SHACL).” July 2017. https://www.w3.org/TR/shacl/.]]
[[gordon2009a|Gordon, Thomas F., Guido Governatori, and Antonino Rotolo. 2009. “Rules and Norms: Requirements for Rule Interchange Languages in the Legal Domain.” In International Workshop on Rules and Rule Markup Languages for the Semantic Web, 282–96. Springer. https://doi.org/10/fwf8xf.]]
[[leone2020a|Leone, Valentina, Luigi Di Caro, and Serena Villata. 2019. “Taking Stock of Legal Ontologies: A Feature-Based Comparative Analysis.” Artificial Intelligence and Law, June. https://doi.org/10/gf3z84.]]
[[rossi2019a|Arianna, Rossi, and Palmirani Monica. 2019. “DaPIS: An Ontology-Based Data Protection Icon Set.” Frontiers in Artificial Intelligence and Applications, 181–95. https://doi.org/10/gf7fbn.]]
[[smes2017a|“GDPR Readiness Checklist Template for SMEs.” 2017. Data Protection Commissioner, Ireland.]]
[[teodoro2017a|“D1.1 Initial List of Main Requirements.” 2017. My Health My Data (MHMD). http://www.myhealthmydata.eu/wp-content/themes/Parallax-One/deliverables/D1.1_Initial-List-of-Main-Requirements.pdf.]]
[[debruyne2019b|Debruyne, Christophe, Jonathan Riggio, Olga De Troyey, and Declan O’Sullivan. 2019. “An Ontology for Representing and Annotating Data Flows to Facilitate Compliance Verification.” In 2019 13th International Conference on Research Challenges in Information Science (RCIS), 1–6. https://doi.org/10/ggkj8n.]]
[[benfenatki2018a|Benfenatki, Hind, Frédérique Biennier, Marco Winckler, Laurent Goncalves, Olivier Nicolas, and Zohra Saoud. 2018. “Towards a User Centric Personal Data Protection Framework.” In ACM CHI Conference on Human Factors in Computing Systems - GDPR Workshop, 6.]]
- [[pandit2018f]]
- [[ujcich2018a]]