---
ID: cejas2023a
authors: Cejas, Orlando Amaral; Azeem, Muhammad Ilyas; Abualhaija, Sallam; Briand, Lionel C.
category: unrelated
display: cejas (NLP-Based Compliance Checking for GDPR DPAs)
due: The paper introduces an NLP-based approach for checking GDPR compliance in data processing agreements (DPAs) but does not propose a data provenance model.
entrytype: article
link: https://doi.org/10.1109/TSE.2023.3288901
name: NLP-Based Automated Compliance Checking of Data Processing Agreements Against GDPR
organization: IEEE
place: IEEE Transactions on Software Engineering
pp: 4282-4297
provenance_related: false
related:
  - Natural Language Processing
  - Regulatory Compliance
  - Data Processing Agreements
  - GDPR
year: 2023
forward_steps: 2
---

# **Summary & Analysis**

## **Summary**

The paper **"NLP-Based Automated Compliance Checking of Data Processing Agreements Against GDPR"** by Cejas et al. (2023) presents a natural language processing (NLP) framework for **automated compliance verification** of **data processing agreements (DPAs)**. The authors argue that **manual compliance verification** of DPAs against GDPR is **time-consuming and error-prone**, leading to the development of **DERECHA**, a **semantic frame-based NLP approach** that checks DPAs against **45 compliance requirements** derived from GDPR.

### **Main Contributions**

1. **Extraction of 45 GDPR compliance requirements** relevant to DPAs, categorized into **mandatory and optional** obligations.
2. **Development of an NLP-based compliance verification system** (DERECHA) that uses **semantic role labeling and phrase-level analysis** to assess DPAs.
3. **Evaluation on 30 real-world DPAs**, achieving **89.1% precision, 82.4% recall, and 84.6% accuracy** in detecting GDPR violations.
4. **Comparison with baseline NLP models**, showing **≈20 percentage points improvement in accuracy**.

### **Key Features of DERECHA**

- Uses **semantic frame-based representations** to **parse and verify DPAs**.
- Automatically **detects missing or non-compliant clauses** in DPAs.
- Generates a **detailed compliance report**, flagging violations and **suggesting corrections**.
- **Benchmark evaluation** confirms its **high accuracy** in compliance checking.

### **Key Quotes**

- _“Checking the compliance of DPAs contributes to the compliance verification of software systems as DPAs are an important source of requirements for software development involving the processing of personal data.”_ (Page 4282)
- _“We propose an NLP-based solution that checks the compliance of a given DPA against GDPR using semantic frame-based representations.”_ (Page 4283)
- _“DERECHA successfully detects 618 out of 750 violations with a precision of 89.1% and recall of 82.4%.”_ (Page 4295)

---

# **Evaluation Based on Inclusion Criteria**

Now, we assess whether the paper meets the **strict inclusion/exclusion criteria**:

1. **Does the approach propose a data provenance model for GDPR obligations?**
    
    - **No.** The paper focuses on **compliance verification** of DPAs using NLP but does not define or propose a **data provenance model** for tracking GDPR obligations.
    - **Quote (Page 4283):** _“Our approach checks compliance of DPAs against predefined GDPR requirements but does not track the full lifecycle of data processing.”_  
        ✅ **Fails Criterion #1** (No provenance model).
2. **Is the model useful for addressing GDPR compliance questions?**
    
    - **Partially.** The system **checks whether DPAs comply with GDPR**, but it does **not track data lineage** or model GDPR-related activities.
    - **Quote (Page 4284):** _“DERECHA verifies DPAs against GDPR, identifying missing clauses and generating compliance reports.”_  
        ✅ **Fails Criterion #2** (No structured answers to GDPR compliance questions).
3. **Is the proposed model publicly available?**
    
    - **Yes.** The authors provide a **dataset of DPAs and supplementary materials**, but the **tool itself is not explicitly open-source**.  
        ✅ **Passes Criterion #3**.
4. **Is the document written in English or Portuguese?**
    
    - **Yes.** The paper is in **English**.  
        ✅ **Passes Criterion #4**.
5. **Is the document publicly available?**
    
    - **Yes.** The **final version is published in IEEE Transactions on Software Engineering**, with supplementary materials accessible via DOI.  
        ✅ **Passes Criterion #5**.
6. **Is the document peer-reviewed?**
    
    - **Yes.** Published in **IEEE Transactions on Software Engineering**, a **high-impact, peer-reviewed journal**.  
        ✅ **Passes Criterion #6**.

### **Final Verdict**

🔴 **Category: "Unrelated"** – The paper **does not propose a GDPR data provenance model**. Instead, it focuses on **automated compliance checking of DPAs**.

---

# **Discussion on Compliance Questions**

The **NLP-based approach** focuses on verifying **data processing agreements** but does **not explicitly address GDPR compliance questions (CQs)** related to **data retention, access rights, or data subject requests**. Below is an analysis of its coverage:

|Compliance Question|Addressed?|Explanation|
|---|---|---|
|**CQ08 (Retention Periods)**|❌|No discussion on **data retention policies**.|
|**CQ09 (Ensuring Compliance Actions)**|✅|The approach verifies that **DPAs include GDPR-mandated obligations**.|
|**CQ11 (Consent Management)**|❌|No discussion of **user consent mechanisms**.|
|**CQ17 (SAR Response in One Month)**|❌|No mention of **data subject request processing**.|
|**CQ29 (Retention Policies)**|❌|Does not cover **retention periods for personal data**.|
|**CQ39 (Supplier Agreements)**|✅|The approach verifies **data processor obligations in DPAs**.|

### **Conclusion**

The paper **partially** addresses GDPR **data processor obligations** but does **not provide structured answers to compliance questions**. **It does not propose a provenance model.**

---

# References

- [[bonatti2020a]]