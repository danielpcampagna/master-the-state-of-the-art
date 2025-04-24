---
ID: okonicha2025a
authors: Okonicha, Ozioma N. and Sadovykh, Andrey
category: unrelated
display: okonicha (NLP-based automated compliance checking of data processing agreements)
due: This paper focuses on NLP-based classification of compliance with GDPR Article 5; it does not propose a data provenance model nor addresses the entire set of compliance questions.
entrytype: article
link: 
name: NLP-based automated compliance checking of data processing agreements against General Data Protection Regulation
organization: Innopolis University
place: Computer Research and Modeling (Special Issue)
pp: 1667-1685
provenance_related: false
related:
  - NLP
  - GDPR compliance
  - Privacy policy classification
  - SBERT
  - BERT
  - GPT2
  - Data Minimization
  - Storage Limitation
year: 2025
forward_steps: 2
---

# Summary & Analysis

## Introduction & Context

This paper investigates how Natural Language Processing (NLP) techniques can automate checks for compliance with the General Data Protection Regulation (**GDPR**), particularly focusing on **data processing agreements** and **privacy policies**. The authors highlight how manual compliance verification is time-consuming and error-prone due to legal documents’ complexity and evolving regulations. NLP-based methods, they argue, can streamline the process by analyzing textual clauses in data-processing agreements, identifying compliance gaps, and continuously adapting to changes in GDPR requirements.

**Key Points**

1. **Motivation**: Organizations struggle to maintain GDPR compliance because data-protection legislation is dynamic and privacy policies are lengthy and complex.
2. **Data Sources**: Two corpora are used: OPP-115 (labeled website privacy policies) and ACL Coling (unlabeled but large privacy-policy corpus).
3. **NLP Methods**: The authors train and compare multiple state-of-the-art language models (e.g., **SBERT**, **BERT**, **GPT2**) in multi-label classification tasks that map policy text to GDPR “Article 5” compliance principles. They do so at both the sentence level and the entire policy level.
4. **Mapping Approach**: They unify OPP-115’s existing categories with GDPR principles like Storage Limitation, Data Minimization, etc.
5. **Results**:
    - **Sentence-level**: BERT yields the highest accuracy (~0.63) and an F1-score of ~0.55, while GPT2 has slightly lower accuracy/f1. SBERT is moderate at sentence-level.
    - **Policy-level**: SBERT shows better performance (Accuracy = 0.57, F1 = 0.80), presumably due to capturing the overall text’s semantic similarity.
    - The authors note large class imbalance (e.g., the Accountability principle was rarely found).
6. **Discussion**:
    - They highlight the difficulty of text segmentation (token limits for BERT or GPT2), ensuring coverage of all GDPR principles, and the cost of model inference.
    - They see potential for real-time compliance monitoring pipelines and extension to other regulations.

---

## Evaluation Against Inclusion Criteria

We assess whether this paper meets the user’s stated criteria for inclusion (i.e., does it “strictly propose a data provenance model,” etc.). The criteria are enumerated below with the assessment:

1. **Strictly propose a data provenance model to represent activities for GDPR obligations?**
    
    - **No**. The paper focuses on NLP-based classification of text for compliance. It does not formalize or present a _data provenance_ or lineage model.
    - **Reference**: “In this research, the focus was on using NLP to automate compliance checking for the GDPR.” [p. 1680]
2. **Should be useful to address the compliance questions we have?**
    
    - The paper addresses how to detect potential compliance / noncompliance with GDPR Article 5. Although it might help detect certain issues around data minimization or storage limitation, it does _not_ systematically address the user’s entire set of compliance questions (like retention times, DPO appointment, data subject rights, etc.).
    - **Reference**: Emphasizes classification for the seven GDPR principles in Art. 5, but does not mention data subject requests (CQ17, etc.) [p. 1672–1673].
3. **Proposed model publicly available?**
    
    - The authors do not mention releasing a stable reference model or complete codebase, though they rely on standard pre-trained models (SBERT/BERT).
    - **Reference**: “The models were then saved [...] tested on unlabeled policies [...] to assess generalizability and performance.” [p. 1671]
4. **Document in English or Portuguese?**
    
    - The paper is in English (with a Russian translation embedded, but the main text is in English).
5. **Publicly accessible in digital libraries?**
    
    - This is from a 2025 volume of “Computer Research and Modeling,” presumably accessible via institutional subscription or open access.
6. **Peer-reviewed?**
    
    - The journal “Computer Research and Modeling” typically is peer-reviewed, so presumably yes.

**Conclusion**  
It does not propose a data provenance model. It is in English, peer-reviewed, and about GDPR, but doesn’t meet the user’s “strict data provenance model” requirement. Therefore it is **unrelated** for the user’s strict inclusion scope.

---

## Discussion on Compliance Questions

The user’s compliance questions (CQ08–CQ65) revolve around data retention, user rights, DPO, etc. This paper addresses _some_ aspects of compliance (the authors focus on Article 5 compliance principles, e.g., data minimization, storage limitation) but not specific answers to the user’s enumerated questions. It does not systematically handle queries like “Are there controls to halt processing upon data-subject objection (CQ20)?” or “Is your business subject to retention periods (CQ30)?” The paper’s multi-label classification is broad and theoretical, with no direct mention of the user’s “compliance questions.”

---

# References

- [[bonatti2020a]]