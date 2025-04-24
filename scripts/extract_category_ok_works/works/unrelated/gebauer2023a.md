---
ID: gebauer2023a
authors: Gebauer, Michael; Maschhur, Faraz; Leschke, Nicola; Grünewald, Elias; Pallas, Frank
category: unrelated
display: gebauer (Human-in-the-Loop for Privacy Policy Information Extraction)
due: The paper introduces a privacy policy annotation system but does not propose a data provenance model for GDPR obligations.
entrytype: inproceedings
link: https://ieeexplore.ieee.org/xpl/conhome/1820965/all-proceedings
name: A ‘Human-in-the-Loop’ approach for Information Extraction from Privacy Policies under Data Scarcity
organization: IEEE
place: 2023 IEEE European Symposium on Security and Privacy Workshops (EuroS&PW)
pp: ""
provenance_related: false
related:
  - Privacy Policies
  - Machine Learning
  - Natural Language Processing
  - GDPR Compliance
year: 2023
forward_steps: 2
---

# **Summary & Analysis**

## **Summary**

The paper **"A ‘Human-in-the-Loop’ approach for Information Extraction from Privacy Policies under Data Scarcity"** presents a system for **semi-automated extraction** of information from privacy policies. The proposed system integrates **machine learning (ML)-generated suggestions** with **human annotation** to **streamline the transformation of written privacy policies into structured, machine-readable formats**. The authors argue that existing automated approaches suffer from **high error rates**, making manual annotation labor-intensive. Their solution leverages **sentence-based machine learning models** (e.g., **Sentence-BERT**) to provide annotation suggestions, which human reviewers validate in an interactive loop.

The paper contributes:

1. A **privacy policy annotation framework** that uses **human-in-the-loop learning** to improve ML-based privacy policy analysis.
2. A **benchmark evaluation** of information extraction models, showing **Sentence-BERT outperforms other ML models** in extracting GDPR-related data subject rights.
3. A **public dataset** of annotated privacy policies for training and evaluating similar models.

## **Key Points**

- **Problem:** Fully automated extraction of **privacy policy information** is error-prone due to **data scarcity** and the complexity of legal texts.
- **Solution:** A **Human-in-the-Loop** (HITL) annotation system that improves ML-based extraction by incorporating human feedback.
- **Architecture:**
    - The system extracts **data subject rights** from privacy policies (e.g., Right to Withdraw Consent, Right to Data Portability).
    - **Machine Learning models (BERT, SBERT)** generate annotation suggestions.
    - **Human reviewers validate and refine** these suggestions, improving model accuracy over time.
- **Evaluation:** The system achieves superior accuracy over traditional methods, particularly in handling **small datasets**.
- **Use Case:** The approach is designed for **regulatory compliance analysis** but does not explicitly model **data provenance**.

**Representative Quotations:**

- _“Machine-readable representations of privacy policies are door openers for a broad variety of novel privacy-enhancing and, in particular, transparency-enhancing technologies (TETs).”_ (Page 1)
- _“We propose a ‘Human-in-the-Loop’ privacy policy annotation system which facilitates the transition from purely textual privacy policies to machine-readable ones.”_ (Page 2)
- _“Benchmarks covering three established information extraction algorithms on a public dataset show that Sentence-BERT provides superior performance.”_ (Page 6)

---

# **Evaluation Based on Inclusion Criteria**

Now, we assess the paper against the **strict inclusion/exclusion criteria**:

1. **Proposes a data provenance model for GDPR obligations?**
    
    - **No.** The paper focuses on extracting privacy policy content, specifically **data subject rights**, rather than **modeling provenance data**.
    - **Quote (Page 2):** _“We present a prototype system for a ‘Human-in-the-Loop’ approach to privacy policy annotation that integrates ML-generated suggestions and ultimately human annotation decisions.”_  
        **✅ Conclusion:** Fails **Criterion #1** (No provenance model).
2. **Is the model useful for addressing GDPR compliance questions?**
    
    - **Partially.** The paper helps extract privacy policy information, including some GDPR **data subject rights** (e.g., right to withdraw consent, right to access). However, it does **not** provide a structured framework for answering the compliance questions directly.
    - **Quote (Page 5):** _“Throughout our benchmark, we will focus solely on data subject rights, as they are stated in full sentences and do not call for pointy extraction of highly specific facts.”_  
        **✅ Conclusion:** Does not fully satisfy **Criterion #2**.
3. **Is the proposed model publicly available?**
    
    - **Yes.** The authors provide a **public dataset of annotated privacy policies**.  
        **✅ Conclusion:** **Criterion #3 is satisfied**.
4. **Is the document written in English or Portuguese?**
    
    - **Yes.** The paper is written in **English**.  
        **✅ Conclusion:** **Criterion #4 is satisfied**.
5. **Is the document publicly available?**
    
    - **Partially.** The **preprint is available on arXiv**, but the final version is behind IEEE paywall.  
        **✅ Conclusion:** **Criterion #5 is conditionally satisfied**.
6. **Is the document peer-reviewed?**
    
    - **Yes.** The paper was **accepted for the IEEE European Symposium on Security and Privacy Workshops (EuroS&PW 2023)**.  
        **✅ Conclusion:** **Criterion #6 is satisfied**.

### **Final Verdict**

🔴 **Category: "Unrelated"** – The paper **does not propose a GDPR-specific data provenance model**. While it provides **ML-based extraction for privacy policies**, it does **not explicitly represent GDPR compliance processes**.

---

# **Discussion on Compliance Questions**

The **Human-in-the-Loop system** focuses on extracting **data subject rights from privacy policies** but does **not explicitly address GDPR compliance questions (CQs)**. Below is a comparison of its coverage:

|Compliance Question|Addressed?|Explanation|
|---|---|---|
|**CQ08 (Retention Periods)**|❌|No mention of **data retention policies** or timelines.|
|**CQ09 (Compliance Actions)**|❌|Extracts GDPR-related rights but **does not analyze compliance actions**.|
|**CQ11 (Consent Management)**|✅|Extracts **Right to Withdraw Consent** from privacy policies.|
|**CQ17 (SAR Response in One Month)**|❌|No mention of **SAR handling timeframes**.|
|**CQ29 (Retention Policies)**|❌|The approach does **not track data storage or deletion policies**.|
|**CQ39 (Supplier Agreements)**|❌|No discussion on **third-party data processing agreements**.|

**Conclusion:**  
The paper **partially** addresses GDPR **data subject rights** but does **not provide structured answers to compliance questions**.

---

# References

- [[bonatti2020a]]