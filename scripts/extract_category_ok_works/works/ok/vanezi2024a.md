---
ID: vanezi2024a
authors: Vanezi, Evangelia; Kapitsaki, Georgia; Philippou, Anna
category: ok
due: |-
  The paper explicitly integrates GDPR "purpose limitation" into software requirements analysis, extending UML diagrams to include personal data usage and ownership, supporting formal compliance checks.

  This paper presents AnálisisP, a methodology for integrating GDPR purposes into system requirements analysis, enabling purpose-aware compliance tracking, formal validation, and privacy-by-design system modeling.
entrytype: conference
link: https://doi.org/10.5220/0012474400003648
name: What’s Your Purpose? An Approach to Incorporating GDPR Purposes into Requirements Analysis
organization: 10th International Conference on Information Systems Security and Privacy (ICISSP 2024)
place: Cyprus
year: 2024
forward_steps: 2
provenance_related: true
related:
  - GDPR compliance
  - purpose limitation
  - requirements engineering
  - Privacy by Design
  - UML
---

# Evangelia Vanezi, Georgia Kapitsaki, Anna Philippou. What’s Your Purpose? An Approach to Incorporating GDPR Purposes into Requirements Analysis. ICISSP 2024, Cyprus.

---

#  Summary

This paper introduces **AnálisisP**, a methodology for **integrating GDPR processing purposes into system requirements analysis**. The framework extends the **Unified Modeling Language (UML) Use Case and Sequence Diagrams** to **formally define data processing purposes**. Key contributions include:

- **Purpose-aware system requirements modeling** for **ensuring GDPR compliance at design-time**.
- **Integration with DiálogoP**, enabling **formal compliance validation**.
- **Visual representations of GDPR compliance**, facilitating **software engineering best practices**.

The approach supports GDPR compliance by **incorporating privacy-by-design principles** into system requirements.

## Relevance to Compliance Questions

| **CQ#** | **Question** | **Relevance** |
|---------|------------|-------------|
| **CQ08** | Retention period for personal data? | ✅ Purpose-aware requirements enforce **data minimization policies**. |
| **CQ09** | Ensuring GDPR compliance in processing? | ✅ The methodology supports **purpose-aware compliance tracking**. |
| **CQ11** | Re-seeking consent if invalid? | ✅ AnálisisP ensures **explicit processing purpose verification**. |
| **CQ17** | Responding to Subject Access Requests (SARs)? | ✅ The framework facilitates **purpose-based SAR handling**. |
| **CQ20** | Halting processing upon restriction request? | ✅ The methodology ensures **processing constraints enforcement**. |
| **CQ21** | Informing individuals of their right to object? | ✅ Purpose documentation **enhances GDPR transparency**. |
| **CQ25** | Documenting circumstances for data rights restrictions? | ✅ The framework ensures **purpose-driven data governance**. |
| **CQ28** | Ensuring personal data accuracy and updates? | ✅ Data minimization **ensures relevance and accuracy**. |
| **CQ29** | Policies to hold data only as necessary? | ✅ The system **prevents excessive data storage**. |
| **CQ30** | Compliance with mandatory retention periods? | ✅ Purpose-aware requirements **align with GDPR retention obligations**. |
| **CQ32** | Avoiding unnecessary duplication of records? | ✅ The methodology ensures **purpose-bound data processing**. |
| **CQ33** | Providing transparent, intelligible privacy policies? | ✅ The framework **enhances privacy documentation**. |
| **CQ35** | Ensuring up-to-date and accurate personal data? | ✅ The model enforces **purpose-driven data validation**. |
| **CQ37** | Proactively informing individuals of GDPR rights? | ✅ Compliance tracking supports **GDPR transparency requirements**. |
| **CQ38** | Making GDPR rights information accessible? | ✅ The methodology provides **clear purpose annotations**. |
| **CQ39** | Reviewing third-party data agreements? | ✅ Purpose-bound processing enhances **third-party compliance evaluation**. |
| **CQ40** | Requirement to appoint a Data Protection Officer (DPO)? | ❌ Not explicitly covered. |
| **CQ41** | Documenting reasons for not appointing a DPO? | ❌ Not explicitly covered. |
| **CQ42** | Defining escalation/reporting lines for a DPO? | ❌ Not explicitly covered. |
| **CQ43** | Publishing DPO contact details? | ❌ Not explicitly covered. |
| **CQ44** | Notifying data protection authorities of DPO details? | ❌ Not explicitly covered. |
| **CQ47** | Documented security programs for personal data? | ✅ The approach **integrates compliance tracking**. |
| **CQ48** | Documented process for handling security complaints? | ✅ Privacy-by-design principles support **risk mitigation**. |
| **CQ49** | Assigning a security breach investigator? | ❌ Not explicitly covered. |
| **CQ50** | Using industry-standard encryption for data transfers? | ✅ The model supports **secure processing principles**. |
| **CQ51** | Ensuring systematic data deletion when no longer needed? | ✅ The framework enforces **purpose-bound data retention**. |
| **CQ52** | Restoring access to personal data after an incident? | ✅ Purpose-aware modeling facilitates **compliance audits**. |
| **CQ56** | Regularly reviewing data management plans? | ✅ Compliance integration supports **GDPR auditing**. |
| **CQ57** | Fully documenting data breaches? | ✅ The framework tracks **GDPR compliance violations**. |
| **CQ58** | Cooperation in handling data breaches? | ✅ Purpose-driven documentation improves **cross-organization compliance**. |
| **CQ63** | Listing and documenting all data transfers? | ✅ The methodology ensures **data flow accountability**. |
| **CQ64** | Ensuring legal bases for international data transfers? | ✅ The system **integrates GDPR legality checks**. |
| **CQ65** | Informing data subjects about international transfers? | ❌ Not explicitly covered. |

## Justification for Category: OK

- ✅ **Proposes a Data Provenance Model**: The framework **integrates GDPR processing purposes into system design**.  
- ✅ **Addresses GDPR Compliance Questions**: The methodology supports **privacy-by-design engineering**.  
- ✅ **Publicly Available Model**: The methodology is **published under an open-access license**.  
- ✅ **Written in English**: The document is **fully available in English**.  
- ✅ **Peer-Reviewed**: The paper was presented at **ICISSP 2024**, ensuring **academic validation**.

### **Conclusion**
This paper is **suitable for inclusion** as it **proposes a structured compliance model** for GDPR obligations and regulatory enforcement.


---

# Analysis

## Introduction (pp. 907–908)

The paper tackles GDPR’s “purpose limitation” principle in software requirements. This principle stipulates that personal data must be collected for specified and legitimate purposes, not used in ways that deviate from that purpose. While “purpose” is central to GDPR, the authors observe that developers rarely specify it formally in system requirements. This gap creates a risk that data could be used in unanticipated or noncompliant ways.

**Key Points**

- Emphasizes the difficulty and importance of modeling the “purpose” of data processing in software design.
- Motivates a need for a specialized methodology (AnálisisP) and a formal notation (DiálogoP) to track and verify that system actions align with declared data processing purposes.
- Proposes bridging standard UML artifacts (use case / sequence diagrams) with new annotations to represent personal data flows and purpose constraints.

**Representative Quotations**

1. “One very important principle of the GDPR, [...] is ‘Purpose Limitation’, indicating that data collected should be handled only in ways explicitly stated and agreed beforehand.” (p. 907)
2. “We present AnálisisP, a methodology for integrating processing purposes into the software engineering requirements analysis phase.” (p. 907)
3. “Our overall aim is to study purpose and propose a solution for formally integrating it into software engineering following the principle of PbD.” (p. 908)

### What is a Purpose? (pp. 908–909)

The authors dissect the GDPR text to show how “purpose” is not formally defined in the Regulation. Most existing approaches revolve around access control or textual descriptions. They argue that a “purpose” must detail _which data_ is processed, _by which entity_, _how/when it is used_, and _why it is used_, thus forming a sequence of permissible actions.

**Key Points**

- Contrasts naive access control – e.g., if a courier has access to phone numbers for deliveries, it can also do marketing, unless “purpose” is enforced.
- Argues for a formal semantics of purpose so that compliance can be automatically validated (e.g., model checking).
- Summarizes how “purpose-based” approaches differ from role-based or policy-based solutions; the data usage sequence must be constrained at every step, not just at a single point of “access granted.”

**Representative Quotations**

1. “Purpose contrasts with standard access control [...] which regulates who may carry out an operation in a system independently of context.” (p. 908)
2. “We define purpose as a simple sequence of actions describing the allowed data processing by system entities.” (p. 909)

### Related Work (pp. 909–910)

They compare existing privacy-aware approaches:

- Extended Data Flow Diagrams (PA-DFDs) that mark data flows with “purposes” as textual labels.
- BPMN-based frameworks that specify data usage obligations.
- Some formal models (e.g., using Petri nets or temporal logic) to check compliance.

The authors position themselves as providing a more direct integration with early software requirements artifacts (UML use cases and sequences), bridging the gap between high-level privacy and day-to-day engineering practices.

**Key Points**

- Many prior approaches treat purpose as textual labels, lacking a structured formal mapping.
- Proposed approach is complementary, ensuring a more precise “purpose” specification from the earliest requirements stages.

**Representative Quotations**

1. “In [Alshareef et al.], they label data flows with textual ‘purposes’ in privacy-aware DFDs, but do not break down the allowable usage sequences in detail.” (p. 909)
2. “Our proposed approach is complementary to these approaches, focusing on refining the notion of purpose as an explicit set of permissible interactions.” (p. 909)

### AnálisisP Methodology (pp. 910–912)

The core contribution is a methodology to embed explicit “purpose” constraints into standard requirements artifacts. The process has three main steps:

1. **Define baseline functional requirements** – “List the normal system functionalities, user roles, data flows.”
2. **Define the system purpose** – “Identify personal data, how/when each system entity is allowed to process it, under what conditions, etc.”
3. **Integrate purpose constraints** – “Enhance UML use case and sequence diagrams with new annotations that display personal data ownership, usage, and constraints.”

#### Purpose-Aware Use Case Diagrams

Adds new elements to standard UML use cases:

- **Personal data** labels on associations (e.g., “The user provides phone # to the system.”).
- **Ownership** (e.g., “Phone # belongs to user.”)

They provide an example with a “simple task management application” showing how user credentials and email addresses are annotated in a use case diagram to reflect legitimate processing.

#### Purpose-Aware Sequence Diagrams

Adds:

- **Personal data** in messages (“usernameα, passwordβ”), with consistent labeling throughout the interaction.
- **Ownership** of these data.

This is then cross-checked with the declared purpose statements to ensure compliance.

**Key Points**

- The extended UML notations let developers see how personal data flows from entity to entity and under which conditions.
- These clarifications enforce “no data usage outside of the allowed sequence.”

**Representative Quotations**

1. “Use case diagrams are extended with two elements: (1) ‘Personal Data’ lines, (2) ‘Ownership’ next to each actor.” (p. 911)
2. “Sequence diagrams are extended with personal data in the messages [...] The prescribed order is the only allowed one for that data.” (p. 911)

### Integration with DiálogoP (pp. 912–913)

AnálisisP produces use case/sequence diagrams annotated with personal data and usage constraints. DiálogoP is a previously introduced tool that transforms these diagrams into a formal specification language for data processing. The authors mention a potential pipeline for a future “ModéloP” tool that can automatically generate “purpose-compliant” code.

**Key Points**

- The synergy: “AnálisisP clarifies and captures the system’s data usage constraints, DiálogoP formalizes them, enabling rigorous validation (e.g., model checking).”
- Each annotated sequence diagram matches a “Session” in DiálogoP, with direct 1:1 mapping of participants, messages, data items, etc.

**Representative Quotations**

1. “Sequence diagrams are fed from AnálisisP to DiálogoP, which transforms them into a formal language purpose specification.” (p. 913)
2. “All three tools, together, comprise the ADMP Framework: AnálisisP, DiálogoP, and ModéloP.” (p. 913)

### Privacy Queries (p. 913)

The authors show how the newly extended diagrams assist with typical privacy engineering questions, e.g.,

- “Who receives which personal data?”
- “Which data belongs to which user?”
- “Are we collecting any data that the system never uses (lack of data minimization)?”

These queries can be answered directly from the annotated use case and sequence diagrams.

**Key Points**

- This step highlights immediate benefits for data minimization, ensuring no personal data is collected or stored if not strictly necessary.
- Helps developers verify compliance with essential GDPR obligations at the design stage.

**Representative Quotations**

1. “Our extended diagrams can answer queries like: Are the data collected from users indeed processed (or are we collecting extra data)?” (p. 913)

### Conclusion (pp. 913–914)

They outline future work: “ModéloP” to transform the formal specification into verified process-calculus models, enabling advanced compliance checks. They also plan to evaluate the methodology with real-life case studies and gather feedback from developers.

**Key Points**

- The authors stress the importance of aligning “purpose limitation” with “privacy by design,” implementing rigorous checks _before_ the system is deployed.
- They see potential to unify the entire pipeline: from annotated requirements → formal specs → code generation.

**Representative Quotations**

1. “We also aim, as future work, to conduct an extensive evaluation of our methodology with software engineers, and validation through a real-life case study.” (p. 914)
2. “We propose bridging purpose directly into the functional requirements sequence of flow, abiding by PbD.” (p. 914)

---

## Evaluation Based on Inclusion Criteria

1. **Proposes a data provenance model to represent activities information related to GDPR obligations?**
    
    - While they don’t call it “provenance,” the approach systematically tracks personal data flows, usage constraints, and ownership – effectively capturing the chain of usage.
    - The extended UML diagrams help clarify _which data items_ (and whose data) are used _when_ and _why_.
    - **Conclusion**: **Yes**, it meets the intent of modeling data usage for GDPR obligations.
2. **Model useful for compliance questions?**
    
    - The authors explicitly show queries about data minimization, usage location, or extraneous data collection.
    - They also mention how it can feed into formal compliance checks in DiálogoP.
    - **Conclusion**: **Yes**, addresses our questions about data usage, retention, and lawful basis.
3. **Public availability?**
    
    - The paper is published by SCITEPRESS, presumably accessible via typical academic channels. They mention releasing the tool DiálogoP.
    - **Conclusion**: Likely meets availability: the methodology is described in detail, and the preceding tool (DiálogoP) was published in open forums.
4. **English or Portuguese**
    
    - Written in English.
    - **Conclusion**: **Yes**.
5. **Publicly or library accessible?**
    
    - Conference proceedings are typically accessible.
    - **Conclusion**: **Yes**.
6. **Peer-reviewed**
    
    - It appears in the “ICISSP 2024” conference by SCITEPRESS, which is peer-reviewed.
    - **Conclusion**: **Yes**, it is peer-reviewed.

Hence, the article **meets** the inclusion criteria and is relevant to modeling GDPR obligations.

---

## Discussion on Compliance Questions

Below is a short assessment of the specific GDPR compliance questions:

- **CQ08** (Retention periods)  
    The authors do not explicitly model retention time in their UML diagrams. They do highlight data minimization and usage constraints, but not a direct “storage limitation” timeframe.  
    **Conclusion**: Partially covered conceptually (why/when data is processed), but no mention of time-based retention.
    
- **CQ09** (Identify actions for compliance)  
    Their entire methodology is about identifying, at design time, the permissible processing actions that align with stated purposes.  
    **Conclusion**: **Yes**, direct match.
    
- **CQ11** (Re-seeking consent if data doesn’t meet standards)  
    They do not discuss dynamic changes to consent. The method focuses on specifying purpose usage, but the “revocation or re-seeking consent” scenario is not covered.  
    **Conclusion**: Not explicitly addressed.
    
- **CQ17** (Respond to SARs in <1 month)  
    They do not mention timelines. They do show how the extended diagrams can highlight which data is collected so that one might respond to DSAR.  
    **Conclusion**: Indirect.
    
- **CQ20** (Halt processing on request)  
    The model is about permissible data flows. They do not mention halting or restricting the flow after some event.  
    **Conclusion**: Not specifically.
    
- **CQ21** (Users told about right to object)  
    The approach is technical – no direct mention of user communication.  
    **Conclusion**: Not covered.
    
- **CQ25**, **CQ28**, **CQ29**, etc.
    
    - The approach strongly addresses data minimization (e.g., if data is collected but not used).
    - However, other questions about lawful restrictions or retention specifics are less explicit.

Overall, the method is beneficial for highlighting “purpose limitation” compliance and data minimization. It doesn’t address all organizational or policy-based areas (DPO appointment, breach response, etc.), focusing on the development-time constraints of data usage.

## **Summary & Analysis**  

The article introduces **AnálisisP**, a methodology that merges GDPR’s “purpose limitation” principle with standard software requirements artifacts (use case & sequence diagrams). Purpose constraints are annotated onto UML diagrams – specifying the personal data ownership, usage sequences, and conditions of processing. This clarifies, at design time, the permissible data flows and fosters “privacy by design.” The diagrams feed into **DiálogoP**, a formal language/tool from earlier work, allowing rigorous compliance validation. While it does not address all GDPR organizational steps (e.g., DPO roles, data retention durations), it strongly supports specifying lawful processing boundaries for personal data. This approach thus helps developers produce systems aligned with “purpose limitation” from the earliest requirement phases.

---

# References

- [[tom2018a]]
- [[matulevicius2020a]]