---
ID: taheri2021a
authors: Taheri, Yousef; Bourgne, Gauvain; Ganascia, Jean-Gabriel
category: unrelated
display: taheri (A Compliance Mechanism for Planning in Privacy Domain Using Policies)
due: This paper focuses on AI planning and compliance checking but does not propose a data provenance model for GDPR obligations.
entrytype: inproceedings
link: ""
name: A Compliance Mechanism for Planning in Privacy Domain Using Policies
organization: Fifteenth International Workshop on Juris-informatics (JURISIN 2021)
place: Kanagawa, Japan
pp: ""
provenance_related: false
related: 
year: 2021
forward_steps: 2
---

# Summary & Analysis

## Introduction & Motivation

**Main ideas**

- Proposes a framework that integrates automated planning with GDPR compliance checking.
- Uses Event Calculus in an Answer Set Programming (ASP) environment to generate sequences of data processing actions (plans).
- Uses the SPECIAL policy language to encode GDPR obligations and user consent constraints.

**Key Points**

1. The authors aim to bridge AI methods (specifically planning) with a legal compliance checker for personal data processing.
2. They introduce a modular architecture: (i) a planning module generating all possible action sequences, and (ii) a “compliance engine” verifying those sequences against GDPR constraints.
3. The framework is illustrated via a scenario where personal data is transferred and analyzed across various servers and geographical locations, and the system identifies which plan(s) comply with GDPR rules and which do not (p.1–3).

**Representative Quotations**

1. “Our goal is to design an AI agent that generates a sequence of data processing actions to satisfy a given goal… and simultaneously ensure compliance with GDPR.” (p.1)
2. “We propose a modular framework that is capable to generate possible plans… check the compliance of the plan with GDPR regulatory constraints… and provide explanation of missing obligations in case of a non-compliant plan.” (p.1)
3. “We use Answer Set Programming (ASP) and event calculus formalism to model the planning problem and… the SPECIAL policy language as an existing work to translate GDPR requirements…” (p.2)

---

## Method & Technical Approach

**Main ideas**

- Planning Model:
    - Relies on Event Calculus to encode the states (fluents) and events (actions) for data movement or data transformations.
    - Example actions: “transfer” and “analyse” require preconditions (e.g., data presence on a specific server) and produce effects (e.g., new data objects).
- Compliance Engine:
    - Encodes GDPR obligations as a set of rules or “fulfillment” predicates in ASP.
    - SPECIAL-based definitions capture relevant attributes (data category, purpose, location, recipient, legal basis).
    - The engine flags missing obligations if a plan’s action does not meet certain regulatory constraints (p.3–6).

**Key Points**

1. Each action is annotated with a “business policy” including data category, purpose, location, recipient, and legal basis (p.5).
2. The system can detect noncompliant actions (e.g., “transfer to a server outside EU without adequate safeguards under Art.46(2),” or “lacking a valid legal basis under Art.6(1)”) (p.7–8).
3. Event Calculus rules generate possible sequences of actions from an initial to a goal state, ignoring compliance. The compliance engine then filters out or explains any regulatory failures (p.6).

**Representative Quotations**

1. “We formalize agent actions (e.g., ‘transfer’, ‘analyse’) in ASP… each with preconditions and effects that change the domain fluents.” (p.4)
2. “The compliance engine assigns legal information to each action… then checks for obligations in the top-level GDPR classification… if not fulfilled, the plan is non-compliant.” (p.5)
3. “We also represent user consent as a usage policy in SPECIAL. An action is coherent with that consent if it does not differ on data category, purpose, or location attributes.” (p.6)

---

## Evaluation & Results

**Main ideas**

- Demonstrates two simplified scenarios to show how the framework systematically flags noncompliant sequences.
- Example 1: A user’s consent allows data transfers only in the EU, so any “transfer” to a US-located server fails the compliance check.
- Example 2: GDPR Chapter 5 obligations for third-country transfers are tested, showcasing how missing “adequate level of protection” leads to plan noncompliance (p.7–8).

**Key Points**

1. The system enumerates all possible action sequences that achieve the same final objective (e.g., data is analyzed on a certain server).
2. It then classifies each sequence as fully compliant or missing specific obligations (with short textual explanations).
3. The authors highlight that the system can be extended to more complex sets of GDPR obligations, data categories, and action types (p.8).

**Representative Quotations**

1. “Our results show that some plans comply with the data subject’s consent while others fail… for instance, transferring data from s2 to s1 is not covered by the data subject’s consent.” (p.8)
2. “Plan 2 is non-compliant because the required conditions for cross-border data transfer are not satisfied… the engine reports missing obligations such as ‘art46_2_e_ApprovedCodeOfConduct’ and so forth.” (p.8)

---

# Evaluation Based on Inclusion Criteria

Below, we check the paper’s content against each inclusion/exclusion criterion:

1. **Propose a data provenance model for activities related to GDPR obligations**
    
    - The paper focuses on an automated planning approach combined with compliance checking. While it tracks sequences of actions on personal data, it **does not** present a data provenance model describing all processes/lineage in the sense of a dedicated “provenance” specification. The approach is policy-based compliance, not an explicit provenance representation framework (p.1–8).  
        **Conclusion**: Fails Criterion #1.
2. **Model is useful for addressing the specific compliance questions**
    
    - The system can check compliance with high-level GDPR obligations (e.g. Chapter 5 cross-border transfers) or user consent restrictions. However, it does **not** specifically address the enumerated compliance questions (retention, right to erasure, data subject rights time limits, etc.). It has a general approach to policies but not a question-by-question compliance analysis (p.6–8).  
        **Conclusion**: Does not explicitly address or structure solutions to the compliance questions.
3. **Model is publicly available**
    
    - The authors mention code in a GitLab repository, but it’s not a “data provenance model.” Their code is for planning + compliance.  
        **Conclusion**: No direct “model” for provenance is offered, so this point is moot.
4. **Language**
    
    - The paper is in English (p.1–10).  
        **Conclusion**: Satisfied.
5. **Document is publicly available**
    
    - The paper is presumably published in JURISIN 2021 workshop post-proceedings. Possibly accessible.  
        **Conclusion**: Likely satisfied.
6. **Peer-reviewed**
    
    - JURISIN is a known international workshop. Likely peer-reviewed.  
        **Conclusion**: Satisfied.

**Overall Verdict**

- Does **not** propose a data provenance model; thus fails the key inclusion criterion.

---

# Discussion on Compliance Questions

This paper does **not** provide direct discussion of the specific compliance questions (like data retention periods, DSAR handling, minimum retention, etc.). Instead, it generically encodes broad “obligations” from GDPR, focusing on cross-border transfers (Chapter 5) and user consent checks. For each question below, there is no direct coverage:

- **CQ08–CQ65**: The text does not address details of these particular questions (p.1–9). All references to GDPR revolve around ensuring that any data-processing action has a valid legal basis, satisfies user consent, and meets general obligations around cross-border transfers.

Hence, no specific coverage of the enumerated compliance queries.

---

# Result

Based on the above analysis, the paper is categorized as _unrelated_ because it does not propose a strict data provenance model and does not systematically address the enumerated compliance questions.

---

# References

- [[bonatti2020a]]