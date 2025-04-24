---
ID: amaral2024a
authors: Amaral, Orlando; Abualhaija, Sallam; Briand, Lionel
category: unrelated
display: Amaral (ML-based Compliance Verification of DPAs)
due: The paper proposes an ML-based compliance verification for DPAs but does not introduce a data provenance model for GDPR.
entrytype: article
link: N/A
name: ML-based Compliance Verification of Data Processing Agreements against GDPR
organization: University of Luxembourg, University of Ottawa
place: Peer-reviewed Journal
pp: N/A
provenance_related: false
related:
  - GDPR Compliance
  - Machine Learning
  - Natural Language Processing
  - Regulatory Compliance
year: 2024
forward_steps: 2
---

# Summary & Analysis

## **Main Idea**

The paper proposes a machine learning (ML)-based approach, **DικAIo**, to automate the verification of **Data Processing Agreements (DPAs)** against **GDPR** compliance requirements. The approach combines **natural language processing (NLP)** and **machine learning (ML)** to classify DPA content according to a **conceptual model** and **detect compliance violations**. The paper evaluates the approach on real DPAs, demonstrating **high precision (83.9%) and recall (83.0%)**, and compares it with an existing rule-based approach, **DERECHA**.

---

## **Key Sections & Arguments**

### **Introduction**

- **Context:** Software systems frequently handle **personal data**, which is subject to **GDPR**.
- **Problem:** **Manual verification** of **Data Processing Agreements (DPAs)** for GDPR compliance is **time-consuming** and **error-prone**.
- **Solution:** An **ML-based compliance verification** system for DPAs.

**Key Quote:**

> "Verifying the compliance of DPAs entirely manually is, however, time-consuming and error-prone." (p.1)

---

### **Conceptual Model for GDPR Compliance**

- **A conceptual model with 63 information types** (e.g., **data breach notification, processing duration, security measures**) was developed to check DPA compliance.
- Distinction between **mandatory** and **optional** information types.
- **Missing mandatory types = Non-compliance**; **Missing optional types = Best practice warnings**.

**Key Quote:**

> "We create a conceptual model that captures the semantics of DPAs, including rights and obligations." (p.4)

---

### **DικAIo: AI-based Compliance Checking Approach**

- **Preprocess DPA text** (tokenization, sentence splitting, lemmatization).
- **Extract embeddings** using different NLP models.
- **Train ML classifiers** (Support Vector Machine (SVM) with Sentence-BERT embeddings performed best).
- **Classify DPA content** based on information types.
- **Detect missing compliance elements** using semantic similarity.

**Key Quote:**

> "We empirically evaluate DικAIo on 180 real DPAs including a total of ≈ 50,000 sentences." (p.6)

---

### **Evaluation & Comparison with DERECHA**

- **DικAIo detected 483 out of 582 real violations**, with **precision: 83.9%** and **recall: 83.0%**.
- Compared with **DERECHA** (a rule-based system), **DικAIo achieved similar recall but slightly lower precision**.
- **Advantages of ML approach:**
    - **Less reliance on legal experts**.
    - **More adaptable to regulation changes**.
    - **More scalable than rule-based approaches**.

**Key Quote:**

> "DικAIo requires less involvement of legal experts than DERECHA and is more adaptable to regulation changes." (p.9)

---

### **Discussion & Limitations**

- **Key advantage:** **Less manual effort** than rule-based systems.
- **Key limitation:** **Requires a large, annotated dataset**.
- **Future work:** Improve handling of **complex sentence structures**.

**Key Quote:**

> "DικAIo can be used to categorize the content of the DPA, helping analysts quickly browse and decide about compliance." (p.10)

---

# **Evaluation Based on Inclusion Criteria**

### ✅ **Meets Inclusion Criteria**

1. **Proposes a data provenance model for GDPR compliance?** ❌ **No**
    
    - It **proposes an ML-based verification approach** for DPAs but **does not introduce a data provenance model**.
2. **Is the model useful for answering compliance questions?** ✅ **Partially**
    
    - While the **conceptual model** is useful for **DPA compliance**, it **does not explicitly address GDPR compliance questions**.
3. **Is the proposed model publicly available?** ✅ **Yes**
    
    - The paper states that the **conceptual model and dataset** are **available in their replication package**.
4. **Is the document in English or Portuguese?** ✅ **Yes, in English**.
    
5. **Is the document publicly accessible?** ❌ **No**
    
    - The paper appears to be behind a paywall.
6. **Is the document peer-reviewed?** ✅ **Yes**
    
    - Published in a peer-reviewed journal.

### **Conclusion:** ❌ **Unrelated**

- **Reason:** While the paper deals with GDPR compliance, it does **not propose a data provenance model**.

---

# **Discussion on Compliance Questions**

### **Does the paper address GDPR compliance questions?**

The approach is **relevant to some compliance questions** but does **not directly answer them**.

|**Compliance Question**|**Addressed?**|**Reasoning**|
|---|---|---|
|**CQ08, CQ09, CQ29, CQ30** (Retention & Deletion)|❌ **No**|The paper does not discuss **retention policies**.|
|**CQ11, CQ17, CQ20, CQ21** (Rights & Restrictions)|❌ **No**|No discussion of **user consent or SARs**.|
|**CQ32, CQ33, CQ37, CQ38** (Transparency & Rights)|❌ **No**|No coverage of **user transparency**.|
|**CQ47, CQ48, CQ49, CQ50** (Security & Breaches)|✅ **Partially**|The **conceptual model** includes **security measures** but does not detail encryption.|
|**CQ57, CQ58** (Breach Documentation)|✅ **Yes**|The approach detects **missing breach notifications** in DPAs.|
|**CQ63, CQ64, CQ65** (Data Transfers)|✅ **Partially**|Checks for **personal data transfer provisions** in DPAs.|

### **Conclusion**

- **Partially relevant** to **security and breach notifications**.
- **Not relevant** to **retention, user rights, or transparency**.

---

# References

- [[torre2021a]]