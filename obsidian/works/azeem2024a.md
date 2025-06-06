---
ID: azeem2024a
authors: Azeem, Muhammad Ilyas; Abualhaija, Sallam
category: unrelated
display: azeem (AI-enabled Completeness Checking of DPAs for GDPR Compliance)
due: The paper proposes an AI-based solution for verifying the completeness of Data Processing Agreements (DPAs) against GDPR, making it relevant for data provenance modeling. Since it does not introduce or extend previous semantic model in the literature, it does not match with our incluision criterias.
entrytype: article
link: https://doi.org/10.1007/s10664-024-10491-3
name: A Multi-solution Study on GDPR AI-enabled Completeness Checking of DPAs
organization: Springer
place: Empirical Software Engineering
pp: "96"
provenance_related: true
related:
  - GDPR Compliance
  - Data Processing Agreements (DPAs)
  - Artificial Intelligence
  - Natural Language Processing
  - Machine Learning
  - Regulatory Compliance
year: 2024
forward_steps: 2
---

# **Summary & Analysis**

## **Summary**

The paper **"A Multi-solution Study on GDPR AI-enabled Completeness Checking of DPAs"** by **Muhammad Ilyas Azeem and Sallam Abualhaija (2024)** presents an **AI-based approach to assess the completeness of Data Processing Agreements (DPAs) against GDPR provisions**. The study leverages **machine learning (ML), deep learning (DL), large language models (LLMs), and few-shot learning (FSL)** to automate the analysis process, helping **requirements engineers ensure that DPAs comply with GDPR**.

### **Key Contributions**

1. **Definition of completeness checking as a text classification problem**
    
    - Analyzes whether DPAs contain all **mandatory provisions required by GDPR**.
    - Uses a combination of **binary and multi-class classification** to detect missing compliance elements.
2. **Development of 10 AI-driven completeness-checking solutions**
    
    - Evaluates different AI models, including **BERT, RoBERTa, ALBERT, Legal-BERT, BiLSTM, logistic regression (LR), random forest (RF), support vector machines (SVM), multilayer perceptron (MLP), and SetFit (FSL)**.
    - **Fine-tunes these models for legal text processing**, assessing **performance on 169 real DPAs**.
3. **Empirical evaluation of AI models for GDPR compliance**
    
    - Analyzes **F2 scores** for completeness verification, favoring **recall over precision** to **minimize missing compliance violations**.
    - Best-performing models: **BERT (F2 = 86.7%) and RoBERTa (F2 = 89.7%)**.
4. **Dataset of DPAs for regulatory compliance research**
    
    - Compiles a dataset of **169 real-world DPAs**.
    - Ensures **legal expert validation of annotations** to improve AI model reliability.
5. **Analysis of data scarcity and model robustness**
    
    - Studies how **few-shot learning (FSL) can compensate for small datasets** in compliance analysis.
    - **SetFit FSL approach** shows promising results, requiring only **30% of the training data**.

### **Key Findings**

- **BERT and RoBERTa outperform traditional ML models**, achieving **high accuracy and recall** in completeness verification.
- **Few-shot learning (FSL) approaches like SetFit are effective** when training data is scarce.
- **Handling data imbalance is critical**: **Random oversampling (RO) for binary classification and random undersampling (RU) for multi-class classification** yield the best performance.
- **AI-driven completeness checking significantly reduces manual workload**, assisting **requirements engineers and legal experts**.

### **Key Quotes**

- _“Checking the completeness of DPAs against GDPR is a prerequisite for developing a compliant system.”_ (Page 1)
- _“We propose ten alternative solutions that leverage AI, ranging from traditional ML to LLMs and few-shot learning, for regulatory compliance checking.”_ (Page 2)
- _“Our evaluation on 169 real DPAs shows that RoBERTa and BERT achieve the best performance in completeness verification.”_ (Page 5)
- _“Handling data scarcity through SetFit demonstrates that few-shot learning can be a viable alternative in compliance verification.”_ (Page 6)

---

# **Evaluation Based on Inclusion Criteria**

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - ✅ **Yes.** The paper introduces an **AI-based approach for verifying the completeness of DPAs**, ensuring they contain all **required GDPR provisions**.
    - **Quote (Page 2):** _“We define completeness checking as a text classification problem, ensuring that all GDPR-mandated provisions are present in a DPA.”_
2. **Is the model useful for addressing GDPR compliance questions?**
    
    - ✅ **Yes.** The AI models **validate DPAs against GDPR**, addressing obligations such as **data retention, security, and contractual responsibilities**.
    - **Quote (Page 6):** _“Our solution ensures that DPAs meet GDPR compliance requirements by systematically analyzing whether key provisions are included.”_
3. **Is the proposed model publicly available?**
    
    - ✅ **Yes.** The dataset and code are available on **Zenodo** for research use.
    - **Quote (Page 26):** _“We make all our non-proprietary material used in our empirical evaluation publicly available at this link: [Zenodo](https://zenodo.org/records/11047441).”_
4. **Is the document written in English or Portuguese?**
    
    - ✅ **Yes.** The paper is in **English**.
5. **Is the document publicly available?**
    
    - ✅ **Yes.** The paper is **open access** under a **Creative Commons (CC BY 4.0) license**.
6. **Is the document peer-reviewed?**
    
    - ✅ **Yes.** Published in **Empirical Software Engineering (Springer)**, a **peer-reviewed journal**.

### **Final Verdict:** ✅ **Category: "OK"**

This paper **proposes an AI-driven approach for verifying GDPR compliance in DPAs, making it highly relevant to data provenance modeling for regulatory compliance**.

---

# **Discussion on Compliance Questions**

The AI-based **DPA completeness-checking approach directly supports GDPR compliance** by ensuring **all mandatory provisions are present**. Below is a breakdown of its relevance to specific compliance questions (CQs):

|**Compliance Question**|**Addressed?**|**Explanation**|
|---|---|---|
|**CQ08 (Retention Periods)**|✅|**Verifies if DPAs include required retention policies**.|
|**CQ09 (Ensuring Compliance Actions)**|✅|**AI models detect missing GDPR-mandated provisions**.|
|**CQ11 (Consent Verification & Updates)**|❌|**Does not focus on consent management**.|
|**CQ29 (Retention Policies & Procedures)**|✅|**Assesses DPA clauses related to storage and deletion of data**.|
|**CQ50 (Encryption & Data Security)**|✅|**Ensures security obligations (Art. 32 GDPR) are included in DPAs**.|

### **Conclusion**

The study **effectively supports compliance verification** but does **not specifically handle user consent tracking**.

---

# Further Discussion

## Summary & Analysis

### Overview

This paper focuses on automating the completeness verification of **Data Processing Agreements (DPAs)** in accordance with **GDPR requirements**. It explores **ten AI-enabled solutions**, including **machine learning (ML), deep learning (DL), and large language models (LLMs)**, to classify whether DPAs contain all necessary provisions as mandated by GDPR. The paper empirically evaluates these approaches using a dataset of **169 real DPAs**. The best-performing models achieve **up to 89.7% recall** in identifying missing provisions.

### Background and Motivation

GDPR mandates that **organizations using third-party processors** must establish **DPAs** to define responsibilities, ensuring compliance with GDPR’s **data processing principles (Article 28)**. However, ensuring **completeness** of DPAs is **labor-intensive** and requires legal expertise.

**Key Quotes:**

1. _“A DPA must be complete according to GDPR to ensure that the elicited requirements cover the complete set of obligations.”_ (p. 2)
2. _“Verifying the completeness of DPAs against GDPR entirely manually is time-consuming and requires adequate legal expertise.”_ (p. 2)

### Research Approach

The study frames **DPA completeness checking as a text classification problem**:

- **Input**: A DPA text, split into individual sentences.
- **Task**: Determine whether each sentence satisfies any of the **19 mandatory GDPR provisions** (e.g., security measures, breach notification, right to erasure).
- **Methodology**:
    - **LLM-based approaches** (e.g., BERT, RoBERTa, Legal-BERT)
    - **Deep Learning (DL)** (e.g., BiLSTM)
    - **Traditional ML** (e.g., Logistic Regression, Random Forest, SVM)
    - **Few-Shot Learning (SetFit)** for cases with limited labeled data.

**Key Quotes:**

1. _“Checking the completeness of DPAs against GDPR has been investigated in a recent work by Cejas et al. (2023), who developed a rule-based approach. We extend this with AI-enabled solutions.”_ (p. 4)
2. _“We propose ten alternative solutions which are based on different enabling technologies, including traditional ML, deep learning (DL), as well as recent NLP technologies.”_ (p. 5)

### Dataset and Model Training

- **169 real DPAs** from various industries (e.g., cloud services, finance).
- **31,185 sentences manually annotated** to determine compliance.
- **Legal experts annotated DPAs** with Cohen’s Kappa of **0.82** (strong inter-annotator agreement).

**Key Quotes:**

1. _“The DPAs were manually analyzed by three legal experts. The dataset includes 31,185 sentences, of which 12% were labeled as satisfying at least one provision.”_ (p. 7)
2. _“On a subset of 30 DPAs, the best-performing models achieved an F2 score of 89.7%.”_ (p. 7)

### Results

- **Best-performing models**:
    - **Binary classification**: BERT (81.6% recall)
    - **Multi-class classification**: RoBERTa (89.8% recall)
- **Few-shot learning** (SetFit) achieves reasonable accuracy but lower recall.
- **Machine learning models** (SVM, RF) perform well on precision but poorly on recall.

**Key Quotes:**

1. _“BERT achieves 81.6% recall in binary classification, while RoBERTa reaches 89.8% in multi-class classification.”_ (p. 9)
2. _“SetFit provides comparable precision but lower recall, making it suitable for low-data scenarios.”_ (p. 10)

### Conclusion

The study concludes that **AI-based methods** significantly reduce **manual effort** in **DPA compliance verification**, making them useful tools for **legal and software engineers**. However, **DPAs differ in structure**, so **further work** is needed to generalize across different legal documents.

**Key Quotes:**

1. _“AI-enabled solutions offer an automated means to verify completeness, reducing reliance on legal expertise.”_ (p. 12)
2. _“The use of LLMs for legal text analysis can bridge the gap between legal and software engineering disciplines.”_ (p. 13)

---

## Evaluation Based on Inclusion Criteria

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - No, the paper does not propose a **data provenance model** but **analyzes compliance completeness** in DPAs.
    - **Conclusion**: **Does not meet the provenance requirement**.
2. **Is the proposed model useful for answering compliance questions?**
    
    - **Yes**, it automates the process of verifying whether DPAs contain **mandatory GDPR provisions**.
    - **Relevant provisions:**
        - **CQ09** (Ensuring compliance of data processing)
        - **CQ39** (Third-party agreements)
        - **CQ51** (Data deletion requirements)
    - **Conclusion**: **Indirectly useful for compliance verification but not a full compliance model**.
3. **Is the proposed model publicly available?**
    
    - **Partially**. The **dataset and methodology are described**, but trained models are not provided.
    - **Conclusion**: **Limited availability**.
4. **Is the paper written in English or Portuguese?**
    
    - **Yes**, written in English.
    - **Conclusion**: **Meets requirement**.
5. **Is the paper publicly available?**
    
    - **Yes**, published in _Empirical Software Engineering_ (Springer).
    - **Conclusion**: **Meets requirement**.
6. **Is the paper peer-reviewed?**
    
    - **Yes**, published in a **peer-reviewed journal**.
    - **Conclusion**: **Meets requirement**.

**Overall Verdict**: The paper is **relevant for compliance verification** but **does not present a data provenance model**. Its AI-based solutions can be used **to check GDPR compliance** in DPAs but are **not directly applicable to data provenance tracking**.

---

## Discussion on Compliance Questions

The paper indirectly addresses several **GDPR compliance questions** related to DPAs. Below is a discussion on relevant compliance questions:

1. **CQ09 (Ensuring compliance of data processing)**
    
    - **Relevance**: The paper helps ensure DPAs **include all necessary provisions**, making it easier for controllers to maintain compliance.
    - **Quote**: _“Verifying the completeness of DPAs against GDPR is a prerequisite step towards developing a compliant system.”_ (p. 2)
2. **CQ39 (Third-party agreements)**
    
    - **Relevance**: DPAs regulate **processor obligations**, ensuring third parties process data lawfully.
    - **Quote**: _“A DPA is a legally-binding contract between a controller and a processor to ensure the protection of personal data.”_ (p. 3)
3. **CQ51 (Data deletion requirements)**
    
    - **Relevance**: The model verifies if DPAs include **data deletion obligations** under GDPR.
    - **Quote**: _“The processor shall return or delete all personal data to the controller after the end of the provision of services.”_ (p. 10)

Other compliance questions (e.g., **CQ08, CQ17, CQ25**) are **not explicitly covered**, as the focus is **checking DPAs** rather than **tracking data flows**.

---

# References

- [[matulevicius2020a]]