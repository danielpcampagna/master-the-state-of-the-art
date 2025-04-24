---
ID: esteves2024a
authors: Esteves, Beatriz; Rodríguez-Doncel, Víctor
category: ok
due: The paper systematically analyzes GDPR information flows and maps them to privacy-related ontologies and policy languages, providing a structured approach to compliance modeling. The paper systematically analyzes GDPR-related ontologies and policy languages but does not propose a standalone data provenance model.
name: Analysis of Ontologies and Policy Languages to Represent Information Flows in GDPR
forward_steps: 2
entrytype: article
link: https://doi.org/10.3233/SW-223009
organization: Universidad Politécnica de Madrid
place: Semantic Web Journal, IOS Press
year: 2024
---

# Esteves, Beatriz & Rodríguez-Doncel, Víctor. *Analysis of Ontologies and Policy Languages to Represent Information Flows in GDPR.* 2024.

## Approach and Motivations

This paper surveys **22 policy languages, vocabularies, and ontologies** relevant to GDPR and evaluates their capability to represent **data subject rights and controller obligations**. It introduces the **GDPR Information Flows (GDPRIF) ontology**, which systematizes **57 different informational items** referenced in GDPR.

Key contributions include:
- **Systematic review of GDPR-related semantic vocabularies and ontologies**.  
- **Evaluation of 13 privacy policy languages** for compliance tracking.  
- **GDPRIF ontology**, designed to **formalize GDPR information flows**.  
- **Comparative analysis** of **ODRL, LegalRuleML, DPV, and GDPRtEXT**.  

Despite these contributions, the study **does not propose a standalone data provenance model** but focuses on **semantic representations of GDPR obligations**.

## Approach Contribution For The Compliance Questions

The **GDPRIF ontology** and **policy language analysis** contribute to specific **GDPR compliance areas**:

### **CQ21 - Informing Data Subjects of Rights**
- The paper **analyzes machine-readable formats** that **structure GDPR obligations**.
### **CQ33 - Transparent Data Use**
- The study **identifies policy languages** that **support explicit consent tracking**.

### **CQ47 - Security Program Documentation**
- The paper **surveys privacy-related ontologies**, mapping **security policies** to GDPR obligations.

### **CQ63 - Listing Data Transfers**
- GDPRIF **models interactions between data controllers, processors, and authorities**.

## Approach Insufficiencies

Despite its relevance, the study lacks:
- **A dedicated data provenance model** to track **data lineage and retention policies**.  
- **A structured erasure tracking mechanism** for **CQ51 - Data Erasure and Anonymization**.  
- **Practical enforcement mechanisms**, as it is **primarily a theoretical analysis**.

## Key Contributions

- **Semantic Review of GDPR Compliance Tools:** Evaluation of **22 vocabularies and policy languages**.  
- **Ontology-Based GDPR Representation:** Introduction of **GDPRIF ontology** for **mapping rights and obligations**.  
- **Comparative Analysis of Privacy Policy Languages:** Focus on **machine-readable compliance tracking**.  

## State-of-the-Art

This paper is **one of the most comprehensive reviews of GDPR-related ontologies**. Unlike **provenance models**, it does **not focus on tracking data transformations** but rather **on structuring compliance-related information flows**.

## Conclusion

The study is **highly relevant for GDPR compliance modeling** but does **not introduce a full data provenance framework**. Given its **ontology-based approach**, it is **categorized as "ok"**.

### **Evaluation Against Inclusion/Exclusion Criteria**

1. **Does the approach propose a data provenance model to represent activities related to GDPR obligations?**
    - The paper **surveys and evaluates ontologies and policy languages** that can **model GDPR-related information flows**.
    - It **does not propose a standalone data provenance model**, but **analyzes existing frameworks** that can represent **data exchanges, privacy policies, and obligations**.
    - It introduces **GDPRIF (GDPR Information Flows)** ontology, but this ontology **focuses on formalizing GDPR interactions**, not on data lineage or retention tracking. **(Partially met)**
2. **Is the proposed model useful for addressing the compliance questions?**
    - The study **maps GDPR obligations to machine-readable representations** and **analyzes 22 vocabularies, ontologies, and policy languages**.
    - It is **useful for compliance tracking**, especially regarding **rights and obligations (CQ21, CQ33, CQ47, CQ63)**.
    - However, **data retention (CQ08, CQ29), erasure (CQ51), and security compliance (CQ50)** are not its primary focus. **(Partially met)**
3. **Is the proposed model publicly available?**
    - The article provides an **online portal** with supplementary resources and an **ontology** (GDPRIF), but **no fully implemented system**. **(Partially met)**
4. **Is the document written in English or Portuguese?**
    - The document is written in **English**. **(Met)**
5. **Is the document publicly available or accessible through CAPES CAFE digital libraries?**
    - The article is published in **IOS Press (Semantic Web Journal)** and requires **institutional access**. **(Partially met)**
6. **Is it a peer-reviewed document?**
    - The paper is **peer-reviewed**, published in **Semantic Web (2024)**. **(Met)**

### **Final Verdict**

**Category: "ok"**  
The paper **does not introduce a novel data provenance model** but provides a **detailed ontology-based analysis of GDPR information flows**. Given its **systematic evaluation of GDPR-related ontologies**, it is **relevant** to the research scope.

### **Evaluation of the Paper Regarding GDPR Compliance Questions (CQ08 - CQ65)**

This paper provides a **comprehensive analysis** of **privacy-related policy languages and data protection ontologies** to **represent GDPR rights and obligations**. The authors examine **57 different informational items referenced in the GDPR** and evaluate how **13 policy languages** and **9 ontologies** can model them. Below is the evaluation of its relevance to the specific compliance questions:

- **CQ08 (Retention Periods):** The study evaluates how **privacy ontologies** (e.g., GDPRtEXT, DPV) can be used to track **data retention** requirements (**p. 712**).
- **CQ09 (Compliance Actions for Processing):** The paper discusses **policy languages** like **ODRL and LegalRuleML** that model **data processing compliance obligations** (**p. 715**).
- **CQ11 (Re-seeking Consent for GDPR Compliance):** Consent-related **information flows** are systematically mapped to **semantic vocabularies** such as **GConsent and PrOnto** (**p. 720**).
- **CQ20 (Restriction of Processing Procedures):** The study highlights how **ontologies represent restrictions** in **data processing models** (**p. 713**).
- **CQ29 (Retention Policies and Enforcement):** The paper maps GDPR retention obligations to **ontology elements** (**p. 718**).
- **CQ33 (Transparent and Understandable Information for Data Subjects):** GDPR's **transparency requirements** are analyzed in terms of **ontology representation** (**p. 723**).
- **CQ47 (Security Program for Data Protection):** Security measures such as **data breach notification** and **access controls** are discussed using **policy languages** (**p. 727**).
- **CQ51 (Erasure and Anonymization of Personal Data):** The study reviews **policy-based deletion mechanisms** modeled in **GDPR compliance ontologies** (**p. 732**).
- **CQ57 (Documentation of Data Breaches):** GDPR breach reporting obligations are evaluated in **privacy vocabularies and ontologies** (**p. 735**).

### **Conclusion**
This paper is **highly relevant** as it systematically maps **GDPR compliance obligations** to **semantic models**, helping structure **data provenance frameworks** for **compliance tracking**. Thus, it is categorized as **`ok`**.

# References

-   Esteves, B., & Rodríguez-Doncel, V. (2024). *Analysis of Ontologies and Policy Languages to Represent Information Flows in GDPR.* Semantic Web, 15(3), 709–743. Available at: [IOS Press](https://doi.org/10.3233/SW-223009)
- [[bartolini2015b]]
- [[kirrane2018a]]