---
ID: tsakalakis2024a
authors: Tsakalakis, Niko; Stalla-Bourdillon, Sophie; Huynh, Dong; Moreau, Luc
category: unrelated
due: This paper presents a typology of explanations to support GDPR-compliant explainability-by-design. However, it does not propose a full data provenance model nor track complete data processing activities. The approach is not applicable to broader compliance questions related to data retention, deletion, or security requirements.
entrytype: article
link: https://doi.org/10.1145/3708504
name: A Typology of Explanations for Explainability-by-Design
organization: ACM Journal of Responsible Computing
place: ACM
year: 2024
forward_steps: 2
---

# Tsakalakis et al. (2024) - A Typology of Explanations for Explainability-by-Design

## Approach and Motivations

The paper introduces a **typology of explanations** to help organizations comply with **GDPR Article 22** on **automated decision-making**. It classifies explanations into **nine hierarchical dimensions**, allowing organizations to structure transparency and justification statements.

The typology aims to:

- Provide a **structured framework** for **explainability-by-design**.
- Facilitate compliance with **automated decision-making transparency rules**.
- Allow the generation of machine-readable **explanation programs**.

However, it **does not propose a comprehensive data provenance model**. The typology primarily focuses on **justifying AI decisions**, rather than **tracking data activities** across GDPR obligations.

## Approach Contribution For The Compliance Questions

### **CQ11: Ensuring valid user consent under GDPR**
- The typology helps explain **why an automated decision was made**, aligning with **GDPR Article 22** requirements.
- Organizations can provide **meaningful explanations** to decision subjects.

### **CQ37 & CQ38: Informing individuals about GDPR rights**
- The framework supports **automated generation of explanations** about **data usage and decision logic**.

## Approach Insufficiencies For Fulfilling The Compliance Questions

### **CQ08 & CQ29: Data retention and deletion policies**
- The model **does not track data retention periods** or provide guidelines on **data deletion processes**.

### **CQ20 & CQ25: Halting processing and restricting data use**
- The typology **does not enforce** the right to **stop data processing** under GDPR restrictions.

### **CQ51: Data anonymization and destruction**
- There is **no mechanism** to **ensure the anonymization or destruction of personal data**.

### **CQ63 & CQ64: Data transfers and legal basis**
- The typology **does not record** legal justifications for **cross-border data transfers**.

## Key Contributions

✅ Provides a **framework for explainability** in AI decision-making.  
✅ Ensures **organizations can document decision logic** for GDPR compliance.  
✅ Supports **automated transparency processes**.  
❌ **Does not provide a full data provenance model**.  
❌ **Lacks tracking mechanisms for data lifecycle management**.  

## State-of-the-Art

This work contributes to the **field of AI transparency and GDPR compliance**, but **is not a complete data tracking model**. While useful for **explaining AI decisions**, it **does not meet the broader requirements of GDPR data provenance**.

# References

- Tsakalakis, N., Stalla-Bourdillon, S., Huynh, D., & Moreau, L. (2024). A Typology of Explanations for Explainability-by-Design. *ACM Journal of Responsible Computing*, 2024. [DOI:10.1145/3708504](https://doi.org/10.1145/3708504)
