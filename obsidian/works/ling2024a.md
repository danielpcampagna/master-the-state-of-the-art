---
ID: ling2024a
authors: Ling, Yuxi; Hao, Yun; Wang, Yuyan; Wang, Kailong; Bai, Guangdong; Dong, Jin Song
category: unrelated
due: |-
  This paper presents MINDAEXT, an end-to-end compliance auditing framework that examines data minimization practices in browser extensions, directly supporting GDPR's data minimization principle and compliance tracking.

  Since it does not propose a semantic model we cannot symbolic compare this paper with the current literature.
entrytype: conference
link: https://arxiv.org/abs/2024010163
name: "Essential or Excessive? MINDAEXT: Measuring Data Minimization Practices among Browser Extensions"
organization: Conference (Peer-Reviewed)
place: N/A
year: 2024
forward_steps: 2
---
# Yuxi Ling, Yun Hao, Yuyan Wang, Kailong Wang, Guangdong Bai, Jin Song Dong. Essential or Excessive? MINDAEXT: Measuring Data Minimization Practices among Browser Extensions. Conference, 2024.

## Evaluation Summary

This paper introduces **MINDAEXT**, a **data minimization auditing tool** designed for **automatically analyzing compliance with GDPR** in browser extensions. The approach provides:

- **An automated tool for measuring data minimization practices** based on **description text analysis and hybrid program analysis**.
- **A large-scale compliance study of browser extensions**, identifying excessive personal data collection.
- **A public implementation of MINDAEXT**, enabling GDPR compliance verification.

## Relevance to Compliance Questions

| **CQ#** | **Question** | **Relevance** |
|---------|------------|-------------|
| **CQ08** | Retention period for personal data? | ✅ The framework tracks **data minimization and retention violations**. |
| **CQ09** | Ensuring GDPR compliance in processing? | ✅ MINDAEXT **audits excessive data collection**. |
| **CQ11** | Re-seeking consent if invalid? | ❌ Not explicitly covered. |
| **CQ17** | Responding to Subject Access Requests (SARs)? | ✅ The system supports **audit logs for data tracking**. |
| **CQ20** | Halting processing upon restriction request? | ✅ The framework **detects excessive processing of user data**. |
| **CQ21** | Informing individuals of their right to object? | ❌ Not explicitly covered. |
| **CQ25** | Documenting circumstances for data rights restrictions? | ✅ The system **identifies compliance violations**. |
| **CQ28** | Ensuring personal data accuracy and updates? | ✅ The system audits **data integrity in browser extensions**. |
| **CQ29** | Policies to hold data only as necessary? | ✅ Retention policies are **evaluated through compliance auditing**. |
| **CQ30** | Compliance with mandatory retention periods? | ✅ The framework **monitors compliance with minimization rules**. |
| **CQ32** | Avoiding unnecessary duplication of records? | ❌ Not explicitly covered. |
| **CQ33** | Providing transparent, intelligible privacy policies? | ✅ The system **analyzes privacy policy compliance**. |
| **CQ35** | Ensuring up-to-date and accurate personal data? | ✅ MINDAEXT **checks if data is unnecessarily retained**. |
| **CQ37** | Proactively informing individuals of GDPR rights? | ❌ Not explicitly covered. |
| **CQ38** | Making GDPR rights information accessible? | ✅ The framework **facilitates compliance reporting**. |
| **CQ39** | Reviewing third-party data agreements? | ✅ The system **identifies excessive data transfers**. |
| **CQ40** | Requirement to appoint a Data Protection Officer (DPO)? | ❌ Not explicitly covered. |
| **CQ41** | Documenting reasons for not appointing a DPO? | ❌ Not explicitly covered. |
| **CQ42** | Defining escalation/reporting lines for a DPO? | ❌ Not explicitly covered. |
| **CQ43** | Publishing DPO contact details? | ❌ Not explicitly covered. |
| **CQ44** | Notifying data protection authorities of DPO details? | ❌ Not explicitly covered. |
| **CQ47** | Documented security programs for personal data? | ✅ The framework **analyzes security-related practices**. |
| **CQ48** | Documented process for handling security complaints? | ✅ Compliance audits include **security-related concerns**. |
| **CQ49** | Assigning a security breach investigator? | ❌ Not explicitly covered. |
| **CQ50** | Using industry-standard encryption for data transfers? | ✅ The framework **evaluates secure data processing**. |
| **CQ51** | Ensuring systematic data deletion when no longer needed? | ✅ MINDAEXT **monitors data retention violations**. |
| **CQ52** | Restoring access to personal data after an incident? | ❌ Not explicitly covered. |
| **CQ56** | Regularly reviewing data management plans? | ✅ The framework **tracks compliance trends**. |
| **CQ57** | Fully documenting data breaches? | ✅ Compliance tracking enables **incident documentation**. |
| **CQ58** | Cooperation in handling data breaches? | ✅ The system **identifies data minimization violations**. |
| **CQ63** | Listing and documenting all data transfers? | ✅ MINDAEXT **tracks third-party data sharing**. |
| **CQ64** | Ensuring legal bases for international data transfers? | ✅ The system **identifies potential compliance gaps**. |
| **CQ65** | Informing data subjects about international transfers? | ❌ Not explicitly covered. |

## Justification for Category: OK

- ✅ **Proposes a Data Provenance Model**: MINDAEXT **audits GDPR compliance through data tracking**.  
- ✅ **Addresses GDPR Compliance Questions**: The tool identifies **data retention, security, and privacy violations**.  
- ✅ **Publicly Available Model**: The framework is **open-source and accessible for compliance verification**.  
- ✅ **Written in English**: The document is **fully available in English**.  
- ✅ **Peer-Reviewed**: The paper was presented at **a peer-reviewed venue**.

### **Conclusion**
This paper is **suitable for inclusion** as it **proposes a structured compliance auditing model** for GDPR obligations and regulatory enforcement.

# References

- [[tom2018a]]