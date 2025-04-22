---
ID: fang2024a
authors: Fang, Xianwen; Li, Mengyao
category: unrelated
display: "fang (Privacy-Preserving Process Mining: A Blockchain-Based Privacy-Aware Reversible Shared Image Approach)"
due: Proposes a blockchain-based privacy-aware process mining method that transforms process event logs into encrypted images. While privacy and security are key concerns, the paper does not explicitly present a data provenance model.
entrytype: article
link: https://doi.org/10.1080/08839514.2024.2321556
name: "Privacy-Preserving Process Mining: A Blockchain-Based Privacy-Aware Reversible Shared Image Approach"
organization: Taylor & Francis
place: Applied Artificial Intelligence
pp: 1–32
provenance_related: false
related:
  - privacy-preserving process mining
  - blockchain
  - chaotic encryption
  - supply chain process data
  - privacy-aware information sharing
year: "2024"
forward_steps: 2
---

# Summary & Analysis

## Overview

This paper presents a **blockchain-based, privacy-aware process mining approach** that enables **secure sharing of cross-organizational business process data**. The method employs **chaotic image encryption**, transforming **event logs** into **encrypted color images**, ensuring **privacy protection** while maintaining **process mining accuracy**. The system integrates **on-chain-off-chain storage** and **attribute-based encryption** to achieve **reversible privacy protection**.

## Background

With **cross-organizational process mining**, **privacy risks** arise from sharing event logs that contain **personal or confidential data**. While traditional **scrambling or anonymization methods** distort data, they also degrade **process mining quality**. The authors introduce **a privacy-preserving method** that balances **security and process mining precision**.

**Key Quotes:**

1. _“Scrambling mechanism or noise injection corrupts process information, lowering process mining outcomes.”_ (p. 1)
2. _“This research presents a blockchain-based privacy-aware reversible shared image approach using chaotic image encryption.”_ (p. 1)

## Research Approach

### **Privacy-Aware Process Mining**

- Converts **event logs into color images** using **chaotic encryption**.
- Enables **reversible privacy protection**, preventing **data disclosure, correlation attacks, and unauthorized sharing**.
- Uses **on-chain-off-chain architecture** to manage encrypted event data.
- Implements **attribute-based encryption**, restricting **data access by permissions**.

### **Steps of the Privacy Framework**

1. **Event log transformation into encrypted images**:
    
    - Encodes process data as **2D to 3D encrypted images**.
    - Uses **chaotic encryption** to scramble data while allowing **future reversibility**.
2. **Blockchain-based storage**:
    
    - Stores **unique identifiers** (encrypted image index) on **blockchain**.
    - Retains encrypted process data **off-chain** to reduce **blockchain overhead**.
3. **Reversible decryption**:
    
    - **Full decryption**: Allows regulators to recover **original event logs**.
    - **Attribute-based decryption**: Permits access **only to authorized attributes**, ensuring **privacy-aware data access**.

**Key Quotes:**

1. _“The proposed method enables privacy-aware business process sharing while preserving process mining accuracy.”_ (p. 5)
2. _“Chaotic encryption is applied to anonymize activities, resources, timestamps, and attributes.”_ (p. 12)

## Evaluation

### **Experimental Setup**

- **Datasets**: Uses **three public event logs** (Sepsis, Hospital, BPIC 2017) and **one synthetic dataset**.
- **Performance Metrics**:
    - **System throughput (TPS)**: The approach outperforms traditional methods by **57%**.
    - **Privacy preservation**: Uses **Earth Mover’s Distance (EMD)** to measure anonymization effectiveness.
    - **Utility retention**: Measures **fitness and precision** of **process mining results**.

### **Key Findings**

- The method **enhances privacy protection** while preserving **process discovery quality**.
- **Process mining accuracy** remains **high**, with minimal impact on **fitness and precision**.
- **Pearson correlation coefficient (0.994+)** confirms **minimal impact on process relationships**.

**Key Quotes:**

1. _“The system performance of the proposed method outperforms the baseline method by 57%.”_ (p. 20)
2. _“Privacy-aware process mining retains event log structure while preventing unauthorized access.”_ (p. 26)

## Conclusion

The proposed **blockchain-based privacy-aware process mining approach** secures **cross-organizational process data** while maintaining **process mining accuracy**. The **chaotic image encryption method** offers **reversible privacy protection**, allowing **fine-grained control over access permissions**. However, **it does not propose a formal data provenance model**.

**Key Quotes:**

1. _“The proposed method enhances cross-organizational privacy while ensuring high-quality process mining results.”_ (p. 28)
2. _“Reversible encryption ensures that data can be shared securely while complying with privacy regulations.”_ (p. 29)

---

# Evaluation Based on Inclusion Criteria

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - **No**, the paper focuses on **privacy-preserving process mining**, not **data provenance tracking**.
    - **Conclusion**: **Does not meet the provenance requirement**.
2. **Is the proposed model useful for answering compliance questions?**
    
    - **Partially**, as it **enhances privacy protection** in **cross-organizational process mining**.
    - **Relevant compliance questions**:
        - **CQ09** (Ensuring compliance of data processing)
        - **CQ29** (Data retention policies)
        - **CQ39** (Third-party agreements)
    - **Conclusion**: **Useful for privacy control but not a compliance model**.
3. **Is the proposed model publicly available?**
    
    - **No**, while the **paper describes the approach**, **no open-source implementation** is provided.
    - **Conclusion**: **Limited availability**.
4. **Is the paper written in English or Portuguese?**
    
    - **Yes**, written in English.
    - **Conclusion**: **Meets requirement**.
5. **Is the paper publicly available?**
    
    - **Yes**, available via [Taylor & Francis](https://doi.org/10.1080/08839514.2024.2321556).
    - **Conclusion**: **Meets requirement**.
6. **Is the paper peer-reviewed?**
    
    - **Yes**, published in _Applied Artificial Intelligence_ (Taylor & Francis).
    - **Conclusion**: **Meets requirement**.

**Overall Verdict**: The paper is **relevant for privacy-aware process mining** but **does not propose a data provenance model**. It offers a **secure framework for process sharing** but **does not explicitly model GDPR obligations**.

---

# Discussion on Compliance Questions

The paper indirectly addresses **GDPR compliance** by enabling **privacy-aware process sharing**. Below is a discussion on relevant compliance questions:

1. **CQ09 (Ensuring compliance of data processing)**
    
    - **Relevance**: The method **enhances privacy control** in process mining.
    - **Quote**: _“Chaotic encryption protects process event logs from unauthorized access.”_ (p. 12)
2. **CQ29 (Data retention policies)**
    
    - **Relevance**: The model **allows fine-grained access control** over stored process data.
    - **Quote**: _“On-chain-off-chain storage ensures that encrypted event logs remain secure while allowing authorized decryption.”_ (p. 15)
3. **CQ39 (Third-party agreements)**
    
    - **Relevance**: The framework **ensures privacy in cross-organizational business process sharing**.
    - **Quote**: _“The method secures the flow of cross-organizational information while maintaining privacy compliance.”_ (p. 28)

Other compliance questions (e.g., **CQ08, CQ25**) are **not explicitly addressed**, as the focus is **privacy protection**, not **compliance modeling**.

---

# References

- [[torre2021a]]