---
ID: besik2019ontology
authors: Besik, Saliha Irem and Freytag, Johann-Christoph
category: ok
cluster_id: '9953792441592462448'
display: besik
due: 'This paper has proposed a compliance-check architecture based on Java technologies.
  This system was built under three ontologies: the first proposes terms for the privacy
  layer, suggesting classes to GDPR (in particular, purpose specifications, data minimization,
  processing compliant-checking, and limit of retention period), privacy policies,
  and privacy preferences (when the data subjects to determine who can access their
  data and for what purposes). To represent the activities, this approach has inherited
  Business Process Model and Notation (BPMN). Finally, the last ontology contains
  terms of the specific clinical domain.


  The authors demonstrate that this approach can check compliance through the ministration
  of a Java-based open source business rule management system. They show the usability
  of this approach in the running process, which also illustrates how these three
  ontologies should work together.


  Although the compliance checker was built over a specific technology (that we probably
  will not utilize), we have considered the privacy ontology can contribute to the
  objective of our study. Indeed, this privacy ontology provides concepts to represent
  privacy policy constraints. Such information is required to answer the obligations
  we have aimed to achieve.


  In face of this, we have included this article to see whether the proposed model
  was extended to meet further obligations.'
entrytype: inproceedings
link: https://www.researchgate.net/profile/Saliha-Besik/publication/336129066_Ontology-Based_Privacy_Compliance_Checking_for_Clinical_Workflows/links/5d90d2cb299bf10cff1a003e/Ontology-Based-Privacy-Compliance-Checking-for-Clinical-Workflows.pdf
name: Ontology-Based Privacy Compliance Checking for Clinical Workflows.
not_directly_related_to_provenance: true
place: LWDA
pp: 218--229
scholar: https://scholar.google.com.br/scholar?cites=9953792441592462448&as_sdt=2005&sciodt=0,5&hl=en
scholar_id: cDwW-Xz5IooJ
scholar_ok: true
start_set: true
useful: true
year: 2019

---
# Besik, Saliha Irem and Freytag, Johann-Christoph. Ontology-Based Privacy Compliance Checking for Clinical Workflows. 2019. LWDA.

## Approach and Motivations

The paper "Ontology-Based Privacy Compliance Checking for Clinical Workflows" by Saliha Irem Besik and Johann-Christoph Freytag introduces an approach to ensure privacy compliance in clinical workflows. The motivation behind this approach is the necessity to safeguard patient data privacy in the healthcare domain, a sector particularly sensitive due to the nature of the data involved. The authors propose using an ontology-based reasoner to verify privacy compliance, leveraging the principles and requirements outlined by the General Data Protection Regulation (GDPR).

The approach is structured around the development of a Privacy-aware Clinical Workflow (PaCW) Ontology. This ontology integrates business process modeling, data privacy regulations, and clinical workflow requirements to create a comprehensive framework for privacy compliance checking. The paper illustrates the applicability of the proposed methodology through a case study involving a newborn screening procedure in Germany, demonstrating how semantic reasoning can be applied to support privacy-awareness in clinical workflows.

The paper is organized into several sections: an introduction that sets the context and importance of data privacy in healthcare, a detailed explanation of the PaCW Ontology, a description of the reasoning approach for privacy compliance, and a running example in the clinical domain. The ontology aims to represent privacy-awareness not only in terms of regulatory compliance but also in adherence to the privacy preferences of patients.

## Approach Contribution For The Compliance Questions

### Question 8

The `PaCW Ontology` can partially contribute to answering Question 8 by ensuring that personal data is retained only for the period necessary for its specified purpose. The ontology includes principles such as `Limited Retention Period` which mandates that data must be erased when it is no longer necessary.

### Question 28

The approach includes a `Consent Check` component that ensures the processing of personal data is lawful and that necessary changes are made when consent is updated, which is related to keeping data up to date and accurate.

### Question 29

Similar to Question 8, the `Limited Retention Period` principle within the `PaCW Ontology` helps ensure that data is not held longer than necessary, aligning with retention policies and procedures.

### Question 51

The `Limited Retention Period` principle also addresses the requirement for systematic destruction, erasure, or anonymization of data when it is no longer legally required, contributing to answering Question 51.

## Approach Insufficiencies For Fulfill The Compliance Questions

### Question 63

The approach does not explicitly cover the listing of all data transfers, including details such as the nature of the data, the purpose of processing, and the countries involved. This lack of detailed tracking and documentation of data transfers means the ontology cannot fully address Question 63.

### Question 64

The `PaCW Ontology` does not provide mechanisms to document the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses. This limitation makes it insufficient to fully answer Question 64.

## Key Contributions

- **Ontology Development**: Introduction of the Privacy-aware Clinical Workflow (PaCW) Ontology.
    - **Purpose Specification**
    - **Data Minimization**
    - **Consent Check**
    - **Limited Retention Period**
- **Semantic Reasoning**: Application of an ontology-based reasoner to verify privacy compliance.
- **Integration of Domains**: Bridging business process modeling, data privacy, and clinical workflows.
- **Case Study**: Demonstration of the approach through a newborn screening scenario in Germany.
- **Privacy-awareness**: Ensuring compliance with GDPR and patient privacy preferences.

## State-of-the-Art

This approach advances the state-of-the-art by integrating ontology-based reasoning into clinical workflow privacy compliance, offering a structured and regulated method to ensure data privacy in healthcare. The use of ontologies facilitates a common understanding across different domains, enhancing the effectiveness of privacy compliance checks.

Related works include:

- **Privacy enforcement in data analysis workflows** by Yolanda Gil et al., which focuses on privacy enforcement but lacks the specific integration of clinical workflows and GDPR principles.
- **Ontology-based Approach for Business Process Compliance Checking** by Tuan Pham and Nhan Le Thanh, which deals with business process compliance but not specifically tailored to clinical workflows or GDPR.

Overall, while the proposed model makes significant strides in privacy compliance for clinical workflows, it still requires enhancements to fully address all compliance questions, particularly those involving detailed data transfer documentation and legal bases for data transfers.
# References

[[nguyen2014a|9. Thi Hoa Hue Nguyen and Nhan Le Thanh. Ensuring the semantic correctness ofworkﬂow processes: an ontological approach. In Proceedings of 10th Workshop onKnowledge Engineering and Software Engineering (KESE10) co-located with 21stEuropean Conference on ]]
[[regulation2016a|1. EU General Data Protection Regulation (GDPR). Regulation (EU) 2016/679 ofthe European Parliament and of the Council of 27 April 2016 on the protectionof natural persons with regard to the processing of personal data and on the freemovement of such data, and repealing Directive 95/46/EC (General Data Protec-tion Regulation), OJ 2016 L 119.]]
[[bartolini2015b|5. Cesare Bartolini, Robert Muthuri, and Cristiana Santos. Using ontologies to modeldata protection requirements in workﬂows. In JSAI Int. Symposium on ArtiﬁcialIntelligence, pages 233–248. Springer, 2015.]]
[[gil2007a|7. Yolanda Gil, William K Cheung, Varun Ratnakar, and Kai-kin Chan. Privacyenforcement in data analysis workﬂows. In Proceedings of the 2007 InternationalConference on Privacy Enforcement and Accountability with Semantics-Volume320, pages 41–48. Citese]]
[[rahmouni2010a|10. Hanene Boussi Rahmouni, Tony Solomonides, Marco Casassa Mont, and SimonShiu. Privacy compliance and enforcement on European healthgrids: an approachthrough ontology. Philosophical Transactions of the Royal Society A: Mathemati-cal, Physical and Engineering Sciences, 368(1926):4057–4072, 2010.]]
[[labda2014a|Wadha Labda, Nikolay Mehandjiev, and Pedro Sampaio. Modeling of privacy-aware business processes in BPMN to protect personal data. In Proc. of the 29thAnnual ACM Symposium on Applied Computing, pages 1399–1405. ACM, 2014.]]
[[natschläger2011a|3. Christine Natschl¨ager. Towards a BPMN 2.0 ontology. In International Workshopon Business Process Modeling Notation, pages 1–15. Springer, 2011.]]
[[guez2007a|6. Alfonso Rodr´ıguez, Eduardo Fern´andez-Medina, and Mario Piattini. A BPMNextension for the modeling of security requirements in business processes. IEICEtransactions on information and systems, 90(4):745–752, 2007.]]
[[belaazi2015a|11. Maherzia Belaazi, Hanen Boussi Rahmouni, and Adel Bouhoula. An OntologyRegulating Privacy Oriented Access Controls. In Int. Conf. on Risks and Securityof Internet and Systems, pages 17–35. Springer, 2015]]
