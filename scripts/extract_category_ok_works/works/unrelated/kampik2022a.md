---
ID: kampik2022a
authors: Kampik, Timotheus; Mansour, Adnane; Boissier, Olivier; Kirrane, Sabrina; Padget, Julian; Payne, Terry R.; Singh, Munindar P.; Tamma, Valentina; Zimmermann, Antoine
category: unrelated
display: kampik (Governance of Autonomous Agents on the Web)
due: The paper introduces a governance framework for autonomous agents using norms, policies, and preferences, but does not propose a data provenance model for GDPR obligations.
entrytype: article
link: https://doi.org/10.1145/3507910
name: "Governance of Autonomous Agents on the Web: Challenges and Opportunities"
organization: ACM
place: ACM Transactions on Internet Technology
pp: Article 104, 31 pages
provenance_related: false
related:
  - Multiagent Systems
  - Semantic Web
  - Norms and Policies
  - Governance
year: 2022
forward_steps: 2
---

# **Summary & Analysis**

## **Summary**

The paper **"Governance of Autonomous Agents on the Web: Challenges and Opportunities"** by Kampik et al. (2022) explores the governance of autonomous agents operating on the Web. The authors propose a **conceptual framework** that integrates elements from **multiagent systems (MAS), the Semantic Web, and the Web of Things (WoT)** to provide a structured approach to governing autonomous agents. The paper highlights how norms, policies, and preferences should be treated as **first-class abstractions** in Web-based MAS environments.

The **main contributions** of the paper are:

1. **A governance framework** structured into three layers: **Reactive Things and Services**, **Autonomous Agents**, and **Normative Organizations**.
2. **A discussion of governance challenges and opportunities**, focusing on norm-aware interaction protocols, distributed MAS, and regulatory concerns.
3. **A motivating scenario using a vaccination rollout**, illustrating the importance of governance mechanisms for ensuring compliance with norms and policies in decentralized systems.

---

## **Key Points**

### **Governance Framework for Autonomous Agents**

The authors propose a **three-layer governance model**:

- **Reactive Things and Services Layer** – Covers non-autonomous entities (IoT devices, web services) and defines policies governing their use.
- **Autonomous Agents Layer** – Represents intelligent agents that can reason, interact, and make decisions.
- **Normative Organizations Layer** – Manages norms, policies, and regulations that apply to agent interactions.

**Representative Quotes:**

- _“We propose a blueprint for the governance of sociotechnical systems that can be instantiated in a variety of ways, using a variety of concrete software components.”_ (Page 12)
- _“Each agent maintains a representation of its internal state built from its internal reasoning, its perceptions of the environment, and interactions with other agents.”_ (Page 14)

### **Challenges in Governing Autonomous Agents**

The paper identifies major challenges:

1. **Norm-aware interaction protocols** – Defining **computational norms** that govern agent behaviors while allowing flexible interactions.
2. **Distributed MAS and Open Organizations** – Enabling **dynamic, decentralized governance structures** where agents can join or leave organizations.
3. **Regulatory Compliance in MAS** – Ensuring **autonomous agents comply with legal regulations**, including GDPR and other data protection laws.

**Representative Quotes:**

- _“Agents should be able to recognize norms, decide whether they want to follow them, and adapt their behavior accordingly.”_ (Page 9)
- _“Ensuring compliance with data protection regulations presents a major challenge for autonomous agents operating in open environments.”_ (Page 20)

---

# **Evaluation Based on Inclusion Criteria**

Now, we assess whether this paper meets the **strict inclusion/exclusion criteria**:

1. **Proposes a data provenance model for GDPR obligations?**
    
    - ❌ **No.** The paper introduces **a governance framework for autonomous agents** but does not **explicitly define a provenance model** for tracking GDPR-related data processing activities.
    - **Quote (Page 2):** _“This article motivates the need for alignment and joint research across the Multiagent Systems, Semantic Web, and WoT communities.”_  
        ✅ **Fails Criterion #1** (No provenance model).
2. **Addresses GDPR compliance questions?**
    
    - ⚠️ **Partially.** The governance model discusses **regulatory compliance** but does not explicitly map to GDPR compliance questions.
    - **Quote (Page 20):** _“Regulatory compliance in MAS is a crucial challenge, particularly as agents interact across different legal jurisdictions.”_  
        ✅ **Fails Criterion #2** (No structured answers to GDPR compliance questions).
3. **Is the proposed model publicly available?**
    
    - ❌ **No explicit reference.** The methodology is **described in the paper**, but **no public dataset or ontology file is provided**.  
        ✅ **Fails Criterion #3**.
4. **Is the document written in English or Portuguese?**
    
    - ✅ **Yes.** The paper is in **English**.  
        ✅ **Passes Criterion #4**.
5. **Is the document publicly available?**
    
    - ⚠️ **Partially.** Available through **ACM Digital Library**, but **may require institutional access**.  
        ✅ **Passes Criterion #5 (conditionally available via institutional login).**
6. **Is the document peer-reviewed?**
    
    - ✅ **Yes.** Published in **ACM Transactions on Internet Technology**, a **peer-reviewed journal**.  
        ✅ **Passes Criterion #6**.

### **Final Verdict**

🔴 **Category: "Unrelated"** – The paper **does not propose a GDPR data provenance model** but instead focuses on **governing autonomous agents with norms and policies**.

---

# **Discussion on Compliance Questions**

The **governance framework** considers **regulatory compliance**, but **does not provide structured answers** to GDPR compliance questions. Below is an analysis of its coverage:

|Compliance Question|Addressed?|Explanation|
|---|---|---|
|**CQ08 (Retention Periods)**|❌|No discussion on **data retention policies**.|
|**CQ09 (Ensuring Compliance Actions)**|❌|Does not define **GDPR-specific compliance measures**.|
|**CQ11 (Consent Management)**|❌|No discussion of **user consent mechanisms**.|
|**CQ17 (SAR Response in One Month)**|❌|No mention of **data subject request processing**.|
|**CQ29 (Retention Policies)**|❌|Does not cover **retention periods for personal data**.|
|**CQ39 (Supplier Agreements)**|❌|No discussion of **third-party data processing agreements**.|

### **Conclusion**

The paper **touches on compliance issues** in autonomous multiagent systems but **does not directly address GDPR compliance questions**. **It does not provide structured compliance mechanisms for GDPR obligations.**

---

# References

- [[bonatti2020a]]