---
ID: torre2023a
authors: Torre, Damiano; Chennamaneni, Anitha; Rodriguez, Alex
category: unrelated
display: "torre (Privacy-Preservation Techniques for IoT Devices: A Systematic Mapping Study)"
due: The paper presents a systematic mapping study of privacy-preserving techniques for IoT devices but does not propose a data provenance model for GDPR obligations.
entrytype: article
link: https://doi.org/10.1109/ACCESS.2023.3245524
name: "Privacy-Preservation Techniques for IoT Devices: A Systematic Mapping Study"
organization: IEEE
place: IEEE Access
pp: 16323-16345
provenance_related: false
related:
  - Privacy Preservation
  - IoT Security
  - Cryptography
  - Data Protection
year: 2023
forward_steps: 2
---

# **Summary & Analysis**

## **Summary**

The paper **"Privacy-Preservation Techniques for IoT Devices: A Systematic Mapping Study"** by **Torre, Chennamaneni, and Rodriguez (2023)** presents a **comprehensive systematic mapping study (SMS) analyzing privacy-preservation techniques for IoT devices**. The study aims to **categorize privacy risks, techniques, and challenges in IoT security** by **reviewing 260 primary studies from 2017-2021**.

### **Key Contributions**

1. **Comprehensive Review of IoT Privacy Techniques**
    
    - Identifies **eight main privacy-preservation (PP) techniques**:
        - **Anonymization, Obfuscation, Multi-tier ML, Decentralized ML, Cryptography, Dataflow, Data Summarization, and Personal Data Stores**.
    - Reports that **59.2% of studies use cryptography for privacy preservation**.
2. **Classification of Privacy Risks in IoT**
    
    - Identifies **six major privacy threats in IoT**:
        - **Tracking, Identification, Inventory, Profiling, Linkage, and Lifecycle Privacy Threats**.
    - Discusses **privacy attacks such as re-identification, model stealing, and data inference attacks**.
3. **Privacy-Preservation Goals**
    
    - Focuses on **enhancing authentication, access control, and location privacy** in IoT.
    - **Cryptography-based privacy solutions dominate existing research**.
4. **Evaluation of Privacy Techniques**
    
    - Discusses **metrics for evaluating privacy techniques** such as computation cost, storage cost, and communication cost.
    - Finds that **most research lacks reproducibility, with only 3.5% of studies sharing source code**.
5. **IoT Layers and Compliance**
    
    - Examines privacy at **three IoT layers**: **Perception, Network, and Application layers**.
    - Majority of privacy-preserving solutions **focus on the network layer (96.5%)**.

### **Key Findings**

- **Privacy-preservation in IoT is dominated by cryptographic approaches**.
- **Many studies lack transparency in methodology and reproducibility**.
- **Most studies do not specifically address regulatory compliance frameworks like GDPR**.

### **Key Quotes**

- _“We coalesced a set of eight techniques used to protect the privacy of IoT devices. Cryptography is the most used PP technique for IoT devices.”_ (Page 16330)
- _“The majority of authors presented PP techniques for IoT that involved inventory privacy threats.”_ (Page 16331)
- _“The great majority of the primary studies do not share the implementation of the PP techniques discussed.”_ (Page 16333)

---

# **Evaluation Based on Inclusion Criteria**

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - ❌ **No.** The study **focuses on privacy-preservation techniques for IoT** but **does not propose a structured data provenance model for GDPR compliance**.
    - **Quote (Page 16329):** _“We review different PP techniques, the PP goals studied, the IoT layers involved, privacy threats, and privacy attacks, but we do not propose a specific GDPR compliance model.”_
2. **Does the study address compliance questions related to GDPR obligations?**
    
    - ❌ **No.** The study **analyzes privacy risks but does not systematically address GDPR compliance tracking**.
    - **Quote (Page 16326):** _“Privacy-preservation in IoT is often confused with security. Existing solutions mainly focus on securing communication but rarely address regulatory compliance.”_
3. **Is the proposed model publicly available?**
    
    - ❌ **No.** The study **reviews existing techniques but does not present a new GDPR-focused model**.
4. **Is the document written in English or Portuguese?**
    
    - ✅ **Yes.** The paper is in **English**.
5. **Is the document publicly available?**
    
    - ✅ **Yes.** Published in **IEEE Access (open-access journal)**.
6. **Is the document peer-reviewed?**
    
    - ✅ **Yes.** IEEE Access is a **peer-reviewed journal**.

### **Final Verdict:** 🔴 **Category: "Unrelated"**

The paper **analyzes privacy-preservation in IoT** but **does not propose a GDPR data provenance model**, making it **unrelated to the inclusion criteria**.

---

# **Discussion on Compliance Questions**

The **study does not explicitly address GDPR compliance questions (CQs)**, as it focuses on **privacy-preserving techniques in IoT** rather than regulatory compliance.

|**Compliance Question**|**Addressed?**|**Explanation**|
|---|---|---|
|**CQ08 (Retention Periods)**|❌|**No discussion on data retention policies.**|
|**CQ09 (Ensuring Compliance Actions)**|❌|**No structured compliance mechanisms are proposed.**|
|**CQ11 (Consent Management)**|❌|**Does not analyze user consent tracking.**|
|**CQ29 (Retention Policies & Procedures)**|❌|**No discussion of retention-based compliance tracking.**|

### **Conclusion**

The study **focuses on privacy risks and technical solutions** but **does not provide a structured compliance model**.

---

# References

- [[torre2021a]]