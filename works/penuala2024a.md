---
ID: penuala2024a
name: "JWS Position Paper: Knowledge Graphs in the AI Landscape"
authors: Merono-Penuela et al.
year: 2024
category: unrelated
due: The paper discusses knowledge graphs as a governance tool in AI but does not propose a data provenance model specifically addressing GDPR obligations. While it mentions compliance verification, it lacks a concrete framework for answering GDPR compliance questions.
forward_steps: 2
---

## **Evaluation Against Inclusion Criteria**

1. **Does the paper propose a data provenance model to represent activities related to GDPR obligations?**  
   - The paper presents *KG.gov*, a framework for using knowledge graphs as a backbone for AI governance. However, it does not introduce a specific **data provenance model** tailored for GDPR-related activities.  
   - Instead, it focuses on transparency, accountability, and interoperability of data in AI systems through knowledge graphs but lacks an explicit structure for GDPR tracking.

2. **Is the proposed model useful to address the compliance questions?**  
   - The paper refers to **Croissant RAI**, a machine-readable metadata format for AI datasets, which includes some regulatory compliance verification mechanisms.  
   - However, there is no detailed mapping to **specific GDPR compliance questions**.  
   - The focus is on AI governance rather than legal compliance enforcement.  

3. **Is the proposed model publicly available for comparison?**  
   - *KG.gov* is conceptual, and some components like Croissant RAI have public documentation.  
   - However, no fully developed, peer-reviewed **compliance-oriented provenance model** is made available.  

4. **Is the document written in English or Portuguese?**  
   - ✅ Yes, the paper is in English.  

5. **Is the document publicly available or within CAPES CAFE-signed digital libraries?**  
   - ✅ Yes, the paper is accessible via Web Semantics Journal and DOI.  

6. **Is it a peer-reviewed document?**  
   - ✅ Yes, it is published in a **peer-reviewed journal** (Web Semantics).  

**Final Verdict:** ❌ *Category: Unrelated*  
- While the paper discusses **data governance and AI compliance mechanisms**, it does not **explicitly propose a GDPR compliance model**.  
- The paper **mentions GDPR** but does not **provide structured solutions for GDPR obligations** such as retention periods, legal basis tracking, or personal data processing constraints.  
- **Not suitable for answering GDPR compliance questions.**  

---

## **Analysis Against GDPR Compliance Questions (CQ08-CQ65)**

### **Potentially Relevant GDPR Aspects**
The paper discusses **data governance transparency**, which indirectly relates to GDPR but **does not provide specific solutions** for compliance tracking. Below is an evaluation of potential relevance to GDPR compliance questions:

| **Compliance Question** | **Relevance** | **Analysis** |
|------------------------|-------------|-------------|
| **CQ08: Retention periods** | ❌ No | The paper does not propose a method for tracking retention periods of personal data. |
| **CQ09: Required actions for GDPR compliance** | ❌ No | Does not list required actions for ensuring GDPR-compliant processing. |
| **CQ11: Consent management** | ❌ No | No mechanisms for re-seeking user consent in compliance with GDPR. |
| **CQ17: Subject Access Requests (SARs)** | ❌ No | No procedures for handling user data requests under GDPR. |
| **CQ20: Halting processing on request** | ❌ No | No system described to allow individuals to halt processing. |
| **CQ25: Documenting restrictions on data protection rights** | ❌ No | The framework does not specify how to document these restrictions. |
| **CQ28: Ensuring data accuracy and updates** | ⚠️ Partial | Discusses dataset transparency in AI models, but not specific to GDPR. |
| **CQ29: Retention policies** | ❌ No | Lacks details on retention timelines for GDPR compliance. |
| **CQ33: Transparency in data usage** | ⚠️ Indirect | Mentions transparency through KGs but lacks GDPR-specific mechanisms. |
| **CQ37: Proactively informing users of GDPR rights** | ❌ No | No structured approach to inform individuals of GDPR rights. |
| **CQ39: Third-party data processing agreements** | ❌ No | No contractual compliance discussions. |
| **CQ51: Data deletion/anonymization** | ⚠️ Partial | Discusses dataset versioning but does not provide GDPR-aligned erasure mechanisms. |
| **CQ56: Regular review of security plans** | ⚠️ Indirect | The framework touches on AI governance but does not provide security plans. |
| **CQ64: Legal basis for data transfers** | ❌ No | No mention of tracking data transfer legality. |

**Summary:**  
- The paper is **indirectly related** to data governance but does not **propose specific mechanisms** for GDPR compliance.  
- Some concepts (**transparency, explainability, metadata tracking**) align **loosely** with GDPR goals, but no **direct implementation for GDPR obligations is presented**.  

---

## **Conclusion**
**Decision: Unrelated (`category: unrelated`)**  
The paper presents **a knowledge-graph-based AI governance framework** but does **not focus on GDPR compliance models**.  
It lacks a **structured data provenance approach for regulatory tracking**, which is essential for GDPR-related obligations.  
Thus, it **does not fulfill the inclusion criteria** for this review.

---

# **References**

- [[fatema2017a]]
