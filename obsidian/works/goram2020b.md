---
ID: goram2020b
authors: Goram, Mandy; Veiel, Dirk
category: unrelated
due: This paper presents a legal domain model integrated into the eCBASE adaptive system framework. While it supports legal explanations and compliance transparency, it does not provide a full GDPR data provenance model or enforce data retention, deletion, or security requirements.
entrytype: conference
link: https://www.scitepress.org/Papers/2020/95650/95650.pdf
name: Considering Legal Regulations in an Extendable Context-based Adaptive System Environment
organization: ICEIS 2020
place: SCITEPRESS
year: 2020
forward_steps: 2
---

# Goram & Veiel (2020) - Considering Legal Regulations in an Extendable Context-based Adaptive System Environment

## Approach and Motivations

The paper introduces an **adaptive system environment (eCBASE)** designed to integrate legal compliance mechanisms dynamically. The framework:

- **Generates personalized legal explanations** for users.  
- **Models legal regulations** using a domain-specific **legal ontology**.  
- **Supports compliance transparency** by **informing users of obligations and restrictions**.  

However, it **does not propose a GDPR data provenance model**, focusing instead on **context-aware legal compliance tracking**.

## Approach Contribution For The Compliance Questions

### **CQ37 & CQ38: Informing individuals about GDPR rights**
- The system **generates legal explanations**, informing users of **their obligations and system data usage**.

### **CQ51: Data integrity and security**
- The **legal domain model** helps define **legal requirements for data processing**.

## Approach Insufficiencies For Fulfilling The Compliance Questions

### **CQ08 & CQ29: Data retention and deletion policies**
- The approach **does not define data retention tracking** or **deletion enforcement**.

### **CQ20 & CQ25: Halting processing and restricting data use**
- While the system **tracks legal obligations**, it **does not implement GDPR processing restrictions**.

### **CQ63 & CQ64: Data transfers and legal basis**
- **Does not document cross-border data transfers** or **legal justifications for data sharing**.

## Key Contributions

✅ **Provides an ontology-based legal compliance tracking model**.  
✅ **Supports compliance transparency through automated explanations**.  
✅ **Informs users about legal obligations dynamically**.  
❌ **Does not track GDPR data processing activities comprehensively**.  
❌ **Lacks enforcement mechanisms for data retention and security policies**.  

## State-of-the-Art

This work contributes to **legal compliance automation** but **does not offer a GDPR-specific data provenance model**. While **context-aware legal tracking is valuable**, the framework **does not fully address GDPR retention, deletion, or security obligations**.

# References

- Goram, M., & Veiel, D. (2020). Considering Legal Regulations in an Extendable Context-based Adaptive System Environment. *22nd International Conference on Enterprise Information Systems (ICEIS 2020)*, 367-376. [SCITEPRESS](https://www.scitepress.org/Papers/2020/95650/95650.pdf)
- [[bartolini2015b]]