---
ID: castiglione2025a
authors: Castiglione, Gianpietro and Bella, Giampaolo and Santamaria, Daniele Francesco
category: unrelated
display: castiglione (SecOnto - Security Ontologies)
due: The paper presents an ontology-based compliance verification approach, but does not explicitly define a GDPR data provenance model.
entrytype: article
link: https://doi.org/10.1016/j.cose.2024.104150
name: "SecOnto: Ontological Representation of Security Directives"
organization: Elsevier
place: Computers & Security
pp: 1-23
provenance_related: false
related:
  - Ontologies
  - Security Directives
  - Compliance Verification
  - NIS 2
year: 2025
forward_steps: 2
---

The paper **"SecOnto: Ontological Representation of Security Directives"** by **Gianpietro Castiglione, Giampaolo Bella, and Daniele Francesco Santamaria** (published in _Computers & Security, 2025_) discusses the use of **Semantic Web ontologies** for representing security directives. It introduces a **five-step methodology** called **SecOnto** to transform juridical security directives into machine-readable ontologies, focusing on **Directive 2022/2555 (NIS 2)**.

I'll now proceed with your requested steps.

---

# **Summary & Analysis**

## **Introduction & Context**

The paper addresses the challenges of implementing and verifying compliance with **European security directives**, which include GDPR and NIS 2. The authors argue that **ontological representation** can improve both the **interpretability and enforceability** of these directives by structuring security measures in a way that is **machine-readable** and suitable for automated compliance verification.

The **main contributions** of the paper are:

1. **A novel methodology (SecOnto) for translating security directives into ontologies**.
2. **A structured, five-step transformation process** (Preprocessing, Interpretation, Structuring, Representation, Verification).
3. **Validation of the methodology using NIS 2**, showing how it can be extended to GDPR and other EU regulations.

**Representative Quotes:**

- _“Ontological representation can be employed to represent and operationalise such security directives, ultimately contributing to the effectiveness and efficiency of the compliance process.”_ (Page 1)
- _“SecOnto breaks down the process of transforming the juridical language of modern security directives into full-fledged ontologies by means of five semi-automated steps.”_ (Page 1)

---

## **The SecOnto Methodology**

The paper outlines a **five-step methodology** for encoding security directives into ontologies:

1. **Preprocessing** – Identifies key articles and structures within the legal text.
2. **Interpretation** – Extracts the relevant entities, agents, and actions.
3. **Structuring** – Designs an ontological framework, ensuring agent- and document-oriented design.
4. **Representation** – Converts security measures into OWL ontologies.
5. **Verification** – Uses **reasoning and SPARQL queries** to check compliance.

**Key Concepts:**

- The methodology focuses on **agent-centric modeling**, representing security measures with respect to the entities responsible for implementing them.
- It incorporates **logical reasoning** to check compliance.
- The **validation case study is based on NIS 2**.

**Representative Quotes:**

- _“Each step is described and validated by means of operational examples based upon Directive 2022/2555 of the European Parliament and of the Council of the European Union on security of network and information systems, better known as NIS 2.”_ (Page 2)
- _“We propose the SecOnto methodology that involves a comprehensive ontological representation of security measures and the corresponding responsible agents.”_ (Page 4)

---

## **Application to Compliance Verification**

The methodology allows **automated compliance verification** using **reasoning and SPARQL queries**. The **representation in OWL** makes it possible to **reason over security measures and check if obligations are fulfilled**.

Example validation scenario:

- A **Member State** is required to **adopt a national cybersecurity strategy**.
- The ontology captures this as:
    - **Entity:** `MemberState`
    - **Action:** `adopt`
    - **Object:** `NationalSecurityStrategy`
- If an individual representing a Member State **lacks this obligation**, **reasoning can detect non-compliance**.

**Representative Quotes:**

- _“The verification approach enables us to simultaneously validate compliance across multiple entities in a single reasoning execution, avoiding separate manual checks.”_ (Page 10)
- _“A key advantage of the ontological approach is that it allows for automatic detection of missing obligations via SPARQL queries.”_ (Page 11)

---

# **Evaluation Based on Inclusion Criteria**

Now, we assess whether this paper meets your strict **inclusion/exclusion criteria**.

1. **Does the approach propose a data provenance model for GDPR-related activities?**
    
    - **No.** The paper introduces an **ontology-based compliance verification approach**, but **it does not explicitly define a data provenance model** for tracking GDPR obligations.
    - **Quote (Page 1):** _“This article introduces SecOnto, a novel methodology for representing security directives as ontologies.”_
    - The focus is on **security compliance** rather than **data lineage or provenance tracking**.
2. **Does the proposed model address compliance questions related to GDPR obligations?**
    
    - **Partially.** The methodology can be **applied** to GDPR-related obligations, but the paper does **not explicitly focus on GDPR**.
    - The validation is done on **NIS 2**, which is related to **cybersecurity compliance**, not **data protection lineage**.
    - **Quote (Page 2):** _“The choice falls on NIS 2 since it is the most recent security Directive in Europe, but the approach could be applied to GDPR.”_
3. **Is the proposed model publicly available?**
    
    - **No direct mention.** The methodology is **described in detail**, but there is **no explicit reference to an open dataset or ontology file**.
4. **Is the document written in English or Portuguese?**
    
    - **Yes.** The paper is in **English**.
5. **Is the document publicly accessible?**
    
    - **No direct confirmation.** The publication is in _Computers & Security_ (Elsevier), which typically requires access via **CAPES/Café or institutional login**.
6. **Is the document peer-reviewed?**
    
    - **Yes.** It is published in **Computers & Security**, a peer-reviewed journal.

### **Conclusion:**

- **Category: "Unrelated"** – The paper is **not strictly about data provenance for GDPR** but focuses on **compliance verification using ontologies**.
- **Reason for exclusion:** _The approach does not propose a provenance model but instead focuses on compliance verification of security measures._

---

# **Discussion on Compliance Questions**

We now examine **whether SecOnto addresses GDPR compliance questions (CQs):**

1. **CQ08 (Retention Periods)** – **Not addressed.** The paper does not discuss data retention timelines.
2. **CQ09 (Ensuring Compliance Actions)** – **Partially addressed.** The ontology **tracks security obligations** but does not focus on **data processing activities**.
3. **CQ11 (Re-seeking Consent)** – **Not addressed.** No mention of consent mechanisms.
4. **CQ17 (SARs response within one month)** – **Not addressed.**
5. **CQ29 (Retention Policies)** – **Not explicitly covered.**
6. **CQ39 (Supplier Agreements & Data Processing)** – **Not addressed.**
7. **CQ50 (Encryption for Sensitive Data)** – **Not addressed.**

**Conclusion:** **SecOnto is focused on security compliance rather than personal data handling.** While the methodology could be **applied to GDPR obligations**, it is **not specialized** for this purpose.

---

# References

- [[bonatti2020a]]