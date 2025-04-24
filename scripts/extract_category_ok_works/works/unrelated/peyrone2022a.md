---
ID: peyrone2022f
authors: Peyrone, Neda
category: unrelated
due: The dissertation proposes formal models for consent management but does not introduce a full data provenance model required for GDPR compliance.
entrytype: thesis
link: https://digital.car.chula.ac.th/chulaetd/5803
name: Formal Models for Consent Management in Healthcare Software System Development
organization: Chulalongkorn University
place: PhD Dissertation
year: 2022
forward_steps: 2
---

# Peyrone, Neda. *Formal Models for Consent Management in Healthcare Software System Development.* 2022.

## Approach and Motivations

This dissertation introduces **formal models for consent management** in **healthcare software systems**, focusing on **GDPR-compliant consent tracking mechanisms**.

Key contributions include:
- **State-machine-based consent models** for **tracking approvals, withdrawals, and renewals**.
- **Implementation of formal verification using Event-B** to **prove correctness**.
- **Integration of consent models into centralized and distributed systems**.

Despite these contributions, the dissertation **does not propose a comprehensive data provenance model**, which is a strict requirement for inclusion.

## Approach Contribution For The Compliance Questions

The research primarily focuses on **consent tracking**, but some **GDPR-related issues** are addressed:

### **CQ11 - Consent Validity**
- Proposes a **formalized approach for tracking consent events**.

### **CQ21 - Informing Data Subjects of Rights**
- Implements a **consent lifecycle model** aligned with GDPR requirements.

### **CQ47 - Security Program Documentation**
- Uses **formal verification (Event-B)** to **ensure correctness in consent tracking**.

## Approach Insufficiencies For Fulfilling Compliance Questions

### **CQ08 - Data Retention Periods**
- No structured framework for **data retention tracking**.

### **CQ29 - Retention Policies**
- Lacks **automated retention enforcement mechanisms**.

### **CQ51 - Data Erasure and Anonymization**
- Does **not provide systematic tracking of erased data**.

### **CQ63 - Listing Data Transfers**
- Does **not explicitly track** personal **data movement**.

### **CQ64 - Legal Basis for Data Transfers**
- The work **focuses on consent modeling**, not **legal documentation for data transfers**.

## Key Contributions

- **Event-B Formal Verification:** Ensures **logical correctness** in consent processing.  
- **State-Machine-Based Consent Models:** Provides a **framework for tracking consent changes**.  
- **Application to Healthcare Systems:** Focuses on **GDPR-compliant medical data handling**.  

## State-of-the-Art

While this study **advances consent management research**, it lacks **data lineage tracking**. Unlike **data provenance models**, this work **centers on consent enforcement rather than full accountability mechanisms**.

## Conclusion

This dissertation **presents formal models for consent tracking**, but it **does not introduce a structured data provenance model** for GDPR compliance. Therefore, it is **unrelated** to the inclusion criteria.

# References

- Peyrone, N. (2022). *Formal Models for Consent Management in Healthcare Software System Development.* PhD Dissertation, Chulalongkorn University. Available at: [Chula Digital Collections](https://digital.car.chula.ac.th/chulaetd/5803)
- [[fatema2017a]]
