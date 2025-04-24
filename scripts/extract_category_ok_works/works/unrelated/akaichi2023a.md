---
ID: akaichi2023a
authors: Akaichi, Ines; Flouris, Giorgos; Fundulaki, Irini; Kirrane, Sabrina
category: unrelated
display: "akaichi (GUCON: A Generic Graph Pattern based Policy Framework for Usage Control Enforcement)"
due: Although the paper introduces a framework for usage control enforcement, it does not strictly present a provenance model to address GDPR obligations.
entrytype: inproceedings
link: ""
name: "GUCON: A Generic Graph Pattern based Policy Framework for Usage Control Enforcement"
organization: RuleML+RR (2023)
place: ""
pp: ""
provenance_related: false
related: 
year: 2023
forward_steps: 2
---

# Summary & Analysis

## Introduction & Motivation

**Main Ideas**

- Introduces GUCON, a generic policy framework aimed at specifying and enforcing usage control (UC) rules in decentralized environments.
- Proposes a formal semantics leveraging graph patterns to express and reason about policies with deontic operators (permissions, prohibitions, obligations, dispensations).
- Seeks to unify usage control requirements (extending basic access control) with explicit policy-based enforcement, conflict resolution, and compliance assessment.

**Key Points**

1. Modern distributed scenarios require robust usage control beyond conventional access control.
2. Most existing approaches handle domain-specific use cases or lack formal semantics, limiting automated compliance checks (p.1–2).
3. GUCON’s key aim: a flexible, semantically grounded framework for “active policy enforcement” – identifying conflicts, ensuring compliance, and checking user requirements (p.2).

**Representative Quotations**

1. “We propose GUCON, a generic policy framework that allows for the expression of and reasoning over granular UC policies.” (p.1)
2. “Existing solutions have limitations in expressing and enforcing usage control policies due to difficulties in capturing complex requirements and the lack of formal semantics.” (p.1)
3. “We show how instantiations provide a bridge between abstract formalism and concrete implementations, thus allowing existing reasoners and implementations to be leveraged.” (p.1)

---

## GUCON Framework

**Main Ideas**

- Relies on RDF graphs and “graph pattern expressions” (from SPARQL) to specify conditions under which deontic rules apply.
- A usage control policy (UCP) is a set of usage control rules (UCR). Each UCR is effectively “IF condition THEN deontic-operator(action).”
- Deontic operators (permission A, prohibition P, obligation O, dispensation D) specify what is (or is not) allowed or required in the presence of certain graph patterns.

**Key Points**

1. A knowledge base (KB) stores domain facts and events in RDF.
2. A usage control policy (UCP) includes multiple usage control rules, each with a condition (graph pattern) and a deontic statement on an (entity, action, resource) triple (p.3–5).
3. GUCON addresses conflicts between rules by applying meta-policy precedence (e.g. negative overrides positive) and modifies the weaker rule’s condition to restore consistency (p.7–8).

**Representative Quotations**

1. “Policies are specified using conditional deontic rules based on graph patterns and deontic concepts… offering flexibility in expressing general UC restrictions.” (p.1)
2. “We introduce the concept of state of affairs, which captures domain knowledge and events, and serves as the basis for reasoning about, and enforcing UC policies.” (p.2)
3. “In GUCON, we also introduce the concept of active rule—i.e., a usage control rule whose condition is satisfied by the KB.” (p.5)

---

## Reasoning & Enforcement

**Main Ideas**

- Three core tasks: (1) **Consistency checking**, detecting conflicting rules (e.g. a single scenario triggers both permission and prohibition for the same action). (2) **Compliance checking**, ensuring the KB’s actions are in line with the policy. (3) **Requirements checking**, listing user rights and obligations.
- Proposes algorithms for each. E.g., conflict resolution updates the weaker rule’s condition using “MINUS” to exclude the conflicting scenario (p.7–9).
- Demonstrates how to leverage existing engines by instantiating the framework in SHACL, OWL 2, and ODRL (p.9–13).

**Key Points**

1. **Consistency checking** algorithm identifies pairs of rules with deontic dilemmas (Obligations vs. Prohibitions, etc.) on the same action, then resolves them per a meta-policy (p.8).
2. **Compliance checking** is ex-post, verifying if performed actions breach any active prohibition, or if an unfulfilled obligation is found (p.8–9).
3. The authors exemplify how to encode usage control rules in SHACL-SPARQL, in OWL 2 axioms, and as ODRL policies—though ODRL has limitations with formal semantics (p.10–13).

**Representative Quotations**

1. “Using GUCON, diverse types of usage control policies can be explicitly defined and effectively enforced, owing to… formal implementable semantics.” (p.2)
2. “Conflict resolution is performed by establishing a precedence relation… If a rule r2 is stronger than r1, the condition of r1 is modified using MINUS, effectively removing the conflicting scenario.” (p.7–8)
3. “We propose ex-post compliance of a given KB against a policy or a set of policies… The system halts as soon as a non-compliant rule is identified.” (p.8–9)

---

## Instantiations & Assessment

**Main Ideas**

- Shows how GUCON rules can be mapped to SHACL or OWL classes with complex restrictions (intersectionOf, unionOf).
- ODRL used for digital rights management, but can express some usage control. They highlight partial coverage in ODRL for “dispensation” and advanced negation or optional patterns.
- Observes that each language has different expressiveness trade-offs: SHACL with SPARQL rules can handle rich patterns, OWL has formal decidability, ODRL is flexible with profiles but lacks formal semantics.

**Key Points**

1. The “UCP core ontology” merges deontic classes (Permission, Prohibition, Obligation, Dispensation) with action, resource, entity definitions in RDF/OWL (p.10).
2. Each example from the motivating scenario is recast in SHACL, OWL, or ODRL with suitable “profile” definitions for the domain.
3. The authors plan future work on automated translation from the abstract GUCON specification to these languages (p.13–14).

**Representative Quotations**

1. “We provide instantiations using SHACL, OWL, and ODRL… bridging the gap between GUCON’s abstract formalism and concrete implementations.” (p.1, p.10)
2. “Although ODRL lacks explicitly defined formal semantics, there is active w3c community work on formal semantics, which would represent a significant advancement.” (p.13)
3. “We plan to investigate how we can facilitate the mapping between our framework and the representation languages by implementing and evaluating automated translation algorithms.” (p.14)

---

# Evaluation Based on Inclusion Criteria

1. **Proposes a data provenance model to represent GDPR obligations**
    
    - The focus is on usage control policies (permissions, prohibitions, obligations, dispensations), enforced via graph patterns. Although it references GDPR compliance scenarios, the paper does not introduce a _data provenance model_ for capturing, e.g., data lineage or transformations for GDPR obligations (p.1–2).  
        **Conclusion**: Fails criterion #1.
2. **Usefulness of the proposed model for addressing specific compliance questions**
    
    - The approach is about usage control policies, deontic rules, and conflict resolution. While it may help with certain GDPR-based constraints (like “Do not process data without user consent”), it does not map or systematically address the enumerated compliance questions (data retention, subject requests, etc.) (p.2–3).  
        **Conclusion**: Does not address or solve the compliance questions in the user’s list.
3. **Public availability of the proposed model**
    
    - The framework is introduced academically, with a GitHub reference for partial code or examples. However, no standard or widely recognized publicly available data-provenance model is put forth.  
        **Conclusion**: Not relevant for direct inclusion.
4. **Document language**
    
    - The paper is in English (p.1–15).  
        **Conclusion**: Satisfied.
5. **Document is publicly available**
    
    - Presumably it is from a workshop or conference. Possibly open or not.  
        **Conclusion**: Could be publicly accessible, but not a factor for inclusion regarding a GDPR provenance model.
6. **Peer-reviewed**
    
    - It appears in the RuleML+RR 2023 proceedings, presumably peer-reviewed.  
        **Conclusion**: Satisfied.

**Overall Verdict**

- The paper does not propose a dedicated data provenance model for GDPR obligations. Thus, **unrelated** per the inclusion criteria.

---

# Discussion on Compliance Questions

The paper does not directly address the user’s enumerated GDPR compliance questions (CQ08–CQ65). Although the authors discuss usage control in relation to data privacy, they do not present or solve any specific queries about retention periods, data subject rights, etc. The approach is a general usage control framework with formal, policy-based enforcement. Hence, no direct coverage of the enumerated compliance questions.

---

# References

- [[bonatti2020a]]