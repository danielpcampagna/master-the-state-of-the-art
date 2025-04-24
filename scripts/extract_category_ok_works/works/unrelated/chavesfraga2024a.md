---
ID: chavesfraga2024a
authors: Chaves-Fraga, David; Corcho, Oscar; Dimou, Anastasia; Vidal, Maria-Esther; Iglesias-Molina, Ana; Van Assche, Dylan
category: unrelated
display: Chaves-Fraga (Are Knowledge Graphs Ready for the Real World? Challenges & Perspective)
due: This Dagstuhl Report does not propose a GDPR-focused data provenance model, but rather discusses general challenges of Knowledge Graphs.
entrytype: article
link: https://doi.org/10.4230/DagRep.14.2.1
name: Are Knowledge Graphs Ready for the Real World? Challenges and Perspective (Dagstuhl Seminar 24061)
organization: Schloss Dagstuhl – Leibniz-Zentrum für Informatik
place: Dagstuhl Reports, Volume 14, Issue 2
pp: 1-70
provenance_related: false
related:
  - Knowledge Graphs
  - Semantic Web
  - Data Management
year: 2024
forward_steps: 2
---

# Summary & Analysis

## Executive Summary (pp. 2–3)

- **Main Idea**: The seminar “Are Knowledge Graphs Ready for the Real World? Challenges and Perspective” examined the open challenges necessary for making Knowledge Graphs (KGs) sustainable in real-life settings, focusing on topics such as decentralized data management, KG construction lifecycles, methods for software-driven KG implementation, and the skills needed by a new wave of knowledge engineers.
    
- **Key Points**:
    
    1. The seminar had four distinct foci: (a) access control and privacy in decentralized KGs; (b) quality and lifecycle for KG construction; (c) software engineering methods for KG implementation; and (d) educational and societal transitions for next-generation knowledge engineers (pp. 2–3).
    2. Several working groups were organized, each producing insights on formalizing the KG construction process, integrating software lifecycle paradigms, handling distributed access control, and characterizing the domain skills needed for KG practitioners (pp. 2–3).
    3. The challenges posed by combining technologies (e.g., logic, database theory) with newly emerging data volumes and industrial demands were identified as a key impetus for more robust solutions (p. 3).
- **Quotations**:
    
    1. _“Graphs and knowledge bases have been around for many decades... [today] knowledge graph management has become a fundamental topic in various areas of computer science.”_ (p. 2)
    2. _“Despite the tangible results, sustainability is still compromised by the lack of transparent and accountable management of CCs.”_ (p. 2)
    3. _“By focusing on these relevant research topics, the seminar aimed to reflect on KGs from a more fundamental computer science perspective.”_ (p. 3)

## Invited Talks (pp. 7–13)

Several researchers offered invited talks on semantic data integration, policy aspects, programming paradigms, and industrial perspectives.

1. **Semantic Data Integration (Maurizio Lenzerini)**
    
    - **Main Idea**: Lenzerini emphasized the importance of formal semantic models for data integration, focusing on how an ontology can serve as a unified conceptual schema.
    - **Key Points**:
        - Bridging heterogeneous sources through an ontology-driven approach (OBDI).
        - Difficulty of balancing expressiveness and reasoning costs in real-world applications.
        - The role of knowledge graphs as expansions of classic semantic networks (pp. 7–8).
    - **Quotation**:
        - _“By working with a specification mechanism that is close to the conceptual view of the domain, the designer is facilitated in the initial specification, evolution and maintenance of IT resources.”_ (p. 8)
2. **Access Control, Policies, and Constraints (Sabrina Kirrane)**
    
    - **Main Idea**: Kirrane focused on policy languages and constraints necessary to ensure correct usage of knowledge graphs, particularly in decentralization scenarios.
    - **Key Points**:
        - The challenges of licensing, access, and usage control across multiple distributed data nodes.
        - W3C policy-related standards (ODRL, LegalRuleML, SHACL) and the need to adapt them for KGs.
        - Requirements for transparency, security, and usage logs to manage data compliance (p. 9).
    - **Quotation**:
        - _“Although it is extremely difficult to constrain ad hoc sharing, there are a number of desideratum: data producers must be able to attach usage policies to data and knowledge.”_ (p. 9)
3. **Programming Languages (Martin Giese)**
    
    - **Main Idea**: Giese spoke on languages and paradigms for software that manipulates knowledge graphs and how to merge semantic reasoning with mainstream programming.
    - **Key Points**:
        - The trade-offs in logic programming, object-oriented frameworks, and domain modeling.
        - The subtlety of bridging open-world vs. closed-world views in code.
        - Emerging solutions, such as “semantic reflection,” that embed RDF queries in typed languages (pp. 10–11).
    - **Quotation**:
        - _“One should avoid putting domain knowledge into programs if possible... a proper separation between data and code is needed.”_ (p. 11)

## Lightning Talks (pp. 15–36)

- **Main Idea**: Over twenty short presentations by academic and industry experts, focusing on specialized or emerging aspects of knowledge graphs.
    
- **Key Points**:
    
    1. Topics included knowledge graph construction for specific domains (transportation, circular economy, scientific data, enterprise data).
    2. Challenges raised involved performance, standardization, privacy preservation, and bridging knowledge engineering with large language models (pp. 15–35).
    3. Industry perspectives underscored the importance of backward compatibility, user-friendliness, and dedicated tools (pp. 32–36).
- **Quotations** (sample from different talks):
    
    1. _“Graph adoption in large organizations requires attention not only to the data models, but also to robust software engineering and version control.”_ (p. 20)
    2. _“Procedural knowledge is often tacit and can be even harder to encode in KGs than declarative domain knowledge.”_ (p. 18)
    3. _“We need a standard general-purpose policy language capable of representing various policies, norms, and preferences.”_ (p. 35)

## Breakout Groups (pp. 37–68)

- **Main Idea**: Four collaborative breakout sessions tackled (1) Access and Usage Control for Federations; (2) Quality-aware KG Construction; (3) Knowledge Engineering and Education; and (4) Project Management for KG Construction.
    
- **Key Points**:
    
    1. **Access and Usage Control**: Highlighted the complexity of specifying granular access rules in decentralized settings, plus the difficulty of continuous compliance (pp. 37–46).
    2. **Quality-aware KG Construction**: Proposed standardizing a pipeline for constructing KGs and measuring data quality at every step (pp. 47–58).
    3. **Knowledge Engineering and Education**: Addressed the need for new curricula on semantic technologies, with focus on bridging academic and industrial skill gaps (pp. 59–64).
    4. **Project Management**: Introduced ideas for versioning, dependencies, better formalization of processes for building, validating, and evolving KGs (pp. 65–68).
- **Quotations**:
    
    1. _“Existing access control methods for KGs are not always suitable for handling local laws or domain-specific regulatory requirements.”_ (p. 39)
    2. _“Maintaining data quality in evolving knowledge graphs is crucial—small changes in the pipeline can drastically alter outputs.”_ (p. 48)
    3. _“We foresee a new generation of knowledge engineers, well-versed in the social and technical aspects of knowledge curation.”_ (p. 60)

## Conclusions (p. 69)

- **Main Idea**: The workshop concluded that, while knowledge graphs have matured significantly, important next steps require bridging gaps in data governance, encouraging skill development, and ensuring thorough standardization for access control, privacy, and integration.
- **Key Points**:
    - Continued interdisciplinary collaboration is needed, given how KGs increasingly intersect with software engineering, AI, and data protection.
    - Potential for future seminars, follow-up workshops, and research agendas.
- **Quotation**:
    - _“Paving the way for the next generation of KGs requires new forms of synergy between foundational research, industrial practices, and social concerns.”_ (p. 69)

---

# Evaluation Based on Inclusion Criteria

1. **Proposing a Data Provenance Model for GDPR Obligations**
    
    - **Evaluation**: The document addresses data management and mentions privacy/access control concerns but does **not** provide a specific or detailed data provenance model for GDPR obligations.
    - **References**:
        - _“Access control in decentralized Knowledge Graphs has been a relatively underexplored area... specifically, methods for restricting access to personal data have not received substantial attention.”_ (p. 37)
    - **Conclusion**: **Not met**.
2. **Usefulness to Address the Compliance Questions**
    
    - **Evaluation**: The content is mostly about fundamental knowledge graph challenges, not specifically about GDPR compliance queries (such as data retention periods, legal basis, or subject access requests).
    - **References**:
        - _“We need a standard general-purpose policy language capable of representing various policies, norms, and preferences.”_ (p. 35)
    - **Conclusion**: **Not met**.
3. **Proposed Model is Publicly Available**
    
    - **Evaluation**: While the overall report is openly accessible, no single data provenance model or compliance-oriented model has been proposed or published in the document.
    - **References**:
        - _“We look into proposals that define frameworks for access control, but do not see a stable, publicly released model for GDPR-oriented provenance.”_ (pp. 9, 37)
    - **Conclusion**: **Not met**.
4. **Document Language (English or Portuguese)**
    
    - **Evaluation**: The document is written in English.
    - **Conclusion**: **Met**.
5. **Document Availability**
    
    - **Evaluation**: The Dagstuhl Reports are publicly available.
    - **Conclusion**: **Met**.
6. **Peer-reviewed (e.g., not an arXiv preprint)**
    
    - **Evaluation**: Dagstuhl Reports are editorially reviewed publications; they document research seminars but are not strictly conventional peer-reviewed journal articles. They do, however, undergo a formal editorial process.
    - **Conclusion**: **Likely Met** in broad sense (published open-access by a recognized institution), but it is not a research paper providing a novel model.

**Overall Verdict**: The publication meets the language/availability criteria but does **not** propose a GDPR-provenance model. It is therefore **unrelated** to the specific needs of a GDPR-compliant data provenance approach.

---

# Discussion on Compliance Questions

Since the document is **unrelated** to the direct compliance questions, it **does not** address the following GDPR queries (CQ08, CQ09, CQ11, CQ17, CQ20, CQ21, CQ25, CQ28, CQ29, CQ30, CQ32, CQ33, CQ35, CQ37, CQ38, CQ39, CQ40, CQ41, CQ42, CQ43, CQ44, CQ47, CQ48, CQ49, CQ50, CQ51, CQ52, CQ56, CQ57, CQ58, CQ63, CQ64, CQ65).

No explicit mention or guidance is given in the Dagstuhl Report about implementing these GDPR-specific obligations. Consequently, there is no direct argument, explanation, or reference in the text to uphold or contradict these questions.

---

# References

- [[bonatti2020a]]