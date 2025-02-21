---
ID: filipczuk2021consent
authors: Filipczuk, Dorota
category: unrelated
cluster_id: "16503246320892567099"
display: filipczuk
due: The thesis introduces a graph-based model for consent management but does not propose a data provenance model required for GDPR compliance.
entrytype: phdthesis
forward_steps: 1
link: https://eprints.soton.ac.uk/456829/
name: Consent mechanisms in privacy engineering
place: Thesis
scholar: https://scholar.google.com.br/scholar?cites=16503246320892567099&as_sdt=2005&sciodt=0,5&hl=en
scholar_id: O96SRRdPB-UJ
scholar_ok: true
year: 2021
---

# Filipczuk, Dorota. *Consent Mechanisms in Privacy Engineering.* 2021.

## Approach and Motivations

This thesis explores **privacy engineering mechanisms** for **consent management** under GDPR. It treats consent as a **multi-step process** involving:
1. **Understanding user consent decision-making**  
2. **Automated consent negotiations**  
3. **Consent enforcement through a graph-theoretic model**  

Key contributions include:
- **An experimental study on privacy knowledge’s impact on consent behavior**.  
- **A negotiation-based model** where users' privacy preferences influence consent decisions.  
- **A graph-based model for service providers** to store and enforce **consent constraints** on data processing workflows.  

Although the thesis proposes a **graph-theoretic approach to structuring consent enforcement**, it **does not introduce a comprehensive data provenance model**, which is a strict requirement for inclusion.

## Approach Contribution For The Compliance Questions

The thesis contributes to **consent enforcement** but does not **track data provenance**. However, some **GDPR-related issues** are addressed:

### **CQ11 - Consent Validity**
- The work **models consent as a dynamic agreement**, which **enhances validity tracking**.

### **CQ21 - Informing Data Subjects of Rights**
- The study investigates **how privacy knowledge impacts consent behavior**.

### **CQ47 - Security Program Documentation**
- The **graph-based model** allows service providers to **map consent restrictions** to data processing workflows.

## Approach Insufficiencies For Fulfilling Compliance Questions

### **CQ08 - Data Retention Periods**
- Does **not define** structured **data retention policies**.

### **CQ29 - Retention Policies**
- No explicit methodology for **automated retention tracking**.

### **CQ51 - Data Erasure and Anonymization**
- Does **not systematically track** **data deletion or anonymization**.

### **CQ63 - Listing Data Transfers**
- The model does not **track historical data movements**.

### **CQ64 - Legal Basis for Data Transfers**
- The research **focuses on consent modeling**, **not legal justifications**.

## Key Contributions

- **Graph-Theoretic Consent Model:** Defines **constraint-based consent enforcement**.
- **Negotiation-Based Consent Management:** Introduces a **user preference-based consent negotiation process**.
- **Privacy Knowledge Impact Study:** Evaluates how **privacy knowledge affects consent behavior**.

## State-of-the-Art

This research enhances **consent enforcement** but lacks **provenance tracking**. Unlike **data lineage models**, the approach focuses on **structured consent control** rather than **historical tracking**.

## Conclusion

While this thesis **presents innovative consent enforcement techniques**, it **does not propose a full-fledged data provenance model** for GDPR compliance. Therefore, it is **unrelated** to the inclusion criteria.

# References

- Filipczuk, D. (2021). *Consent Mechanisms in Privacy Engineering.* PhD Thesis, University of Southampton. Available at: [EPrints Soton](https://doi.org/10.5258/SOTON/D2003)
- [[kirrane2018a]]
- [[fatema2017a]]
