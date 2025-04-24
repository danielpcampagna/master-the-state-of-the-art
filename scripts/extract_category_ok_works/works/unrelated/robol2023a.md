---
ID: robol2023a
authors: Robol, Marco; Breaux, Travis D; Paja, Elda; Giorgini, Paolo
category: unrelated
display: robol (Consent Verification Monitoring)
due: This paper focuses on modeling and verifying user consent evolution but does not propose a data provenance model aimed at GDPR obligations.
entrytype: article
link: https://doi.org/10.1145/3490754
name: Consent Verification Monitoring
organization: ACM
place: ACM Transactions on Software Engineering and Methodology (TOSEM)
pp: Article 2, 33 pages
provenance_related: false
related: 
year: 2023
forward_steps: 2
---

# Summary & Analysis

## Summary

“Consent Verification Monitoring” (ACM TOSEM 2023) by Robol, Breaux, Paja, and Giorgini discusses an approach for formally modeling and verifying user consent for personal data collection and use in dynamic systems subject to evolving privacy policies. The authors note that modern services frequently update their data practices and that data subjects must be able to grant and withdraw consent in ways that can affect both future and previously collected data. The GDPR formalizes these obligations but does not prescribe a specific representation. The paper therefore proposes a **Description Logic** (DL) framework to capture:

1. **Consent grant and withdrawal** events (both retroactive and non-retroactive),
2. **Data categories** (e.g., location, purchase data),
3. **Purposes/recipients** (e.g., advertiser, analytics) modeled as roles,
4. **Collection and access** events,
5. **Temporal intervals** expressed as forward time steps.

The framework shows how changing data policies can be captured in a monotonic knowledge base (i.e., only growing facts) while verifying whether each data collection or access remains valid under the user’s evolving consent. The paper also addresses potentially overlapping consents and the complexity of hierarchical data type classification. A test simulation demonstrates that the approach scales for daily or weekly checks, though advanced optimizations may be needed for very large numbers of data subjects or more frequent policy changes.

## Key Points

1. **Consent Evolution**  
    The authors formalize six possible “windows” of consent derived from whether a user’s grant or withdrawal is retroactive or non-retroactive. For example, a withdrawal can apply only to future data collections or also disallow access to previously collected data.
    
2. **Description Logic**  
    They encode data categories, recipients, and temporal intervals in DL, building an ontology that includes “Collection,” “Access,” “Time,” and “Consent” concepts. Each new event (e.g., user grants or revokes consent, user collects or accesses data) adds a new assertion in the knowledge base.
    
3. **Policy Updates**  
    The authors illustrate five typical use cases for policy evolution (e.g., refining data categories, overlapping authorizations, or adding new data purposes). They show how to maintain correctness — ensuring data is still used only in ways permitted by consent — despite changes to classification hierarchies.
    
4. **Scalability**  
    A simulation measuring performance under daily “consent checks” and occasional new data types or roles found the approach could still respond in a few seconds to each check for one data subject. The authors note real implementations can batch queries or adjust policy updates to reduce overhead.
    
5. **Limitations & Future Work**
    
    - The work focuses on the limited scope of “collection” and “access” for verifying consent evolution; for example, it does not track data erasure or “right to be forgotten,” though it notes these are related features.
    - The technique is general but must be integrated with existing systems’ logs or extended for more complex actions such as sharing data with third-party applications.
    - Potential expansions include bridging with provenance approaches or role-based access control to handle multi-party scenarios.

## Evaluation Against Inclusion Criteria

- **Strict data provenance model for GDPR?**  
    No. The paper primarily models user consent for data collection and access using Description Logic; it does not define or adopt a data provenance model for representing GDPR-relevant activities. The coverage is about “who collected what data when,” but its purpose is verifying consent, not lineage/provenance in detail.
    
- **Usefulness for answering specific GDPR compliance questions (CQ08–CQ65)?**  
    While it helps handle “consent” requirements in an evolving policy environment, it does not directly address typical compliance questions on data retention, restrictions, or data subject request timeframes. Instead, it focuses on the narrower aspect of verifying changing user consent.
    
- **Public availability of proposed model?**  
    The authors provide a formal approach and code for verification but not a comprehensive “data provenance model.”
    
- **Document language**  
    The paper is in English.
    
- **Peer-reviewed**  
    Published in ACM TOSEM, indicating peer review.
    

Hence, while the paper is academically valuable, it does not meet the strict “data provenance model” requirement for GDPR obligations.

## Discussion on Compliance Questions

Because the authors concentrate on user consent formalization (granting, withdrawal, retroactive vs. non-retroactive) and verifying compliance with that consent, they do not explicitly address the enumerated GDPR compliance questions (e.g., data retention periods, access rights within one month, etc.). The framework does not systematically show whether it addresses or answers those questions, focusing instead on consent-based authorization windows.

## Conclusion

Robol et al.’s work on “Consent Verification Monitoring” offers a robust formal method for encoding and verifying changes in user consent within dynamic, evolving data policies. It demonstrates a specialized description logic approach for capturing time intervals, collection events, and overlapping consents while ensuring monotonic updates and compliance checks. However, it does **not** propose a complete data provenance model nor systematically address the broader set of GDPR compliance questions. Consequently, for the current inclusion criteria, this paper is deemed **unrelated**.

---

# References

- [[bonatti2020a]]