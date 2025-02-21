---
ID: falduti2020a
authors: Falduti, Mattia
category: unrelated
due: This thesis presents the CRIKE (CRIme Knowledge Extraction) approach, which focuses on knowledge extraction from court decisions. However, it does not propose a data provenance model for GDPR obligations, nor does it track personal data processing. The approach is not applicable to the broader GDPR compliance questions.
entrytype: thesis
link: N/A
name: "Law and Data Science: Knowledge Modeling and Extraction from Court Decisions"
organization: University of Milan
place: Milan, Italy
year: 2020
forward_steps: 2
---

# Falduti (2020) - Law and Data Science: Knowledge Modeling and Extraction from Court Decisions

## Approach and Motivations

The thesis introduces **CRIKE (CRIme Knowledge Extraction)**, a **data science approach** designed to support **legal knowledge extraction** from court decisions (CDs). It presents:

- **LATO (Legal Abstract Terms Ontology)** to model legal terminology and relationships.  
- **Multi-label annotation** techniques for knowledge extraction.  
- **Application to 180,000 court decisions from the U.S. Caselaw Access Project (CAP).**  

However, **CRIKE is not a GDPR data provenance model** and does not track **personal data processing**.

## Approach Contribution For The Compliance Questions

### **CQ37 & CQ38: Informing individuals about regulations**
- The ontology supports **structuring legal knowledge** for case law analysis.  

## Approach Insufficiencies For Fulfilling The Compliance Questions

### **CQ08 & CQ29: Data retention and deletion policies**
- The approach **does not track personal data lifecycles** or **enforce deletion policies**.

### **CQ20 & CQ25: Halting processing and restricting data use**
- The system is **not designed for GDPR restrictions on data processing**.

### **CQ51: Data anonymization and destruction**
- There is **no mechanism to enforce anonymization, erasure, or retention limits**.

### **CQ63 & CQ64: Data transfers and legal basis**
- The ontology **does not document** personal data transfers or their legal justifications.

## Key Contributions

✅ Provides a **legal knowledge modeling framework**.  
✅ Uses **semantic technologies** for case law analysis.  
✅ Supports **automated legal knowledge extraction**.  
❌ **Does not provide a full data provenance model**.  
❌ **Lacks tracking mechanisms for GDPR compliance**.  

## State-of-the-Art

This work contributes to **legal knowledge extraction**, but **is not applicable to GDPR data provenance modeling**. While useful for **court decision analysis**, it **does not meet the broader requirements of GDPR compliance**.

# References

- Falduti, M. (2020). Law and Data Science: Knowledge Modeling and Extraction from Court Decisions. *University of Milan, PhD Thesis*.

- [[bartolini2015b]]
