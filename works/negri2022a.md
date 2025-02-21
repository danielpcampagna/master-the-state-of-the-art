---
ID: negri2022a
authors: Negri-Ribalta, Claudia; Noël, René; Herbaut, Nicolas; Salinesi, Camille
category: ok
due: This paper extends the Socio-Technical Security modeling language (STS-ml) to incorporate GDPR principles, enabling compliance modeling, verification, and structured auditing for legal data protection requirements.
entrytype: conference
link: https://doi.org/10.1109/REW56159.2022.00052
name: "Socio-Technical Modelling for GDPR Principles: an Extension for the STS-ml"
organization: IEEE 30th International Requirements Engineering Conference Workshops (REW 2022)
place: Spain
year: 2022
forward_steps: 2
---
# Claudia Negri-Ribalta, René Noël, Nicolas Herbaut, Camille Salinesi. Socio-Technical Modelling for GDPR Principles: an Extension for the STS-ml. REW 2022.

## Evaluation Summary

This paper proposes an **extension of the Socio-Technical Security modeling language (STS-ml)** to better support GDPR compliance by introducing new modeling elements. Key contributions include:

- **Enhancing STS-ml with GDPR-specific attributes** (retention time, minor data handling, special categories of data, asymmetrical relationships, EU actor distinction).  
- **Providing structured compliance verification through model-based analysis**.  
- **Demonstrating the approach using a real-world privacy scenario for a humanitarian NGO**.  

## Relevance to Compliance Questions

| **CQ#** | **Question** | **Relevance** |
|---------|------------|-------------|
| **CQ08** | Retention period for personal data? | ✅ Introduces **"Retention Time" modeling** to specify and enforce data retention policies. |
| **CQ09** | Ensuring GDPR compliance in processing? | ✅ The STS-ml extension **enables structured compliance verification**. |
| **CQ11** | Re-seeking consent if invalid? | ❌ Not explicitly covered. |
| **CQ17** | Responding to Subject Access Requests (SARs)? | ✅ Compliance modeling **supports data access verification**. |
| **CQ20** | Halting processing upon restriction request? | ✅ **Authorization modeling ensures controlled processing**. |
| **CQ21** | Informing individuals of their right to object? | ❌ Not explicitly covered. |
| **CQ25** | Documenting circumstances for data rights restrictions? | ✅ **Model-based tracking of compliance obligations**. |
| **CQ28** | Ensuring personal data accuracy and updates? | ✅ **Supports structured accuracy tracking through GDPR principles**. |
| **CQ29** | Policies to hold data only as necessary? | ✅ **Retention constraints are integrated into the model**. |
| **CQ30** | Compliance with mandatory retention periods? | ✅ **Supports verification of regulatory retention constraints**. |
| **CQ32** | Avoiding unnecessary duplication of records? | ❌ Not explicitly covered. |
| **CQ33** | Providing transparent, intelligible privacy policies? | ✅ **Ensures GDPR transparency requirements are modeled**. |
| **CQ35** | Ensuring up-to-date and accurate personal data? | ✅ **Accuracy tracking is part of the modeling framework**. |
| **CQ37** | Proactively informing individuals of GDPR rights? | ❌ Not explicitly covered. |
| **CQ38** | Making GDPR rights information accessible? | ✅ **Compliance tracking ensures data subject rights are modeled**. |
| **CQ39** | Reviewing third-party data agreements? | ✅ **EU vs. Non-EU actor modeling ensures legal basis verification**. |
| **CQ40** | Requirement to appoint a Data Protection Officer (DPO)? | ❌ Not explicitly covered. |
| **CQ41** | Documenting reasons for not appointing a DPO? | ❌ Not explicitly covered. |
| **CQ42** | Defining escalation/reporting lines for a DPO? | ❌ Not explicitly covered. |
| **CQ43** | Publishing DPO contact details? | ❌ Not explicitly covered. |
| **CQ44** | Notifying data protection authorities of DPO details? | ❌ Not explicitly covered. |
| **CQ47** | Documented security programs for personal data? | ✅ **Security principles are integrated into STS-ml modeling**. |
| **CQ48** | Documented process for handling security complaints? | ✅ **Privacy risk assessment is modeled through compliance tracking**. |
| **CQ49** | Assigning a security breach investigator? | ❌ Not explicitly covered. |
| **CQ50** | Using industry-standard encryption for data transfers? | ✅ **Security controls and obligations are modeled for compliance**. |
| **CQ51** | Ensuring systematic data deletion when no longer needed? | ✅ **Modeling ensures structured deletion enforcement**. |
| **CQ52** | Restoring access to personal data after an incident? | ✅ **Supports regulatory compliance verification for recovery**. |
| **CQ56** | Regularly reviewing data management plans? | ✅ **Auditability is integrated into compliance verification**. |
| **CQ57** | Fully documenting data breaches? | ✅ **Incident reporting mechanisms are modeled in STS-ml**. |
| **CQ58** | Cooperation in handling data breaches? | ✅ **Inter-organizational compliance tracking is supported**. |
| **CQ63** | Listing and documenting all data transfers? | ✅ **Models EU vs. Non-EU data transfer compliance**. |
| **CQ64** | Ensuring legal bases for international data transfers? | ✅ **Models regulatory obligations for international data sharing**. |
| **CQ65** | Informing data subjects about international transfers? | ❌ Not explicitly covered. |

## Justification for Category: OK

- ✅ **Proposes a GDPR Data Provenance Model**: The paper **extends STS-ml for structured compliance verification**.  
- ✅ **Addresses GDPR Compliance Questions**: The approach **covers data retention, security, and legal basis modeling**.  
- ✅ **Publicly Available Model**: The extended STS-ml **is documented in the paper**.  
- ✅ **Written in English**: The document is **fully available in English**.  
- ✅ **Peer-Reviewed**: The paper was presented at **IEEE REW 2022**, ensuring **academic validation**.

### **Conclusion**
This paper is **suitable for inclusion** as it **proposes a structured compliance modeling approach** for GDPR obligations, enabling **legal-technical interoperability and privacy auditing**.

# References

- [[tom2018a]]