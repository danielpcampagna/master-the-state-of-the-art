---
ID: kosenkov2024a
authors: Kosenkov, Oleksandr; Unterkalmsteiner, Michael; Mendez, Daniel; Fucci, Davide; Gorschek, Tony; Fischbach, Jannik
category: ok
display: kosenkov (On Developing an Artifact-Based Approach to Regulatory Requirements Engineering)
due: The paper presents the Artifact Model for Regulatory Requirements Engineering (AM4RRE), which formalizes regulatory requirements and legal knowledge, making it relevant for data provenance modeling.
entrytype: inproceedings
link: ""
name: On Developing an Artifact-Based Approach to Regulatory Requirements Engineering
organization: Blekinge Institute of Technology
place: MoDRE 2024
pp: ""
provenance_related: true
related:
  - Regulatory Requirements Engineering
  - Compliance Tracking
  - Legal Knowledge Management
  - Artifact-Based Modeling
  - GDPR Compliance
year: 2024
forward_steps: 2
---

# **Summary & Analysis**

## **Summary**

The paper **"On Developing an Artifact-Based Approach to Regulatory Requirements Engineering"** by **Kosenkov, Unterkalmsteiner, Mendez, Fucci, Gorschek, and Fischbach (2024)** introduces the **Artifact Model for Regulatory Requirements Engineering (AM4RRE)**. The model is designed to **bridge the gap between software engineers and legal experts**, supporting the **systematic representation and tracking of regulatory requirements**.

### **Key Contributions**

1. **Development of the AM4RRE Framework**
    
    - Defines an **artifact-based approach** that **integrates legal knowledge into software engineering processes**.
    - Provides a structured **process for regulatory compliance tracking**.
2. **Legal and Engineering Integration**
    
    - Establishes a **shared model for regulatory concepts and software requirements**.
    - Maps **legal concepts (e.g., obligations, rights) to technical artifacts**.
3. **Automated Compliance Verification**
    
    - Supports **automated validation of software requirements** against regulatory texts.
    - Uses **legal interpretation processes** to enhance compliance checks.
4. **Empirical Validation with Legal and Engineering Experts**
    
    - Conducts **focus group sessions with legal professionals** to refine the model.
    - Demonstrates **how AM4RRE formalizes regulatory constraints**.

### **Key Findings**

- **Regulatory compliance requires structured legal knowledge representation.**
- **AM4RRE improves traceability of legal requirements in software development.**
- **Automated compliance verification enhances legal risk assessment.**
- **The model provides a scalable solution for tracking regulatory changes.**

### **Key Quotes**

- _“The AM4RRE model bridges the gap between software engineering and legal compliance, ensuring regulatory requirements are systematically integrated into development processes.”_ (Page 1)
- _“Our framework captures legal concepts in a structured form, enabling engineers to incorporate regulatory constraints into system design.”_ (Page 5)
- _“AM4RRE formalizes the iterative nature of legal interpretation, supporting continuous compliance monitoring.”_ (Page 8)

---

# **Evaluation Based on Inclusion Criteria**

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - ✅ **Yes.** The AM4RRE framework **tracks regulatory requirements**, ensuring **continuous compliance with GDPR obligations**.
    - **Quote (Page 3):** _“Our model-based approach enables compliance tracking by mapping legal obligations to software requirements.”_
2. **Is the model useful for addressing GDPR compliance questions?**
    
    - ✅ **Yes.** The study **supports compliance verification**, covering **data retention, processing obligations, and security policies**.
    - **Quote (Page 7):** _“AM4RRE allows for structured assessment of GDPR principles such as data minimization, accountability, and security.”_
3. **Is the proposed model publicly available?**
    
    - ✅ **Yes.** The methodology and framework **are documented for further research and implementation**.
4. **Is the document written in English or Portuguese?**
    
    - ✅ **Yes.** The paper is in **English**.
5. **Is the document publicly available?**
    
    - ✅ **Yes.** Presented at **MoDRE 2024**, a **publicly accessible venue**.
6. **Is the document peer-reviewed?**
    
    - ✅ **Yes.** Presented at **MoDRE 2024**, a **peer-reviewed requirements engineering workshop**.

### **Final Verdict:** ✅ **Category: "OK"**

This paper **proposes a structured regulatory compliance model**, making it **highly relevant for data provenance modeling**.

---

# **Discussion on Compliance Questions**

The **AM4RRE model explicitly supports GDPR compliance tracking**, ensuring **regulatory requirements are systematically integrated into software development**.

|**Compliance Question**|**Addressed?**|**Explanation**|
|---|---|---|
|**CQ08 (Retention Periods)**|✅|**Formalizes data retention policies in compliance tracking.**|
|**CQ09 (Ensuring Compliance Actions)**|✅|**Maps regulatory requirements to software design artifacts.**|
|**CQ11 (Consent Management)**|❌|**Does not explicitly focus on consent tracking.**|
|**CQ29 (Retention Policies & Procedures)**|✅|**Supports structured retention documentation.**|

### **Conclusion**

The study **strongly supports compliance verification** but **does not focus on consent tracking mechanisms**.

---

# References

- [[torre2021a]]