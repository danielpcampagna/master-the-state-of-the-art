---
ID: chhetri2022a
authors: Chhetri, Tek Raj and Kurteva, Anelia and DeLong, Rance J and Hilscher, Rainer and Korte, Kai and Fensel, Anna
category: ok
display: chhetri (Data Protection by Design Tool for Automated GDPR Compliance)
due: This paper proposes a knowledge-graph-based approach to represent consent and data usage for automated GDPR compliance verification, aligning with data protection by design.
entrytype: article
link: https://doi.org/10.3390/s22072763
name: Data Protection by Design Tool for Automated GDPR Compliance Verification Based on Semantically Modeled Informed Consent
organization: MDPI
place: Sensors
pp: 1-35
provenance_related: true
related:
  - GDPR compliance
  - semantic web
  - data protection by design
  - informed consent
  - privacy policy
year: 2022
forward_steps: 2
---

# Summary & Analysis

## Introduction (pp. 1–3)

The paper begins by highlighting the GDPR’s enforcement challenges for companies that process personal data. It emphasizes the principle of data protection by design and underscores the need for scalable, automated compliance verification solutions that make use of semantic technologies and knowledge graphs.

**Key points**

- Explains the paradigm shift introduced by GDPR and the complexity of consent requirements.
- Motivates a need for tools to automate compliance verification for organizations at scale (e.g., insurance, smart cities).
- Presents the authors’ core objective: a tool to operationalize GDPR principles (consent, accountability, data protection by design) through a knowledge graph.

**Representative quotations**

1. “Organizations face significant challenges, such as demonstrating compliance [...] as well as the scale at which compliance verification must be performed.” (p. 2)
2. “We present a scalable data protection by design tool for automated compliance verification and auditability based on informed consent that is modeled with a knowledge graph.” (p. 2)
3. “Our tool makes extensive use of semantic technologies, specifically a knowledge graph (KG) and an ontology [...], for representing informed consent as defined by the GDPR.” (p. 2)

## Background (pp. 3–5)

The authors describe how GDPR has reshaped the data-sharing landscape by requiring explicit informed consent and accountability for personal data processing. They note that companies must ensure data processing operations match the user’s consent and demonstrate compliance to regulators.

**Key points**

- Contrasts the simpler, pre-GDPR environment with the new mandatory consent obligations.
- Stresses that compliance, audit, and accountability now demand advanced technical measures and automation, especially in sectors like smart cities or car insurance.
- States that verifying each data transaction manually becomes infeasible at large scale.

**Representative quotations**

1. “Prior to the GDPR, there was no requirement for consent, and thus the data sharing process was simple [...] With the implementation of the GDPR, the data sharing landscape has shifted and become more complicated.” (p. 3)
2. “Having reviewed the existing GDPR compliance verification tools [...], we have identified several issues that many companies still face.” (p. 4)
3. “In light of current challenges and industrial requirements [...] we present a scalable tool for automated GDPR compliance based on semantically modeled informed consent.” (p. 5)

## Related Work (pp. 6–9)

The authors survey existing compliance approaches, some relying on blockchain, formal logic, or partial semantic modeling. They find most solutions incomplete in fully automating compliance checks or in translating GDPR requirements into robust technical measures.

**Key points**

- Existing tools either address only fragments of GDPR obligations (e.g., partial consent management or logs) or lack proven scalability.
- Legal–technical alignment (via standard data protection models) is usually missing or only partly tackled.
- Semantic solutions exist but do not fully implement data protection by design or unify all GDPR obligations (purpose limitation, auditing, user revocation, etc.) in a single approach.

**Representative quotations**

1. “A major challenge for companies, when complying with the GDPR, is to adhere to the ‘principles of data protection by design’ and ‘data protection by default.’” (p. 7)
2. “Although several software tools for GDPR compliance have already been developed [...], in most cases, these tools address only a specific subset of the GDPR regulations.” (p. 7)
3. “The details on the implementation [in many solutions] are limited, and TOMs have not been considered.” (p. 8)

## KG Overview and Legal Background (pp. 9–10)

Here, the authors introduce the Standard Data Protection Model (SDM) as a bridge from abstract GDPR principles to well-defined “protection goals,” mapped onto technical/organizational measures (TOMs). They also describe the knowledge graph that encodes informed consent—storing states such as granted, revoked, or expired, and the relevant data-processing attributes.

**Key points**

- The SDM systematically ties GDPR provisions (e.g., lawfulness, fairness, purpose limitation) to protection goals that software can implement.
- The knowledge graph (KG) stores consent details, the type of data collected, and the exact processing operations.
- This approach ensures transparency and supports automated validation of consent-based processing.

**Representative quotations**

1. “We present a process with a sequence of intermediate steps (regulation -> SDM -> TOM -> code) that translates legal regulations into code.” (p. 9)
2. “Automated compliance verification is made possible by implementing a regulation-to-code process that translates GDPR regulations [...] ultimately, software code.” (p. 9)
3. “Consent is collected via consent forms [...] The KG can be accessed directly via the SPARQL API, providing consistent consent representation in a machine-readable format.” (p. 10)

## System Architecture (pp. 10–16)

The architecture is microservices-based. Core modules include (1) a consent module to generate and validate user consent into the KG; (2) a compliance module to systematically check if data processing operations align with the user’s stated consent; (3) a security/privacy module implementing encryption and access control; and (4) an auditing module providing logs for accountability.

**Key points**

- Microservices pattern was chosen for flexibility, maintainability, and scalability.
- Each module enforces a GDPR principle: e.g., encryption for data confidentiality, logs for accountability, role-based access for data minimization.
- Policy enforcement points (PEP) and policy decision points (PDP) incorporate user privacy preferences vs. the data processor’s declared policy.

**Representative quotations**

1. “Our architecture follows a microservices architecture pattern [...], providing a solution to problems such as technology lock-in and dependency typical of monolithic patterns.” (p. 10)
2. “The consent module ensures that only necessary and required consent information is used, thereby minimizing data usage.” (p. 14)
3. “Security typically concerns confidentiality, integrity, availability [...] privacy adds concern for the right of a person to authorize and restrict the use of data that describes that person.” (p. 15)

## Implementation (pp. 17–24)

Implementation details show how each microservice is realized (Flask for REST APIs, GraphDB for the KG, MongoDB for logs, and cryptographic libraries). The authors emphasize the approach to storing and verifying all data-sharing or processing events in line with the original informed consent (e.g., the “broken consent chain” scenario).

**Key points**

- The tool uses SPARQL queries for compliance checks (comparing processing requests to valid consent items in the KG).
- Consent JSON schemas ensure minimal, relevant data is used.
- Layered AES + RSA encryption provides “data protection by default.”

**Representative quotations**

1. “The reason for using a NoSQL database is the scalability it offers [...] suitable for storing the information logs.” (p. 18)
2. “Our AES implementation allows for searchable encryption while preserving confidentiality.” (p. 20)
3. “By providing personal information that resolves to a unique ID, users can access their data via a user interface [...], supporting the right to rectification or erasure.” (p. 22)

## Evaluation (pp. 24–31)

The performance tests focus on (a) consent creation time, (b) audit queries, and (c) compliance checks under different loads. Scalability is addressed by container orchestration (Kubernetes). They also map how the tool meets the GDPR’s technical/organizational measures (TOMs) by referencing the Standard Data Protection Model.

**Key points**

- Average consent creation time is ~7 s with moderate payload sizes; compliance checks remain feasible at scale.
- The architecture supports horizontal scaling (e.g., microservices can be replicated).
- GDPR coverage is demonstrated by systematically matching each principle to a specific TOM, tested in the final system.

**Representative quotations**

1. “A microservices architecture pattern [...] provides the flexibility and maintainability required for scaling.” (p. 25)
2. “We have evaluated the execution overhead of our tool’s key functionalities [...], demonstrating that the approach is suitable for high-volume scenarios such as smart cities.” (p. 27)
3. “The SDM systematically ties legal requirements into the code base via protection goals mapped to well-defined measures.” (p. 29)

## Conclusion (pp. 31–35)

The authors finalize that the proposed knowledge-graph-based compliance tool is ready to be deployed in real-world contexts, such as insurance and smart cities. They note future work includes further expansions to dynamic use-case scenarios and continuing to refine the “regulation-to-code” pipeline.

**Key points**

- The tool addresses multiple GDPR challenges: consent, purpose limitation, data subject rights, revocation, and audit.
- Its microservices architecture can integrate with existing systems to track data usage.
- The flexible design can adapt to additional regulatory frameworks beyond GDPR.

**Representative quotations**

1. “We show that GDPR regulations can be translated into code via several intermediate steps, bridging the gap between legal text and technical implementation.” (p. 32)
2. “Our approach can be readily extended to other domains and adapted to additional regulatory frameworks.” (p. 34)
3. “Future work will explore further data protection by design solutions and dynamic use-case scenarios to meet evolving industrial needs.” (p. 34)

---

# Evaluation Based on Inclusion Criteria

Below, we evaluate this paper against each of the specified inclusion/exclusion criteria. Where relevant, we include quotations or key arguments (with page numbers) from the text.

1. **The approach should strictly propose a data provenance model to represent activities information related to GDPR obligations**
    
    - The paper’s knowledge-graph-based approach stores consent states, data usage events, and relevant processing details. While it does not explicitly label the structure as a “data provenance model,” it does track “who did what data processing and under which consent” (pp. 9–10). This fits the essence of a provenance model, as it retains details of data collection and subsequent usage, thereby linking activities with the user’s informed consent.
    - “Consent is collected via consent forms [...] The KG can be accessed directly [...] providing consistent consent representation in a machine-readable format.” (p. 10)
    - Conclusion: **Meets** this criterion, because it captures and represents core processing activities, consent state, and relevant obligations.
2. **The proposed model should be useful to address the compliance questions we have**
    
    - The paper explicitly discusses automated checks of data processing behavior against the semantically modeled consent. This is central to compliance audits (p. 14).
    - “Our tool makes extensive use of semantic technologies [...] for representing informed consent as defined by the GDPR.” (p. 2)
    - Conclusion: **Meets** the criterion that the authors’ model is designed to check compliance and can be extended to queries about lawful processing, retention, and data subject rights.
3. **The proposed model should be publicly available so that we can compare it against the other approaches**
    
    - The paper states it is an open-access publication; the approach (ontology, code elements) is described in detail. However, the text does not explicitly confirm a fully open-source repository for the entire tool or the knowledge graph. It appears the model is documented, with at least partial availability (p. 2, p. 32).
    - “Our work adheres to data protection by design principles by implementing a novel regulation-to-code process.” (p. 2)
    - Conclusion: The main text suggests that the semantic model is accessible in the context of the smashHit project, but does not unequivocally confirm free public repositories. This _may_ be partially fulfilled.
4. **Document must be in English or Portuguese**
    
    - The paper is in English.
    - Conclusion: **Meets** this criterion.
5. **Document is publicly available or at least accessible under CAPES CAFE**
    
    - The article is published in MDPI’s Sensors, which is open access (p. 1).
    - Conclusion: **Meets** this criterion.
6. **Must be a peer-reviewed document**
    
    - Sensors is a peer-reviewed journal.
    - Conclusion: **Meets** this criterion.

Based on the above, the article **meets** the core inclusion criteria and is relevant for the analysis.

---

# Discussion on Compliance Questions

Below is an exhaustive discussion of how the model and system described in the paper address (or do not address) each listed compliance question. All quotations are followed by a specific page reference.

**CQ08**: “For each category of personal data, list the period for which the data will be retained.”

- The authors implement “Storage limitation” (Art. 5(1)(e)) via their “availability” concept in Table 1 and mention time-based compliance checks (p. 5, p. 25). However, the exact retention durations per data category are not fully enumerated; they mainly rely on consent expiration.
- “We demonstrate the effectiveness of the tool in the insurance and smart cities domains. We highlight ways in which our tool can be adapted [...] including retention.” (p. 2)
- **Conclusion**: The tool partially addresses retention via expiration checks, but does not present a structured mechanism for forcibly listing every period for each data category.

**CQ09**: “Identify actions required to ensure all personal data processing operations are GDPR compliant.”

- The paper’s core objective is to automate verification that any data-processing action is covered by the relevant consent. Noncompliant actions trigger alerts (p. 14–15).
- “When the compliance check is performed [...] the tool determines that the consent has expired [..], effectively blocking unauthorized data processing.” (p. 15)
- **Conclusion**: Directly addressed. The system identifies compliance issues automatically and notifies the controller/processor to prevent or stop further noncompliant operations.

**CQ11**: “If personal data that you currently hold on the basis of consent does not meet GDPR standards, have you re-sought consent?”

- Although re-seeking consent is mentioned in principle, the paper does not detail an automated mechanism for reacquiring new consent. It does handle “broken consent chain” (p. 16).
- “A system that can handle dynamic consent should be able to [...] re-establish valid consent.” (p. 2, p. 16)
- **Conclusion**: The system design is capable of invalidating old consent and prompting reacquisition, but the paper does not provide deep detail on re-soliciting consent from data subjects.

**CQ17**: “Is your organisation able to respond to SARs (Subject Access Requests) within one month?”

- The authors mention they store everything in a knowledge graph, enabling quick retrieval. They do not specifically mention the one-month timeframe, but they do note that audit logs and data subject queries can be quickly executed (p. 14, p. 22).
- **Conclusion**: Indirectly supported. The KG architecture allows timely retrieval of personal data and its usage. No explicit mention of one-month, but the mechanism is fast enough to help fulfill it.

**CQ20**: “Are there controls to halt processing where an individual has sought restriction of processing?”

- Revocation or withdrawal of consent is fundamental in the approach. Once consent is revoked in the KG, the system blocks subsequent processing (p. 15–16).
- **Conclusion**: **Yes**, it supports halting processing automatically via consent revocation.

**CQ21**: “Are individuals told about their right to object to certain types of processing?”

- The paper does not describe data subject notifications or how the individual is educated about rights; it focuses on the underlying compliance tool.
- **Conclusion**: **Not explicitly** addressed in the text regarding user outreach or informing them of rights.

**CQ25**: “Have the circumstances been documented in which an individual’s data protection rights may be lawfully restricted?”

- The approach addresses consent-based restrictions, but does not discuss lawful restrictions (e.g., Article 23 exceptions).
- **Conclusion**: **Not addressed** in detail. They focus on standard consent scenarios, not lawful derogations.

**CQ28**: “Are procedures in place to ensure personal data are up to date and accurate, and changed without delay?”

- The paper’s “Intervenability” measure ensures that data subjects can rectify or remove their data (p. 10, Table 1).
- “By providing personal information [...] users can access their data [...] supporting the right to rectification or erasure.” (p. 22)
- **Conclusion**: **Yes**, the system’s knowledge graph approach supports up-to-date data, as data subjects or controllers can update it.

**CQ29**: “Are retention policies in place to ensure data are held no longer than necessary?”

- Similar to CQ08, the system can incorporate an expiration date in consent. They do not explicitly mention broad data retention beyond consent expiry.
- **Conclusion**: Partially addressed, since consent expiration halts usage, but a formal retention policy mechanism is not extensively discussed.

**CQ30**: “Is your business subject to other rules that require a minimum retention period?”

- The authors do not address domain-specific retention rules beyond the general notion of purpose limitation.
- **Conclusion**: **Not** discussed.

**CQ32**: “Are procedures in place to ensure no unnecessary duplication of records?”

- Not explicitly mentioned. The system does mention data minimization, but duplication across systems is not thoroughly explored.
- **Conclusion**: **Not** explicitly addressed.

**CQ33**: “Are service users/employees fully informed of how you use their data, in a transparent way?”

- The tool provides audit logs and a semantically explicit representation. However, user-facing transparency about all processing steps is not described in detail (p. 14–15).
- **Conclusion**: The architecture _could_ support transparency, but user notification processes are not elaborated.

**CQ35**: “Are procedures in place to ensure data are kept accurate and updated without delay?”

- Overlaps with CQ28. The authors emphasize the capability to rectify data and processes.
- **Conclusion**: **Yes**, covered by intervenability and the knowledge graph updates (p. 10, p. 22).

**CQ37**: “Are procedures in place to proactively inform individuals of their GDPR rights (e.g., when providing a service)?”

- As with CQ21, the paper does not detail any proactive user communication or outreach system.
- **Conclusion**: **Not** addressed.

**CQ38**: “Is information on how the organisation facilitates individuals exercising their GDPR rights published in an easily accessible format?”

- The paper emphasizes the system’s architecture for compliance but not user-facing communication channels or policy documents.
- **Conclusion**: **Not** specifically covered.

**CQ39**: “Have agreements with suppliers and other third parties processing personal data on your behalf been reviewed to ensure proper GDPR clauses?”

- Focus is on technical compliance checks within a single architecture. Third-party agreements or DP–DC relationships are not described in detail.
- **Conclusion**: **Not** covered.

**CQ40**: “Do you need to appoint a DPO?”

- The text does not address DPO obligations or organizational roles beyond referencing typical GDPR responsibilities.
- **Conclusion**: **Not** covered.

**CQ41**, **CQ42**, **CQ43**, **CQ44**: Questions about DPO appointment, escalation, published contact details, etc.

- Same as above: the paper focuses on technical solutions, not DPO management processes.
- **Conclusion**: **Not** covered.

**CQ47**: “Is there a documented security programme specifying technical, administrative, and physical safeguards for personal data?”

- The tool outlines encryption, logging, role-based access controls, and compliance checks, all of which are part of “technical and organizational measures” (pp. 5–10).
- **Conclusion**: They do present a partial security program, referencing the SDM-based TOMs (p. 9). **Yes**, in the sense of technical measures.

**CQ48**: “Is there a documented process for resolving security-related complaints and issues?”

- The paper addresses detection of compliance issues (p. 15–16) but does not mention a formal complaint resolution process.
- **Conclusion**: **Not** specifically addressed.

**CQ49**: “Is there a designated individual responsible for preventing/investigating security breaches?”

- No mention of a dedicated official or role.
- **Conclusion**: **Not** addressed.

**CQ50**: “Are industry standard encryption technologies employed?”

- Yes, they employ RSA and AES with layered encryption for data. They mention PKCS and NIST standards (p. 20).
- **Conclusion**: **Yes**.

**CQ51**: “Are personal data systematically destroyed or anonymized when no longer legally required?”

- The approach focuses on blocking further use if consent expires or is revoked, but does not describe actual data destruction or anonymization steps (p. 16).
- **Conclusion**: Possibly partial: not fully described.

**CQ52**: “Can access to personal data be restored in a timely manner in the event of physical or technical incident?”

- They mention availability as one of the protection goals (p. 5, Table 1) but do not detail disaster recovery or backup procedures.
- **Conclusion**: **Not** explicitly covered.

**CQ56**: “Are plans/procedures regularly reviewed?”

- Ongoing updates are implied but not specifically addressed.
- **Conclusion**: **Not** explicitly covered.

**CQ57**: “Are all data breaches fully documented?”

- They mention auditing but not specifically data breaches.
- **Conclusion**: **Not** fully addressed.

**CQ58**: “Are there cooperation procedures between data controllers, suppliers, partners to deal with data breaches?”

- Not discussed.
- **Conclusion**: **Not** covered.

**CQ63**, **CQ64**, **CQ65**: Questions about international transfers of data, legal basis for the transfer, standard contractual clauses, informing data subjects.

- The paper focuses on general compliance at a system level, not specific cross-border data transfer rules.
- **Conclusion**: **Not** addressed.

Overall, the paper directly addresses or partially supports the queries concerned with consent management, halting unlawful processing (CQ20), ensuring data subject rectification rights (CQ28, CQ35), and employing cryptographic safeguards (CQ50). Many of the more organizational or policy-based compliance questions (e.g., DPO responsibilities, third-party contractual compliance, breach response) are out of scope or not explicitly detailed.

---

# Summary & Analysis

The article systematically describes a data-protection-by-design tool for GDPR compliance, using semantics (knowledge graphs) to model and verify informed consent. It maps legal requirements to protection goals (via the Standard Data Protection Model) and then to well-defined technical and organizational measures. Core modules handle consent creation, compliance checking (with alerts on violation), encryption, and auditing. The work was validated in automotive insurance and smart city scenarios, demonstrating performance scalability and partial coverage of key GDPR obligations.

# Evaluation Based on Inclusion Criteria

The approach proposes a knowledge-graph-based method that captures GDPR-related consent events and processing activities, effectively aligning with a data provenance mindset. It is in English and published in a peer-reviewed, open-access journal. While it does not absolutely confirm open-source availability of every component, the paper’s model and architecture are documented to the extent that it seems publicly examinable.

# Discussion on Compliance Questions

The tool addresses core GDPR concerns (consent expiration, halting processing on withdrawal, privacy by design) but does not delve into many organizational or policy-based requirements (e.g., DPO appointment, cross-border transfer documentation). It provides partial solutions or references for data minimization, data accuracy, audit logs, encryption standards, and role-based access control. However, certain compliance topics like breach notification or minimum retention times for specific data categories are not deeply elaborated.

---
# References

- [[bonatti2020a]]