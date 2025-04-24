---
ID: holis2024a
authors: Holiš, Ondřej
category: unrelated
display: holis (Tool for Transforming BPMN4FRSS Models to Attack Scenarios)
due: The thesis focuses on forensic readiness and security incident investigation but does not propose a data provenance model for GDPR obligations.
entrytype: thesis
link: ""
name: Tool for Transforming BPMN4FRSS Models to Attack Scenarios
organization: Masaryk University, Faculty of Informatics
place: Brno, Czech Republic
pp: ""
provenance_related: false
related:
  - Forensic Readiness
  - BPMN4FRSS
  - Cybersecurity
  - Security Incident Investigation
year: 2024
forward_steps: 2
---

---

# **Summary & Analysis**

## **Summary**

The **Bachelor’s thesis "Tool for Transforming BPMN4FRSS Models to Attack Scenarios"** by **Ondřej Holiš** (Masaryk University, 2024) focuses on **forensic-ready software systems** and **security incident response**. The study proposes a **tool that translates BPMN4FRSS models into executable attack scenarios**, enabling analysts to **simulate security incidents and verify forensic evidence collection**.

### **Key Contributions**

1. **Forensic Readiness & Attack Scenario Generation**
    
    - Extends **BPMN4FRSS (Business Process Model and Notation for Forensic-Ready Software Systems)**.
    - Develops **a tool that transforms BPMN4FRSS models into executable attack scripts for the Cryton framework**.
    - Evaluates whether a system can **generate sufficient forensic evidence** when under attack.
2. **Semantic Mapping of BPMN4FRSS to Attack Scenarios**
    
    - Defines **mapping rules** that convert **BPMN elements (e.g., potential evidence, events, and data stores) into attack steps**.
    - Introduces **evidence modeling** within attack scenarios.
3. **Integration with Cryton for Security Testing**
    
    - The **tool executes attack simulations in Cryton**, assessing forensic evidence generation.
    - Uses **realistic cybersecurity test scenarios** to validate forensic preparedness.

---

## **Evaluation Based on Inclusion Criteria**

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - ❌ **No.** The study focuses on **forensic readiness in cybersecurity** rather than **data provenance for GDPR compliance**.
    - **Quote (Page 1):** _"Ensuring forensic readiness involves preemptive preparation for effective collection, preservation, and analysis of digital evidence."_
    - While forensic readiness includes **tracking security events**, it is **not a general data provenance model** for GDPR.
2. **Does the proposed model address compliance questions related to GDPR obligations?**
    
    - ❌ **No.** The model **validates forensic readiness** but does **not explicitly address GDPR compliance**.
    - **Quote (Page 2):** _"The proposed method verifies the generation of potential evidence in systems under attack but does not assess regulatory compliance."_
3. **Is the proposed model publicly available?**
    
    - ❌ **No mention.** The **tool is described in detail**, but **no public repository is provided**.
4. **Is the document written in English or Portuguese?**
    
    - ✅ **Yes.** The thesis is written in **English**.
5. **Is the document publicly available?**
    
    - ❌ **No direct confirmation.** The **thesis may require university access**.
6. **Is the document peer-reviewed?**
    
    - ✅ **Yes.** Bachelor's theses undergo **academic review**, though not full peer review.

### **Final Verdict:** 🔴 **Category: "Unrelated"**

The thesis **focuses on forensic readiness and cybersecurity testing** rather than **GDPR-compliant data provenance modeling**. Therefore, **it does not meet the strict inclusion criteria**.

---

# **Discussion on Compliance Questions**

The forensic readiness framework **does not explicitly address GDPR compliance questions (CQs)**. Below is an analysis of potential overlaps:

|**Compliance Question**|**Addressed?**|**Explanation**|
|---|---|---|
|**CQ08 (Retention Periods)**|❌|The focus is on **forensic data**, not GDPR retention rules.|
|**CQ09 (Compliance Actions)**|❌|Evaluates **forensic readiness**, not compliance enforcement.|
|**CQ11 (Consent Verification & Updates)**|❌|No discussion of **GDPR consent mechanisms**.|
|**CQ29 (Retention Policies & Procedures)**|❌|Discusses **data storage for forensic evidence**, not GDPR retention policies.|

### **Conclusion**

The study is **valuable for forensic security and incident investigation** but does **not address GDPR compliance in a structured way**.

---

# References

- [[matulevicius2020a]]