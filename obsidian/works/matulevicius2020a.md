---
ID: matulevivcius2020method
authors: Matulevicius, Raimundas and Tom, Jake and Kala, Kaspar and Sing, Eduard
category: unrelated
cluster_id: "14432861032546387089"
display: matulevicius
due: This paper do not extend prior model or propose a new one. It's only evaluating a previous model.
entrytype: inproceedings
forward_steps: 1
link: https://www.researchgate.net/profile/Raimundas-Matulevicius/publication/343930785_A_Method_for_Managing_GDPR_Compliance_in_Business_Processes/links/605b19a592851cd8ce623228/A-Method-for-Managing-GDPR-Compliance-in-Business-Processes.pdf
name: A Method for Managing GDPR Compliance in Business Processes
organization: Springer
place: CAiSE
pp: 100--112
scholar: https://scholar.google.com/scholar?cites=14432861032546387089&as_sdt=2005&sciodt=0,5&hl=en
scholar_id: kUSB-aPSS8gJ
scholar_ok: true
year: 2020
---


# Matulevicius, Raimundas and Tom, Jake and Kala, Kaspar and Sing, Eduard. A Method for Managing GDPR Compliance in Business Processes. 2020.


---
# Summary

### Approach and Motivations

This publication introduces a comprehensive method for managing GDPR compliance within business processes. The motivation behind this approach is to address the growing need for businesses to adhere to GDPR regulations effectively. The paper is structured to provide a detailed overview of the GDPR model, methods for achieving compliance, and processes for extracting and comparing compliance models.

The approach includes several key components such as the `GDPR model`, `Method for achieving compliance`, `Extracting AS-IS compliance model`, and `Comparing two models`. These components are designed to help businesses understand their current compliance status (`AS-IS compliance model`), identify compliance issues, and make necessary changes to their business processes. The method is aimed at ensuring that businesses can systematically track, manage, and update their GDPR compliance efforts.

### Approach Contribution For The Compliance Questions

#### Question 8

The approach involves the `GDPR model` and `Method for achieving compliance` components, which can be used to outline the retention periods for different categories of personal data. However, it does not specify retention periods for each category.

#### Question 28

The `GDPR model` and `Method for achieving compliance` could help ensure data accuracy and timely corrections by defining processes and responsibilities. However, the approach does not provide detailed procedures for maintaining data accuracy.

#### Question 29

The `GDPR model` and `Method for achieving compliance` may assist in developing retention policies but do not explicitly address the procedures for ensuring data is held for no longer than necessary.

#### Question 51

The provided method includes components that could help in managing data retention and destruction, such as `Defining compliance issues` and `Changing business process model`. However, it does not explicitly ensure that data is systematically destroyed when no longer needed.

#### Question 63

The approach does not specifically address listing all transfers of data, including the nature of the data, purpose of processing, and details of the transfer.

#### Question 64

While the `GDPR model` and `Method for achieving compliance` cover aspects of legal bases for processing, they do not explicitly document the legal bases for data transfers.

### Approach Insufficiencies For Fulfill The Compliance Questions

#### Question 8

The model lacks specific components for listing retention periods for each category of personal data. It primarily focuses on compliance processes rather than detailed data management guidelines.

#### Question 28

The approach does not provide explicit procedures for ensuring personal data is kept up to date and accurate, nor does it describe the process for making necessary corrections without delay.

#### Question 29

Although the approach includes the `GDPR model` and `Method for achieving compliance`, it does not detail the retention policies and specific procedures required to ensure data is held only as long as necessary.

#### Question 51

The approach does not explicitly address the systematic destruction, erasure, or anonymization of personal data when it is no longer legally required, leaving a gap in compliance.

#### Question 63

The methodology does not cover the listing of all data transfers, including detailed information about the data, purpose, and countries involved in the transfer.

#### Question 64

The current model does not fully document the legal bases for data transfers, such as EU Commission adequacy decisions or standard contractual clauses.

### Key Contributions

- Comprehensive method for managing GDPR compliance in business processes.
- Components introduced:
  - `GDPR model`
  - `Method for achieving compliance`
  - `Extracting AS-IS compliance model`
  - `Comparing two models`
  - `Defining compliance issues`
  - `Changing business process model`

- Background concepts include GDPR regulations and business process management.
- Evaluation includes comparing current compliance models and identifying compliance gaps.

### State-of-the-Art

This approach advances the state-of-the-art by providing an integrated method for managing GDPR compliance within business processes. It offers a structured way to extract and compare compliance models, identify issues, and implement necessary changes. This method stands out by focusing on the practical aspects of compliance management, rather than theoretical guidelines.

Related works may include other GDPR compliance frameworks and business process management models. However, this approach differentiates itself by offering a detailed method for comparing `AS-IS compliance models` and defining compliance issues, providing businesses with actionable insights for achieving GDPR compliance.

---

# Summary & Analysis

## Introduction (pp. 1–2)

This chapter addresses the challenge of ensuring GDPR compliance in organizational processes. It proposes a model-driven approach, with a supporting method and software tool, to analyze how business process activities align—or fail to align—with specific GDPR requirements. The motivation is that GDPR obligations are nontrivial to interpret, and organizations risk fines if they cannot demonstrate compliance.

**Key Points**

- Emphasizes the need for a systematic approach to identify GDPR obligations within business processes.
- Argues that failing to meet GDPR compliance can lead to significant financial and reputational consequences (p. 1).
- Proposes a GDPR model to capture core concepts (e.g., personal data, data processing, controllers, legal grounds) and a method to apply the model to business processes.

**Representative Quotations**

1. “Regardless of industry or size, one needs to find ways to achieve and maintain the specified privacy standards.” (p. 1)
2. “Failing to meet compliance requirements may result in administrative fines [...].” (p. 1)
3. “In this paper, we discuss the GDPR model and its application to achieve compliance in business processes.” (p. 2)

## Related Work (p. 2)

The authors briefly survey existing approaches that have emerged since the GDPR was enacted in 2018. These works provide foundations, such as GDPR-based vocabularies, UML representations of GDPR for compliance checking, and reference models capturing data processing principles.

**Key Points**

- Recognizes the growing body of GDPR compliance research, including approaches that use conceptual modeling, UML, enterprise architecture, or domain-specific languages.
- Differentiates their work by focusing on a method that uses a “compliance model” and a structured process for extracting and comparing an “as-is” business process model with the GDPR conceptual model.

**Representative Quotations**

1. “In [13] a UML representation of GDPR for assessing compliance is proposed [...] however this still remains future work.” (p. 2)
2. “In [9] authors introduce the GDPR-based privacy vocabulary for data interoperability when creating privacy policies.” (p. 2)
3. “We discuss how regulation compliance could be achieved using tool-supported model-based approach.” (p. 2)

## GDPR Model (pp. 2–4)

A key contribution is a conceptual model (in UML style) capturing major GDPR entities—personal data, data processing activities, controllers, processors, consent, legal grounds, data subject rights, technical/organizational measures, and so on. The model covers 40 of the GDPR’s ~99 articles, focusing specifically on those with direct obligations for controllers and processors.

**Key Points**

- The model or “metamodel” organizes GDPR requirements in a form that business analysts can map onto operational processes.
- Classes such as PersonalData and DataProcessing represent the fundamental processing chain; Consent and LegalGround ensure lawful basis; classes for organizational and technical measures indicate how compliance might be enforced.
- Data subject rights (e.g., rectify, inform, object) also appear in the model, with relationships to controllers that must enable those rights.

**Representative Quotations**

1. “The GDPR regulation introduces the major principles for the personal data processing. But it is rather broad and leaves room for interpretation.” (p. 3)
2. “The GDPR model [...] covers 40 articles, focusing on specific legal requirements obliging controllers and processors.” (p. 3)
3. “Classes LegalGroundDataTransfer, LegalGroundSpecialCategory, and DataProtectionImpactAssessment represent regulation Art. 45–59, 9(2) and 35–36 respectively.” (p. 3)

## The Proposed Method for Achieving Compliance (pp. 4–5)

The authors outline a four-step, iterative method that uses the GDPR model to check a given business process:

1. **Extract AS-IS compliance model**: Identify how each GDPR concept is (or is not) manifested in the current business process.
2. **Compare two models**: Match the AS-IS model to the reference GDPR model to find missing elements or noncompliance.
3. **Define compliance issues**: Register each gap or noncompliance as an “issue” (NC#1, NC#2, etc.).
4. **Change business process model**: Modify the original process to resolve identified issues, then re-run the procedure.

**Key Points**

- The method ensures systematic coverage of GDPR obligations by mapping them to specific aspects of the business process.
- If certain obligations (e.g., logging of processing activities under Art. 30, or obtaining valid legal grounds under Art. 6) are missing, the method flags noncompliance.
- The authors illustrate this with a running “Tollgate” scenario, showing how personal data flows from a driver’s bank info into a toll payment process.

**Representative Quotations**

1. “The method for achieving GDPR compliance consists of four steps [...] The extraction includes identification of the following GDPR model elements.” (p. 4)
2. “In case of non-compliance, one changes the business process model so that non-compliance is removed from the model.” (p. 4)
3. “We present a method to extract an as-is compliance model that describes non-compliance issues and offers solutions to achieve process compliance.” (p. 2)

## Tollgate Scenario (pp. 5–9)

The authors use a hypothetical scenario of a connected vehicle paying tolls: personal data flow from a driver’s bank info to a tollgate to a bank. They demonstrate extracting a “GDPR instance” from this scenario, revealing missing elements: no explicit logging of processing, no declared legal grounds, no mention of data breach procedures, etc.

**Key Points**

- Each missing GDPR concept (e.g., an absence of “records of processing,” or no organizational measure specified) becomes a non-compliance issue (NC#1, NC#2, NC#3).
- Remediations include introducing a log-keeping step, clarifying or obtaining consent, and implementing encryption or other technical measures.

**Representative Quotations**

1. “Following Art. 30(1), each controller [...] shall maintain a record of processing activity. This is not the case in the Tollgate example.” (p. 7)
2. “The Tollgate should potentially receive the driver’s consent for processing the transaction details.” (p. 7)
3. “Change business process model: we illustrate how identified non-compliance issues are addressed in the Tollgate example.” (p. 8)

## Tool Support (pp. 9–10)

A prototype software tool (available on GitHub) implements steps 1–3 of the method (extraction, comparison, defining compliance issues). It flags missing elements in the business process. A user or analyst then modifies the model manually. The authors note that automating step 4—auto-generating compliant process variants—remains future work.

**Key Points**

- Demonstrates partial automation: the tool identifies compliance gaps and suggests solutions.
- Future research might incorporate design patterns to automate how to fix certain classes of noncompliance.

**Representative Quotations**

1. “A prototype tool [...] is implemented. The main functions of the prototype support the method for achieving regulation compliance.” (p. 9)
2. “The updated model should be the input to the next iteration of compliance checking.” (p. 10)
3. “Future research is also needed for tool support regarding the change of the business process model.” (p. 11)

## Limitations, Completeness, and Validity (pp. 10–11)

The chapter closes by stressing that the model addresses “specific legal requirements” (40 GDPR articles) and does not cover all national deviations. The authors highlight how focusing on key controller/processor obligations yields high coverage for business processes. They also discuss how the method was validated with several business scenarios (e.g., an airline contact center).

**Key Points**

- The authors argue the model is relatively comprehensive compared to other partial approaches.
- They acknowledge that some GDPR articles are broad or contain “effort clauses” difficult to represent in UML.
- Emphasize that, while not all 99 articles are modeled, the coverage is sufficient for typical controller/processor tasks.

**Representative Quotations**

1. “In total the GDPR model concerns 40 articles [...] resulting in rather high completeness while checking the compliance of business processes.” (p. 10)
2. “The GDPR model does not consider how it may be adapted in a national context [...] The model would have to be adjusted where member-state deviations apply.” (p. 10)
3. “The GDPR model, its supporting method and tool have been applied in a few other cases [...] domain experts found the application intuitive and helpful.” (p. 11)

---

# Evaluation Based on Inclusion Criteria

Below, we assess how this paper meets the inclusion/exclusion criteria:

1. **Proposes a data provenance model to represent activities information related to GDPR obligations?**
    
    - The paper does not explicitly use the term “provenance.” However, it systematically models “who is processing what personal data, for what reason, under which legal grounds, and with which technical/organizational measures.” This _does_ capture a form of data usage traceability, especially around logging.
    - “The GDPR model also describes the data processing principles and the principle of accountability [...] records of the processing activities.” (p. 3, p. 7)
    - **Conclusion**: **Yes**, the approach includes a structured representation of processing activities, logging, and compliance needs; this is quite akin to a provenance approach.
2. **Model should be useful to address the compliance questions we are interested in**
    
    - The model systematically covers data subject rights, logging obligations, consent, risk-based measures, etc. This aligns with many of the compliance questions about data retention, lawful basis, user rights, etc.
    - “In case of non-compliance, one changes the business process model so that the non-compliance is removed.” (p. 4)
    - **Conclusion**: **Yes**, it is a method for discovering and fixing compliance gaps in business processes, so it can be adapted to answer different GDPR obligations.
3. **The proposed model should be publicly available**
    
    - The authors mention a GitHub repository (p. 9–10): “(see, [https://github.com/motekaj/gdpr-analyzer).”](https://github.com/motekaj/gdpr-analyzer\).%E2%80%9D) The details about how extensively the model is documented or whether it is fully open are not fully elaborated in the excerpt, but the link indicates a public code base.
    - **Conclusion**: It _appears_ the conceptual model and the supporting tool are at least partly available in a public repository. Likely satisfies the requirement of public availability.
4. **Document in English or Portuguese**
    
    - The chapter is written in English.
    - **Conclusion**: **Yes**.
5. **Publicly accessible or in a digital library signed by CAPES CAFÉ**
    
    - It is published in the “Lecture Notes in Business Information Processing” (Springer) and also found on ResearchGate. This suggests it is likely accessible under standard academic library subscriptions.
    - **Conclusion**: **Yes**, it is publicly available via Springer or ResearchGate.
6. **Peer-reviewed document**
    
    - This is a chapter in Lecture Notes in Business Information Processing. LNCS and LNBIP volumes typically undergo a peer review process for conference or workshop contributions.
    - **Conclusion**: **Yes**, it is presumably a peer-reviewed contribution.

Hence, **the paper meets our inclusion criteria**.

---

# Discussion on Compliance Questions

Below is an examination of how this paper’s content, approach, and model address (or do not address) each compliance question. Whenever relevant, we cite specific passages or arguments:

### CQ08

“For each category of personal data, list the period for which the data will be retained [...]”

- The authors mention that the GDPR model includes attributes such as “legal grounds” or “records of processing,” but do not explicitly show “retention period” for each data category.
- Noncompliance might be flagged if a process omits time-based retention. However, a direct mechanism or class for “retention schedule” is not described (pp. 7–9).
- **Conclusion**: The model can highlight if data are processed without an expiry or if a log is missing, but explicit retention durations are not clearly shown.

### CQ09

“Identify actions that are required to ensure all personal data processing operations are GDPR compliant [...]”

- The entire paper focuses on discovering missing GDPR elements in a business process (consent, logging, purpose, etc.) so that organizations can “define compliance issues” and fix them (p. 4).
- **Conclusion**: This is exactly the main aim of their four-step method—i.e., systematically identifying and remedying compliance gaps.

### CQ11

“If personal data that you currently hold on the basis of consent does not meet the required standard [...] re-sought the individual’s consent?”

- The paper’s example focuses on obtaining consent in the first place, but not specifically on re-seeking it if the standard changes. Still, the “method for achieving compliance” can highlight if the lawful basis is no longer valid, prompting an update.
- **Conclusion**: Indirect coverage; re-seeking consent is not explicitly shown, but the approach would detect missing or invalid legal grounds.

### CQ17

“Is your organisation able to respond to SARs within one month?”

- The model includes “Data subject rights,” e.g. right to rectification, right to be informed, etc. (p. 3–4). However, they do not discuss time-bound performance explicitly.
- **Conclusion**: The process can detect if the right to rectification is missing, but it does not mention the one-month timeframe. Partial coverage.

### CQ20

“Are there controls to halt processing where an individual has sought restriction of processing?”

- The approach primarily highlights whether the business process has legal grounds, log-keeping, or data subject rights. The scenario does not mention “restriction of processing.”
- **Conclusion**: Not directly covered; the model references data-subject rights, but the “right to restriction” or halting a process is not exemplified.

### CQ21

“Are individuals told about their right to object to certain types of processing?”

- The model includes “enablesExercise on Right” from the controller to the data subject, referencing Art. 13, 14, and 21 (p. 3). But the scenario does not detail the communication channel for informing individuals.
- **Conclusion**: The model recognizes a “right to object,” but the paper does not detail how controllers must inform individuals. Partial coverage.

### CQ25

“Have the circumstances been documented in which an individual’s data protection rights may be lawfully restricted?”

- The model references legal grounds, special categories, and other obligations. It does not delve into scenario-based restrictions on data-subject rights (like public security, ongoing investigations, etc.).
- **Conclusion**: Not specifically addressed.

### CQ28

“Are procedures in place to ensure personal data are up to date and accurate [...]?”

- The model addresses “right to rectification” (p. 3), so if a process lacks steps to let a user rectify data, that’s flagged.
- **Conclusion**: **Yes**, the right to rectification is part of the GDPR model, so the method will highlight if it is absent in a business process.

### CQ29

“Are retention policies in place to ensure data are held for no longer than necessary?”

- Similar to CQ08, the authors do not present an explicit mechanism for retention periods. The model references only “records of processing” and “purpose,” not a formal retention schedule.
- **Conclusion**: Not explicitly covered beyond general references to principle of storage limitation.

### CQ30

“Is your business subject to other rules that require a minimum retention period?”

- Not discussed in detail. The method addresses GDPR specifically, not other legal frameworks.
- **Conclusion**: **Not** covered.

### CQ32

“Are procedures in place to ensure no unnecessary or unregulated duplication of records?”

- The authors do not address duplication or data minimization explicitly beyond noting general data protection principles (p. 3).
- **Conclusion**: **Not** explicitly addressed.

### CQ33

“Are service users/employees fully informed about how you use their data...?”

- The model references “Controller must inform data subjects,” but the authors show no direct or user-facing approach.
- **Conclusion**: Partial coverage at the conceptual level (Art. 13/14) but no explicit mention of user-friendly transparency steps.

### CQ35

“Are procedures in place to keep personal data accurate and up to date, and correct them without delay?”

- Overlaps with CQ28. The model includes “Right of rectification,” so that concept is recognized.
- **Conclusion**: **Yes**, at least conceptually.

### CQ37

“When engaging individuals, are procedures in place to proactively inform them of their GDPR rights?”

- As with CQ21, the model says the controller must enable rights, but “proactive informing” is not described in detail.
- **Conclusion**: **Not** specifically addressed how that “informing” is operationalized.

### CQ38

“Is info on how the organization facilitates GDPR rights published in an accessible format?”

- The authors do not address the publishing or accessibility format. They focus on internal business process transformations.
- **Conclusion**: **Not** covered.

### CQ39

“Have agreements with suppliers/other third parties been reviewed to ensure all appropriate data protection requirements?”

- The model handles data transfers to third countries or recipients, but not contractual or supplier relationships.
- **Conclusion**: **Not** covered beyond the mention of cross-border scenarios (p. 3).

### CQ40–CQ44

(Regarding the Data Protection Officer)

- No mention of DPO roles, escalation, or contact details.
- **Conclusion**: **Not** covered.

### CQ47

“Is there a documented security program specifying the technical/administrative safeguards?”

- The model addresses “technical measures” and “organizational measures” (p. 3–4). This implies organizations must define how data security is handled.
- **Conclusion**: **Yes**, at a conceptual level. The Tollgate example also highlights how encryption and organizational rules are flagged as needed (p. 9).

### CQ48

“Is there a documented process for resolving security-related complaints and issues?”

- The paper shows how to address noncompliance items, but it does not specify a “complaint resolution” process.
- **Conclusion**: **Not** addressed.

### CQ49

“Is there a designated individual responsible for preventing/investigating security breaches?”

- The text references data breach notification (Art. 33, 34) but no mention of a designated official.
- **Conclusion**: **Not** covered.

### CQ50

“Are industry standard encryption technologies employed for storing/transferring sensitive data?”

- The example includes encryption as a measure but does not detail “industry standard” forms.
- **Conclusion**: The concept is recognized, though no specific technology is mandated.

### CQ51

“Are personal data systematically destroyed, erased, or anonymized when no longer required?”

- Not explicitly covered. The method focuses on identifying missing steps, but deletion/anonymization is not illustrated in the example.
- **Conclusion**: **Not** specifically mentioned.

### CQ52

“Can access to personal data be restored in a timely manner if an incident occurs?”

- Not discussed in detail.
- **Conclusion**: **Not** covered.

### CQ56

“Are plans and procedures regularly reviewed?”

- Not specified.
- **Conclusion**: **Not** covered.

### CQ57

“Are all data breaches fully documented?”

- The model references a “DataBreachNotification” class (p. 3) but not full documentation details.
- **Conclusion**: Potential partial coverage (notification is recognized), but no in-depth detail.

### CQ58

“Are there cooperation procedures in place between controllers and partners for data breaches?”

- Not covered.
- **Conclusion**: **Not** addressed.

### CQ63–CQ65

(International data transfers)

- The model does discuss “legal ground data transfer” for cross-border flows, but not the full details about Commission adequacy decisions or standard contractual clauses.
- **Conclusion**: The model references cross-border scenarios, but not specifics about documenting the legal basis or fully informing data subjects.

Overall, the paper supports a method to discover GDPR compliance gaps in business processes, especially around lawful basis, data subject rights, logging, and technical measures. Many policy-level or organizational tasks (like a DPO’s role or third-party contracts) are not deeply discussed.

---
## Summary & Analysis

The chapter provides a conceptual GDPR model and a companion method to evaluate and fix potential compliance gaps in business process models. It defines a UML-style representation of core GDPR constructs—data subject, personal data, lawful basis, data breach notifications, records of processing, data subject rights—and walks through a “Tollgate” use case to show how missing elements (consent, logging, encryption) can be discovered and rectified. A prototypical software tool automates large portions of this analysis. While the approach is thorough for typical controller obligations (Art. 5–6, 30, 32, etc.), it does not cover all 99 articles, nor does it delve deeply into specialized rules (e.g., member-state exceptions). Nonetheless, it stands as a systematic, model-driven solution for adapting business processes to meet GDPR.

## Evaluation Based on Inclusion Criteria

The paper is written in English, peer-reviewed, and openly accessible via Springer/ResearchGate. It focuses on representing GDPR obligations as a structured model—effectively capturing data lifecycle activities akin to provenance. The tool is publicly referenced via GitHub. Therefore, it meets our inclusion requirements.

## Discussion on Compliance Questions

The method supports many compliance aspects: lawful basis, logging, user rights, and technical measures. However, it does not explicitly detail certain organizational, policy-based, or administrative elements (e.g., DPO appointments, retention times, third-party agreements). It also does not give explicit instructions on how to proactively inform data subjects or how to set minimum retention schedules. Nevertheless, it can detect many core GDPR issues in a business process, especially around data subject rights, logging, consent, and security.


---

# References

- [[tom2018a]]
- [[pandit2019c]]
