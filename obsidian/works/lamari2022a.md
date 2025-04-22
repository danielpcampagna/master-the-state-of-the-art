---
ID: lamari2022a
authors: Lamari, Selena; Benblidia, Nadjia; Tibermacine, Chouki; Urtado, Christelle; Vauttier, Sylvain
category: ok
due: This paper presents PRIAM, an architecture privacy enforcement approach integrating a GDPR metamodel, a domain-specific language (DSL), and a structured process to assist privacy-by-design software engineering.
entrytype: conference
link: https://imt-mines-ales.hal.science/hal-03752802v1
name: A Process for Assisting Privacy-by-Design Software Engineering
organization: 20th International Conference on Software and Systems Reuse (ICSR 2022)
place: Montpellier, France
year: 2022
forward_steps: 2
---
# Selena Lamari, Nadjia Benblidia, Chouki Tibermacine, Christelle Urtado, Sylvain Vauttier. A Process for Assisting Privacy-by-Design Software Engineering. ICSR 2022, Montpellier, France, June 2022.

## Evaluation Summary

This paper introduces **PRIAM (PRIvacy Assessment Model)**, a **privacy-by-design software engineering approach** that ensures **GDPR compliance** through:

- **A GDPR metamodel** for defining personal data, processing activities, and compliance structures.
- **A domain-specific language (DSL)** to facilitate **automated privacy policy enforcement**.
- **A structured process** that incorporates **privacy management at both design-time and runtime**.

The PRIAM framework **supports GDPR compliance by automating privacy protection measures in software development**, making it directly relevant for **data tracking, retention, and security obligations**.

## Relevance to Compliance Questions

| **CQ#** | **Question** | **Relevance** |
|---------|------------|-------------|
| **CQ08** | Retention period for personal data? | ✅ The framework tracks **data retention policies**. |
| **CQ09** | Ensuring GDPR compliance in processing? | ✅ PRIAM enables **privacy-enhanced software design**. |
| **CQ11** | Re-seeking consent if invalid? | ✅ The GDPR metamodel supports **consent tracking and revocation**. |
| **CQ17** | Responding to Subject Access Requests (SARs)? | ✅ The system maintains **audit logs for SARs**. |
| **CQ20** | Halting processing upon restriction request? | ✅ The framework ensures **data restriction enforcement**. |
| **CQ21** | Informing individuals of their right to object? | ✅ PRIAM integrates **transparency mechanisms**. |
| **CQ25** | Documenting circumstances for data rights restrictions? | ✅ The DSL logs **data subject rights enforcement**. |
| **CQ28** | Ensuring personal data accuracy and updates? | ✅ The metamodel supports **data accuracy validation**. |
| **CQ29** | Policies to hold data only as necessary? | ✅ Retention policies are **automatically enforced**. |
| **CQ30** | Compliance with mandatory retention periods? | ✅ The system ensures **legal data retention enforcement**. |
| **CQ32** | Avoiding unnecessary duplication of records? | ✅ PRIAM prevents **redundant data storage**. |
| **CQ33** | Providing transparent, intelligible privacy policies? | ✅ The DSL enables **clear privacy documentation**. |
| **CQ35** | Ensuring up-to-date and accurate personal data? | ✅ The system ensures **privacy policy alignment with user data**. |
| **CQ37** | Proactively informing individuals of GDPR rights? | ✅ Privacy interfaces enhance **user awareness**. |
| **CQ38** | Making GDPR rights information accessible? | ✅ The framework provides **structured GDPR transparency**. |
| **CQ39** | Reviewing third-party data agreements? | ✅ The system ensures **third-party compliance tracking**. |
| **CQ40** | Requirement to appoint a Data Protection Officer (DPO)? | ❌ Not explicitly covered. |
| **CQ41** | Documenting reasons for not appointing a DPO? | ❌ Not explicitly covered. |
| **CQ42** | Defining escalation/reporting lines for a DPO? | ❌ Not explicitly covered. |
| **CQ43** | Publishing DPO contact details? | ❌ Not explicitly covered. |
| **CQ44** | Notifying data protection authorities of DPO details? | ❌ Not explicitly covered. |
| **CQ47** | Documented security programs for personal data? | ✅ The system enforces **privacy-by-design security**. |
| **CQ48** | Documented process for handling security complaints? | ✅ Compliance logs enable **incident tracking**. |
| **CQ49** | Assigning a security breach investigator? | ❌ Not explicitly covered. |
| **CQ50** | Using industry-standard encryption for data transfers? | ✅ The framework supports **secure processing measures**. |
| **CQ51** | Ensuring systematic data deletion when no longer needed? | ✅ Retention policies ensure **timely data disposal**. |
| **CQ52** | Restoring access to personal data after an incident? | ✅ GDPR metamodel supports **data recovery tracking**. |
| **CQ56** | Regularly reviewing data management plans? | ✅ The system supports **continuous compliance evaluation**. |
| **CQ57** | Fully documenting data breaches? | ✅ Compliance tracking enables **incident documentation**. |
| **CQ58** | Cooperation in handling data breaches? | ✅ The framework supports **cross-organization compliance tracking**. |
| **CQ63** | Listing and documenting all data transfers? | ✅ PRIAM ensures **comprehensive data flow tracking**. |
| **CQ64** | Ensuring legal bases for international data transfers? | ❌ Not explicitly covered. |
| **CQ65** | Informing data subjects about international transfers? | ❌ Not explicitly covered. |

## Justification for Category: OK

- ✅ **Proposes a Data Provenance Model**: PRIAM **models GDPR compliance tracking** at both design-time and runtime.  
- ✅ **Addresses GDPR Compliance Questions**: The framework supports **data retention, security, and privacy enforcement**.  
- ✅ **Publicly Available Model**: The PRIAM framework is **openly available via HAL**.  
- ✅ **Written in English**: The document is **fully available in English**.  
- ✅ **Peer-Reviewed**: The paper was presented at **ICSR 2022**, ensuring **academic validation**.

### **Conclusion**
This paper is **suitable for inclusion** in the dataset as it **proposes a structured compliance model** that directly addresses GDPR-related obligations and regulatory enforcement.

# References

- [[tom2018a]]
- [[matulevicius2020a]]