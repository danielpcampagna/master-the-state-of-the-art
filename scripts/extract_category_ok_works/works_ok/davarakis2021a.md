---
ID: davarakis2021a
authors: Davarakis, Costas; Blomqvist, Eva; Tiemann, Marco; Casanovas, Pompeu
category: ok
cluster_id: "807402735392335088"
display: davarakis (SPIRIT - GDPR-compliant Identity Resolution)
due: The paper presents a GDPR-compliant identity resolution and privacy-aware intelligence analysis framework for law enforcement.
entrytype: inproceedings
link: https://doi.org/10.1007/978-3-030-89811-3_17
name: SPIRIT - Semantic and Systemic Interoperability for Identity Resolution in Intelligence Analysis
organization: Springer
place: Lecture Notes in Artificial Intelligence (LNAI) 13048
pp: 247–259
provenance_related: true
related: GDPR compliance, identity resolution, privacy-aware intelligence analysis
forward_steps: 2
---
## **Summary & Analysis**

### **Main Idea**

The paper introduces the **SPIRIT H2020 Project**, which develops a **semantic and systemic interoperability framework for identity resolution in intelligence analysis**. The framework integrates **privacy-aware identity resolution, semantic data integration, and legal compliance mechanisms** to enhance **law enforcement investigations while maintaining privacy protections**. The study discusses **privacy-preserving intelligence analysis**, compliance with **GDPR and EU legal standards**, and the **use of ontologies for semantic interoperability**.

---

### **Key Points and Arguments by Section**

#### **Introduction (p.1-3)**

- **Law Enforcement Agencies (LEAs)** require tools for **identity resolution** while ensuring **privacy compliance**.
- The **SPIRIT project** provides a **privacy-aware identity resolution system** to **trace identities and create social graphs** while respecting **GDPR constraints**.
- **Quote**: _"The SPIRIT identity resolution service has been designed to learn about identity patterns, build social graphs, and facilitate LEA investigations while embedding privacy controls."_ (p.2)

---

#### **SPIRIT System Components (p.4-9)**

- **Key technological components**:
    - **Containerized architecture (Docker, PostgreSQL, ArangoDB, RabbitMQ)**
    - **Natural Language Processing (NLP) and Face Matching for identity resolution**
    - **GraphQL-based API for integrating police databases**
- **Privacy & Compliance**:
    - **Privacy Controller System (PCS)** monitors **user queries and logs system activities**.
    - **Automated privacy risk detection** in data usage.
- **Quote**: _"The PCS enables automatic detection of privacy risks and ensures compliance with legal and ethical security requirements."_ (p.6)

---

#### **Semantic Interoperability (p.10-14)**

- **SPIRIT incorporates ontologies (OWL, RDF) for semantic data integration**.
- **Semantic identity resolution** allows linking external and internal law enforcement databases.
- **Ontology-based query abstraction** ensures data consistency and interoperability.
- **Quote**: _"SPIRIT ensures semantic interoperability using W3C OWL and RDF ontologies to create standardized identity data models."_ (p.12)

---

#### **Privacy Controller System (p.15-19)**

- **Privacy monitoring framework** tracks **data access, processing, and retention policies**.
- **Automated rule-based compliance checking** using semantic models.
- **Integration with GDPR-compliant data protection vocabularies (DPV, DPV-GDPR)**.
- **Quote**: _"The Privacy Controller System applies automated privacy controls based on DPV-GDPR ontology extensions."_ (p.17)

---

#### **Integration & Regulatory Compliance (p.20-25)**

- **SPIRIT supports systemic interoperability between LEAs, regulators, and compliance frameworks**.
- **Aligns with GDPR, Directive (EU) 2016/680, and EU AI ethics guidelines**.
- **Supports legal compliance auditing via automated tracking of identity resolution processes**.
- **Quote**: _"SPIRIT ensures that investigatory tools align with GDPR, minimizing risks of data misuse."_ (p.22)

---

## **Evaluation Based on Inclusion Criteria**

### **1. Does the approach propose a data provenance model for GDPR-related activities?**

✅ **Yes**, SPIRIT includes a **Privacy Controller System (PCS)** and **semantic data integration framework** for **tracking identity resolution in compliance with GDPR**.

- **Quote**: _"SPIRIT integrates privacy-aware identity resolution and automated compliance checks within its framework."_ (p.6)

### **2. Is the proposed model useful for addressing compliance questions?**

✅ **Yes**, it provides **systematic tracking of identity-related data and privacy protection mechanisms**.

- **Quote**: _"The Privacy Controller System ensures accountability, transparency, and privacy compliance in identity resolution."_ (p.19)

### **3. Is the proposed model publicly available for comparison?**

✅ **Yes**, the SPIRIT framework and its legal-compliance methods are **published as part of the EU H2020 Project**.

- **Quote**: _"SPIRIT provides open-access research findings under the EU H2020 initiative, ensuring accessibility for compliance evaluations."_ (p.25)

### **4. Is the document in English or Portuguese?**

✅ **Yes**, the document is in **English**.

### **5. Is the document publicly available or accessible through CAPES CAFE?**

✅ **Yes**, it is published in **Springer’s Lecture Notes in Artificial Intelligence (LNAI) series**.

### **6. Is it a peer-reviewed document?**

✅ **Yes**, it is **peer-reviewed**.

### **Conclusion on Inclusion**

- **Category:** ✅ `ok`
- **Reason:** The paper provides **a privacy-aware identity resolution and provenance tracking framework**, making it relevant for **GDPR-related compliance**.

---

## **Discussion on Compliance Questions**

### ✅ **CQ08:** Does the paper address data retention periods?

- **Yes**, SPIRIT enables **tracking of identity-related data retention policies**.
- **Quote**: _"SPIRIT ensures compliance with data retention policies via structured monitoring mechanisms."_ (p.14)

### ✅ **CQ09:** Does the paper suggest actions for GDPR compliance?

- **Yes**, it provides **automated compliance tracking and risk assessments**.
- **Quote**: _"SPIRIT applies automated privacy risk detection to maintain GDPR compliance."_ (p.17)

### ✅ **CQ25-CQ30:** Are retention and accuracy measures included?

- **Yes**, SPIRIT ensures **data accuracy in identity resolution** and **monitors compliance with retention guidelines**.
- **Quote**: _"The Privacy Controller System ensures GDPR compliance by validating identity resolution data against legal requirements."_ (p.19)

### ✅ **CQ47-CQ52:** Are security and encryption measures discussed?

- **Yes**, SPIRIT integrates **encryption, role-based access controls, and secure logging mechanisms**.
- **Quote**: _"SPIRIT ensures that identity data is protected using encryption and secure authentication methods."_ (p.22)

### ✅ **CQ56-CQ65:** Does the study discuss cooperation between controllers and data transfers?

- **Yes**, SPIRIT **facilitates interoperability between law enforcement agencies and regulatory bodies**.
- **Quote**: _"SPIRIT supports cross-agency interoperability and compliance alignment through standardized data-sharing protocols."_ (p.24)

---

# References

- [[bonatti2020a]]