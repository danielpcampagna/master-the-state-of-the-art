---
ID: hayashi2024a
authors: Hayashi, Hisashi and Taheri, Yousef and Tsushima, Kanae and Bourgne, Gauvain and Ganascia, Jean-Gabriel and Satoh, Ken
category: unrelated
display: hayashi (Toward smooth integration of an online HTN planning agent with legal and ethical checkers)
due: This paper does not propose a data provenance model. It focuses on an HTN planning approach integrated with legal and ethical checkers rather than modeling provenance information for GDPR obligations.
entrytype: conference
link: https://hal.science/hal-04669533v1
name: Toward smooth integration of an online HTN planning agent with legal and ethical checkers
organization: HAL/Open Access
place: International Workshop on AI Value Engineering and AI Compliance Mechanisms (VECOMP 2024), A Coruña, Spain
pp: 1-9
provenance_related: false
related:
  - HTN planning
  - GDPR compliance
  - legal checking
  - ethical checking
year: 2024
forward_steps: 2
---

# Summary & Analysis

## Introduction (pp.1–2)

The paper begins by motivating the need for integrating **automated planning** methods with **legal and ethical checkers** due to the growing complexity of regulations (like the GDPR) that govern data usage across different countries. It highlights the authors’ objective to present a **new architecture** where each module (a planning agent, a legal checker, and an ethical checker) can be deployed independently.

**Key Points:**

- The complexity of **legal and ethical norms** when transferring or utilizing data internationally.
- Necessity of **online (dynamic) planning** to adapt to changing environments (e.g., node availability).
- Desire to separate the **planning** logic from **legal** and **ethical** checkers for modularity.

**Representative Quotations:**

1. “Given the variability in legal and ethical norms across countries and the specialized knowledge required, we assume that legal and ethical checkers are implemented as independent modules…” (p.1)
2. “In particular, we demonstrate how to integrate a planning agent, which utilizes an online HTN (hierarchical task network) planner, with legal and ethical checkers.” (p.1)
3. “Research has focused on automated compliance checks for data transfer norms, particularly the policy representation of the GDPR…” (p.1)

## Overall Architecture (pp.2–3)

The authors propose an **online HTN planner** that incrementally adapts plans. Alongside it, two separate modules (the **legal checker** and the **ethical checker**) evaluate the feasibility and alignment of these plans. The **legal checker** determines the legality under specific regulations (in this case, GDPR rules about intra- and extra-EU transfers), and the **ethical checker** selects the “most ethical” plan based on various criteria (safety levels, occupancy, bias, etc.).

**Key Points:**

- **Planning Agent** uses a **forward-chaining HTN** approach.
- **Legal Checker** ensures **plan compliance** by evaluating each action.
- **Ethical Checker** orders or filters out plans based on **moral/ethical** preferences.

**Representative Quotations:**

1. “We propose a new architecture that integrates an online planning agent with a legal and an ethical checker.” (p.2)
2. “The legal checker evaluates each action in a plan … and deems the plan legal only if all actions are legal.” (p.2)
3. “The ethics checker … selects the most ethical plan from the given legal plans … to reduce the risk of breach and potential harm.” (p.3)

## Interaction Modes Between Modules (pp.3–4)

They compare **three modes** of interaction to reduce computational overhead and optimize communications among the planning agent, legal checker, and ethical checker:

1. **Default Mode:** Each checker queries the planner’s database every time.
2. **Subscription Mode:** Checkers only consult the planner when “subscribed” fluents (those relevant to legal/ethical norms) change.
3. **All-Subscription Mode:** A special case of subscription mode where **all** fluents are tracked in the checkers’ local databases.

**Key Points:**

- Reducing **redundant checks** significantly improves efficiency.
- “Subscription” to key facts (fluents) helps localize queries and reduce network calls.
- The mode selection affects the **computation time** and the **number of interactions** between modules.

**Representative Quotations:**

1. “In subscription mode, the legal (or ethical) checker maintains a separate database of the subscribed fluents.” (p.3)
2. “Each time an action is executed … if the action execution does not change the truth values of fluents that affect legal or ethical norms, it is unnecessary to modify the current plan…” (p.4)
3. “All-subscription mode is a special case … it is unnecessary to declare the subscribed fluents.” (p.4)

## Use Case Model (pp.4–5)

Their main **demonstration** concerns transferring personal data across different **nodes** (some inside, some outside the EU) with an HTN approach. Various **scenarios** show how the system _replans_ when conditions such as node availability, safety level, or user permissions change.

**Key Points:**

- A network of nodes is used to store or process personal data.
- **GDPR constraints**: data transfer outside the EU might be illegal if the data owner disallows it.
- The **ethical checker** might prefer more secure nodes (safety) or less busy nodes (occupancy).

**Representative Quotations:**

1. “A well-known set of data-protection regulations is the European General Data Protection Regulations (GDPR) [7].” (p.4)
2. “In this use case, users’ personal data are stored in circle nodes … The planner in our architecture generates possible plans to satisfy the given task.” (p.4)
3. “Transferring personal data outside the legislative zone may have ethical implications … it is also used in the ethical verification process.” (p.5)

## Experiments and Discussions (pp.6–8)

They run **four scenarios** (basecase, precondition-replan, ethical-replan, legal-replan) to illustrate how the combined system **adapts**. They measure the **computation time** and the **number of interactions** between modules. Their results show that the **subscription modes** significantly reduce interaction overhead compared to the default mode, especially in distributed environments.

**Key Points:**

- The **computation time** for default vs. subscription mode is nearly the same, but subscription drastically reduces remote calls.
- The scenario `legal-replan` shows how changing **GDPR permissions** (a user disallowing data export) forces the system to pick different data or routes.

**Representative Quotations:**

1. “The subscription mode was the most efficient in terms of the number of interactions and computation time.” (p.7)
2. “In any case, the subscription mode … significantly reduces the number of interactions, which is vital for smooth and efficient integration.” (p.7)
3. “If the data owner does not grant permission to transfer the data outside the EU, the legal checker determines that it is illegal.” (p.8)

## Conclusion (p.8)

The paper closes by emphasizing the usefulness of **integrating** a dynamic hierarchical planner with specialized **legal** and **ethical** checkers. They plan to extend the approach for more **real-time** legal and ethical updates.

**Key Points:**

- The approach can handle **dynamic changes** in norms, safety, or user permissions.
- The focus is on **modular** design for reusability of legal/ethical checkers.

**Representative Quotations:**

1. “We compared and evaluated three interaction modes and found that the fluent subscription technique works well.” (p.8)
2. “In future, we plan to improve our integration method for real-time computation of legal and ethical planning.” (p.8)
3. “This would ensure high efficiency through frequent interactions between these modules.” (p.8)

---

# Evaluation Based on Inclusion Criteria

Below, each numbered statement references the specific text or argument (with page numbers) that supports (or contradicts) whether the paper meets or fails each of the **inclusion/exclusion criteria**.

1. **Proposes a data provenance model to represent activities under GDPR obligations?**
    
    - **Evaluation**: **No**, the paper does not propose a structured provenance model. Instead, it implements a **planning approach** with legal/ethical checkers.
    - **Reference**: “We propose a new architecture that integrates an online planning agent with a legal and an ethical checker.” (p.2) – This describes a planning-based approach rather than a provenance data model.
2. **Is this model useful to address the compliance questions?**
    
    - **Evaluation**: **No**, the paper focuses on verifying plan legality and picking “most ethical” plans. It does not describe or represent provenance details for each GDPR obligation.
    - **Reference**: “The legal checker evaluates each action in a plan … to determine whether it is legal.” (p.2) – This indicates a checking mechanism, not an explicit representation of data lineage or provenance.
3. **Is the proposed model publicly available for comparison?**
    
    - **Evaluation**: **Not applicable** – The paper does not present a formal provenance model. They do discuss an **architecture** and mention Prolog-based modules, but these do not constitute a standardized data model for provenance.
    - **Reference**: “Because of the complexity of legal and ethical norms, specialized expertise is required … we proposed a general-purpose online planner…” (p.1) – Emphasizes modular checkers, not a shared data model.
4. **Is the document in English or Portuguese?**
    
    - **Evaluation**: **Yes**, the document is written in English.
    - **Reference**: The entire text is clearly in English (p.1–9).
5. **Is the document publicly available (e.g., in a digital library)?**
    
    - **Evaluation**: **Yes**, it is available in the HAL open-access repository.
    - **Reference**: “HAL Id: hal-04669533 … [https://hal.science/hal-04669533v1”](https://hal.science/hal-04669533v1%E2%80%9D) (cover page)
6. **Is it a peer-reviewed document?**
    
    - **Evaluation**: **Likely** – It is presented at the International Workshop on AI Value Engineering and AI Compliance Mechanisms (VECOMP 2024). Workshops generally imply peer review, though not always as rigorous as a journal.
    - **Reference**: “International Workshop on AI Value Engineering and AI Compliance Mechanisms (VECOMP 2024), Oct 2024, A Coruña, Spain.” (cover page)

**Conclusion on Inclusion**: The paper **does not** satisfy the primary criterion (#1) of presenting a data provenance model. It therefore **fails** the core requirements. Despite addressing GDPR aspects for planning, it is **unrelated** in terms of proposing a provenance-oriented model.

---

# Discussion on Compliance Questions

Below is a consideration of whether the paper (and the model it proposes) addresses each **Compliance Question** (CQ). For brevity, only relevant quotes are included. If a question is not addressed, we note that explicitly.

1. **CQ08 (Data retention period)?**
    
    - **Discussion**: Not addressed. The text focuses on data transfers and compliance checks regarding location constraints (EU vs. non-EU).
    - **Reference**: No content on specific retention policies (pp.1–9).
2. **CQ09 (Identify actions required to ensure data processing is GDPR-compliant)?**
    
    - **Discussion**: Partially. They do identify if transferring data is permitted or not; however, they do **not** detail the specific actions (like “deleting data post-purpose”) to ensure compliance.
    - **Reference**: “If the data owner does not grant permission to transfer the data outside the EU, the legal checker determines that it is illegal.” (p.8) – This is about data transfer constraints, not broader actions for compliance.
3. **CQ11 (Re-seeking individual’s consent)?**
    
    - **Discussion**: Not addressed. Consent is mentioned only in the sense of permission changes, but the mechanism of re-seeking consent is not described.
    - **Reference**: “The legal checker checks … if a data owner does not grant permission … the given plan uses the data and a route that goes outside the EU.” (p.2) – Mentions permission but no mention of re-consent.
4. **CQ17 (Responding to SARs within one month)?**
    
    - **Discussion**: Not addressed. No mention of subject access requests or time limits.
    - **Reference**: Not found (pp.1–9).
5. **CQ20 (Halt processing upon valid restriction)?**
    
    - **Discussion**: Not addressed. The system can adapt if a user changes data permissions, but halting or restricting processing is not explicitly discussed.
    - **Reference**: “During execution, the permission information for du28 was rewritten to prohibit taking the data out of the EU…” (p.8) – This triggers re-planning but does not discuss a formal “restriction of processing” mechanism.
6. **CQ21 (Right to object to certain types of processing)?**
    
    - **Discussion**: Not addressed. The system checks if a user’s permission is valid for data transfer, but the question of user’s “right to object” is not the focus.
    - **Reference**: Not found (pp.1–9).
7. **CQ25 (Documenting circumstances where data protection rights may be lawfully restricted)?**
    
    - **Discussion**: Not addressed. The paper does not detail documentation of lawful restrictions.
    - **Reference**: Not found (pp.1–9).
8. **CQ28, CQ29, CQ30, CQ32, CQ33, CQ35, CQ37, CQ38**
    
    - **Discussion**: All revolve around correctness, accuracy, duplication, or transparency about usage, or ensuring updates. None of these are mentioned. The focus is on route planning and compliance checks about data movement or location.
    - **Reference**: Not found (pp.1–9).
9. **CQ39 (Agreements with suppliers/third parties)?**
    
    - **Discussion**: Not addressed. The system’s approach does not mention data-processing agreements.
    - **Reference**: Not found (pp.1–9).
10. **CQ40–CQ44 (DPO appointment and contact details)?**
    
    - **Discussion**: Not addressed. The paper does not mention Data Protection Officers.
    - **Reference**: Not found (pp.1–9).
11. **CQ47–CQ52 (Security measures, encryption, destruction of data, incident responses)?**
    
    - **Discussion**: Some mention of a “safety level” for nodes, but there is no discussion of encryption or data destruction.
    - **Reference**: “Node safety level corresponds to the safety protocols supported by each node … high, medium, or low.” (p.5) – This is a simplified concept of security, not an in-depth measure for data destruction or breach handling.
12. **CQ56–CQ58 (Reviewing plans, data breach cooperation)?**
    
    - **Discussion**: Not addressed. The system only covers basic planning scenarios for compliance; no formal data-breach procedure is described.
    - **Reference**: Not found (pp.1–9).
13. **CQ63–CQ65 (International transfers, legal bases, data subject awareness)?**
    
    - **Discussion**: The paper does revolve around **international transfers** (EU vs. non-EU). However, it does not detail the exact “legal bases” or “data subject awareness” beyond noting whether the user allows out-of-EU transfers.
    - **Reference**: “When transferring personal data outside the legislative zone … if a data owner does not grant permission, the plan is declared illegal.” (p.8) – No further detail on documenting the legal basis or user notification.

**Conclusion on Compliance Questions**:  
The paper **does not** explicitly address any of the listed compliance questions in detail; it focuses on high-level route/transfer legality checks (EU vs. non-EU) and rudimentary ethical preference criteria (e.g., safer node). The granular GDPR obligations (retention periods, data subject rights, DPO, etc.) are **not** covered.

---

# Metadata

Below is a distilled set of attributes describing this paper, based on the evaluations in the steps above and our discussion of the inclusion criteria and compliance questions:

All told, the publication is **in English** and **publicly available**, but it does **not** propose a dedicated data provenance model to represent GDPR obligations; hence it is **unrelated** for the strict scope of the inclusion criteria.

---

# References

- [[bonatti2020a]]