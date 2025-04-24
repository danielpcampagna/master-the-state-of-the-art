---
ID: krook2024a
name: Mapping the Complexity of Legal Challenges
authors: Krook et al.
year: 2024
category: unrelated
due: The paper discusses legal challenges and compliance mechanisms for drones but does not propose a data provenance model specifically addressing GDPR obligations. While it mentions privacy protection and legal frameworks, it lacks a concrete framework for answering GDPR compliance questions.
forward_steps: 2
---

## **Evaluation Against Inclusion Criteria**

1. **Does the paper propose a data provenance model to represent activities related to GDPR obligations?**  
   - The paper discusses GDPR principles **in the context of drone usage** and compliance, particularly focusing on **Privacy by Design** and **Data Protection Impact Assessments (DPIAs)**&#8203;:contentReference[oaicite:0]{index=0}.  
   - However, it **does not introduce a structured data provenance model** for tracking compliance obligations.  

2. **Is the proposed model useful to address the compliance questions?**  
   - The study **touches on GDPR principles**, such as **storage limitation, minimization, consent, and security** but **does not offer a concrete model** for systematic compliance tracking&#8203;:contentReference[oaicite:1]{index=1}.  
   - It lacks a **structured approach** for answering compliance questions such as **retention policies or data access controls**.  

3. **Is the proposed model publicly available for comparison?**  
   - The paper is **theoretical** and **does not provide a reusable compliance model**.  

4. **Is the document written in English or Portuguese?**  
   - ✅ Yes, the paper is in English.  

5. **Is the document publicly available or within CAPES CAFE-signed digital libraries?**  
   - ✅ Yes, it is available in the **ACM Journal of Responsible Computing**&#8203;:contentReference[oaicite:2]{index=2}.  

6. **Is it a peer-reviewed document?**  
   - ✅ Yes, it is published in a **peer-reviewed journal**.  

**Final Verdict:** ❌ *Category: Unrelated*  
- The paper **examines GDPR compliance in drone regulation** but does not propose a **data provenance model** for compliance tracking.  
- It lacks **detailed solutions** for **retention policies, legal basis tracking, or processing constraints**.  
- **Not suitable for answering GDPR compliance questions.**  

---

## **Analysis Against GDPR Compliance Questions (CQ08-CQ65)**

### **Potentially Relevant GDPR Aspects**
The paper discusses **privacy compliance** within drone operations, but it **does not systematically map to GDPR compliance questions**. Below is an evaluation:

| **Compliance Question** | **Relevance** | **Analysis** |
|------------------------|-------------|-------------|
| **CQ08: Retention periods** | ❌ No | No framework for tracking retention periods. |
| **CQ09: Required actions for GDPR compliance** | ⚠️ Indirect | Mentions **Privacy by Design** but does not define concrete GDPR actions. |
| **CQ11: Consent management** | ⚠️ Indirect | Discusses **informed consent for drones** but does not generalize to GDPR compliance tracking&#8203;:contentReference[oaicite:3]{index=3}. |
| **CQ17: Subject Access Requests (SARs)** | ❌ No | No procedures for handling SARs. |
| **CQ20: Halting processing on request** | ❌ No | No discussion on data subject requests for halting data processing. |
| **CQ25: Documenting restrictions on data protection rights** | ❌ No | No explicit methodology for documenting restrictions. |
| **CQ28: Ensuring data accuracy and updates** | ⚠️ Indirect | Mentions **data minimization** but does not propose an update mechanism&#8203;:contentReference[oaicite:4]{index=4}. |
| **CQ29: Retention policies** | ❌ No | Lacks detailed GDPR-aligned retention policies. |
| **CQ33: Transparency in data usage** | ⚠️ Indirect | Discusses drone privacy risks but lacks GDPR-specific documentation. |
| **CQ37: Proactively informing users of GDPR rights** | ❌ No | No structured GDPR user education strategies. |
| **CQ39: Third-party data processing agreements** | ❌ No | Does not address data processing agreements. |
| **CQ51: Data deletion/anonymization** | ⚠️ Partial | Mentions **pseudonymization** but lacks GDPR-compliant data deletion practices&#8203;:contentReference[oaicite:5]{index=5}. |
| **CQ56: Regular review of security plans** | ❌ No | No review framework for GDPR security compliance. |
| **CQ64: Legal basis for data transfers** | ❌ No | No mention of tracking the legality of data transfers. |

**Summary:**  
- The paper **touches on GDPR principles** but does not **provide a structured approach** for GDPR compliance.  
- Some concepts (**privacy impact assessments, informed consent**) align **loosely** with GDPR, but **there is no concrete implementation**.  

---

## **Conclusion**
**Decision: Unrelated (`category: unrelated`)**  
The paper presents **legal and privacy challenges in drone operations**, referencing GDPR but **not providing a structured compliance model**.  
It lacks **a systematic approach to GDPR data governance** and **does not meet inclusion criteria**.  

---

# **References**
- [[fatema2017a]]
