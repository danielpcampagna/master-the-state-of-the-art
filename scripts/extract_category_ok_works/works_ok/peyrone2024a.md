---
ID: peyrone2024a
name: A Formal Model for Integrating Consent Management into MLOps
authors: Neda Peyrone, Duangdao Wichadakul
year: 2024
category: ok
due: The paper proposes a formal model for integrating consent management into MLOps, directly addressing GDPR compliance concerns. It introduces a consent management framework that tracks data subject rights, integrates privacy by design, and includes a structured approach for compliance monitoring.
forward_steps: 2
---

## **Evaluation Against Inclusion Criteria**

1. **Does the paper propose a data provenance model to represent activities related to GDPR obligations?**  
   - ✅ Yes. The paper presents a **formal model for consent management (CM)** that integrates into MLOps and ensures GDPR compliance&#8203;:contentReference[oaicite:0]{index=0}.  
   - It explicitly discusses **data subject rights tracking, consent status monitoring, and privacy by design (PbD) principles** in data pipelines&#8203;:contentReference[oaicite:1]{index=1}.  

2. **Is the proposed model useful to address the compliance questions?**  
   - ✅ Yes. The **Event-B-based formal model** defines **consent validation, revocation, and renewal mechanisms**, ensuring that ML systems adhere to GDPR principles&#8203;:contentReference[oaicite:2]{index=2}.  
   - It provides **a mapping to GDPR articles**, addressing the compliance lifecycle.  

3. **Is the proposed model publicly available for comparison?**  
   - ✅ Yes. The **Event-B model and class diagram** are provided in the paper for implementation&#8203;:contentReference[oaicite:3]{index=3}.  

4. **Is the document written in English or Portuguese?**  
   - ✅ Yes, the paper is in English.  

5. **Is the document publicly available or within CAPES CAFE-signed digital libraries?**  
   - ✅ Yes, it is available in **IEEE Access**, which is widely indexed&#8203;:contentReference[oaicite:4]{index=4}.  

6. **Is it a peer-reviewed document?**  
   - ✅ Yes, it is published in a **peer-reviewed journal**.  

**Final Verdict:** ✅ *Category: OK*  
- The paper presents a **formal GDPR compliance model** focusing on **consent tracking** and **MLOps integration**, making it **highly relevant** for GDPR-related research.  

---

## **Analysis Against GDPR Compliance Questions (CQ08-CQ65)**

### **Potentially Relevant GDPR Aspects**
The paper introduces **Event-B-based compliance verification**, **privacy by design**, and **machine unlearning techniques** to **manage personal data rights**. Below is an evaluation:

| **Compliance Question** | **Relevance** | **Analysis** |
|------------------------|-------------|-------------|
| **CQ08: Retention periods** | ✅ Yes | The model includes retention controls and compliance tracking&#8203;:contentReference[oaicite:5]{index=5}. |
| **CQ09: Required actions for GDPR compliance** | ✅ Yes | Defines automated **consent monitoring** and **data subject rights management**. |
| **CQ11: Consent management** | ✅ Yes | Directly addresses **consent acquisition, renewal, and withdrawal**, mapped to GDPR articles&#8203;:contentReference[oaicite:6]{index=6}. |
| **CQ17: Subject Access Requests (SARs)** | ✅ Yes | The model supports SARs by ensuring **data accessibility and auditability**&#8203;:contentReference[oaicite:7]{index=7}. |
| **CQ20: Halting processing on request** | ✅ Yes | Ensures data processing **stops upon consent withdrawal**. |
| **CQ25: Documenting restrictions on data protection rights** | ✅ Yes | Provides a **structured compliance verification approach**. |
| **CQ28: Ensuring data accuracy and updates** | ✅ Yes | Includes **mechanisms to track data accuracy and updates**&#8203;:contentReference[oaicite:8]{index=8}. |
| **CQ29: Retention policies** | ✅ Yes | Defines **explicit data retention limits** in compliance with GDPR. |
| **CQ33: Transparency in data usage** | ✅ Yes | Implements **auditable consent tracking and data flow transparency**&#8203;:contentReference[oaicite:9]{index=9}. |
| **CQ37: Proactively informing users of GDPR rights** | ✅ Yes | Defines **clear obligations for informing data subjects of their rights**. |
| **CQ39: Third-party data processing agreements** | ✅ Yes | Mentions **the need for agreements and data controller responsibilities**. |
| **CQ51: Data deletion/anonymization** | ✅ Yes | Provides a **privacy-by-design approach** that includes **machine unlearning techniques**&#8203;:contentReference[oaicite:10]{index=10}. |
| **CQ56: Regular review of security plans** | ✅ Yes | Discusses **security measures and compliance verification**. |
| **CQ64: Legal basis for data transfers** | ✅ Yes | Analyzes **legal obligations for data sharing and consent requirements**. |

**Summary:**  
- The paper **strongly aligns with GDPR compliance needs**, offering a **formalized approach for consent tracking**.  
- The **Event-B model, privacy by design, and machine unlearning** make it **highly relevant for GDPR compliance research**.  

---

## **Conclusion**
**Decision: OK (`category: ok`)**  
The paper provides a **formal model for consent management**, **ensuring GDPR compliance in AI and MLOps pipelines**.  
It presents a **systematic approach to GDPR obligations**, making it **highly relevant** for compliance tracking and research.  

---

# **References**
- [[fatema2017a]]
