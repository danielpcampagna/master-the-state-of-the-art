---
ID: basile2023a
authors: Basile, Davide and Di Ciccio, Claudio and Goretti, Valerio and Kirrane, Sabrina
category: unrelated
display: basile (ReGov - Blockchain based resource governance)
due: The paper offers usage control with TEE, but does not specifically present a data provenance model for GDPR obligations.
entrytype: article
link: https://www.frontiersin.org/articles/10.3389/fbloc.2023.1141909/pdf
name: Blockchain based resource governance for decentralized web environments
organization: Frontiers Media
place: Frontiers in Blockchain
pp: 1-23
provenance_related: false
related:
  - Usage control
  - Blockchain
  - TEE
  - Decentralized web
year: 2023
forward_steps: 2
---

# Summary & Analysis

## Introduction / Context

The paper “Blockchain based resource governance for decentralized web environments” by Basile, Di Ciccio, Goretti, and Kirrane, published in Frontiers in Blockchain (May 2023), addresses how decentralization efforts (e.g., Solid, Digi.me, ActivityPub) can be improved by employing governance tools to regulate data usage and ensure policy compliance even after data is accessed (page 1). The authors argue that typical access control solutions do not always verify compliance with usage conditions once data leaves the original owner’s hands (page 1).

They propose a conceptual framework, **ReGov**, that allows usage control in decentralized web environments and demonstrate an implementation employing blockchain and trusted execution environments (TEE, specifically Intel SGX) (page 2). Their main contributions are:

1. A **conceptual usage governance framework** for decentralized contexts.
2. A **technical instantiation** (with code) that uses **blockchain smart contracts** to record and verify usage policies, plus **Intel SGX** to enforce usage control in consumers’ devices (pages 2–3).
3. An **evaluation** focusing on scenario-driven requirements (section 3.2) and the architecture’s security, privacy, and cost (section 6) (page 16).

### Key Points per Section

1. **Motivating Scenario and Requirements (Section 3)**
    
    - They present a data market scenario (named “DecentralTrading”) in which users (e.g., Bob) share resources (images), specifying usage constraints such as domain, geographic location, usage count, and time limit (pages 4–5).
    - Derived requirements revolve around ensuring usage control before and after data is accessed, providing transparency, preserving data immutability, and avoiding reliance on central services (pages 5–6).
    
    **Representative Quotes:**
    
    - “However, the vast majority of decentralized web initiatives [...] manage data access via simple access control mechanisms [...] that are not able to verify that usage conditions are adhered to after access has been granted” (page 1).
    - “Through blockchain technologies, we record policies expressing the usage conditions associated with resources and monitor their compliance” (page 1).
    - “Bob makes his images available only for applications belonging to the scientific domain [...] he sets a maximum number of 100 local accesses and an expiry date of 20 days” (page 5).
2. **Conceptual Resource Governance (ReGov) Framework (Section 4)**
    
    - Introduces the abstract architecture: each **Node** has **Data Provision** (sharing data), **Data Consumption** (retrieving data), and a **Governance Interface** that communicates with the “governance ecosystem.”
    - The “governance ecosystem” is conceptualized as multiple components: **Resource Indexing** (metadata about resources) and **Policy Governance** (storing policies, verifying compliance) (pages 6–9).
    - **Representative Quotes:**
        - “The ReGov framework extends these aspects by not only controlling data access but also supporting the continuous monitoring of compliance with usage policies” (page 6).
        - “Nodes facilitate communication with the Governance Ecosystem via the Governance Interface” (page 8).
        - “The data retrieval process [...] verifies that the request has been generated in the Isolated Environment of a Data Consumption technology” (page 9).
3. **Instantiation with Blockchain and TEE (Section 5)**
    
    - They provide a concrete prototype using **Intel SGX** for trust at the consumer side and **smart contracts** on an Ethereum Virtual Machine (EVM) network to store usage policies and audit logs (pages 10–16).
    - Four rule types are used: **temporal, access counter, domain, and geographic** (page 11).
    - The solution ensures that data (and usage logs) remain protected inside a TEE, and that policy compliance can be monitored via the blockchain (pages 14–16).
    - **Representative Quotes:**
        - “The code is openly available at the following address: [https://github.com/ValerioGoretti/UsageControl-DecentralTrading”](https://github.com/ValerioGoretti/UsageControl-DecentralTrading%E2%80%9D) (page 10).
        - “In our setting, Nodes store their private key in an encrypted format to increase confidentiality [...] employing the asymmetric encryption methodology that underlies the EVM Blockchain” (page 10).
        - “We leverage security guarantees offered by the Intel SGX Trusted Execution Environment [...] to implement a Trusted Application containing the logic for Data Consumption” (page 10).
4. **Evaluation (Section 6)**
    
    - They revisit the requirements from the motivating scenario (e.g., verifying usage constraints, guaranteeing tamper resistance, transparency, etc.) and map how these are met in their approach (page 16).
    - They then discuss **Security**, **Privacy**, and **Affordability** (gas costs for contract calls, encryption overhead) (pages 20–22).
    - **Representative Quotes:**
        - “Our solution involves the storage of resource metadata and usage policies in data structures that are part of smart contracts [...] we rely on the cryptographic structure underlying the blockchain to guarantee the integrity of published smart contracts” (page 17).
        - “Privacy is key for decentralized web environments [...] we leverage Intel SGX Trusted Execution Environment that manages retrieved resources through the SGX Protected File System” (page 21).
        - “The deployment cost of DTindexing is 32 55 000 Gas units. The registerPod method is the most expensive with 20 82 494 Gas units” (page 21).

# Evaluation Based on Inclusion Criteria

The paper is now evaluated against the stated inclusion/exclusion criteria:

1. **“The approach should strictly propose a data provenance model to represent activities information related to GDPR obligations.”**
    
    - The paper does propose a usage-control model for data governance with TEE + blockchain (pages 4–5). It does not specifically describe it as a “data provenance” model. Its focus is on usage control (verifying policy compliance, not necessarily capturing a detailed chain-of-custody or data transformations typically associated with provenance). The authors do store usage logs that can be audited (pages 5, 9, 14–16). However, it is **not** explicitly framed as a data provenance schema or model for capturing GDPR’s lineage or obligations. Instead, it is a usage policy enforcement framework.
    - **Quote (page 2):** “We subsequently demonstrate how our framework can be instantiated by combining blockchain and trusted execution environments [...] to facilitate usage control in decentralized web environments.”
2. **“The proposed model should be useful to address the compliance questions we have.”**
    
    - The authors mention compliance in a broader sense (including possible synergy with regulations such as GDPR), but the approach is not specialized to GDPR obligations. The solution addresses usage constraints like purpose, location, time, number of accesses. That overlaps partially with GDPR principles (e.g. data minimization, retention limits), yet the text does not articulate compliance specifically with standard GDPR articles or obligations.
    - They do not reference or address the set of compliance questions from the user’s list (e.g., CQ08, CQ09, etc.). The paper’s usage constraints (domain, location, time limit, usage count) might help with aspects of data retention (CQ29), but the link to each compliance question is not spelled out.
3. **“The proposed model should be publicly available.”**
    
    - The paper’s model and code are publicly available via GitHub, so it **is** openly accessible (page 10).
4. **“The document should be written in English or Portuguese.”**
    
    - The paper is published in English (page 1).
5. **“The document should be publicly available or at least accessible under digital libraries CAPES CAFE has signed.”**
    
    - It is an open-access publication under CC-BY license (page 1).
6. **“It should be a peer-reviewed document.”**
    
    - Yes, it is peer-reviewed and published in Frontiers in Blockchain (page 1).

**Conclusion Based on Criteria**

- The approach is a usage-control framework that partially addresses some aspects relevant to GDPR compliance (e.g., limiting data usage by time or domain). But it does **not** focus on a data-provenance structure for GDPR obligations specifically. Its overall contribution is about usage-control and compliance with usage policies, not a formal data provenance model or lineage representation for GDPR.

Hence, if we are **very** strict about requiring a “data provenance model explicitly addressing GDPR,” the paper does not strongly match. However, it does have partial overlap with compliance concerns (like record-keeping usage logs, restricting usage, etc.).

# Discussion on Compliance Questions

Below is a discussion of how, if at all, the proposed paper’s content (and the TEE-based approach) addresses each of the compliance questions enumerated. For each question (CQ08, CQ09, CQ11, etc.), we check if the paper’s model or approach is relevant:

1. **CQ08 (Retention period)**
    
    - The framework supports “temporal rule,” which can limit how long data is stored locally (page 11). This partially addresses CQ08, as it ensures data is stored no longer than a user-defined timeframe.
    - **Quote (page 5):** “Bob sets a maximum number of 100 local accesses and an expiry date of 20 days.”
2. **CQ09 (Actions required to ensure compliance, e.g. deletion)**
    
    - The paper’s usage rules can automatically cause data to be erased at TEE-level enforcement (page 11). This is partially relevant to ensuring data is not kept longer than necessary.
    - **Quote (page 11):** “Once the term expires, the rule stipulates that the resource must be deleted.”
3. **CQ11 (Re-seeking consent)**
    
    - The paper does not mention re-seeking consent. So, no direct coverage.
4. **CQ17 (Respond to SARs in one month)**
    
    - No mention in the paper. The usage logs might help with transparency, but no explicit mention of the timescale to handle SARs.
5. **CQ20 (Halt processing upon restriction request)**
    
    - The paper does not discuss halting processing per user request, beyond the usage rules set by the resource owner. So, no direct coverage.
6. **CQ21 (Right to object to direct marketing)**
    
    - The paper’s domain rule could conceptually block certain domain uses. This might tangentially address marketing vs. research domains. However, not specifically discussed.
7. **CQ25 (Documenting lawful restrictions)**
    
    - The approach records usage policies. Possibly you could document lawful restrictions as usage rules. The paper does not mention.
8. **CQ28 (Ensuring data accuracy and updates)**
    
    - The authors do not mention any correctness or update procedures.
9. **CQ29 (Retention policies)**
    
    - Again, the temporal rule directly addresses retention at a device level, so partial coverage.
    - **Quote (page 11):** “Once the term expires, the resource must be deleted.”
10. **CQ30 (Minimum retention periods)**
    
    - The paper’s approach includes an expiry date but not a minimum retention time. No mention.
11. **CQ32 (No unnecessary duplication)**
    
    - The TEE approach tries to avoid data duplication by restricting usage; if an application is not in the correct domain, it cannot be opened (pages 11–12). Not a direct statement about duplication, but partial synergy.
12. **CQ33 (Concise, transparent notice)**
    
    - The system ensures a certain measure of transparency, but does not mention user-facing notice.
13. **CQ35 (Keeping data up to date)**
    
    - Not discussed.
14. **CQ37, CQ38 (Proactively inform individuals of GDPR rights)**
    
    - No direct mention in the paper.
15. **CQ39 (Review agreements with third-party processors)**
    
    - The paper provides a decentralized environment, but does not mention third-party agreements.
16. **CQ40, CQ41, CQ42, CQ43, CQ44 (DPO appointment)**
    
    - No mention of a data protection officer.
17. **CQ47, CQ48, CQ49 (Documented security program, complaint resolution, designated individual)**
    
    - The authors present a TEE-based approach, but not from the vantage of an organizational security program.
18. **CQ50 (Encryption)**
    
    - They do mention encryption in TEE contexts, plus usage logs in a secure environment. So partially yes for the data security dimension.
    - **Quote (page 21):** “One of the key features of SGX-PFS is that it allows for files to be stored in a secure, encrypted format, even when the operating system is not running.”
19. **CQ51 (Systematic destruction when no longer required)**
    
    - The usage policy approach triggers local deletion after time or usage count. This addresses part of CQ51.
20. **CQ52 (Timely restore)**
    
    - No mention of restore processes.
21. **CQ56 (Regularly review plans/procedures)**
    
    - Not addressed.
22. **CQ57, CQ58 (Breach documentation, cooperation)**
    
    - Not explicitly covered.
23. **CQ63, CQ64, CQ65 (International data transfers)**
    
    - They do mention geographic constraints to usage, but not specifically about international transfers or standard contractual clauses.

**Overall**: The approach partially addresses retention-related and usage-limitation aspects (e.g., the temporal rule) and might indirectly help with some GDPR obligations (e.g., data minimization by restricting usage). But it does **not** systematically or explicitly address the wide scope of the compliance questions.


---

# References

- [[bonatti2020a]]