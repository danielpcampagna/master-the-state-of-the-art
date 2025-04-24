---
ID: ahmadov2024a
authors: Ahmadov, Samur
category: unrelated
display: ahmadov (Data Encryption as a Method of Protecting Personal Data in a Cloud Environment)
due: The paper focuses on encryption techniques for cloud security and GDPR compliance but does not propose a data provenance model.
entrytype: article
link: https://doi.org/10.62660/bcstu/3.2024.31
name: Data Encryption as a Method of Protecting Personal Data in a Cloud Environment
organization: Cherkasy State Technological University
place: Bulletin of Cherkasy State Technological University
pp: 29(3), 31-41
provenance_related: false
related:
  - Cloud Security
  - Data Encryption
  - GDPR Compliance
  - Key Management
year: 2024
forward_steps: 2
---


# **Summary & Analysis**

## **Summary**

The paper **"Data Encryption as a Method of Protecting Personal Data in a Cloud Environment"** by **Samur Ahmadov** (2024) examines **encryption techniques used in cloud environments to enhance data security and meet legal compliance requirements**. The study focuses on **symmetric and asymmetric encryption methods**, their impact on **system performance**, and **their role in regulatory compliance, including GDPR**.

The main **contributions** of the paper include:

1. **Comparative analysis of encryption methods** in cloud environments, evaluating their performance, security levels, and efficiency.
2. **Discussion on encryption key management** challenges, highlighting **static vs. dynamic keys** and their role in multi-cloud setups.
3. **Review of regulatory requirements**, particularly GDPR and other international privacy laws.
4. **Case studies on encryption implementation in cloud providers like AWS, Microsoft Azure, and Google Cloud**.
5. **Recommendations for balancing encryption strength and performance in cloud security frameworks**.

### **Key Findings**

- **Encryption is essential for GDPR compliance**, but effective key management is crucial.
- **Symmetric encryption (e.g., AES)** is **faster and more efficient** but requires **secure key transfer**.
- **Asymmetric encryption (e.g., RSA)** ensures **stronger security for key exchange** but is **computationally expensive**.
- **Hybrid approaches** (combining symmetric and asymmetric methods) are commonly used in **cloud security frameworks**.
- **GDPR mandates encryption for data protection, but companies struggle with implementation challenges**.
- **Quantum encryption** may offer a **future-proof solution** but is currently **resource-intensive**.

### **Key Quotes**

- _“Encryption remains one of the most reliable ways to protect data in a cloud environment, but an integrated approach is needed for its effective application.”_ (Page 1)
- _“GDPR compliance requires robust encryption and proper key management, as failure to protect encryption keys may result in regulatory violations.”_ (Page 5)
- _“Amazon AWS, Microsoft Azure, and Google Cloud implement a combination of symmetric and asymmetric encryption to ensure high security in cloud services.”_ (Page 8)
- _“Key management remains the greatest challenge in encryption, as static keys risk exposure, while dynamic keys require frequent updates.”_ (Page 10)

---

# **Evaluation Based on Inclusion Criteria**

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - ❌ **No.** The paper discusses **encryption methods for data security** but **does not model data provenance**.
    - **Quote (Page 6):** _“Encryption techniques contribute to compliance but do not replace broader GDPR accountability frameworks.”_  
        ✅ **Fails Criterion #1** (No provenance model).
2. **Is the model useful for addressing GDPR compliance questions?**
    
    - ❌ **Partially.** The paper focuses on **encryption compliance under GDPR** but does **not provide a structured model for compliance tracking**.
    - **Quote (Page 7):** _“While encryption helps fulfill GDPR requirements, compliance is broader than technical safeguards.”_  
        ✅ **Fails Criterion #2** (No structured GDPR compliance tracking).
3. **Is the proposed model publicly available?**
    
    - ❌ **No.** The paper discusses **encryption techniques but does not provide an implementable framework**.  
        ✅ **Fails Criterion #3**.
4. **Is the document written in English or Portuguese?**
    
    - ✅ **Yes.** The paper is in **English**.  
        ✅ **Passes Criterion #4**.
5. **Is the document publicly available?**
    
    - ✅ **Yes.** The paper is **open access under a Creative Commons license**.  
        ✅ **Passes Criterion #5**.
6. **Is the document peer-reviewed?**
    
    - ✅ **Yes.** Published in a **peer-reviewed journal (Bulletin of Cherkasy State Technological University)**.  
        ✅ **Passes Criterion #6**.

### **Final Verdict**

🔴 **Category: "Unrelated"** – The paper **does not propose a GDPR data provenance model**, focusing instead on **cloud encryption strategies**.

---

# **Discussion on Compliance Questions**

The **paper addresses GDPR encryption requirements** but **does not comprehensively cover GDPR compliance questions (CQs)**.

|Compliance Question|Addressed?|Explanation|
|---|---|---|
|**CQ08 (Retention Periods)**|❌|No discussion on **retention periods** for encrypted data.|
|**CQ09 (Ensuring Compliance Actions)**|✅|Discusses **encryption as a GDPR compliance mechanism** but not **accountability tracking**.|
|**CQ11 (Consent Management)**|❌|No mention of **consent mechanisms**.|
|**CQ29 (Retention Policies)**|❌|Discusses **encryption policies**, but not **data retention frameworks**.|
|**CQ50 (Encryption for Data Security)**|✅|Analyzes encryption strategies for **cloud security and GDPR compliance**.|

### **Conclusion**

The paper **focuses on encryption techniques** but does **not provide a structured GDPR compliance model**.

---

# References

- [[matulevicius2020a]]