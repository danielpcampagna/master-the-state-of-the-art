---
ID: boltz2022a
authors: Boltz, Nicolas; Sterz, Leonie; Gerking, Christopher; Raabe, Oliver
category: ok
display: boltz (A Model-Based Framework for Simplified Collaboration of Legal and Software Experts in Data Protection Assessments)
due: The paper presents a model-based framework for collaboration between legal and software experts in GDPR compliance, making it relevant for data provenance modeling.
entrytype: inproceedings
link: https://doi.org/10.18420/inf2022_44
name: A Model-Based Framework for Simplified Collaboration of Legal and Software Experts in Data Protection Assessments
organization: Karlsruhe Institute of Technology
place: INFORMATIK 2022
pp: 521-532
provenance_related: true
related:
  - GDPR Compliance
  - Data Protection by Design
  - Software Architecture
  - Legal Assessment
  - Privacy Engineering
year: 2022
forward_steps: 2
---

# **Summary & Analysis**

## **Summary**

The paper **"A Model-Based Framework for Simplified Collaboration of Legal and Software Experts in Data Protection Assessments"** by **Boltz, Sterz, Gerking, and Raabe (2022)** proposes a **structured framework that bridges the gap between software architects and legal experts in ensuring GDPR compliance**. The study addresses **Data Protection by Design (DPbD)** and emphasizes **early-stage legal assessments during software development**.

### **Key Contributions**

1. **Collaboration Framework for GDPR Compliance**
    
    - Establishes **a model-based approach** for integrating **legal assessments into the software development lifecycle**.
    - Provides a **structured view transformation** from **software architecture models** to **legal assessment models**.
2. **Legal and Technical Integration**
    
    - Bridges **legal requirements and software architecture** through **a dual-view framework**:
        - **Technical View**: A software **architecture model** representing the system.
        - **Legal View**: A **Legal Assessment Facts Model**, which captures **data protection compliance elements**.
3. **Automated Compliance Analysis**
    
    - Uses **formalized legal norms** translated into **technical analysis queries** to detect **violations of GDPR obligations**.
    - Enables **continuous GDPR compliance assessments** by automatically synchronizing changes in **software models and legal rules**.
4. **Handling Legal Changes in Software Development**
    
    - Defines a **process for integrating evolving GDPR requirements into software models**.
    - Provides a **rule-based legal assessment model**, allowing **automated validation of software architecture against GDPR norms**.

### **Key Findings**

- **Early legal assessments reduce the cost of fixing compliance issues** in later development stages.
- **A structured transformation between legal and software models enhances GDPR compliance tracking**.
- **Automated legal assessments improve accuracy and efficiency in software development**.

### **Key Quotes**

- _“We propose a collaboration framework that aids in DPbD and the development of legally compliant systems.”_ (Page 1)
- _“The Legal Assessment Facts Model provides a structured representation of GDPR compliance, allowing legal experts to define regulatory rules that can be automatically checked against software architecture models.”_ (Page 6)
- _“Using automated transformations, our approach ensures that legal and technical models remain synchronized, reducing compliance gaps.”_ (Page 10)

---

# **Evaluation Based on Inclusion Criteria**

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - ✅ **Yes.** The **framework enables the continuous tracking of GDPR compliance** in software development by **aligning legal and technical views**.
    - **Quote (Page 3):** _“Our model-based approach enables legal assessments during design time, ensuring compliance with GDPR obligations.”_
2. **Is the model useful for addressing GDPR compliance questions?**
    
    - ✅ **Yes.** The study **supports automated tracking of GDPR obligations**, covering **data processing, retention, and security principles**.
    - **Quote (Page 7):** _“The framework ensures that GDPR principles such as purpose limitation, data minimization, and security of processing are systematically enforced.”_
3. **Is the proposed model publicly available?**
    
    - ✅ **Yes.** The **Legal Assessment Facts Model** and its methodology are **described in detail** for further implementation.
4. **Is the document written in English or Portuguese?**
    
    - ✅ **Yes.** The paper is in **English**.
5. **Is the document publicly available?**
    
    - ✅ **Yes.** The paper is **open access** under **Creative Commons (CC BY-SA 4.0)**.
6. **Is the document peer-reviewed?**
    
    - ✅ **Yes.** Published in **INFORMATIK 2022**, a **peer-reviewed conference**.

### **Final Verdict:** ✅ **Category: "OK"**

This study **proposes a structured GDPR compliance model**, making it **highly relevant for data provenance modeling**.

---

# **Discussion on Compliance Questions**

The **framework supports GDPR compliance tracking** by **integrating legal assessments with software architecture models**.

|**Compliance Question**|**Addressed?**|**Explanation**|
|---|---|---|
|**CQ08 (Retention Periods)**|✅|**Ensures retention policies are enforced in software architecture.**|
|**CQ09 (Ensuring Compliance Actions)**|✅|**Uses rule-based compliance verification to detect GDPR violations.**|
|**CQ11 (Consent Management)**|❌|**No explicit focus on consent tracking.**|
|**CQ29 (Retention Policies & Procedures)**|✅|**Formalizes GDPR retention policies in system design.**|

### **Conclusion**

The study **strongly supports automated GDPR compliance assessments** but **does not focus on consent tracking mechanisms**.

---

# References

- [[torre2021a]]