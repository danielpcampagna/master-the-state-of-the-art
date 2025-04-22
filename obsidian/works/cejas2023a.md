---
ID: cejas2023a
authors: Cejas, Orlando Amaral
category: unrelated
display: cejas (Artificial Intelligence-enabled Automation for Compliance Checking against GDPR)
due: This dissertation does not propose a data provenance model for representing GDPR-related activities. Instead, it focuses on automating textual compliance checking for Privacy Policies (PPs) and Data Processing Agreements (DPAs).
entrytype: thesis
link: PhD-FSTM-2023-084 (University of Luxembourg)
name: Artificial Intelligence-enabled Automation for Compliance Checking against GDPR
organization: University of Luxembourg
place: Doctoral Dissertation
pp: 1–139
provenance_related: false
related:
  - Compliance Checking
  - GDPR
  - AI
  - NLP
  - Data Processing Agreements
  - Privacy Policies
year: "2023"
forward_steps: 2
---

# Summary & Analysis

Below is a high-level summary of each major chapter (or “section”) of _Artificial Intelligence-enabled Automation for Compliance Checking against GDPR_ by Orlando Amaral Cejas. Each subsection includes the main ideas, key points, arguments, and illustrative quotations (with approximate page references) that best characterize that portion of the dissertation.

## Chapter 1: Introduction

**Main Ideas & Key Points**

- Provides the context of how modern data-driven software systems must comply with the General Data Protection Regulation (GDPR).
- Emphasizes the significant fines and legal risks of non-compliance.
- Positions the dissertation as an investigation into artificial intelligence (AI)-driven techniques (NLP, machine learning) for automated support in checking textual documents that GDPR regulates: specifically Privacy Policies (PPs) and Data Processing Agreements (DPAs).
- Explains the main challenges: the complexity of legal text, the need for machine-analyzable representations of GDPR provisions, and the labor-intensive nature of manual checking.

**Representative Quotations**

1. “Breaching GDPR can be charged with large fines reaching up to billions of euros.” (p. 1)
2. “PPs and DPAs are documents regulated by GDPR to ensure, among other things, secure collection and processing of personal data.” (p. 2)
3. “Checking the compliance of regulated documents entirely manually is a laborious and error-prone task.” (p. 3)

## Chapter 2: Background

**Main Ideas & Key Points**

- Reviews GDPR’s structure, focusing on articles that define obligations for controllers and processors.
- Introduces core concepts of natural language processing (NLP) and machine learning (ML), including the typical NLP pipeline, feature engineering, and handling data imbalance.
- Argues that automating legal compliance tasks must be grounded on a solid understanding of both legal and technical domains.

**Representative Quotations**

1. “GDPR is a complex document composed of 173 recitals, 99 articles, and 11 chapters, making its interpretation challenging, especially for non-experts.” (p. 7)
2. “A comprehensive NLP pipeline typically includes text preprocessing, tokenization, and parts-of-speech tagging, among other tasks.” (p. 8)
3. “Imbalanced data is a common scenario in compliance tasks, requiring special techniques to improve classifier performance.” (p. 10)

## Chapter 3: AI-enabled Automation for Compliance Checking of Privacy Policies

**Main Ideas & Key Points**

- Proposes and details a conceptual model for privacy-policy information types (e.g., personal data origin, legal basis, data subject rights).
- Translates relevant GDPR articles into specific compliance criteria for PPs (e.g., the policy must state how data subjects can withdraw consent, how long personal data is stored, etc.).
- Introduces a two-phase approach (information-type identification and automated compliance checking), leveraging NLP and machine learning.
- Validates this approach on publicly available privacy policies, showing how well the automated tool can detect missing or incomplete GDPR requirements.

**Representative Quotations**

1. “We devise an automated solution that leverages natural language processing (NLP) and machine learning (ML) for checking the compliance of PPs against the applicable provisions in GDPR.” (p. 11)
2. “We create a comprehensive conceptual model capturing all information types pertinent to PPs, and further define a set of compliance criteria for automated checks.” (p. 17)
3. “The approach identifies whether the PP includes essential rights (such as the right to rectification, erasure, or objection) and whether legal bases are clearly stated.” (p. 26)

## Chapter 4: NLP-based Automation for Compliance Checking of Data Processing Agreements

**Main Ideas & Key Points**

- Examines Data Processing Agreements (DPAs) as legally binding documents that outline obligations between controllers and processors under GDPR.
- Presents “DERECHA,” an NLP-driven method to parse DPAs at a phrasal level, mapping text segments to semantic frames (e.g., _assist_, _inform_, _ensure security_) that correspond to GDPR’s mandatory or optional requirements for DPAs.
- Demonstrates how the tool generates a detailed compliance report, including which clauses are missing or which obligations are partially covered.

**Representative Quotations**

1. “Using NLP semantic analysis technologies, we develop an automated solution that checks at phrasal-level the compliance of DPAs against GDPR.” (p. 51)
2. “Our solution is able to provide not only a compliance assessment, but also detailed recommendations about avoiding GDPR violations.” (p. 52)
3. “We represent GDPR requirements using semantic frames that capture actor, beneficiary, object, and other roles essential for compliance.” (p. 62)

## Chapter 5: ML-enabled Automation for Compliance Checking of Data Processing Agreements

**Main Ideas & Key Points**

- Introduces a second method for DPA analysis, “DικAIo,” that relies more extensively on machine learning rather than purely rule-based NLP.
- Compares two representation strategies: (i) raw textual representation with rules, vs. (ii) conceptual modeling combined with ML classifiers trained to recognize compliance elements.
- Shows empirical results on real-world DPAs, highlighting pros and cons of each approach in terms of accuracy, maintainability, and scalability.

**Representative Quotations**

1. “We develop an automated solution that utilizes a combination of conceptual modeling and ML ... to classify each DPA excerpt according to GDPR obligations.” (p. 87)
2. “We further empirically compare our previously proposed solution, which uses rules alongside NLP semantic analysis, with a purely ML-based approach.” (p. 88)
3. “The results suggest that a hybrid method can outperform purely rule-based or purely ML-based approaches in accuracy.” (p. 95)

## Chapter 6: Conclusion

**Main Ideas & Key Points**

- Summarizes the dissertation’s contributions to automating compliance checking of PPs and DPAs.
- Highlights future work, such as extending the approach to other regulations (e.g., e-Privacy Directive, HIPAA) or other textual artifacts.
- Concludes that combining legal expertise, conceptual modeling, and AI methods (NLP/ML) can reduce compliance-checking costs and improve consistency.

**Representative Quotations**

1. “Our automated solutions aim to assist requirements engineers and legal experts in rapidly identifying compliance issues within regulated documents.” (p. 105)
2. “Future work could explore more dynamic techniques that adapt to evolving regulations, including adding or revising compliance rules.” (p. 106)
3. “Ultimately, bridging legal and technical knowledge through AI helps organizations implement GDPR obligations more reliably.” (p. 106)

---

# Evaluation Based on Inclusion Criteria

Below, we assess whether the dissertation aligns with each of the stated inclusion/exclusion criteria. We refer to specific arguments or quotations (with page numbers) from the dissertation to substantiate our conclusions:

1. **The approach should strictly propose a data provenance model to represent activities information related to GDPR obligations.**
    
    - The dissertation provides conceptual models capturing textual elements needed for PPs and DPAs; however, it does **not** present a _data provenance_ model describing processes, their inputs/outputs, or the typical “lineage” structure. The focus is on text classification for compliance, not on an explicit representation of data-processing provenance.
    - “We create a comprehensive conceptual model capturing all information types pertinent to PPs ...” (p. 17) but no mention of tracking or modeling _activity lineage_ in the sense of a provenance framework.
2. **The proposed model should be useful to address the compliance questions we have.**
    
    - While the dissertation’s conceptual models do capture GDPR obligations for PPs and DPAs, they are not primarily oriented to the _provenance-based_ compliance questions. Instead, the primary use is text-based completeness and compliance checking.
    - “Our solution is able to provide not only a compliance assessment, but also detailed recommendations...” (p. 52) – relevant to textual obligations, but not structured as a data provenance representation.
3. **The proposed model should be publicly available so that we can compare it against the other approaches.**
    
    - The textual representation rules, code, and conceptual models may be partially available (“Implementation and Availability” sections in Chapters 3–5), but they are not introduced as a _provenance model_.
    - “Implementation and Availability ... we make our approach and dataset available in a public repository.” (p. 34) – This is beneficial, yet does not satisfy the provenance-model requirement.
4. **The document should be written in English or Portuguese.**
    
    - The dissertation is written in **English**.
5. **It should be publicly available or at least accessible under digital libraries CAPES CAFE has signed.**
    
    - This is a doctoral dissertation, presumably publicly available through the University of Luxembourg or standard dissertation repositories.
6. **It should be a peer-reviewed document (e.g., we have discarded arXiv as a source).**
    
    - This is a formally defended PhD dissertation, which typically goes through an academic committee review. It is not the same as a peer-reviewed journal/conference publication, but it is an officially examined document.

**Conclusion of Evaluation:**  
Even though the dissertation is in English, publicly accessible, and deals with GDPR compliance, it does **not** present a _data provenance model_ focusing on “activities information” in the sense of the stated criteria. Its emphasis is on AI-powered textual analysis. Therefore, it falls outside the narrow scope of “strictly proposes a data provenance model” for GDPR obligations, so we classify it as **unrelated** with respect to these particular inclusion criteria.

---

# Discussion on Compliance Questions

Below is a discussion of how (or whether) the dissertation’s content addresses each of the listed compliance questions (CQ08 to CQ65). We rely on the dissertation’s focus on textual compliance checks for Privacy Policies and Data Processing Agreements. Where applicable, we quote and cite page references that show partial alignment; otherwise, we note the lack of direct coverage.

**CQ08**: “For each category of personal data, list the period for which the data will be retained...”

- The dissertation’s PP conceptual model includes “PD TIME STORED” as an information type (p. 19), suggesting that the automated approach checks whether the privacy policy mentions _time periods_ for storing personal data.
- However, it does not specifically discuss whether or how to operationalize different retention lengths. It only checks the textual presence or absence of statements about retention periods.

**CQ09**: “Identify actions that are required to ensure all personal data processing operations are GDPR compliant...”

- Chapters 3–5 deal with identifying textual references to GDPR obligations (e.g., Chapter 4, p. 52–53). While the system flags missing clauses in a DPA or PP, it does not list _all operational actions_ in detail.
- “Detailed recommendations” (p. 52) do indicate some text-based guidance, but not a full operational plan.

**CQ11**: “If personal data that you hold on the basis of consent does not meet the required standard under GDPR, have you re-sought the individual’s consent?”

- The dissertation does check for the presence of “LEGAL BASIS” (including “CONSENT”) in PPs (p. 26, 28). Yet it does not delve into whether re-seeking consent is performed.
- There is no direct mechanism described for verifying ongoing re-consenting processes.

**CQ17**: “Is your organisation able to respond to SARs (Subject Access Requests) within one month?”

- The approach checks for “DATA SUBJECT RIGHT ACCESS” in privacy policies (p. 21–22). While it ensures that a PP states the existence of a right of access, it does not confirm any timeline.
- So the question of one-month responsiveness is not explicitly addressed.

**CQ20**: “Are there controls and procedures to halt processing where an individual sought restriction of processing?”

- The dissertation’s model for PPs includes “DATA SUBJECT RIGHT RESTRICTION” (p. 19). It only checks whether the policy text references that right.
- Actual procedural or technical controls are not covered; the text analysis cannot confirm real implementation.

**CQ21**: “Are individuals told about their right to object to certain types of processing?”

- The dissertation includes “DATA SUBJECT RIGHT OBJECT” as part of the conceptual model for PPs (p. 19, 22). If absent, the approach would flag a violation.
- Actual clarity or understandability for individuals is not deeply measured beyond textual presence.

**CQ25**: “Have the circumstances been documented in which an individual’s data protection rights may be lawfully restricted?”

- The text classification can highlight if the PP or DPA mentions exceptions or conditions, but the dissertation does not explicitly show evaluation of “lawful restrictions.”
- No direct mention beyond whether the right to restriction is included (p. 22).

**CQ28**: “Are procedures in place to ensure personal data are kept accurate and updated?”

- The automated approach checks whether the documents mention the right to rectification (p. 26). That implies an obligation to keep data accurate.
- The dissertation does not detail how “procedures” are validated; it only detects textual statements.

**CQ29**: “Are retention policies and procedures in place to ensure data are held no longer than necessary?”

- Similar to CQ08, the presence of “PD TIME STORED” is checked (p. 19). The approach flags if no duration is specified.
- The dissertation does not confirm if the stated durations align with legal necessity thresholds.

**CQ30**: “Is your business subject to other rules that require a minimum retention period (e.g. medical records/tax records)?”

- The dissertation does not cover domain-specific regulations or cross-references. It strictly focuses on GDPR textual compliance, so it does not check for other rules (p. 49 mentions “extending methodology beyond GDPR,” but not implemented).

**CQ32**: “Are procedures in place to ensure no unnecessary duplication of records?”

- This is not mentioned in the conceptual models or compliance criteria in Chapters 3–5. No direct coverage.

**CQ33**: “Are service users/employees fully informed of how you use their data in a concise, transparent, intelligible way?”

- The approach only checks the presence of the relevant obligations in PPs or DPAs (Ch. 3, 4). Whether it is “concise” or “plain language” is not measured.
- So there is partial coverage: textual references to data usage might be found, but no measure of actual readability.

**CQ35**: “Are procedures in place to ensure personal data are accurate and updated, and changes made without delay?”

- Similar to CQ28. The dissertation checks textual references to data rectification but does not address timeliness beyond what the text states.

**CQ37**: “Are procedures in place to proactively inform individuals of their GDPR rights (e.g., when providing a service)?”

- The approach verifies if the PP mentions data subject rights (p. 19, 26). However, “proactive informing” or procedures beyond text mention is not addressed.

**CQ38**: “Is information on how the organisation facilitates individuals exercising GDPR rights published in an accessible format?”

- The tool checks for presence or absence of certain rights in the text. It does not address formatting or accessibility standards.
- “We define a set of compliance criteria ... to verify if essential rights are mentioned.” (p. 26)

**CQ39**: “Have agreements with suppliers or third parties been reviewed to ensure appropriate data protection requirements are included?”

- The DPA analysis (Ch. 4, 5) checks if the document includes clauses about “sub-processor obligations,” referencing Article 28 (p. 57–61).
- But there is no mention of broader third-party or supply chain reviews beyond the textual DPA sub-processor checks.

**CQ40**: “Do you need to appoint a Data Protection Officer (DPO) as per Article 37 of the GDPR?”

- The dissertation’s conceptual model for PPs includes “DPO,” e.g., checking if the policy states a DPO or DPO contact (p. 22).
- Whether an organization _needs_ one is not analyzed beyond textual references.

**CQ41**: “If it is decided that a DPO is not required, have you documented the reasons why?”

- The solutions do not examine any rationale for not appointing a DPO. This is not covered.

**CQ42**: “Where a DPO is appointed, are escalation and reporting lines in place? Are these procedures documented?”

- The presence of “DPO contact details” is sought (p. 22). No mention of escalation lines or internal procedures in the approach.

**CQ43**: “Have you published the DPO contact details so customers/employees can make contact?”

- The approach for PPs can identify “DPO contact” references if stated in the policy (p. 22).
- Publishing them specifically is not validated beyond the text mention.

**CQ44**: “Have you notified your data protection authority of your DPO’s contact details?”

- Not addressed by the dissertation; it only checks the textual mention that a DPO exists and is contactable.

**CQ47**: “Is there a documented security program specifying technical, administrative, physical safeguards?”

- The dissertation checks for “PD SECURITY” references in PPs or for “take all measures” in DPAs (p. 26, 60). The approach flags if such language is missing.
- No deeper check on the actual details or scope of security measures.

**CQ48**: “Is there a documented process for resolving security complaints?”

- This is not specifically covered. The approach only looks for mention of data breach notifications or obligations to communicate. No mention of a “complaints resolution process.”

**CQ49**: “Is there a designated individual responsible for preventing and investigating security breaches?”

- Possibly a reference to a DPO or security official. The dissertation’s textual checks do not confirm such a role beyond the mention of “DPO” or “supervisory authority” (p. 22, 57).

**CQ50**: “Are industry standard encryption technologies employed for transferring, storing, and receiving sensitive personal data?”

- The text checks mention “technical and organizational measures” or “appropriate security” (p. 25, 58). They do not specifically verify encryption.
- Some references in optional DPA requirements (p. 66) talk about pseudonymization, encryption, etc., but only as a recognized item of Article 32(1).

**CQ51**: “Are personal data systematically destroyed or anonymized when no longer required?”

- The dissertation’s DPA approach checks if the contract states the processor shall “return or delete” data after the provision of services (p. 60, requirement R19).
- That partially addresses disposal but not anonymization specifically, nor whether it is truly “systematic.”

**CQ52**: “Can access to personal data be restored in a timely manner after a physical or technical incident?”

- The optional “MD7” from the dissertation (p. 58, 61) references measures including “restore the availability and access to personal data in a timely manner.” The approach flags whether the DPA states this.
- No deeper operational verification.

**CQ56**: “Are plans and procedures regularly reviewed?”

- Not specifically covered. The approach does not check for references to “regular review of procedures” beyond data breach or DPIA contexts.

**CQ57**: “Are all data breaches fully documented?”

- The approach sees if DPAs mention “document personal data breaches” (p. 59, 60). This can be flagged if missing.
- But it does not check completeness or the thoroughness of breach documentation.

**CQ58**: “Are there cooperation procedures between data controllers, suppliers, and partners to deal with data breaches?”

- The solution checks references to “assist the controller in notifying a breach,” and “sub-processor obligations” (p. 57–60).
- That partially addresses cooperation but not general multi-partner breach collaboration.

**CQ63**: “Are all transfers listed (nature of data, purpose, origin, receiving country)?”

- The PP conceptual model includes “TRANSFER OUTSIDE EUROPE,” “COUNTRY,” “SECTOR,” “TERRITORY” (p. 19, 22). If absent, it flags the violation.
- The approach cannot confirm if _all_ transfers are exhaustively listed—only that mention of the transfer elements is or is not present.

**CQ64**: “Is there a legal basis for the transfer (e.g. standard contractual clauses) documented?”

- The dissertation checks if the text mentions “EU MODEL CLAUSES,” “BINDING CORPORATE RULES,” or “ADEQUACY DECISION” (p. 19, 22).
- This partially covers the question but cannot confirm the actual legal basis beyond textual presence.

**CQ65**: “Are data subjects fully informed about any intended international transfers of their personal data?”

- The approach for PPs flags the presence of statements about “TRANSFER OUTSIDE EUROPE” (p. 22).
- Whether “fully informed” is satisfied is again a matter of textual completeness, not actual comprehension.

## Summary of Discussion

The dissertation partially addresses many of these compliance questions at the _document-text level_ by searching for specific references or obligations. It does not, however, verify procedural or technical implementation or confirm that any mention meets the question’s practical requirements (timelines, scope, or completeness). Where a question requires verifying the existence of internal processes, real enforcement, or external confirmations, the dissertation’s methods do not extend beyond the presence or absence of relevant textual clauses. Consequently, while there is some overlap (particularly around data subject rights, security, and breach notification), the dissertation does not provide robust coverage of detailed, process-oriented compliance questions.

---

# References

- [[bonatti2020a]]
- [[torre2021a]]