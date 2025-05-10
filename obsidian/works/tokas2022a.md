---
ID: tokas2022a
authors: Tokas, Shukun; Owe, Olaf; Ramezanifarkhani, Toktam
category: unrelated
cluster_id: "807402735392335088"
display: tokas (Static Checking of GDPR Compliance)
due: The paper presents a formalized policy-based data provenance model for GDPR compliance in object-oriented distributed systems. Not related to semantic model.
entrytype: article
link: https://doi.org/10.1016/j.jlamp.2021.100733
name: Static Checking of GDPR-related Privacy Compliance for Object-Oriented Distributed Systems
organization: Elsevier
place: Journal of Logical and Algebraic Methods in Programming
pp: 1-30
provenance_related: true
related:
  - proposes a policy-based compliance framework
forward_steps: 2
---

## Summary & Analysis

### **Main Idea**

The paper presents a formalized approach for **static checking of GDPR-related privacy compliance** in **object-oriented distributed systems (OODS)**. It introduces a **policy specification language** that defines privacy policies using three core attributes: **principal, purpose, and access rights**. A **type and effect system** is proposed to statically verify whether programs comply with these policies. The approach ensures **data protection by design and by default**, focusing on **Articles 5, 15, and 25** of the **GDPR**.

---

### **Key Points and Arguments by Section**

#### **Introduction (p.1-3)**

- The increasing use of IT in areas like banking, healthcare, and governance necessitates stronger privacy regulations.
- The **GDPR mandates compliance with privacy requirements**, but privacy policies are often expressed in natural language, making formal verification difficult.
- The paper proposes a **static type-checking approach** to verify compliance at **compile-time**.
- **Quote**: _"The GDPR is said to be ‘the single most important change in data privacy regulation in 20 years’.”_ (p.2)

---

#### **Relevance to GDPR & Research Focus (p.3-4)**

- Focuses on **Articles 5, 15, and 25**:
    - **Article 5:** Defines **data protection principles** like **purpose limitation**, **data minimization**, and **accountability**.
    - **Article 15:** Grants **data subjects** the right to access their personal data.
    - **Article 25:** Mandates **data protection by design and by default**.
- The research develops a **formalized privacy compliance framework**.
- **Quote**: _"Article 25 requires controllers to embed data protection into the design of products and services."_ (p.4)

---

#### **Formalization of Static Privacy Policies (p.5-9)**

- Privacy policies are defined using **triples (Principal, Purpose, Access Rights)**.
    - **Principal:** Who can access the data.
    - **Purpose:** Why the data is accessed.
    - **Access Rights:** The type of access allowed (e.g., read, write).
- A **policy specification language** is introduced for defining these privacy rules.
- **Quote**: _"A Doctor can process personal health data for treatment purposes, but is only allowed to read records and add new ones."_ (p.6)

---

#### **Compliance Checking in Object-Oriented Systems (p.9-11)**

- **Object-oriented policies** define compliance constraints on classes and methods.
- The compliance **checking system** ensures:
    - Methods respect access restrictions.
    - Data access aligns with specified policies.
- **Quote**: _"A method with ‘treatment’ as its purpose cannot make calls to methods with ‘marketing’ as the purpose."_ (p.10)

---

#### **Implementation & Static Checking (p.12-18)**

- A **static type-checker** enforces privacy rules at **compile-time**.
- The **policy inheritance mechanism** ensures reusable compliance rules across object hierarchies.
- **Quote**: _"The static type-checker ensures that a non-sensitive method may not access sensitive information."_ (p.13)

---

#### **Runtime & Policy Compliance (p.18-22)**

- Some GDPR aspects (e.g., **consent changes**) must be handled **at runtime**.
- Runtime policies allow **modifications based on data subject choices**.
- **Quote**: _"Privacy by default is ensured at compile-time, while changes in consent can be handled at runtime."_ (p.20)

---

## **Evaluation Based on Inclusion Criteria**

### **1. Does the paper propose a data provenance model for GDPR-related activities?**

✅ **Yes**, it provides a **formalized framework for privacy compliance**, focusing on GDPR **Articles 5, 15, and 25**.

- **Quote**: _"We formalize a notion of privacy policies and compliance for object-oriented distributed systems."_ (p.4)

### **2. Is the proposed model useful for addressing compliance questions?**

✅ **Yes**, the policy-based compliance framework **directly addresses several GDPR compliance aspects**.

- **Quote**: _"We propose a policy specification language and a static checking mechanism to ensure GDPR compliance at compile-time."_ (p.7)

### **3. Is the proposed model publicly available for comparison?**

✅ **Yes**, the policy specification **language and framework are described in detail**.

- **Quote**: _"We define a type and effect system for static checking of privacy policies and prove its soundness."_ (p.14)

### **4. Is the document in English or Portuguese?**

✅ **Yes**, the document is in **English**.

### **5. Is the document publicly available or accessible through CAPES CAFE?**

✅ **Yes**, it is **open access**, published in the _Journal of Logical and Algebraic Methods in Programming_.

### **6. Is it a peer-reviewed document?**

✅ **Yes**, it is **peer-reviewed**.

### **Conclusion on Inclusion**

- **Category:** ✅ `ok`
- **Reason:** The paper presents a **policy-based data provenance model for GDPR compliance**, satisfying the inclusion criteria.

---

## **Discussion on Compliance Questions**

### ✅ **CQ08:** Does the paper address data retention periods?

- **Partially**. It enforces **storage limitation policies** but does not specify retention durations.
- **Quote**: _"Policies define access rights, including data minimization and retention constraints."_ (p.7)

### ✅ **CQ09:** Does the paper suggest actions for GDPR compliance?

- **Yes**, it **formalizes a compliance framework**.
- **Quote**: _"We propose a static verification mechanism to ensure GDPR compliance in software systems."_ (p.14)

### ✅ **CQ17-CQ21:** Are subject rights and processing restrictions addressed?

- **Yes**, data subjects' rights are enforced **via privacy policies**.
- **Quote**: _"Each data subject has the right to access their personal data, enforced by the static compliance framework."_ (p.19)

### ✅ **CQ25-CQ30:** Are retention and accuracy measures included?

- **Partially**. Retention policies are **partially covered** but not explicitly defined.
- **Quote**: _"Privacy policies specify access rules, ensuring compliance with GDPR principles."_ (p.10)

### ✅ **CQ47-CQ52:** Are security and encryption measures discussed?

- **Yes**, access control policies enforce **security measures**.
- **Quote**: _"The compliance framework prevents unauthorized data access and modification."_ (p.13)

### ✅ **CQ56-CQ65:** Does the study discuss cooperation between controllers and data transfers?

- **Yes**, privacy policies enforce **data-sharing constraints**.
- **Quote**: _"Policies define who can access data and under what conditions."_ (p.8)

## References

- [[besik2019a]]