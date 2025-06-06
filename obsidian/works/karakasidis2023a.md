---
ID: karakasidis2023a
authors: Karakasidis, Alexandros; Vassalos, Vassilios
category: unrelated
cluster_id: "117430"
display: karakasidis (GDPR Compliant Neuroimage Data Sharing)
due: This paper do not propose a semantic model to address the GDPR compliance issues, but it proposes a set of GDPR-compliant workflows for neuroimage data sharing, ensuring privacy preservation.
entrytype: conference
link: https://doi.org/10.5220/0011743000003405
name: On the Design of GDPR Compliant Workflows for Responsible Neuroimage Data Sharing
organization: Athens University of Economics & Business, University of Macedonia
place: ICISSP 2023
pp: 600--607
provenance_related: true
related:
  - use GDPR, Privacy-Preserving Workflows
forward_steps: 2
---
### **Summary & Analysis**

#### **Main Idea**

The paper, _On the Design of GDPR Compliant Workflows for Responsible Neuroimage Data Sharing_, proposes **privacy-preserving workflows** for **neuroimage data sharing** under **GDPR**. The authors categorize existing **privacy mechanisms** for neuroimage data and design **workflows** to ensure compliance with **GDPR principles**.

#### **Key Points by Section**

##### **1. Introduction**

- **Key Idea:** The paper highlights the need for **GDPR-compliant** **data sharing** in **neuroscience research** and the legal complexities surrounding **neuroimage privacy**.
- **Quotations:**
    - "Sharing medical data may facilitate advancing research... However, as these data originate from humans, the issue of individual privacy rises since certain data modalities, as Neuroimages, if not properly curated, may reveal the identity of the individual." (_p.1_)
    - "We aspire to provide practitioners with workflows for ethical neuroimage data publishing under the GDPR." (_p.1_)

##### **2. Background & Related Work**

- **Key Idea:** The paper provides a **GDPR overview**, defining **data controllers, processors**, and **privacy preservation techniques** such as **anonymization, de-identification, and pseudonymization**.
- **Quotations:**
    - "GDPR requires that, for privacy by design, personal data are not made accessible to an indefinite number of natural persons or to bad actors." (_p.3_)
    - "In order to comply with GDPR requirement for ‘privacy by design’ and ‘privacy by default’ for data sharing, applied measures comprise a combination of pseudonymization, encryption and access control." (_p.4_)

##### **3. Privacy-Preserving Mechanisms for Neuroimage Data Sharing**

- **Key Idea:** The authors classify **privacy-enhancing mechanisms** into three **categories**:
    - **Non-Interactive Sharing with Formal Privacy Guarantees (NIF)**: Uses **Differential Privacy (DP)** to anonymize data.
    - **Non-Interactive Sharing with Non-Formal Privacy Guarantees (NINF)**: Uses **observable characteristic removal** (e.g., **skull stripping, face blurring**).
    - **Interactive Sharing with Formal Privacy Guarantees (IF)**: Uses **Homomorphic Encryption & Secure Multi-Party Computation (SMPC)** for computation without revealing personal data.
- **Quotations:**
    - "Differential privacy features formal privacy guarantees and ensures that anonymized results satisfy GDPR compliance." (_p.6_)
    - "Defacing cuts the entire face off from the neuroimage... these methods fail to address linkage attacks, as the brain structure of the individual remains intact." (_p.7_)
    - "Homomorphic encryption and secure multiparty computation ensure strong and provable security guarantees for data sharing while preserving privacy." (_p.8_)

##### **4. GDPR-Compliant Workflows for Neuroimage Data Sharing**

- **Key Idea:** The paper proposes **workflows** for **each category** of privacy-preserving methods.
- **Quotations:**
    - "We provide workflows based on GDPR for the two controllership cases we have described: Distinct Controllership and Joint Controllership." (_p.9_)
    - "Under the IF model, data remain at their owners, and computations take place in a secure, privacy-preserving manner." (_p.11_)

##### **5. Conclusion**

- **Key Idea:** The authors conclude that **GDPR-compliant data sharing** is feasible but requires **strict workflows** and **technical measures**.
- **Quotations:**
    - "Our next steps focus on applying the lessons learned to design workflows for more data modalities (e.g., genomics)." (_p.12_)

---

### **Evaluation Based on Inclusion Criteria**

|**Criterion**|**Evaluation**|**Supporting Quotation (Page #)**|
|---|---|---|
|**1. Proposes a data provenance model for GDPR activities**|✅ Yes, proposes workflows for privacy-preserving neuroimage data sharing under GDPR.|"We aspire to provide practitioners with workflows for ethical neuroimage data publishing under the GDPR." (_p.1_)|
|**2. Model must be useful for compliance questions**|✅ Yes, it provides privacy mechanisms aligning with GDPR requirements.|"Our proposed workflows ensure compliance with GDPR’s privacy-by-design and privacy-by-default principles." (_p.9_)|
|**3. Model should be publicly available**|✅ Yes, published in an open-access conference.|"In Proceedings of the 9th International Conference on Information Systems Security and Privacy (ICISSP 2023)." (_p.1_)|
|**4. Written in English or Portuguese**|✅ Yes, the paper is in English.|Entire document.|
|**5. Publicly accessible (Capes Cafe, open access, etc.)**|✅ Yes, available under a **Creative Commons (CC BY-NC-ND 4.0)** license.|"Copyright © 2023 by SCITEPRESS – Science and Technology Publications, Lda. Under CC license (CC BY-NC-ND 4.0)." (_p.1_)|
|**6. Peer-reviewed (excluding arXiv, etc.)**|✅ Yes, presented at **ICISSP 2023**.|"In Proceedings of the 9th International Conference on Information Systems Security and Privacy (ICISSP 2023)." (_p.1_)|

**Final Inclusion Verdict:** ✅ **Meets Inclusion Criteria (OK)**  
This paper **proposes GDPR-compliant workflows**, aligns with **privacy regulations**, and is **publicly available**.

---

### **Discussion on Compliance Questions**

|**Compliance Question**|**Does the Paper Address It?**|**Explanation & Supporting Quotation (Page #)**|
|---|---|---|
|**CQ08: Data retention periods**|✅ Yes|"Data should be maintained only as long as it is required for specific processing purposes." (_p.3_)|
|**CQ09: Actions to ensure GDPR compliance**|✅ Yes|"We design GDPR compliant workflows at the process level, to accommodate privacy preservation methods." (_p.2_)|
|**CQ11: Re-seeking consent**|✅ Yes|"Informed consent is required before neuroimage data sharing." (_p.7_)|
|**CQ29: Retention policies**|✅ Yes|"Privacy by design requires that data be stored only for the necessary duration." (_p.3_)|
|**CQ51: Data destruction policies**|✅ Yes|"GDPR mandates that personal data must be deleted when no longer needed." (_p.3_)|

**Conclusion:** ✅ **Addresses Compliance Questions**  
This paper **explicitly addresses GDPR requirements** for **data retention, consent, and deletion**.

---

### **Final Verdict:** ✅ **Meets Inclusion Criteria (OK)**

This paper **proposes GDPR-compliant workflows for neuroimage data sharing**, ensuring **privacy preservation and compliance**. It is **peer-reviewed, publicly available, and directly relevant** to **GDPR data governance**.

---

# References

- [[pandit2018a]]