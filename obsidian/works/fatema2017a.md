---
ID: fatema2017compliance
authors: Fatema, Kaniz and Hadziselimovic, Ensar and Pandit, Harshvardhan J and Debruyne,
  Christophe and Lewis, Dave and O'Sullivan, Declan
category: ok
cluster_id: '7851795297572476037'
display: fatema
due: This approach presents an ontology to represent the activities, consent and permissions.
entrytype: inproceedings
link: http://www.tara.tcd.ie/bitstream/handle/2262/82659/88248c5b669175f267069c3319d9ac2d3e84.pdf?sequence=1
name: 'Compliance through Informed Consent: Semantic Based Consent Permission and
  Data Management Model.'
place: ISWC
scholar: https://scholar.google.com.br/scholar?cites=7851795297572476037&as_sdt=2005&sciodt=0,5&hl=en
scholar_id: hdTj-Dgu92wJ
scholar_ok: true
start_set: true
summary: focused in the representation of consent and permissions
year: 2017

---
# Fatema, Kaniz and Hadziselimovic, Ensar and Pandit, Harshvardhan J and Debruyne, Christophe and Lewis, Dave and O'Sullivan, Declan. Compliance through Informed Consent: Semantic Based Consent Permission and Data Management Model. 2017. ISWC

## Approach and Motivations

The approach presented in this publication proposes a semantic model for consent that leverages existing models of provenance, processes, permission, and obligations to ensure compliance with GDPR requirements. The motivations behind this approach include the need to satisfy GDPR's requirements for specificity and unambiguity in user consent and to enable organizations to efficiently demonstrate their compliance. The model aims to make consent explicit, establish a common understanding, and enable the re-use of consent.

The paper introduces a Consent and Data Management Model (CDMM) that uses an open vocabulary for expressing consent. This model incorporates changes in the context of the relationship between data controllers and data subjects into the data processing activities. By doing so, it seeks to improve the integration of data management systems and to help controllers demonstrate compliance with GDPR.

The reference architecture proposed in the paper aims to automate the reasoning over the contextual integrity of the relationship between user consent and compliance by service providers. The implementation of the ontology in Protégé and the use of XACML for machine-enforceable consent permissions are key components of this approach.

## Approach Contribution For The Compliance Questions

### Question 8

The `Consent and Data Management Model (CDMM)` incorporates the lifecycle of consent and data. This includes the period for which the data will be retained as part of the consent information. The `Provenance` component can be used to track the retention period associated with each category of personal data, ensuring it is retained no longer than necessary.

### Question 28

The model's focus on the lifecycle of consent and data can help ensure that personal data is kept up to date and accurate. The `Processes` and `Obligations` components can be utilized to define procedures for data correction and updates, ensuring that necessary changes are made without delay.

### Question 29

Retention policies can be managed using the `Permission` and `Provenance` components of the CDMM. These components ensure that data is held only for as long as necessary and provide a clear audit trail for data retention decisions.

### Question 51

The `Obligations` component can define rules for the systematic destruction, erasure, or anonymization of personal data. The `Provenance` component tracks compliance with these rules, ensuring data is handled appropriately when no longer legally required.

### Question 63

The `Provenance` component can document all data transfers, including the nature of the data, purpose of processing, and details of the transfer. This ensures comprehensive tracking of data flows and compliance with GDPR requirements.

### Question 64

The `Permission` component can record the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses. This information can be documented and managed within the CDMM to demonstrate compliance.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8

The current model might not fully cover the granularity required for all possible retention scenarios across different categories of personal data. It may need further refinement to address specific retention periods comprehensively.

### Question 28

While the model addresses data corrections and updates, it might lack the detailed mechanisms to automatically ensure all data remains up to date across multiple databases and systems, especially in complex environments.

### Question 29

The model's approach to retention policies may need more detailed guidelines and enforcement mechanisms to ensure that data is not retained longer than necessary in all possible scenarios.

### Question 51

The systematic destruction, erasure, or anonymization processes might require more specific implementation details to ensure they are carried out consistently across different systems and platforms.

### Question 63

Although the model tracks data transfers, it might not cover all the complexities involved in international data transfers and the specific legal requirements for each transfer case.

### Question 64

While the model records the legal basis for transfers, it might require additional components to ensure that all legal bases are documented and managed correctly across different jurisdictions and regulatory environments.

## Key Contributions

- **Open Vocabulary for Expressing Consent**:
  - Leveraging existing open ontology models.
  - Improving integration across different information systems.

- **Machine Readable and Enforceable Consent**:
  - Mapping consent into XACML for policy enforcement.

- **Consent and Data Management Model (CDMM)**:
  - Incorporating consent and data lifecycle.
  - Addressing changes in context and ensuring compliance.

- **Implementation in Protégé**:
  - Preliminary ontology version implemented.
  - Use of XACML for consent permission enforcement.

## State-of-the-Art

This approach advances the state-of-the-art by providing a semantic model for consent that addresses GDPR requirements for specificity and unambiguity. By integrating existing models of provenance, processes, permission, and obligations, it creates a comprehensive framework for managing consent and data processing activities.

The use of XACML for machine-enforceable consent permissions provides a robust mechanism for ensuring compliance. The proposed CDMM offers a structured approach to handling the lifecycle of consent and data, improving the ability of organizations to demonstrate their compliance with GDPR.

Related works include ontology-based tools for reasoning about consent permission and integrating patient consent in e-health access control. However, this approach distinguishes itself by focusing on the comprehensive management of consent and data lifecycle, incorporating changes in context, and providing automated reasoning over contextual integrity.

# References

[[regulation2016a|[1] General Data Protection Regulations (GDPR), http://ec.europa.eu/justice/dataprotection/reform/files/regulation_oj_en.pdf]]
[[asghar2012a|[13] Asghar, M. R., and Russello, G.: Actors: A goal-driven approach for capturing and managing consent in e-health systems. In. Policies for Distributed Systems and Networks]]
[[o2005a|[9] O'Keefe, C. M., Greenfield, P., and Goodchild, A.: A decentralised approach to electronic consent and health information access control. Journal of Research and Practice in Information Technology 37 (2), 161-178 (2005).]]
[[gruber1995a|[17] Gruber, T.:Toward principles for the design of ontologies used for knowledge sharing. International Journal of Human-Computer Studies, 907–928, (1993).]]
[[fatema2013a|[16] Fatema K.: Adding Privacy Protection to Policy Based Authorisation Systems. , PhD thesis, 2013, https://kar.kent.ac.uk/47905/]]
[[mont2009a|[12] Mont, M. C., et al.: On the management of consent and revocation in enterprises: setting the context. HP Laboratories, Technical Report HPL-2009-49,( 2009).]]
[[latif2009a|[5] Mather, T., Kumaraswamy, S. and Latif, S.: Cloud security and privacy: an enterprise perspective on risks and compliance. In. O'Reilly Media, Inc. (2009).]]
[[russello2008a|[14] Russello, G., Dong, C. and Dulay, N.: Consent-based workflows for healthcare management. Policies for Distributed Systems and Networks, 2008. POLICY 2008. IEEE Workshop on. IEEE, (2008).]]
[[nissenbaum2011a|[6] Nissenbaum, H.: A Contextual Approach to Privacy Online. Daedalus 140 (4), 32-48 (2011).]]
[[spyns2002a|[20] Spyns, P., Meersman, R. and Jarrar, M.: Data Modelling versus Ontology Engineering. SIGMOD Record 31(4), 12-17 (2002).]]
[[moor2006a|[19] de Moor, A., Leenheer, P. D., and Meersman, R.: DOGMA-MESS: A Meaning Evolution Support System for Interorganizational Ontology Engineering. In. Conceptual Structures: Inspiration and Application, 14th International Conference on Conceptual Structures]]
[[chen2012a|[4] Chen, D., Zhao, H.: Data Security and Privacy Protection Issues in Cloud Computing. In: 2012 International Conference on Computer Science and Electronics Engineering (ICCSEE), vol.1, pp. 647-651. Hangzhou, China (23-25 March 2012).]]
[[mather2009a|[5] Mather, T., Kumaraswamy, S. and Latif, S.: Cloud security and privacy: an enterprise perspective on risks and compliance. In. O'Reilly Media, Inc. (2009).]]
[[directive1995a|[3] European Union Data Protection Directive, Directive 95/46/EC .]]
[[chadwick2009a|[21] Chadwick, D. W., and Fatema, K.: An advanced policy based authorisation infrastructure. In. Proceedings of the 5th ACM work-shop on Digital identity management, DIM’09, pp.81-84, Chicago, Illinois, USA, (2009).]]
[[wuyts2011a|[8] Wuyts, K., Scandariato, R., Verhenneman, G., Joosen, W.: Integrating patient consent in e-health access control. In. Developing and Evaluating Security-Aware Software Systems, IGI Global, pp. 285-308. (2013).]]
[[fatema2016a|[15] Fatema, K., Debruyne, C., Lewis, D., OSullivan, D., Morrison, J. P. and Mazed, A. A.: A Semi-Automated Methodology for Extracting Access Control Rules from the European Data Protection Directive. In. 2016 IEEE Security and Privacy Workshops (SPW), pp.]]
[[heinze2011a|[10] Heinze, O., et al.: Architecture of a consent management suite and integration into IHEbased regional health information networks. BMC medical informatics and decision making,11- 58. (2011).]]
[[grando2013a|[7] Grando, A. and Schwab, R.: Building and evaluating an ontology-based tool for reasoning about consent permission. In. AMIA annual symposium proceedings. Vol. 2013. American Medical Informatics Association, (2013).]]
[[fatema2010a|[22] Fatema, K., Chadwick, D.W. and Lievens, S.: A Multi Privacy Policy Enforcement System. In. Privacy and Identity, IFIP AICT 352, pp. 297–310.(2011).]]
[[fatema2014a|[23] Fatema, K. and Chadwick, D.: Resolving Policy Conflicts - Integrating Policies from Multiple Authors. In. CAiSE International Workshops, Thessaloniki, Greece, (2014).]]
[[mont2010a|[11] Mont, M. C., et al.: A conceptual model for privacy policies with consent and revocation requirements. In. IFIP PrimeLife International Summer School on Privacy and Identity Management for Life, Springer Berlin Heidelberg, (2010).]]
[[bischof2012a|[24] Bischof, S., Decker, S., Krennwallner, T., Lopes, N., Polleres, A.: Mapping between RDF and XML with XSPARQL. J. Data Semantics 1(3), 147-185 (2012)]]
