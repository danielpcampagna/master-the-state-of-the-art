---
ID: marikyan2021a
authors: Marikyan, Davit; Llanos, Jose; Barati, Masoud; Aujla, Gagangeet; Li, Yinhao; Adu-Duodu, Kwabena; Tahir, Sabeen; Rana, Omer; Papagiannidis, Savvas; Ranjan, Rajiv; Carr, Madeline
category: unrelated
display: "marikyan (Privacy & Cloud Services: Are We There Yet?)"
due: The paper does not propose a strict data provenance model to represent activities information related to GDPR obligations.
entrytype: article
link: ""
name: "Privacy & Cloud Services: Are We There Yet?"
organization: ""
place: ""
pp: 1-9
provenance_related: false
related: 
year: 2021
forward_steps: 2
---

# Summary & Analysis

## Introduction & Motivation (Section I)

**Main Ideas**

- Explains how the General Data Protection Regulation (GDPR) is intended to address privacy concerns when users share personal data.
- Motivates the work with questions about how users perceive GDPR and whether GDPR is an enabler or a barrier to the use of cloud services.
- Sets up a study (via user survey) to investigate user awareness of GDPR and outlines the architectural idea of verifying compliance through blockchain-based logs.

**Key Points**

1. The authors highlight that GDPR compliance involves ensuring user consent and transparent data sharing (p.1).
2. They observe that users are often “ambivalent” about GDPR, leading to weak adoption in practice (p.1).
3. They propose an approach that records data processing operations on blockchain for subsequent auditing (p.1).

**Representative Quotations**

1. “GDPR compliance verification for a cloud provider is aimed to confirm that personal data provided by a user is shared in-line with the requirements of this legislation” (p.1)
2. “We motivate this work by two questions: how do users perceive benefit in using privacy technologies to support GDPR legislation, particularly in the context of cloud hosted services?” (p.1)
3. “In order to secure broad access to personal data under the semblance of GDPR compliance, website owners are increasingly relying on ‘dark patterns’.” (p.1)

---

## GDPR Use for Cloud Services (Section II)

### Subsection A: Data Privacy Concerns under GDPR

**Main Ideas**

- Explains different user attitudes toward privacy and how GDPR tries to give individuals control over their data.
- Mentions widespread concerns about how personal data is shared with third parties, or used for other unintended purposes.
- Observes that the COVID-19 pandemic has exacerbated the tension between user privacy and the need to access online/cloud services.

**Key Points**

1. The paper notes that while GDPR aims to improve individual control over personal data, many websites resort to “dark patterns” that undermine free choice (p.2–3).
2. It references official surveys indicating that a large proportion of users do not feel fully informed about how their data is processed (p.3).
3. The discussion highlights that “consent” is only one of several legal bases in GDPR, causing confusion when data controllers mix consent with “legitimate interests” (p.3).

**Representative Quotations**

1. “Privacy concerns are one of the main obstacles to greater use of on-line services.” (p.2)
2. “Consent must be given by ‘a clear affirmative act establishing a freely given, specific, informed and unambiguous indication’ of an individual’s agreement.” (p.3)
3. “If incomplete lists of recipients are provided, this information will be insufficient to elicit informed consent.” (p.3)

### Subsection B: Apathy towards the GDPR: User Acceptance Survey

**Main Ideas**

- Describes a large-scale online survey of 506 participants about their GDPR awareness, familiarity, and perceived importance.
- Finds a relatively high level of awareness yet low perceived importance or trust in the regulation’s effectiveness.

**Key Points**

1. Over half of respondents (56.5%) believe that GDPR is “not important,” implying apathy or distrust (p.4).
2. Results hint that users may doubt GDPR enforcement or fear it might not be effectively upheld (p.4).
3. The authors infer that a disconnect arises between knowledge about GDPR and tangible trust in how providers comply (p.4).

**Representative Quotations**

1. “We conducted a survey to measure the importance of privacy protection as afforded by the GDPR legislation.” (p.4)
2. “52.8% of respondents are familiar with the GDPR, while 47.2% of respondents score low on this scale.” (p.4)
3. “More than 50% of respondents did not perceive GDPR to be relevant, which can be interpreted as a lack of objective knowledge of GDPR benefits.” (p.4)

---

## GDPR Compliance Checking (Section III)

### Subsection A: Prior Work

**Main Ideas**

- Summarizes relevant research efforts on making GDPR machine-readable and automatically enforceable (policy languages, compliance rules).
- Points out that legal texts often have open-ended terminology, making purely automatic compliance checks challenging.

**Key Points**

1. Implementations like LPL or YaPPL formalize consent but do not address multi-provider usage or large-scale cloud settings (p.5–6).
2. “Ambiguity” in GDPR text is seen as a significant barrier to automated verification (p.5–6).
3. The authors emphasize that they translate only strongly specified GDPR rules into code, while the rest requires human interpretation (p.6).

**Representative Quotations**

1. “Legal rules tend to be ‘open-textured’, flexible and subject to interpretation, particularly in the GDPR.” (p.5)
2. “We have been able to translate into code only those rules that are strongly specified… well-suited to be accurately represented in code.” (p.6)
3. “Legal concepts can be mapped into a form that can be automatically verified, but this remains a challenge.” (p.6)

### Subsection B: GDPR-Compliant Privacy Policy

**Main Ideas**

- Proposes that each data processing purpose should be written explicitly and placed on-chain (blockchain) so that user consent or refusal is specific and unbundled.
- Suggests a system where any operation (read, write, transfer, profile) on personal data is monitored and recorded via smart contracts.

**Key Points**

1. “Purpose limitation” is verified by enumerating each “actor, operation, and personal data item,” storing them in a block (p.7).
2. Noncompliant operations—e.g., a provider accessing data without a declared purpose—can be flagged (p.7).
3. Performance overhead is recognized, but the approach is said to improve “transparency, accountability, and trust” (p.7–8).

**Representative Quotations**

1. “A privacy policy on Dh… is a set of statements: ‘pi executes α on d for pr’…” (p.7)
2. “Based on such purposes retrieved from the blockchain, a user can give positive or negative consent (for each purpose).” (p.7)
3. “We believe this will significantly strengthen privacy in the operations of cloud providers.” (p.8)

---

## Improving User Engagement with GDPR (Section IV)

**Main Ideas**

- Argues that “lack of user interest” in GDPR can be reversed if the actual operations on personal data are made visible and user-friendly.
- Proposes layering user controls on top of transparent logging so that individuals can see exactly which data fields are accessed, by which provider, and for what reason.

**Key Points**

1. Making data usage logs more granular (read/write/transfer) helps align with GDPR’s accountability principle (p.8).
2. A blockchain-based log can be audited by third-party verifiers or the user, potentially increasing trust (p.8).
3. The authors acknowledge the cost of logging on-chain but see the advantage in building user confidence (p.8).

**Representative Quotations**

1. “User trust in a cloud provider can be improved by identifying these data processing operations and the actors involved.” (p.8)
2. “If individuals can identify the purposes of the data processing operations, they gain the ability to make informed decisions about their data privacy.” (p.8)
3. “With increasing take up of on-line services... data privacy needs have often been overlooked just to be able to access such on-line services.” (p.8)

---

## Conclusions & Future Work (Section V)

**Main Ideas**

- Reiterates the importance of GDPR for cloud services but highlights that user apathy remains a critical adoption barrier.
- Presents the authors’ blockchain-based compliance checking approach as a means to bolster trust.
- Acknowledges the necessity of further work in scaling, performance tuning, and bridging interpretative legal text with code-based compliance.

**Key Points**

1. Concludes that “ambivalence” toward GDPR is a serious limitation to its real impact (p.9).
2. Cautions that purely technical approaches must still handle the ambiguous aspects of legal text (p.9).
3. Suggests next steps to refine the auditing overhead and accommodate “mobile device” usage (p.9).

**Representative Quotations**

1. “GDPR remains an important requirement for many on-line services which utilise user data.” (p.9)
2. “Our survey results show that users are ambivalent to GDPR benefits, and often are not fully conversant with the actions carried out by a cloud provider.” (p.9)
3. “The overhead of using a blockchain implementation... remains a challenge.” (p.9)

---

# Evaluation Based on Inclusion Criteria

Below, each inclusion/exclusion criterion is considered, with precise links to statements from the paper (page references in parentheses).

1. **Proposes a data provenance model to represent activities information related to GDPR obligations**
    
    - The paper provides a “compliance-aware architecture” and a logging strategy using blockchain to capture personal-data operations (p.5–7). However, it does **not** explicitly define a _data provenance model_—it focuses on compliance verification of read/write events rather than a formal, domain-agnostic “provenance model” describing process, transformations, or lineage in detail.
        
    
    > “...we have converted a number of GDPR operation requests into smart contracts to verify their compliance...” (p.6)  
    > This describes an implementation for compliance, not a structured “provenance” specification.
    
    **Conclusion**: Does not strictly meet the “data provenance model” requirement.
    
2. **Usefulness of the proposed model for addressing our compliance questions**
    
    - The architecture addresses general GDPR obligations (“purpose limitation,” “user consent,” “accountability”) and captures data operations in logs (p.7–8). However, the paper does not walk through or systematically discuss the specific compliance questions (data retention period, response to SARs, etc.).
        
    
    > “We believe this approach... ensures that GDPR legislation is automatically enforced across such a platform.” (p.5)
    
    **Conclusion**: While it helps with some GDPR obligations, it does not directly address or structure answers to the specific compliance questions enumerated.
    
3. **Public availability of the proposed model**
    
    - The paper does not reference a publicly available repository or formal data model that researchers can download or compare.
        
    
    > “Another recent extension to YaPPL... The scalability of the toolkit was not evaluated in cloud-based systems...” (p.6)
    
    **Conclusion**: The text does not show that their solution is fully published as a standalone, accessible provenance model.
    
4. **Document language**
    
    - The paper is in English.
        
    
    > The entire text is written in English (all pages).
    
    **Conclusion**: Criterion satisfied.
    
5. **Document is publicly available**
    
    - The PDF is presumably a publicly shared research manuscript. The text indicates it is affiliated with EPSRC-funded universities, commonly leading to open-access or widely circulated publications.
        
    
    > “This work has been funded by EPSRC project PACE...” (p.9)
    
    **Conclusion**: Likely publicly available, or accessible at least through typical academic channels.
    
6. **Peer-reviewed document**
    
    - The text presents itself as a formal academic study. Though the exact conference/journal name is not stated, it reads like a conference or workshop paper with references, methodology, and a standard academic structure.
    
    **Conclusion**: Most likely peer-reviewed.
    

**Overall Verdict**

- Fails criterion #1 (“strictly propose a data provenance model”).
- The paper is thus **excluded** for not meeting the main inclusion requirement.

---

# Discussion on Compliance Questions

Below is a point-by-point check on how (or whether) the paper addresses each compliance question. Where it does not address the question, we make that explicit. Page references are provided where partial alignment might exist.

**CQ08**: “For each category of personal data, list the period for which the data will be retained...”

- **Not explicitly addressed**. The paper does not discuss retention durations or policies (p.1–9).
- Quote: None specifically referencing retention period.

**CQ09**: “Identify actions required to ensure all personal data processing operations are GDPR compliant...”

- **Partially addressed** in that the authors propose logging all data processing operations and verifying them via blockchain (p.5–7).
- Quote: “How do we verify compliance in an automatic manner and ensure the ‘right to be informed’ obligation?” (p.5)

**CQ11**: “If personal data held on the basis of consent does not meet the GDPR standard, have you re-sought individual consent?”

- **Not addressed**. There is no mention of re-seeking consent or processes for that scenario.

**CQ17**: “Is your organisation able to respond to SARs within one month?”

- **Not addressed**. No mention of subject access request timelines.

**CQ20**: “Controls/procedures to halt processing where an individual has validly sought restriction?”

- **Not addressed**. The paper focuses on capturing operations, not on halting them (p.5–9).

**CQ21**: “Are individuals told about their right to object to certain types of processing?”

- **Not addressed**. The paper discusses user consent but not the user’s explicit right to object (p.3–4).

**CQ25**: “Have the circumstances been documented in which an individual’s data protection rights may be lawfully restricted?”

- **Not addressed**. No mention of restricting user rights.

**CQ28**: “Procedures to ensure personal data are up to date and accurate...”

- **Not addressed** in the text (p.1–9).

**CQ29**: “Are retention policies in place to ensure data are held no longer than necessary?”

- **Not addressed**. The paper does not describe any retention policy mechanism.

**CQ30**: “Business subject to rules requiring a minimum retention period (medical/tax records)?”

- **Not addressed**.

**CQ32**: “Procedures to ensure no unnecessary or unregulated duplication of records?”

- **Not addressed**. The approach is about logging usage, not record duplication.

**CQ33**: “Are service users/employees fully informed how you use their data in a concise, transparent, intelligible manner?”

- **Partially addressed** with an emphasis on “transparency” via the blockchain log of data usage (p.7–8).
- Quote: “If individuals can identify the purposes of the data processing operations, they gain the ability to make informed decisions.” (p.8)

**CQ35**: “Procedures for keeping personal data up to date and accurate…?”

- **Not addressed**. The paper does not discuss data updating or accuracy.

**CQ37**: “Are procedures in place to proactively inform individuals of their GDPR rights?”

- **Not addressed**. The paper focuses on verifying compliance operations, not user-rights notifications.

**CQ38**: “Is information on how the organisation facilitates individuals exercising their GDPR rights published accessibly?”

- **Not addressed**. The paper does not detail how or where such information is published.

**CQ39**: “Have agreements with suppliers/third parties been reviewed to ensure data protection requirements are included?”

- **Not addressed**. The text mentions multi-cloud or external providers but does not delve into contractual coverage (p.2–3).

**CQ40**: “Do you need to appoint a DPO as per Article 37 of GDPR?”

- **Not addressed**.

**CQ41**: “If no DPO is required, have you documented the reasons?”

- **Not addressed**.

**CQ42**: “Where a DPO is appointed, are escalation/reporting lines documented?”

- **Not addressed**.

**CQ43**: “Have you published the DPO contact details?”

- **Not addressed**.

**CQ44**: “Have you notified your data protection authority… of your DPO contact details?”

- **Not addressed**.

**CQ47**: “Is there a documented security programme specifying safeguards for personal data?”

- **Partially addressed** insofar as the authors discuss blockchain’s secure logging, but no mention of a broader security program (p.5–8).
- Quote: “We propose a compliance-aware multi-layered service stack… ensures the security of personal data through logging.” (p.5)

**CQ48**: “Is there a documented process for resolving security-related complaints/issues?”

- **Not addressed**.

**CQ49**: “Is there a designated individual responsible for preventing/investigating security breaches?”

- **Not addressed**.

**CQ50**: “Industry-standard encryption for transferring/storing individuals’ sensitive personal info?”

- **Partially mentioned**: “Similarly, the data protection smart contract verifies whether or not personal data records are encrypted.” (p.6) – but details are minimal.

**CQ51**: “Are personal data systematically destroyed, erased, or anonymised when no longer required?”

- **Not addressed**.

**CQ52**: “Can access to personal data be restored in a timely manner in a physical or technical incident?”

- **Not addressed**.

**CQ56**: “Are plans and procedures regularly reviewed?”

- **Not addressed**.

**CQ57**: “Are all data breaches fully documented?”

- **Not addressed** specifically, though blockchain logs might help discover unauthorized access.

**CQ58**: “Are there cooperation procedures in place between data controllers and suppliers for data breaches?”

- **Not addressed**.

**CQ63**: “Are all transfers listed… who receives the data and for what purpose?”

- **Partially addressed**: They propose that data access/transfer can be logged with a stated purpose on blockchain (p.7).
- Quote: “A privacy policy on Dh… states which operations will be executed by which providers… on what personal data and for what purposes.” (p.7)

**CQ64**: “Is there a legal basis for the transfer? Are these bases documented?”

- **Partially addressed**: The system captures a user’s consent for each operation, but no deeper mention of alternative legal bases or their documentation (p.7).

**CQ65**: “Are data subjects fully informed about any intended international transfers of their personal data?”

- **Not addressed**. The paper does not detail how cross-border transfers are exposed or flagged.

---

# Analysis Result

All evidence shows that the paper, although related to GDPR compliance, **does not** fulfill the core requirement of proposing a “strict data provenance model” for GDPR obligations. Therefore, the final verdict is “unrelated” given the specified inclusion criteria.

---

# References

- [[bonatti2020a]]