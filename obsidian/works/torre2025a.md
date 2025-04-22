---
ID: torre2025a
authors: Torre, Damiano; Chennamaneni, Anitha; Jo, Jaeyun; Vyas, Gitika; Sabrsula, Brandon
category: unrelated
display: "torre (Toward Enhancing Privacy Preservation of a Federated Learning CNN Intrusion Detection System in IoT: Method and Empirical Study)"
due: The paper focuses on privacy preservation in Federated Learning for IoT Intrusion Detection Systems but does not propose a data provenance model for GDPR obligations.
entrytype: article
link: https://doi.org/10.1145/3695998
name: "Toward Enhancing Privacy Preservation of a Federated Learning CNN Intrusion Detection System in IoT: Method and Empirical Study"
organization: ACM
place: ACM Transactions on Software Engineering and Methodology
pp: 53:1-53:48
provenance_related: false
related:
  - Federated Learning
  - Privacy Preservation
  - Intrusion Detection
  - Differential Privacy
  - Homomorphic Encryption
year: 2025
forward_steps: 2
---

# **Summary & Analysis**

## **Summary**

The paper **"Toward Enhancing Privacy Preservation of a Federated Learning CNN Intrusion Detection System in IoT: Method and Empirical Study"** by **Torre et al. (2025)** focuses on **improving privacy preservation in Federated Learning (FL) for Intrusion Detection Systems (IDS) in IoT environments**. The study **introduces a CNN-based FL model** and **implements three privacy-preserving (PP) techniques**:

1. **Differential Privacy (DP)** – Adds noise to training data to prevent adversarial learning.
2. **Diffie–Hellman Key Exchange (DK)** – Ensures secure key sharing between clients.
3. **Homomorphic Encryption (HE)** – Allows computations on encrypted data without decryption.

The study **evaluates the FL-based IDS on seven IoT datasets** (TON-IoT, IoT-23, BoT-IoT, CIC IoT 2023, CIC IoMT 2024, RT-IoT 2022, EdgeIIoT) and **compares its performance with other AI-based IDS models**.

### **Key Contributions**

1. **Privacy-Preserving Federated Learning Model**
    
    - Implements a **CNN-based FL system** for **detecting cyber threats in IoT networks**.
    - Uses **three layers of privacy-preserving techniques** to enhance security.
2. **Evaluation on Real-World IoT Datasets**
    
    - Tests the approach on **seven widely used IoT datasets**.
    - Measures **accuracy, precision, recall, and F1-score** for intrusion detection.
3. **Comparative Analysis of IDS Approaches**
    
    - Compares the proposed **CNN-FL IDS** with **other ML-based IDS models**.
    - Demonstrates **high detection accuracy** while maintaining privacy.
4. **Performance Assessment of Privacy Techniques**
    
    - Evaluates **computational overhead of privacy-preserving methods**.
    - Reports a **10% increase in computation time** due to privacy mechanisms.

### **Key Findings**

- **CNN-based FL IDS achieves an average accuracy of 97.31%** across all datasets.
- **Implementing DP, DK, and HE adds minimal overhead (10%)**, making it feasible for real-world deployment.
- **Privacy techniques effectively enhance security** without compromising detection performance.

### **Key Quotes**

- _“To improve the security of FL systems, this article proposes an IDS leveraging an FL CNN that implements three PP algorithms: Differential Privacy, Diffie–Hellman Key Exchange, and Homomorphic Encryption.”_ (Page 3)
- _“Our empirical evaluation demonstrates that integrating privacy techniques only incurs a 10% increase in computation time, ensuring feasibility in real-world scenarios.”_ (Page 17)
- _“Our approach outperforms previous AI-based IDSs, achieving superior accuracy while preserving data privacy.”_ (Page 25)

---

# **Evaluation Based on Inclusion Criteria**

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - ❌ **No.** The study **focuses on privacy preservation in Federated Learning** rather than **data provenance modeling for GDPR compliance**.
    - **Quote (Page 1):** _“This work enhances privacy in Federated Learning-based IDSs, addressing security concerns in IoT networks.”_
2. **Does the study address GDPR compliance questions?**
    
    - ❌ **No.** The paper discusses **privacy preservation techniques** but does **not systematically address GDPR obligations**.
    - **Quote (Page 5):** _“The focus of this study is on securing FL models rather than legal compliance frameworks.”_
3. **Is the proposed model publicly available?**
    
    - ❌ **No.** The study provides **empirical results** but **does not release an open-source implementation of the model**.
4. **Is the document written in English or Portuguese?**
    
    - ✅ **Yes.** The paper is in **English**.
5. **Is the document publicly available?**
    
    - ✅ **Yes.** Published in **ACM Transactions on Software Engineering and Methodology**, a **publicly accessible journal**.
6. **Is the document peer-reviewed?**
    
    - ✅ **Yes.** Published in **a peer-reviewed ACM journal**.

### **Final Verdict:** 🔴 **Category: "Unrelated"**

The study **focuses on Federated Learning and privacy in IoT** but **does not propose a GDPR data provenance model**, making it **unrelated to the inclusion criteria**.

---

# **Discussion on Compliance Questions**

The **study does not explicitly address GDPR compliance questions (CQs)** since its focus is on **privacy-enhancing techniques for Federated Learning-based IDS**.

|**Compliance Question**|**Addressed?**|**Explanation**|
|---|---|---|
|**CQ08 (Retention Periods)**|❌|**No discussion on data retention policies.**|
|**CQ09 (Ensuring Compliance Actions)**|❌|**No structured compliance mechanisms are proposed.**|
|**CQ11 (Consent Management)**|❌|**Does not analyze user consent tracking.**|
|**CQ29 (Retention Policies & Procedures)**|❌|**No discussion of GDPR retention policies.**|

### **Conclusion**

The study **focuses on Federated Learning security** rather than **compliance tracking or provenance modeling**.

---

# References

- [[torre2021a]]