---
ID: gleim2023s
authors: Gleim, Lars Christoph
category: ok
due: This paper presents a data provenance model (FactDAG) that supports GDPR-related obligations such as data lifecycle management, retention policies, and accountability. It provides a structured model for tracking data activities and ensuring compliance.
entrytype: phdthesis
link: https://publications.rwth-aachen.de/record/956518
name: Sustainable Data Management in the Internet of Production
organization: RWTH Aachen University
place: Germany
year: 2023
forward_steps: 2
---
# Lars Christoph Gleim. Sustainable Data Management in the Internet of Production. RWTH Aachen University, 2023.

## Evaluation Summary

This dissertation introduces the **World Wide Data Management (WWDM)** paradigm, a **scalable and interoperable** 
approach to data lifecycle management with **provenance and persistent identifiers**. It defines key components, 
including:

- **FactDAG**: A data integration and interoperability model using **provenance links** to track data across 
  systems and organizations throughout its lifecycle.
- **FactStack**: An implementation of FactDAG based on **Linked Data and FAIR data management principles**.
- **ReShare**: A model for **verifiable accountability** in data sharing across organizational boundaries using 
  **Digital Transmission Contracts**.

These contributions directly support **data tracking, retention, accuracy, and compliance auditing**, making them 
relevant to GDPR obligations.

## Relevance to Compliance Questions

| **CQ#** | **Question** | **Relevance** |
|---------|------------|-------------|
| **CQ08** | Retention period for personal data? | ✅ FactDAG enables tracking of data retention policies. |
| **CQ09** | Ensuring GDPR compliance in processing? | ✅ FactDAG provides provenance tracking for compliance verification. |
| **CQ11** | Re-seeking consent if invalid? | ✅ ReShare enables verifiable consent tracking. |
| **CQ17** | Responding to Subject Access Requests (SARs)? | ✅ FactDAG maintains audit trails for data access requests. |
| **CQ20** | Halting processing upon restriction request? | ✅ FactStack supports **controlled access and policy enforcement**. |
| **CQ21** | Informing individuals of their right to object? | ❌ Not explicitly addressed. |
| **CQ25** | Documenting circumstances for data rights restrictions? | ✅ Provenance metadata can log restrictions. |
| **CQ28** | Ensuring personal data accuracy and updates? | ✅ FactDAG enables **data lineage tracking** and updates. |
| **CQ29** | Policies to hold data only as necessary? | ✅ FactDAG supports **data lifecycle management**. |
| **CQ30** | Compliance with mandatory retention periods? | ✅ The framework can enforce **industry-specific retention policies**. |
| **CQ32** | Avoiding unnecessary duplication of records? | ✅ FactDAG links data across systems to prevent redundant copies. |
| **CQ33** | Providing transparent, intelligible privacy policies? | ❌ Not explicitly addressed. |
| **CQ35** | Ensuring up-to-date and accurate personal data? | ✅ FactDAG enables data verification and updates. |
| **CQ37** | Proactively informing individuals of GDPR rights? | ❌ Not explicitly covered. |
| **CQ38** | Making GDPR rights information accessible? | ❌ Not explicitly covered. |
| **CQ39** | Reviewing third-party data agreements? | ✅ ReShare facilitates **accountability in data-sharing agreements**. |
| **CQ40** | Requirement to appoint a Data Protection Officer (DPO)? | ❌ Not covered. |
| **CQ41** | Documenting reasons for not appointing a DPO? | ❌ Not covered. |
| **CQ42** | Defining escalation/reporting lines for a DPO? | ❌ Not covered. |
| **CQ43** | Publishing DPO contact details? | ❌ Not covered. |
| **CQ44** | Notifying data protection authorities of DPO details? | ❌ Not covered. |
| **CQ47** | Documented security programs for personal data? | ✅ FactStack supports **security measures in data access**. |
| **CQ48** | Documented process for handling security complaints? | ✅ ReShare provides **auditability in data-sharing transactions**. |
| **CQ49** | Assigning a security breach investigator? | ❌ Not explicitly covered. |
| **CQ50** | Using industry-standard encryption for data transfers? | ✅ FactDAG allows **data integrity validation** but does not focus on encryption. |
| **CQ51** | Ensuring systematic data deletion when no longer needed? | ✅ FactDAG enables **lifecycle-based data deletion policies**. |
| **CQ52** | Restoring access to personal data after an incident? | ✅ FactStack supports **data recovery processes**. |
| **CQ56** | Regularly reviewing data management plans? | ✅ WWDM encourages **continuous evaluation of data policies**. |
| **CQ57** | Fully documenting data breaches? | ✅ FactDAG maintains **provenance logs for security events**. |
| **CQ58** | Cooperation in handling data breaches? | ✅ FactDAG allows interorganizational **data-sharing accountability**. |
| **CQ63** | Listing and documenting all data transfers? | ✅ FactDAG enables **tracking of cross-system data movement**. |
| **CQ64** | Ensuring legal bases for international data transfers? | ❌ Not explicitly covered. |
| **CQ65** | Informing data subjects about international transfers? | ❌ Not explicitly covered. |

## Justification for Category: OK

- ✅ **Proposes a Data Provenance Model**: FactDAG, FactStack, and ReShare provide **structured tracking of data activities**.
- ✅ **Addresses GDPR Compliance Questions**: The model supports **data retention, tracking, access management, and accountability**.
- ✅ **Publicly Available Model**: The described framework is **openly accessible**.
- ✅ **Written in English**: The dissertation is available in **English**.
- ❌ **Not Peer-Reviewed**: As a dissertation, it **lacks formal peer review**, but references prior peer-reviewed work.

### **Conclusion**

This dissertation is **suitable for inclusion** in the dataset as it **proposes a data provenance model** that directly addresses GDPR-related obligations and compliance verification.

# References

- [[kirrane2018a]]