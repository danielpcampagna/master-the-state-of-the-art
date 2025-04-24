---
ID: ling2022a
authors: Ling, Yuxi; Wang, Kailong; Bai, Guangdong; Wang, Haoyu; Dong, Jin Song
category: ok
due: This paper presents an end-to-end approach for diagnosing GDPR compliance violations in browser extensions, using NLP and hybrid static-dynamic analysis to verify compliance against privacy policies and runtime behaviors.
entrytype: conference
link: https://doi.org/10.1145/3551349.3560436
name: Are they Toeing the Line? Diagnosing Privacy Compliance Violations among Browser Extensions
organization: IEEE/ACM International Conference on Automated Software Engineering (ASE 2022)
place: USA
year: 2022
forward_steps: 2
---
# Yuxi Ling, Kailong Wang, Guangdong Bai, Haoyu Wang, Jin Song Dong. Are they Toeing the Line? Diagnosing Privacy Compliance Violations among Browser Extensions. ASE 2022.

## Evaluation Summary

This paper proposes a **comprehensive approach for detecting GDPR privacy compliance violations in browser extensions**. The methodology includes:

- **Using BERT-based NLP models to assess compliance of privacy policies with GDPR obligations**.
- **Performing hybrid static-dynamic analysis to verify runtime data collection behaviors**.
- **Identifying discrepancies between declared privacy practices and actual processing**.

## Relevance to Compliance Questions

| **CQ#** | **Question** | **Relevance** |
|---------|------------|-------------|
| **CQ08** | Retention period for personal data? | ✅ Analyzes **data retention statements in privacy policies**. |
| **CQ09** | Ensuring GDPR compliance in processing? | ✅ **Evaluates runtime behaviors** against GDPR requirements. |
| **CQ11** | Re-seeking consent if invalid? | ❌ Not explicitly covered. |
| **CQ17** | Responding to Subject Access Requests (SARs)? | ✅ **Identifies inconsistencies in declared vs. actual data access practices**. |
| **CQ20** | Halting processing upon restriction request? | ✅ **Verifies declared processing restrictions in privacy policies**. |
| **CQ21** | Informing individuals of their right to object? | ✅ **Analyzes privacy policies for missing user rights statements**. |
| **CQ25** | Documenting circumstances for data rights restrictions? | ✅ **Models missing GDPR compliance elements in privacy policies**. |
| **CQ28** | Ensuring personal data accuracy and updates? | ❌ Not explicitly covered. |
| **CQ29** | Policies to hold data only as necessary? | ✅ **Identifies GDPR compliance failures in retention statements**. |
| **CQ30** | Compliance with mandatory retention periods? | ✅ **Detects extensions with no clear retention policies**. |
| **CQ32** | Avoiding unnecessary duplication of records? | ❌ Not explicitly covered. |
| **CQ33** | Providing transparent, intelligible privacy policies? | ✅ **Uses NLP models to check policy clarity and completeness**. |
| **CQ35** | Ensuring up-to-date and accurate personal data? | ❌ Not explicitly covered. |
| **CQ37** | Proactively informing individuals of GDPR rights? | ✅ **Evaluates policy statements regarding GDPR rights**. |
| **CQ38** | Making GDPR rights information accessible? | ✅ **Measures privacy policy compliance completeness**. |
| **CQ39** | Reviewing third-party data agreements? | ✅ **Assesses inconsistencies in third-party data declarations**. |
| **CQ40** | Requirement to appoint a Data Protection Officer (DPO)? | ❌ Not explicitly covered. |
| **CQ41** | Documenting reasons for not appointing a DPO? | ❌ Not explicitly covered. |
| **CQ42** | Defining escalation/reporting lines for a DPO? | ❌ Not explicitly covered. |
| **CQ43** | Publishing DPO contact details? | ❌ Not explicitly covered. |
| **CQ44** | Notifying data protection authorities of DPO details? | ❌ Not explicitly covered. |
| **CQ47** | Documented security programs for personal data? | ✅ **Identifies missing security documentation in privacy policies**. |
| **CQ48** | Documented process for handling security complaints? | ✅ **Verifies the presence of security-related declarations**. |
| **CQ49** | Assigning a security breach investigator? | ❌ Not explicitly covered. |
| **CQ50** | Using industry-standard encryption for data transfers? | ✅ **Checks policy statements regarding encryption and security**. |
| **CQ51** | Ensuring systematic data deletion when no longer needed? | ✅ **Detects missing data deletion statements** in privacy policies. |
| **CQ52** | Restoring access to personal data after an incident? | ✅ **Verifies if policies mention restoration mechanisms**. |
| **CQ56** | Regularly reviewing data management plans? | ✅ **Analyzes compliance with policy review obligations**. |
| **CQ57** | Fully documenting data breaches? | ✅ **Verifies privacy policies for data breach documentation**. |
| **CQ58** | Cooperation in handling data breaches? | ✅ **Checks for GDPR compliance in incident response policies**. |
| **CQ63** | Listing and documenting all data transfers? | ✅ **Identifies missing data transfer documentation in policies**. |
| **CQ64** | Ensuring legal bases for international data transfers? | ✅ **Checks policies for adherence to GDPR transfer requirements**. |
| **CQ65** | Informing data subjects about international transfers? | ✅ **Evaluates privacy policies for GDPR-mandated disclosures**. |

## Justification for Category: OK

- ✅ **Proposes a GDPR Compliance Model**: The paper **introduces a structured compliance analysis framework**.  
- ✅ **Addresses GDPR Compliance Questions**: The approach **identifies violations in retention, security, and transparency obligations**.  
- ✅ **Publicly Available Model**: The **PrivAud-100 corpus and compliance dataset are released** for research.  
- ✅ **Written in English**: The document is **fully available in English**.  
- ✅ **Peer-Reviewed**: The paper was **published in IEEE/ACM ASE 2022**, ensuring **academic validation**.

### **Conclusion**
This paper is **suitable for inclusion** as it **proposes a structured compliance tracking framework**, enabling **automated GDPR violation detection and privacy policy verification**.

# References

- [[tom2018a]]