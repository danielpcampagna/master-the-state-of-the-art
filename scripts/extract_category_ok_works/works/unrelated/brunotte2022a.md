---
ID: brunotte2022a
authors: Brunotte, Wasja; Chazette, Larissa; Köhler, Lukas; Klünder, Jil; Schneider, Kurt
category: unrelated
display: brunotte (Helping Users Understand Online Privacy Policies)
due: The paper introduces a tool for analyzing and explaining online privacy policies but does not propose a data provenance model for GDPR obligations.
entrytype: inproceedings
link: https://doi.org/10.1145/3529320.3529327
name: What About My Privacy? Helping Users Understand Online Privacy Policies
organization: ACM
place: International Conference on Software and System Processes (ICSSP'22)
pp: 1-10
provenance_related: false
related:
  - Privacy Policies
  - GDPR Compliance
  - Explainability
  - User Awareness
year: 2022
forward_steps: 2
---

# **Summary & Analysis**

## **Summary**

The paper **"What About My Privacy? Helping Users Understand Online Privacy Policies"** by **Wasja Brunotte et al. (2022)** introduces **PriX**, a **browser extension** designed to **help users understand online privacy policies** by providing **automated analysis and visual explanations**.

### **Key Contributions**

1. **PriX – Online Privacy Policy eXplainer**
    
    - A browser extension that **automatically detects and analyzes privacy policies**.
    - Provides **visual explanations** to help users **understand privacy policies more easily**.
2. **Privacy Policy Analysis**
    
    - Uses **machine learning classification algorithms** trained on the **OPP-115 corpus** (a dataset of privacy policies).
    - **Automatically categorizes privacy policies** into key areas such as **data collection, third-party sharing, data security, and user rights**.
3. **Evaluation with End Users**
    
    - A **user study with 65 participants** showed that PriX:
        - **Reduces time spent searching for privacy policies**.
        - **Improves user comprehension of privacy policy content**.
        - **Increases user awareness of data collection practices**.

### **Key Findings**

- **Privacy policies are often too long and difficult to understand**.
- **Users rarely read privacy policies** due to **complexity and lack of accessibility**.
- **Providing visual explanations significantly improves user understanding**.
- **Users support the idea of automated tools for privacy policy analysis**.

### **Key Quotes**

- _“Privacy policies are extensive and purposefully obfuscating. Information about data practices is hidden in long, vague, and ambiguous text passages.”_ (Page 1)
- _“The primary goal of PriX is to help users find and comprehend privacy policies through automated analysis and visual explanations.”_ (Page 3)
- _“User studies show that PriX reduces the time needed to find a privacy policy and improves the user’s ability to understand its content.”_ (Page 7)

---

## **Evaluation Based on Inclusion Criteria**

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - ❌ **No.** The study focuses on **privacy policy explainability** but does **not introduce a structured data provenance model**.
    - **Quote (Page 3):** _“PriX helps users understand privacy policies but does not track data provenance.”_  
        ✅ **Fails Criterion #1** (No provenance model).
2. **Is the model useful for addressing GDPR compliance questions?**
    
    - ❌ **No.** While the paper discusses **privacy policies**, it does **not provide a structured approach to answering GDPR compliance questions**.
    - **Quote (Page 6):** _“PriX provides explanations for privacy policies but does not serve as a compliance verification tool.”_  
        ✅ **Fails Criterion #2** (No structured GDPR compliance tracking).
3. **Is the proposed model publicly available?**
    
    - ❌ **No.** PriX is described, but the **paper does not provide a publicly available implementation**.  
        ✅ **Fails Criterion #3**.
4. **Is the document written in English or Portuguese?**
    
    - ✅ **Yes.** The paper is in **English**.  
        ✅ **Passes Criterion #4**.
5. **Is the document publicly available?**
    
    - ✅ **Yes.** The paper is **open access via ACM**.  
        ✅ **Passes Criterion #5**.
6. **Is the document peer-reviewed?**
    
    - ✅ **Yes.** Published in the **peer-reviewed ICSSP conference proceedings**.  
        ✅ **Passes Criterion #6**.

### **Final Verdict**

🔴 **Category: "Unrelated"** – The paper **does not propose a GDPR data provenance model**, focusing instead on **privacy policy explainability**.

---

# **Discussion on Compliance Questions**

While the study **relates to GDPR compliance through privacy policies**, it **does not systematically address compliance questions (CQs)**.

|Compliance Question|Addressed?|Explanation|
|---|---|---|
|**CQ08 (Retention Periods)**|❌|No discussion on **data retention policies**.|
|**CQ09 (Ensuring Compliance Actions)**|❌|Does not focus on **compliance enforcement**.|
|**CQ11 (Consent Management)**|❌|No mention of **consent verification**.|
|**CQ29 (Retention Policies)**|❌|No structured **GDPR retention tracking**.|
|**CQ33 (User Awareness & Transparency)**|✅|Discusses **privacy transparency** but does not track compliance.|

### **Conclusion**

The paper **focuses on privacy policy explainability** but **does not provide a structured GDPR compliance model**.

---

# References

- [[matulevicius2020a]]