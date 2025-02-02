---
ID: rantos2019blockchain
authors: Rantos, Konstantinos and Drosatos, George and Kritsas, Antonios and Ilioudis,
  Christos and Papanikolaou, Alexandros and Filippidis, Adam P
category: unrelated
cluster_id: '4977037163942878668'
display: rantos
due: Unrelated to provenance
entrytype: article
forward_steps: 1
link: https://www.hindawi.com/journals/scn/2019/1431578/
name: A blockchain-based platform for consent management of personal data processing
  in the IoT ecosystem
organization: Hindawi
place: JSCN
scholar: https://scholar.google.com/scholar?cites=4977037163942878668&as_sdt=2005&sciodt=0,5&hl=en
scholar_id: zJ27Xu78EUUJ
scholar_ok: true
volume: '2019'
year: 2019
---

# Rantos et al. (2019) - A Blockchain‐Based Platform for Consent Management of Personal Data Processing in the IoT Ecosystem

## Approach and Motivations

The paper presents the **ADVOCATE** platform, a **blockchain-based** framework designed to manage user **consents** for processing personal data in compliance with the **General Data Protection Regulation (GDPR)**. It provides an immutable and verifiable mechanism for consent tracking and versioning.

The system allows users to:
- Provide **explicit consent** for data processing.
- Withdraw consent at any time.
- Monitor consent usage.
- Ensure compliance through **blockchain transparency**.

While the **ADVOCATE** platform addresses an **important aspect of GDPR compliance**, it **does not propose a full data provenance model** to track the entire **lifecycle of personal data processing**. The model **focuses on user consent** rather than broader compliance requirements.

## Approach Contribution For The Compliance Questions

### **CQ11: Ensuring valid user consent under GDPR**
- The **ADVOCATE** platform allows **recording and verifying user consent**, ensuring that data processing is based on valid consent at all times.
- Blockchain technology ensures **immutability** of consent records.

### **CQ37 & CQ38: Informing individuals about GDPR rights**
- The platform enables **transparent user notification** about their data processing rights.
- Consent requests must be **clear, transparent, and legally compliant**.

## Approach Insufficiencies For Fulfilling The Compliance Questions

### **CQ08 & CQ29: Data retention and deletion policies**
- The approach **does not track** how long personal data is retained or **when it must be deleted**.
- It lacks a mechanism to **enforce data retention limits** beyond consent withdrawal.

### **CQ20 & CQ25: Halting processing and restricting data use**
- ADVOCATE records **consent withdrawals**, but **does not enforce** automatic halting of data processing.
- It does **not document legal exemptions** under GDPR.

### **CQ51: Data anonymization and destruction**
- The platform tracks **consent history**, but does **not ensure systematic deletion, anonymization, or erasure** of personal data.

### **CQ63 & CQ64: Data transfers and legal basis**
- While ADVOCATE **logs consent**, it does not **record legal justifications** for **data transfers** across jurisdictions.

## Key Contributions

✅ Provides **user-centric** consent management.  
✅ Uses **blockchain** for consent integrity and **immutability**.  
✅ Ensures **transparent consent tracking**.  
❌ **Does not provide** a full **data provenance model**.  
❌ **Lacks data lifecycle tracking** beyond consent withdrawal.  

## State-of-the-Art

This work contributes to the field of **GDPR-compliant consent management**, leveraging **blockchain** for **transparency and security**. However, it does **not propose a full-fledged data provenance model**, limiting its applicability to the broader compliance requirements.

# References

- Rantos, K., Drosatos, G., Kritsas, A., Ilioudis, C., Papanikolaou, A., & Filippidis, A. P. (2019). A Blockchain‐Based Platform for Consent Management of Personal Data Processing in the IoT Ecosystem. *Security and Communication Networks*, 2019, 1431578. [DOI:10.1155/2019/1431578](https://doi.org/10.1155/2019/1431578)

- [[bartolini2015b]]
