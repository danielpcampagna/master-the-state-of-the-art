---
ID: fernandez2019p
authors: Fernández García, Javier D.; Ekaputra, Fajar J.; Aryan, Peb R.; Kiesling, Elmar; Azzam, Amr
category: unrelated
due: The paper discusses privacy-aware mashups in Linked Widgets but does not propose a structured data provenance model required for GDPR compliance.
entrytype: inproceedings
link: https://doi.org/10.1145/3308560.3317591
name: Privacy-aware Linked Widgets
organization: Vienna University of Economics and Business; Vienna University of Technology
place: Companion Proceedings of the World Wide Web Conference (WWW '19)
year: 2019
forward_steps: 2
---

# Fernández García, Javier D. et al. *Privacy-aware Linked Widgets.* 2019.

## Approach and Motivations

This paper introduces **privacy-aware Linked Widgets** designed to check **ex-ante GDPR compliance** in **Linked Data mashups**. It integrates the SPECIAL framework for **semantic-based consent and compliance tracking**.

Key contributions include:
- **Integration of SPECIAL policy language** into the Linked Widgets Platform (LWP).  
- **Dynamic ex-ante compliance checking** for consent policies using **OWL-based constraints**.  
- **Prototype implementation and evaluation** in the **smart energy building** case study.

Despite these contributions, the platform focuses on **consent and usage policy compliance**, but **does not propose a full data provenance model**, which is required for inclusion.

## Approach Contribution For The Compliance Questions

The Linked Widgets Platform enhances **consent compliance checking** but does not track data lineage. It addresses consent-related aspects:

### **CQ11 - Consent Validity**
- The system verifies that **data processing aligns with the recorded user consents**.

### **CQ21 - Informing Data Subjects of Rights**
- Tracks **consent and compliance metadata**.

### **CQ47 - Security Program Documentation**
- Provides **policy-based verification of workflows**.

## Approach Insufficiencies For Fulfilling Compliance Questions

### **CQ08 - Data Retention Periods**
- Does not implement **structured retention tracking**.

### **CQ29 - Retention Policies**
- Lacks **automated enforcement** of retention limits.

### **CQ51 - Data Erasure and Anonymization**
- No mechanism for **tracking or enforcing data deletion**.

### **CQ63 - Listing Data Transfers**
- The platform **does not track data transfers across components**.

### **CQ64 - Legal Basis for Data Transfers**
- Focuses on **consent checking**, not **legal documentation for data transfers**.

## Key Contributions

- **Ex-Ante Compliance:** Checks compliance **before data processing begins**.  
- **Consent Metadata Management:** Integrates **semantic vocabularies** for compliance checks.  
- **Prototype Implementation:** Demonstrates the **feasibility of dynamic GDPR compliance checks**.  

## State-of-the-Art

This study improves **semantic-based compliance checking** but lacks **data provenance mechanisms**. Unlike **data lineage models**, it **focuses on consent tracking**.

## Conclusion

The paper describes a privacy-aware mashup system that checks consent-based usage policies dynamically. However, it **does not propose a structured data provenance model**, making it **unrelated** to the inclusion criteria.

# References

- Fernández García, J. D., Ekaputra, F. J., Aryan, P. R., Kiesling, E., & Azzam, A. (2019). *Privacy-aware Linked Widgets.* Companion Proceedings of the World Wide Web Conference (WWW '19). Available at: [ACM Digital Library](https://doi.org/10.1145/3308560.3317591)
- [[fatema2017a]]
- [[kirrane2018a]]