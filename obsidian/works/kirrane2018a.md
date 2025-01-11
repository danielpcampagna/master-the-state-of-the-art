---
ID: kirrane2018scalable
authors: Kirrane, Sabrina and Fernández, Javier D and Dullaert, Wouter and Milosevic, Uros and Polleres, Axel and Bonatti, Piero A and Wenning, Rigo and Drozd, Olha and Raschke, Philip
backward_steps: 1
category: ok
display: kirrane
due: Although the approach this document introduces presents a model where components are capable of representing the provenance of the activities related to GDPR, in this document, specifically, this model is not introduced. Thus, we consider this document unrelated.
entrytype: inproceedings
link: https://research.wu.ac.at/files/19833040/ESWC2018.pdf
name: A scalable consent, transparency and compliance architecture
organization: Springer
place: ESWC
pp: 131--136
scholar: https://scholar.google.com/scholar?cites=13808115522786291090&as_sdt=2005&sciodt=0,5&hl=pt-BR
scholar_ok: |-
  @inproceedings{kirrane2018scalable,
    title={A scalable consent, transparency and compliance architecture},
    author={Kirrane, Sabrina and Fern{\'a}ndez, Javier D and Dullaert, Wouter and Milosevic, Uros and Polleres, Axel and Bonatti, Piero A and Wenning, Rigo and Drozd, Olha and Raschke, Philip},
    booktitle={European Semantic Web Conference},
    pages={131--136},
    year={2018},
    organization={Springer}
  }
year: 2018
---
# Kirrane, Sabrina and Fernández, Javier D and Dullaert, Wouter and Milosevic, Uros and Polleres, Axel and Bonatti, Piero A and Wenning, Rigo and Drozd, Olha and Raschke, Philip. A scalable consent, transparency and compliance architecture. 2018.

> [SPECIAL Demo Video](https://purl.com/specialprivacy/demos/ESWC2018)

## Approach and Motivations

The SPECIAL consent, transparency, and compliance system aims to provide data subjects with greater control over their personal data processing and sharing, while also enabling data controllers and processors to comply with the European General Data Protection Regulation (GDPR). The system facilitates automatic compliance verification, contrasting with existing tools that rely on self-assessment questionnaires.

The approach integrates a consent management dashboard and a transparency and compliance dashboard. The former supports granting and revoking consent for data processing and sharing, while the latter offers transparency about data processing and sharing events in a user-friendly manner. The system employs RDF vocabularies to express usage policies and data processing events, ensuring compliance with data protection obligations.

This architecture leverages the Kafka distributed streaming platform for scalability and performance. Future work includes benchmarking the system's components and enhancing security measures against potential attacks.

## Approach Contribution For The Compliance Questions

### Question 8

The SPECIAL system can record and express usage constraints, including data retention periods, using RDF vocabularies. This enables the system to document how long each category of personal data will be retained, aligning with GDPR requirements. The `SPECIAL usage policy language` allows specifying retention periods, thus contributing to answering this compliance question.

### Question 28

The compliance dashboard can help ensure data accuracy and prompt updates by recording and monitoring data processing events. The system's transparency features can be employed to verify that procedures for keeping personal data up-to-date and accurate are in place, contributing to this compliance requirement.

### Question 29

The `SPECIAL usage policy language` includes provisions for defining retention policies. By recording and verifying these policies, the system can help ensure that data is retained only as long as necessary. The compliance dashboard provides transparency regarding these policies, aiding in adherence to this requirement.

### Question 51

The system's focus on transparency and compliance includes documenting data processing events and usage constraints. While it provides tools for monitoring compliance, it may not directly handle the destruction, erasure, or anonymization of data. However, by ensuring policies are followed, it indirectly supports this compliance question.

### Question 63

The transparency dashboard records data processing and sharing events, including the nature of the data and its transfer details. This documentation can be used to answer questions about data transfers, including the purpose, origin, destination, and recipient of the data.

### Question 64

The system can document the legal basis for data transfers using the `SPECIAL usage policy language`. This ensures that all transfers are recorded, and their legal bases are documented, aiding in compliance with this requirement.

## Approach Insufficiencies For Fulfill The Compliance Questions

### Question 51

While the SPECIAL system documents policies and events related to data processing, it does not explicitly handle the destruction, erasure, or anonymization of data. This gap means the system cannot fully address this compliance question, as it lacks components to enforce or automate data destruction processes.

## Key Contributions

- Integration of consent management and transparency dashboards
  - `Consent Management Dashboard`
  - `Transparency and Compliance Dashboard`

- Use of RDF vocabularies to express usage policies and data processing events
  - `SPECIAL usage policy language`
  - `Log vocabulary`

- Automatic compliance verification with GDPR requirements
- Scalability and performance facilitated by the Kafka distributed streaming platform
- Future enhancements planned for benchmarking and security

## State-of-the-Art

The SPECIAL system advances the state-of-the-art by providing a scalable, automated solution for GDPR compliance that integrates consent management and transparency features. Unlike traditional self-assessment tools, it offers real-time compliance verification using RDF technologies. This approach contrasts with existing works that focus on self-assessment questionnaires, offering a more dynamic and automated compliance mechanism.

The related works by the Information Commissioner’s Office (ICO), Microsoft, and Nymity, which rely on predefined questionnaires, highlight the novelty of the SPECIAL system. By automating the compliance process and providing transparency dashboards, the SPECIAL system represents a significant step forward in data privacy and protection technologies.

# References

