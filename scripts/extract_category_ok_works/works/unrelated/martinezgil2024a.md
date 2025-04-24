---
ID: martinezgil2024a
authors: Martinez-Gil, Jorge
category: unrelated
display: martinezgil (Framework to Automatically Determine the Quality of Open Data Catalogs)
due: Proposes a framework for assessing the quality of Open Data Catalogs, considering provenance as a key non-core quality dimension. However, it does not provide a structured data provenance model.
entrytype: article
link: https://arxiv.org/abs/2307.15464v7
name: Framework to Automatically Determine the Quality of Open Data Catalogs
organization: arXiv
place: ""
pp: 1-20
provenance_related: true
related:
  - data catalog quality
  - metadata management
  - provenance assessment
  - data governance
year: "2024"
forward_steps: 2
---

# Summary & Analysis

## Overview

This paper presents **a framework for automatically assessing the quality of Open Data Catalogs (ODCs)**. The framework evaluates **core**, **cross-catalog**, and **non-core** quality dimensions to determine the reliability and usability of ODCs. It specifically includes **provenance** as a **non-core quality dimension**, analyzing how well an ODC documents the lineage and historical context of cataloged datasets. However, **it does not introduce a structured data provenance model**.

## Background

ODCs are essential for **data discovery, understanding, and governance**, but ensuring their **quality and reliability** remains challenging. The study highlights common issues in ODCs:

- **Inaccuracy** (incorrect metadata)
- **Incompleteness** (missing attributes)
- **Inconsistency** (contradictory relationships)
- **Lack of provenance information** (unclear data lineage)

To address these issues, the paper proposes a **multi-dimensional framework** that quantifies ODC quality through **automated assessment methods**.

**Key Quotes:**

1. _“Ensuring the quality of Open Data Catalogs (ODCs) is a complex challenge that requires systematic evaluation across multiple dimensions, including provenance.”_ (p. 2)
2. _“The presence of provenance information in an ODC enhances credibility and supports quality assessment.”_ (p. 12)

## Research Approach

The proposed framework evaluates ODC quality along three main dimensions:

### **Core Quality Dimensions**

1. **Accuracy** – Correctness of metadata descriptions.
2. **Completeness** – Coverage of essential metadata attributes.
3. **Consistency** – Logical coherence of relationships.
4. **Scalability** – Ability to handle growing data volumes.
5. **Timeliness** – Up-to-date status of metadata.

### **Cross-Catalog Quality Dimensions**

1. **Compatibility** – Ability to integrate with other ODCs.
2. **Similarity** – Degree of metadata similarity between ODCs.

### **Non-Core Quality Dimensions (Including Provenance)**

1. **Provenance** – Documentation of dataset lineage and transformation history.
2. **Readability** – Ease of understanding metadata descriptions.
3. **Licensing** – Clarity of data usage restrictions.

**Key Quotes:**

1. _“Our framework includes provenance as a critical dimension, assessing whether an ODC provides clear lineage and historical context.”_ (p. 14)
2. _“We define a provenance score that quantifies the availability of metadata tracing data sources, transformations, and ownership.”_ (p. 15)

## Evaluation

The framework is tested on **four public ODCs** from the **European Union Open Data Portal**. The results show:

- High accuracy (82%-94%)
- Provenance scores of **0% across all ODCs**, indicating **a significant gap in metadata lineage documentation**.
- Correlation between **metadata completeness and provenance availability**.

**Key Quotes:**

1. _“Despite their importance, provenance scores remain at 0% across all tested ODCs, highlighting a critical weakness in metadata quality.”_ (p. 18)
2. _“Our findings suggest that provenance metadata is rarely documented, despite being crucial for assessing data reliability.”_ (p. 19)

## Conclusion

The framework provides **a systematic method for assessing ODC quality**, emphasizing **provenance as a key dimension**. However, **it does not propose a formal data provenance model**, focusing instead on evaluating existing metadata.

**Key Quotes:**

1. _“By incorporating provenance assessment, we enhance metadata quality evaluation and support trust in open data ecosystems.”_ (p. 20)
2. _“Future work should explore how provenance metadata can be systematically integrated into ODCs.”_ (p. 20)

---

# Evaluation Based on Inclusion Criteria

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - **No**, it evaluates **provenance metadata quality** but does **not introduce a structured provenance model**.
    - **Conclusion**: **Does not meet the provenance requirement**.
2. **Is the proposed model useful for answering compliance questions?**
    
    - **Partially**, as it **assesses provenance availability**, which relates to:
        - **CQ09** (Ensuring compliance of data processing)
        - **CQ51** (Ensuring systematic data erasure)
    - **Conclusion**: **Supports provenance assessment but does not structure compliance models**.
3. **Is the proposed model publicly available?**
    
    - **Yes**, available at [GitHub](https://www.github.com/jorge-martinez-gil/dataq).
    - **Conclusion**: **Meets requirement**.
4. **Is the paper written in English or Portuguese?**
    
    - **Yes**, written in English.
    - **Conclusion**: **Meets requirement**.
5. **Is the paper publicly available?**
    
    - **Yes**, hosted on [arXiv](https://arxiv.org/abs/2307.15464v7).
    - **Conclusion**: **Meets requirement**.
6. **Is the paper peer-reviewed?**
    
    - **No**, it is a **preprint on arXiv**, not yet peer-reviewed.
    - **Conclusion**: **Fails peer-review requirement**.

**Overall Verdict**: The paper is **relevant for provenance metadata assessment** but **does not introduce a structured provenance model**. It provides **a framework for evaluating ODC quality**, including **provenance documentation gaps**.

---

# Discussion on Compliance Questions

The paper **assesses provenance metadata** but does not **model compliance obligations**. Below is a discussion of relevant compliance questions:

1. **CQ09 (Ensuring GDPR-compliant processing)**
    
    - **Relevance**: The framework **identifies gaps in metadata provenance**, impacting compliance.
    - **Quote**: _“Our findings show that most ODCs lack documented provenance information, making compliance verification challenging.”_ (p. 19)
2. **CQ51 (Ensuring systematic data erasure)**
    
    - **Relevance**: Provenance metadata helps **trace data lifecycles**, supporting **deletion policies**.
    - **Quote**: _“An ODC with strong provenance metadata can facilitate data erasure tracking.”_ (p. 14)

Other compliance questions (e.g., **CQ08, CQ39**) are **not explicitly addressed**, as the focus is **metadata quality assessment** rather than **compliance modeling**.

---

# References

- [[ryan2021a]]