---
ID: hassett2022m
authors: Hassett, Peter
category: unrelated
due: The patent describes an e-consent tracking system but does not propose a full data provenance model required for GDPR compliance.
entrytype: patent
link: https://patents.google.com/patent/US11309065B2/en
name: Management and Tracking Solution for Specific Patient Consent Attributes and Permissions
organization: IQVIA Inc.
place: USPTO
year: 2022
forward_steps: 2
---

# Hassett, Peter. *Management and Tracking Solution for Specific Patient Consent Attributes and Permissions.* 2022.

## Approach and Motivations

This patent introduces an **e-consent management system** that enables **structured consent tracking** in **clinical research**. The system allows patients to **authorize, update, and withdraw consent**, while **generating manifests that document consent permissions over time**.

Key contributions include:
- **E-Consent System**: Tracks **patient permissions and consent status** dynamically.  
- **Manifest Generation**: Creates **structured metadata records** linking patient consent to **specific medical studies**.  
- **Consent Update Mechanism**: Allows patients to **revoke or modify** previously given consent.  
- **Clinical Research Application**: Designed for **managing consent across multiple research sites**.

Despite these contributions, the system **does not propose a comprehensive data provenance model**, which is a core requirement for inclusion.

## Approach Contribution For The Compliance Questions

The **e-consent tracking** approach primarily focuses on **managing user permissions**. Some GDPR compliance aspects are supported:

### **CQ11 - Consent Validity**
- The system maintains **structured metadata for consent events**, allowing **validity checks over time**.

### **CQ21 - Informing Data Subjects of Rights**
- Provides a **mechanism for updating and revoking consent**.

### **CQ47 - Security Program Documentation**
- Captures **consent attributes as structured data**, enabling **auditability**.

## Approach Insufficiencies For Fulfilling Compliance Questions

### **CQ08 - Data Retention Periods**
- Does not define **data retention policies**.

### **CQ29 - Retention Policies**
- Lacks a **structured mechanism** for enforcing data retention.

### **CQ51 - Data Erasure and Anonymization**
- Does **not track or enforce data erasure processes**.

### **CQ63 - Listing Data Transfers**
- The system **does not track historical data transfers**.

### **CQ64 - Legal Basis for Data Transfers**
- Focuses on **consent permissions**, not **legal justifications for data movement**.

## Key Contributions

- **E-Consent System**: Allows patients to **dynamically manage consent**.  
- **Consent Metadata Management**: Stores **structured data attributes** linked to consent decisions.  
- **Clinical Research Application**: Designed for **patient consent tracking in medical trials**.  

## State-of-the-Art

While this patent enhances **consent tracking capabilities**, it lacks **data lineage features**. Unlike **data provenance models**, this system **focuses on permissions rather than full accountability tracking**.

## Conclusion

The patent **presents an innovative consent management solution**, but it **does not propose a structured data provenance model** for GDPR compliance. Therefore, it is **unrelated** to the inclusion criteria.

# References

- Hassett, P. (2022). *Management and Tracking Solution for Specific Patient Consent Attributes and Permissions.* US Patent 11,309,065 B2. Available at: [Google Patents](https://patents.google.com/patent/US11309065B2/en)
- [[fatema2017a]]
