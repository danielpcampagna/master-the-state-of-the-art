---
ID: hayashi2023a
authors: Hayashi, Hisashi and Satoh, Ken
category: unrelated
display: hayashi (Online HTN Planning for Data Transfer and Utilization)
due: This paper does not propose a data provenance model. It is a peer-reviewed conference paper focusing on dynamic HTN planning for data transfer with legal/ethical constraints.
entrytype: inproceedings
link: 
name: "Online HTN Planning for Data Transfer and Utilization Considering Legal and Ethical Norms: Case Study"
organization: SCITEPRESS
place: ICAART 2023
pp: 154-164
provenance_related: false
related:
  - HTN planning
  - Data transfers
  - Legal norms
  - Ethical constraints
  - Utilitarian cost
  - Dynamic planning
year: 2023
forward_steps: 2
---

# Summary & Analysis

## Introduction

**Paper Title**  
“Online HTN Planning for Data Transfer and Utilization Considering Legal and Ethical Norms: Case Study” (ICAART 2023, pp. 154–164)

**Main Idea**  
The authors propose a method to plan multi-hop data transfers and data analyses across distributed servers while adhering to relevant legal and ethical constraints. They build on a Hierarchical Task Network (HTN) planning approach (specifically, an “online” forward-chaining HTN planner) so that each partial plan can be dynamically updated in reaction to new information (e.g., about changed legality or ethical acceptability). The paper demonstrates how these constraints can be encoded as preconditions (legal norms) and cost adjustments (ethical norms), illustrated through a case study.

**Key Points**

1. **Motivation**: Data transfer and analysis are complicated by national laws and guidelines such as the GDPR, plus ethical guidelines. Compliance requirements often cannot be fully known in advance, because new information or changes may emerge on distributed servers.
2. **Online HTN Planning**: Building on the Dynagent algorithm, the system supports incremental plan updates (replanning) during execution.
3. **Legal Norms**: Represented as preconditions of actions – if a transfer or analysis step would violate a legal rule, the precondition fails, and the planner must find an alternative.
4. **Ethical Norms**: Treated as adjustable costs. The planner tries to minimize cost, so unethical steps are dispreferred, but can be performed if no other viable plan is available (reflecting a form of utilitarian principle).
5. **Case Study**: They model a small network with seven nodes in different companies and countries, each with data or analysis capabilities. Initially, the plan uses a path that becomes illegal as new rules are discovered; the planner replans to avoid that route. Later, an ethical constraint arises, raising the cost for using certain nodes belonging to another company. The planner again replans to avoid the unethical route if possible.

**Quotations**

1. “In this paper, we propose a dynamic hierarchical task network (HTN) planning method that considers legal and ethical norms while planning multi-hop data transfers and data analyses/transformations.” [p. 154]
2. “We also show that legal norms can be expressed as the preconditions of tasks and actions, and ethical norms can be expressed as the costs of tasks and actions [...] following the ethical theory of utilitarianism.” [p. 154]
3. “Considering real international data transfers among distributed servers, replanning is crucial because the latest information necessary for planning is also distributed and not available when initially planning.” [p. 155]
4. “The data-transfer plan must be dynamically checked and updated [...] even in the middle of the plan execution when new information is found on distributed servers.” [p. 155]
5. “The objective is to deliver the analysis output of specified data to a specified node for a specific purpose.” [p. 156]
6. “Therefore, it is important to dynamically check and update the plan while executing it.” [p. 162]

---

## Evaluation Based on Inclusion Criteria

1. **Strictly proposes a data provenance model to represent activities information related to GDPR obligations?**
    
    - The paper focuses on using HTN planning to orchestrate data transfer steps so that legal and ethical constraints are not violated. It does **not** present or formalize a data provenance/lineage model. Instead, it encodes constraints on data usage/transfers via HTN methods, costs, and preconditions.
    - **Reference**: “We present a dynamic [...] HTN planning method that considers legal and ethical norms. [...] we show how data-transfer tasks can be represented by task-decomposition rules of total-order HTN planning.” [p. 154] There is no mention of a “provenance model.”
2. **Should be useful to address the compliance questions we have?**
    
    - The paper does not provide a structured approach to answering the user’s detailed compliance questions (e.g., data retention, right to object, data subject access requests). It only shows a blueprint for how a dynamic planner can skip illegal or high-cost (ethically questionable) steps. Hence, it does **not** directly address the specific compliance questions.
    - **Reference**: They focus on real-time replanning for data usage/transfer constraints, not on enumerating or ensuring coverage of all compliance questions (pp. 154–164).
3. **Proposed model publicly available for comparison?**
    
    - The paper introduces an algorithm and an example, but does not provide a publicly available specification or library of norms. It is primarily a conceptual and algorithmic exposition.
    - **Reference**: Implementation references appear as small code snippets in SWI Prolog. No stable link is mentioned (p. 161–163).
4. **Document is in English or Portuguese?**
    
    - The paper is written in English.
    - **Reference**: Entire text is in English [pp. 154–164].
5. **Document publicly available or accessible from digital libraries (e.g. CAPES CAFE)?**
    
    - It appears in ICAART 2023 Proceedings, published by SCITEPRESS. Likely accessible via academic repositories or purchase.
    - **Reference**: “In Proceedings of the 15th International Conference on Agents and Artificial Intelligence (ICAART 2023) [...]” [cover page, p. 154].
6. **Peer-reviewed?**
    
    - ICAART is a peer-reviewed conference. So yes, it meets the criterion for a refereed publication.
    - **Reference**: “ICAART 2023 [...]. Copyright © 2023 by SCITEPRESS.” [p. 154]

**Verdict**  
This paper does **not** propose a data provenance model. Although it is indeed peer-reviewed and in English, it fails the key criterion about modeling data provenance for GDPR compliance. Thus, by the user’s classification scheme, it should be labeled **unrelated**.

---

## Discussion on Compliance Questions

Below we consider whether the paper addresses each compliance question (CQ08–CQ65) regarding data processing under GDPR:

- **Retention times (CQ08, CQ29, CQ30)**: No mention of data-retention policies or usage durations.
- **Ensuring compliance operations (CQ09)**: The planner ensures each step meets constraints, but the user’s question about “identifying actions required for full GDPR compliance” is not answered specifically.
- **Consent standard (CQ11)**: Not addressed.
- **Ability to respond to data subject rights (CQ17, CQ20, CQ21, etc.)**: The paper focuses on general data transfers, not data subject requests or complaint-handling.
- **Security controls, breach management (CQ47–CQ58)**: These aspects (encryption, breach logs) are not covered.
- **International transfers (CQ63–CQ65)**: The system does show how to avoid illegal cross-border data transfers, but it does not address the broad range of considerations or documentation specifics.

Overall, the paper shows how to encode “is it legal or not” as a precondition to block certain cross-border steps, and how to reflect “ethical or not” as a cost factor. It does not discuss or systematically handle the detailed compliance questions from the user’s list.

---

# References

- [[bonatti2020a]]