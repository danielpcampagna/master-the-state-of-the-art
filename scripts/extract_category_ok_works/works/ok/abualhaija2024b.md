---
ID: abualhaija2024b
authors: Abualhaija, Sallam; Ceci, Marcello; Briand, Lionel C.; Zetzsche, Dirk; Bodellini, Marco
category: ok
display: abualhaija (AI-enabled Regulatory Change Analysis of Legal Requirements)
due: Proposes an AI-driven approach (MURCIA) to analyze regulatory changes affecting compliance requirements. The work is useful for identifying evolving compliance obligations but does not propose a data provenance model.
entrytype: conference paper
link: https://doi.org/10.34961/researchrepository-ul.28398224.v1
name: AI-enabled Regulatory Change Analysis of Legal Requirements
organization: IEEE
place: 2024 IEEE 32nd International Requirements Engineering Conference (RE), Reykjavik, Iceland
pp: 5-17
provenance_related: false
related:
  - regulatory compliance
  - requirements engineering
  - legal AI
  - GDPR compliance
  - large language models
  - legal requirements evolution
year: "2024"
forward_steps: 2
---

# Summary & Analysis

## Overview

This paper presents **MURCIA**, an AI-driven approach that assists analysts in identifying **regulatory changes** and assessing their **impact on compliance requirements**. It focuses on **how legal requirements evolve over time**, particularly in financial regulations, but the methodology is **generalizable to GDPR and other domains**. The authors define a **taxonomy of regulatory changes** and evaluate **MURCIA's ability to track textual, semantic, and legal interpretations of changes**. The AI model achieves an **F1 score of 90.8% for detecting changes in text meaning** and **83.7% for legal interpretation**.

## Background

Regulations **change frequently**, and ensuring software compliance at **time t₀ does not guarantee compliance at time t₁**. Compliance engineers must track changes and **adapt software accordingly**. The problem is that **manual regulatory change analysis is time-consuming and error-prone**. Missing a change can result in **non-compliant systems and legal fines**.

**Key Quotes:**

1. _“Understanding the implications of regulatory change on compliance of software requirements requires navigating hundreds of legal provisions.”_ (p. 1)
2. _“Missing a change may result in non-compliant software which can in turn lead to hefty fines.”_ (p. 1)

## Research Approach

The paper introduces **MURCIA (MUlti-layered Regulatory Change Identification and Analysis)**, which automates the detection of **regulatory changes** by leveraging **large language models (LLMs)**.

### **Regulatory Change Taxonomy**

The authors define a **taxonomy** for categorizing legal changes at **three levels**:

1. **Textual Level** (raw text changes)
    - Additions, deletions, modifications of words, sentences, or paragraphs.
2. **Semantic Level** (changes in meaning)
    - Changes in obligations, conditions, references, roles, and constraints.
3. **Deontic Level** (legal interpretation)
    - Changes in legal norms (e.g., obligations becoming permissions).

**Key Quotes:**

1. _“We propose a taxonomy that characterizes regulatory changes at different levels of abstraction: textual, semantic, and deontic.”_ (p. 3)
2. _“For example, a modification of a time constraint from ‘without undue delay’ to ‘within 15 working days’ impacts compliance timelines.”_ (p. 4)

### **MURCIA AI Model**

- **Inputs**: Two versions of a legal document (e.g., GDPR before and after an amendment).
- **Processing Steps**:
    1. **Identify textual changes** (text comparison).
    2. **Classify semantic changes** (meaning alterations).
    3. **Analyze legal interpretation impact** (norms and obligations).
    4. **Assess impact on compliance requirements**.
- **Technology**: Uses **ChatGPT, BERT, and NLP models** for detecting and classifying changes.

### **Evaluation & Results**

- Evaluated on **four financial regulations** with **25 revisions**.
- Achieves:
    - **90.5% F1 score** for textual change detection.
    - **90.8% F1 score** for semantic meaning changes.
    - **83.7% F1 score** for legal interpretation.

**Key Quotes:**

1. _“MURCIA can provide text meaning changes with an F1 score of 90.8% and legal interpretation with an F1 score of 83.7%.”_ (p. 7)
2. _“Our results indicate that AI models can effectively assist compliance experts in tracking regulatory changes.”_ (p. 9)

## Conclusion

MURCIA provides **an AI-based solution for monitoring regulatory changes**. It enables software engineers to **track compliance updates**, reducing **manual effort and legal risks**. However, the paper does **not propose a data provenance model** but focuses on **tracking changes in legal obligations**.

**Key Quotes:**

1. _“MURCIA supports compliance teams in identifying regulatory changes and assessing their impact.”_ (p. 12)
2. _“While our approach does not provide a compliance checker, it assists in tracking evolving compliance obligations.”_ (p. 13)

---

# Evaluation Based on Inclusion Criteria

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - **No**, the paper focuses on **regulatory change analysis**, not **provenance tracking**.
    - **Conclusion**: **Does not meet the provenance requirement**.
2. **Is the proposed model useful for answering compliance questions?**
    
    - **Yes**, MURCIA helps detect **evolving compliance requirements**.
    - **Relevant compliance questions**:
        - **CQ09** (Ensuring compliance of personal data processing)
        - **CQ39** (Third-party agreements and obligations)
        - **CQ56** (Regular review of plans and procedures)
    - **Conclusion**: **Useful for compliance tracking but not a full compliance model**.
3. **Is the proposed model publicly available?**
    
    - **Partially**. The **dataset and evaluation results** are shared, but MURCIA itself is not **open-source**.
    - **Conclusion**: **Limited availability**.
4. **Is the paper written in English or Portuguese?**
    
    - **Yes**, written in English.
    - **Conclusion**: **Meets requirement**.
5. **Is the paper publicly available?**
    
    - **Yes**, available via [University of Limerick Repository](https://doi.org/10.34961/researchrepository-ul.28398224.v1).
    - **Conclusion**: **Meets requirement**.
6. **Is the paper peer-reviewed?**
    
    - **Yes**, published in _2024 IEEE 32nd International Requirements Engineering Conference (RE)_.
    - **Conclusion**: **Meets requirement**.

**Overall Verdict**: The paper is **relevant for compliance tracking** but **does not present a data provenance model**. It offers an **AI-based approach for tracking regulatory changes**, which **can assist in compliance management but does not provide a structured GDPR provenance model**.

---

# Discussion on Compliance Questions

The paper indirectly addresses several **GDPR compliance questions** by tracking changes in legal obligations. Below is a discussion on relevant compliance questions:

1. **CQ09 (Ensuring compliance of data processing)**
    
    - **Relevance**: MURCIA tracks **changes in legal obligations**, ensuring organizations remain **compliant with evolving requirements**.
    - **Quote**: _“Tracking regulatory changes is necessary to ensure continued compliance of data processing operations.”_ (p. 10)
2. **CQ39 (Third-party agreements)**
    
    - **Relevance**: Changes in **data sharing agreements** can be tracked using MURCIA.
    - **Quote**: _“We evaluate MURCIA on four financial regulations to detect obligations that affect contracts and agreements.”_ (p. 8)
3. **CQ56 (Regular review of plans and procedures)**
    
    - **Relevance**: Regulatory changes may require **updating compliance frameworks**.
    - **Quote**: _“Our taxonomy categorizes legal changes to help compliance officers track necessary adaptations.”_ (p. 6)

Other compliance questions (e.g., **CQ08, CQ25**) are **not explicitly addressed**, as the focus is **tracking legal changes** rather than **structuring compliance models**.

---

# References

- [[torre2021a]]