---
ID: hublet2024a
authors: Hublet, François and Kvamme, Alexander and Krstić, Srđan
category: unrelated
display: hublet (Towards an Enforceable GDPR Specification)
due: This paper is not peer-reviewed (arXiv preprint) and does not propose a data provenance model. Thus it does not meet the inclusion criteria.
entrytype: article
link: http://arxiv.org/abs/2402.17350v1
name: Towards an Enforceable GDPR Specification
organization: arXiv
place: arXiv
pp: 1-14
provenance_related: false
related:
  - GDPR
  - Runtime Enforcement
  - Formal Methods
  - Privacy by Design
year: 2024
forward_steps: 2
---

# Summary & Analysis

## Introduction (Section 1)

The paper highlights the challenge of achieving Privacy by Design in software systems and proposes Runtime Enforcement (RE) as a method to ensure systems remain compliant with privacy regulations at runtime. The authors emphasize that privacy regulations, such as the GDPR, need to be translated into a precise and formally enforceable specification for RE to be applied.

**Key Points**

- The motivation stems from the difficulty of ex-post compliance approaches (fines and after-the-fact checks) and the need for more pro-active enforcement mechanisms.
- The proposal is to use a formal, machine-readable specification of the GDPR, coupled with an enforcer that can intercept system actions and ensure they are compliant.
- The paper provides a methodology for creating such enforceable specifications, illustrating it with a partial formalization of the GDPR.

**Quotations**

1. “With mounting evidence that current regulations such as the EU’s General Data Protection Regulation (GDPR) are poorly implemented by a majority of data controllers [...], the capacity of ex-post enforcement and fines to bring about widespread compliance appears limited.” [p. 1]
2. “One emerging technique to realize PbD is Runtime Enforcement (RE), in which an enforcer, loaded with a specification of a system’s privacy requirements, observes the actions performed by the system and instructs it to perform actions that will ensure compliance [...].” [p. 1]
3. “To be able to use RE techniques for PbD, privacy regulations first need to be translated into an enforceable specification.” [p. 1]
4. “In this paper, we report on our ongoing work in formalizing the GDPR. We first present a set of requirements and an iterative methodology for creating enforceable formal specifications of legal provisions.” [p. 1]
5. “Our work can serve as a common ground for both computer scientists and legal experts to collaborate in achieving PbD.” [p. 2]

---

## Related Work (Section 2)

The authors present a survey of existing initiatives and research on formalizing legal provisions, highlighting that efforts in the runtime verification community have rarely extended to fully enforceable specifications of large and complex regulations like the GDPR. They specifically discuss tax code formalizations, partial privacy rule encodings, and prior attempts to represent GDPR obligations in logical frameworks.

**Key Points**

- There is a rich history of formalizing legal provisions, but comprehensive, enforceable models of the GDPR remain scarce.
- Efforts such as DAPRECO or DeYoung et al. tackled formalizations of entire regulations or substantial parts thereof, yet lacked a clear link to runtime enforcement.
- Many prior works focus on detecting ex-post violations rather than ensuring continuous compliance at runtime.

**Quotations**

1. “Formal specifications of legal provisions amenable to formal reasoning are still relatively rare.” [p. 2]
2. “Only a handful of previous works have attempted to formalize entire privacy regulations in a more literal way.” [p. 3]
3. “DeYoung et al. use an extension of Least Fixed Point logic (LFP) to encode these requirements into a well-documented set of LFP formulae.” [p. 3]
4. “None of these two series of work consider enforcement.” [p. 3]
5. “The latter study required very careful policy engineering, as temporal logic policies had to be extracted from an informal description of protocol properties provided by engineers.” [p. 3]

---

## Runtime Enforcement (Section 3)

Here, the authors explain the mechanics of RE, describing how a dedicated enforcer observes system events in real time, and then either allows or blocks those events in order to keep the system’s actions compliant with the specified rules. They also provide details on the formalism—Metric First-Order Temporal Logic (MFOTL)—they use to express enforceable policies.

**Key Points**

- A system under scrutiny (SuS) reports events; the enforcer has the power to cause or suppress actions.
- Policies expressed in MFOTL specify which sequences of events are legal and thus must be enforced.
- Enforceability depends on whether the required events can be instrumented: i.e., can they be observed and possibly blocked or triggered by the enforcer?

**Quotations**

1. “In RE, a formal specification is input to a software system, called an enforcer, that observes the actions performed by a System under Scrutiny (SuS).” [p. 3]
2. “A specification for which such an enforcer exists is called enforceable.” [p. 3]
3. “During its execution, S reports events to E. An event is e(a1, ... , ak) where e is called the ‘event name’ and a1, ... , ak are ‘arguments.’” [p. 4]
4. “As an example, the policy P1 can be expressed as MFOTL formula ϕ1 [...], meaning ‘any use of a data item in a system has been preceded by user consent.’” [p. 4]
5. “Given an ontology and assumptions on the causability and suppressability of events, we say that a policy is enforceable if there exists an enforcer ensuring that SuS is policy-compliant at all times.” [p. 5]

---

## Requirements and Methodology (Section 4)

The authors propose four requirements to ensure that the formalization of legal provisions is (1) enforceable, (2) realistically implementable via instrumentation, (3) faithful to the law, and (4) understandable to both legal and technical experts. They then present an iterative workflow for producing such enforceable specifications.

**Key Points**

- **R1**: The policy must be enforceable (or transparently enforceable).
- **R2**: The system must be instrumentable based on the stated capabilities for each relevant event.
- **R3**: The specification must capture an acceptable (faithful) interpretation of the law.
- **R4**: The specification must be understandable by both legal and technical experts.
- The methodology includes drafting an ontology, drafting a policy, setting capabilities, and verifying enforceability via tools like WhyEnf.

**Quotations**

1. “What properties should a specification of legal provisions amenable to RE have? The first requirement is straightforward; it comes in two variants [...].” [p. 5]
2. “We thus get R2) The system must be instrumentable based on the stated capabilities.” [p. 6]
3. “Another key requirement for a specification of legal provisions is that it should capture an acceptable interpretation of the law.” [p. 6]
4. “As formal specifications of legal provisions should serve as bridges between the legal and technical communities, it is reasonable to require that these specifications be understandable.” [p. 6]
5. “Our methodology resembles pair programming in which a technical expert (TE) collaborates with a legal expert (LE) to develop an enforceable specification of a given set of legal provisions.” [p. 7]
6. “If this is the case, then the TE and LE have successfully derived a specification that fulfills all of the stated requirements. Otherwise, the following can be attempted to recover enforceability.” [p. 8]
7. “We suggest to try these in the order of the least required changes to the specification.” [p. 8]

---

## Case Study (Section 5)

The authors demonstrate their methodology with a portion of the GDPR (notably Articles 5, 6, 7, 11, 12, 13, and 17 in the DAPRECO knowledge base) and discuss how they identified and corrected several inaccuracies in a previously published formalization.

**Key Points**

- They illustrate the conversion of DAPRECO’s formalization into MFOTL, discovering errors related to the handling of time and unclear semantics of certain events.
- The example of Article 7(1) highlights the adjustments needed to ensure a correct and enforceable representation (e.g., ensuring “consent” is an event that precedes processing).
- The authors note that their approach—grounded in runtime enforcement—makes temporal requirements explicit, revealing hidden mistakes in prior formalisms.

**Quotations**

1. “We first developed a series of algorithms to convert the Reified I/O Logic specification by Robaldo et al. into an equivalent MFOTL specification.” [p. 9]
2. “After an automated conversion to MFOTL, the DAPRECO version of this provision reads ϕᴰ7(1) = ALWAYS (EXISTS ep, eau, ...).” [p. 9]
3. “We claim that the temporal structure of the formula is not correct, as the specification states that an obligation to demonstrate consent only exists when the data processing and consent are simultaneous.” [p. 10]
4. “In order to obtain an enforceable, state-of-the-art specification that can serve as a reference for both computer scientists and legal experts, our preliminary case study needs to be extended [...].” [p. 12]
5. “The fact that even the specification that Robaldo et al. validated with legal experts proved to be incorrect after a more precise analysis shows the benefits of our methodology.” [p. 11]
6. “Hence, another take-away is that MFOTL is a promising specification language to formalize legal provisions, allowing for expressive first-order modeling with a transparent encoding of time.” [p. 11]
7. “Making this formula understandable to non-technical experts does, however, require some accurate higher-level representation.” [p. 11]

---

## Conclusion and Open Questions (Section 6)

The paper concludes by reiterating that formalizing laws in a runtime-enforceable way can help achieve Privacy by Design. The authors acknowledge that extensive, collaborative efforts involving legal and technical experts will be needed to cover the entire GDPR. They also raise open problems such as how to refine broad ‘literal’ specifications of the law into system-specific constraints.

**Key Points**

- Future work includes a more user-friendly interface or surface language that captures MFOTL logic.
- Further coverage of all GDPR articles and deeper legal-technical collaboration is planned.
- There is a call for development of “joint assessment” methods that address both legal correctness and technical feasibility.

**Quotations**

1. “In this paper, we have presented four requirements and a new methodology for developing enforceable formal specifications of privacy laws.” [p. 12]
2. “We have then reported on a preliminary case study focusing on selected provisions of the General Data Protection Regulation (GDPR).” [p. 12]
3. “Our case study demonstrates the benefits of our methodology and suggests Metric First-Order Temporal Logic (MFOTL) as a promising language for formalizing laws.” [p. 12]
4. “In order to obtain an enforceable, state-of-the-art specification that can serve as a reference [...], our preliminary case study needs to be extended [...] by involving several technical and legal experts.” [p. 12]
5. “As a result, only a joint assessment of compliance is ever possible.” [p. 13]
6. “This raises fundamental theoretical and practical questions than can be interesting to both the technical and legal communities.” [p. 13]

---

# Evaluation Based on Inclusion Criteria

Below, we evaluate whether the paper meets each of the stated inclusion/exclusion criteria. In every conclusion, we provide the supporting quotes (with page numbers) that form the basis of our assessment.

1. **The approach should strictly propose a data provenance model to represent activities information related to GDPR obligations.**
    
    - The paper proposes a _runtime enforcement specification_ of the GDPR, focusing on the formalization of legal rules in Metric First-Order Temporal Logic and building an enforcer that can prevent or cause specific actions at runtime to ensure compliance. The text does not describe or present a _data provenance_ model (i.e., a model that explicitly captures lineage or transformations of data, typical of “provenance” solutions). Instead, it describes a formalization of GDPR constraints for continuous system monitoring.
    - **Reference**: “In RE, a formal specification is input to a software system, [...] the enforcer seeks to ensure that the behavior of the SuS adheres to its specification at all times.” [p. 3]; no mention of “provenance” or tracking lineage.
2. **The proposed model should be useful to address the compliance questions we have addressing.**
    
    - Although it provides a general method to enforce compliance, the paper does not explicitly address, nor does it define, a compliance “model” that can be directly mapped to the user’s specific compliance questions (such as retention, access rights, data subject rights, etc.). The method is general, but it lacks direct reference to answering questions about data subject rights or data retention.
    - **Reference**: “We present a set of requirements and an iterative methodology for creating enforceable formal specifications of legal provisions. [...] Our work can serve as a common ground for both computer scientists and legal experts to collaborate in achieving PbD.” [p. 1–2]
3. **The proposed model should be publicly available so that we can compare it against other approaches.**
    
    - The paper describes code and approach references, but primarily it indicates ongoing work or partial releases (e.g., the WhyEnf tool). It does not clarify in the text whether the entire formal specification is published in a stable repository for broad re-use. Some references to the DAPRECO knowledge base exist, but that is prior work.
    - **Reference**: “We first developed a series of algorithms to convert the Reified I/O Logic specification [...] into an equivalent MFOTL specification.” [p. 9]. The text does not provide a stable link for the final model.
4. **The document should be written in English or Portuguese.**
    
    - The document is written in English.
    - **Reference**: The entire PDF is in English [p. 1–14].
5. **The document should be publicly available or at least accessible under those digital libraries CAPES CAFE has signed.**
    
    - The paper is available on arXiv, thus publicly accessible.
    - **Reference**: “[http://arxiv.org/abs/2402.17350v1”](http://arxiv.org/abs/2402.17350v1%E2%80%9D) [p. 1 header].
6. **It should be a peer-reviewed document (e.g., we have discarded arXiv as a source).**
    
    - As of the version provided (arXiv:2402.17350v1), it appears to be a preprint on arXiv, which is typically _not_ peer-reviewed.
    - **Reference**: “arXiv:2402.17350v1 [cs.CR] 27 Feb 2024” [cover page].

**Conclusion of Evaluation**  
This paper _does not_ meet the inclusion criteria because it is an unreviewed arXiv preprint (criterion #6). It also does not offer a data provenance model in the sense required (criterion #1). Consequently, it should be categorized as **unrelated** for the purposes of the stated requirements.

---

# Discussion on Compliance Questions

We now discuss whether, and how, this paper addresses each compliance question. Because the authors focus on a general specification and runtime enforcement methodology rather than domain-specific details, they do not tackle these specific compliance questions in a direct or detailed manner. Where relevant, we point to statements that indicate the paper’s position or omission of a topic.

1. **CQ08**: Retention periods for each category of personal data.
    
    - **Discussion**: The paper does not mention data retention or how long data must be stored.
    - **References**: No direct mention of retention periods or data storage duration anywhere in the text [pp. 1–14].
2. **CQ09**: Identify actions required to ensure operations are GDPR compliant (e.g., deleting data no longer needed).
    
    - **Discussion**: While the enforcement approach _could_ theoretically include a rule about deleting data, the paper does not discuss deletion or disposal processes explicitly.
    - **References**: “An enforcer [...] can send commands to the SuS, typically instructing the SuS to prevent or cause certain actions.” [p. 3] – but no mention of data deletion.
3. **CQ11**: Re-sought consent if the existing consent does not meet GDPR standard.
    
    - **Discussion**: Although the paper addresses consent in its example (Article 7(1) case study), it focuses on demonstrating previously obtained consent rather than re-seeking it.
    - **References**: “Article 7(1) GDPR states: Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented [...].” [p. 9]. No mention of re-seeking consent.
4. **CQ17**: Ability to respond to SARs (Subject Access Requests) within one month.
    
    - **Discussion**: There is no specific mention of time-bound SAR processing or the system’s ability to expedite such requests.
    - **References**: Not discussed [pp. 1–14].
5. **CQ20**: Halting processing where an individual has validly restricted processing.
    
    - **Discussion**: Halting or blocking data usage is conceptually in scope for the enforcer, but the paper does not mention restrictions triggered by individuals exercising rights.
    - **References**: The general enforcement approach is described [p. 3–5], but restricting processing at user request is not addressed.
6. **CQ21**: Informing individuals about their right to object to certain types of processing.
    
    - **Discussion**: The paper deals with formalizing and enforcing GDPR provisions, but user-facing information duties (e.g., “right to object” notices) are not discussed.
    - **References**: No mention [pp. 1–14].
7. **CQ25**: Documentation of circumstances in which data protection rights may be lawfully restricted.
    
    - **Discussion**: This specific question is not covered.
    - **References**: Not addressed in the text.
8. **CQ28**: Procedures to ensure data are kept up to date and accurate.
    
    - **Discussion**: The paper’s focus is on the feasibility of runtime logic enforcement. It does not discuss data updates or data quality.
    - **References**: Not addressed [pp. 1–14].
9. **CQ29**: Retention policies to ensure data are held no longer than necessary.
    
    - **Discussion**: Again, the text does not address data retention policies or maximum retention times.
    - **References**: No references to data retention [pp. 1–14].
10. **CQ30**: Whether the business is subject to other rules that require minimum retention periods.
    
    - **Discussion**: No mention of other rules or specific cross-regulatory constraints.
    - **References**: Not addressed [pp. 1–14].
11. **CQ32**: Ensuring no unnecessary or unregulated duplication of records.
    
    - **Discussion**: No mention of duplication or controlling multiple copies of data.
    - **References**: Not addressed [pp. 1–14].
12. **CQ33**: Whether service users/employees are fully informed in plain language of how their data is used.
    
    - **Discussion**: This question is about transparency obligations. The paper focuses on runtime enforcement of a formal specification, not user-facing notices.
    - **References**: Not addressed [pp. 1–14].
13. **CQ35**: Procedures to ensure data are kept accurate and corrected without delay.
    
    - **Discussion**: This question is not explicitly referenced.
    - **References**: Not addressed [pp. 1–14].
14. **CQ37**: Procedures to inform individuals of their GDPR rights when interacting.
    
    - **Discussion**: The paper discusses a system-enforced methodology; it does not detail how data subjects are informed of their rights.
    - **References**: Not addressed [pp. 1–14].
15. **CQ38**: Information on exercising GDPR rights published in an easily accessible format.
    
    - **Discussion**: No mention of publishing instructions or data subject rights in accessible form.
    - **References**: Not addressed [pp. 1–14].
16. **CQ39**: Whether agreements with suppliers/third parties ensure appropriate data protection.
    
    - **Discussion**: The paper focuses on a single system’s internal logic enforcement, not supply chain data protection agreements.
    - **References**: No relevant content [pp. 1–14].
17. **CQ40**: Need to appoint a Data Protection Officer (DPO).
    
    - **Discussion**: The text does not discuss organizational roles like DPO.
    - **References**: Not addressed [pp. 1–14].
18. **CQ41**: Documenting reasons if a DPO is not required.
    
    - **Discussion**: Not covered by the paper.
    - **References**: Not addressed [pp. 1–14].
19. **CQ42**: Escalation/reporting lines for an appointed DPO, and procedures.
    
    - **Discussion**: Not discussed.
    - **References**: Not addressed [pp. 1–14].
20. **CQ43**: Publishing DPO contact details.
    
    - **Discussion**: Not mentioned.
    - **References**: Not addressed [pp. 1–14].
21. **CQ44**: Notifying data protection authority of DPO contact details.
    
    - **Discussion**: Not mentioned.
    - **References**: Not addressed [pp. 1–14].
22. **CQ47**: Documented security programme specifying technical, administrative, physical safeguards.
    
    - **Discussion**: The authors propose a formal logic for specifying constraints on system actions, but not a security program.
    - **References**: Not discussed [pp. 1–14].
23. **CQ48**: Process for resolving security-related complaints and issues.
    
    - **Discussion**: No mention of complaint-handling.
    - **References**: Not addressed [pp. 1–14].
24. **CQ49**: Designated individual for preventing and investigating security breaches.
    
    - **Discussion**: Not included; the focus is on real-time policy enforcement, not breach investigations.
    - **References**: Not addressed [pp. 1–14].
25. **CQ50**: Industry standard encryption for transferring/storing personal information.
    
    - **Discussion**: The paper does not discuss encryption or data transmission security.
    - **References**: Not addressed [pp. 1–14].
26. **CQ51**: Systematic destruction or anonymization of personal data no longer required.
    
    - **Discussion**: While the enforcer can “cause or suppress events,” there is no mention of an automated data destruction or anonymization function.
    - **References**: “E can send commands instructing S to prevent or cause certain actions.” [p. 3] – but no mention of data destruction.
27. **CQ52**: Data restoration in the event of an incident.
    
    - **Discussion**: Not referenced; the paper focuses on preventing non-compliant processing at runtime.
    - **References**: Not addressed [pp. 1–14].
28. **CQ56**: Regular review of plans and procedures.
    
    - **Discussion**: The paper presents a general methodology but doesn’t mention periodic reviews or updates.
    - **References**: Not addressed [pp. 1–14].
29. **CQ57**: Full documentation of data breaches.
    
    - **Discussion**: Not covered.
    - **References**: Not addressed [pp. 1–14].
30. **CQ58**: Cooperation procedures between controllers/suppliers for data breaches.
    
    - **Discussion**: Not covered.
    - **References**: Not addressed [pp. 1–14].
31. **CQ63**: Listing of all international transfers.
    
    - **Discussion**: Not covered.
    - **References**: Not addressed [pp. 1–14].
32. **CQ64**: Legal basis for data transfer (adequacy decision, standard clauses, etc.).
    
    - **Discussion**: Not covered.
    - **References**: Not addressed [pp. 1–14].
33. **CQ65**: Informing data subjects about intended international transfers.
    
    - **Discussion**: Not covered.
    - **References**: Not addressed [pp. 1–14].

**Overall Discussion on Compliance Questions**  
The paper proposes a general method to encode and enforce the GDPR at runtime, yet does not explicitly address any of the compliance questions in detail (e.g., data retention, subject access requests, data deletion, DPO appointment, or others). Hence, while the methodology might in principle be _extended_ to enforce rules relevant to those questions, it does _not_ itself address them.

---

# References

- [[bonatti2020a]]
- [[torre2021a]]