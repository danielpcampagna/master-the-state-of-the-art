---
ID: guitton2024b
authors: Guitton, Clement; Tamò-Larrieux, Aurelia; Mayer, Simon; van Dijck, Gijs
category: unrelated
display: guitton (The Challenge of Open-Texture in Law)
due: The paper discusses the challenge of encoding open-textured legal norms but does not propose a data provenance model for GDPR obligations.
entrytype: article
link: https://doi.org/10.1007/s10506-024-09390-1
name: The Challenge of Open-Texture in Law
organization: Springer
place: Artificial Intelligence and Law
pp: ""
provenance_related: false
related:
  - Computational Law
  - Legal Text Encoding
  - Automated Regulation Processing
  - GDPR Compliance
year: 2024
forward_steps: 2
---

# **Summary & Analysis**

## **Summary**

The paper **"The Challenge of Open-Texture in Law"** by **Clement Guitton, Aurelia Tamò-Larrieux, Simon Mayer, and Gijs van Dijck** explores **how open-textured terms affect the feasibility of encoding legal norms into machine-processable formats**. Open-textured terms—such as **"reasonable," "appropriate," or "fair"**—require contextual interpretation, making automated processing of legal texts complex.

### **Key Contributions**

1. **Conceptual Framework for Open-Texture**
    
    - Proposes a **lever model** to represent how legal terms **oscillate** between determinate and indeterminate meanings based on **internal, external, and lateral forces**.
    - **Internal Forces**: Words themselves and their inherent ambiguity.
    - **External Forces**: Legal challenges and new case law that shift meaning.
    - **Lateral Forces**: The legal and social importance of the term, affecting its stability.
2. **Empirical Study on Open-Texture Measurement**
    
    - Conducts an experiment with **26 legal annotators** to measure agreement on open-textured terms.
    - Finds that **agreement on open-textured terms is possible** and statistically significant (**Cohen’s kappa = 0.7**).
    - Identifies a **list of open-textured terms**, such as "proportional," "necessary," "appropriate," and "justified."
3. **Implications for Computational Law**
    
    - Argues that laws with **high open-texture values** are **unsuitable for full automation**.
    - Suggests that **partially automating legal interpretation** is possible by tracking how terms shift over time.

---

## **Evaluation Based on Inclusion Criteria**

We now assess whether this paper meets the **strict inclusion/exclusion criteria**.

1. **Proposes a data provenance model for GDPR obligations?**
    
    - **No.** The paper **analyzes legal language complexity** but does **not propose a provenance model** to track GDPR compliance processes.
    - **Quote (Page 1):** _“Encoding open-textured norms (or balancing norms) is inherently problematic.”_
    - **✅ Conclusion:** **Fails Criterion #1 (No provenance model).**
2. **Addresses GDPR compliance questions?**
    
    - **Partially.** While the study **identifies terms relevant to GDPR (e.g., "legitimate interest," "appropriate safeguards")**, it does **not structure answers to compliance questions**.
    - **Quote (Page 2):** _"Knowing how much of a law is open-textured can help determine whether automatically processable regulation is feasible."_
    - **✅ Conclusion:** **Fails Criterion #2 (No structured compliance analysis).**
3. **Is the proposed model publicly available?**
    
    - **No.** The authors provide **empirical data** but do **not release a structured, machine-readable model**.
    - **✅ Conclusion:** **Fails Criterion #3 (No public model).**
4. **Is the document written in English or Portuguese?**
    
    - **Yes.** The paper is in **English**.
    - **✅ Conclusion:** **Criterion #4 is satisfied.**
5. **Is the document publicly available?**
    
    - **Partially.** The **final version is behind Springer paywall**, but **preprint availability is unclear**.
    - **✅ Conclusion:** **Criterion #5 is conditionally satisfied.**
6. **Is the document peer-reviewed?**
    
    - **Yes.** Published in **Artificial Intelligence and Law**, a **peer-reviewed journal**.
    - **✅ Conclusion:** **Criterion #6 is satisfied.**

### **Final Verdict**

🔴 **Category: "Unrelated"** – The paper **does not propose a GDPR-specific data provenance model** but rather explores **legal text ambiguity and its impact on automated regulation**.

---

# **Discussion on Compliance Questions**

The paper discusses **legal ambiguity** but does **not provide structured answers** to GDPR **compliance questions (CQs)**. Below is a **mapping**:

|Compliance Question|Addressed?|Explanation|
|---|---|---|
|**CQ08 (Retention Periods)**|❌|No discussion of **data retention**.|
|**CQ09 (Compliance Actions)**|❌|Discusses **legal ambiguity** but **not compliance actions**.|
|**CQ11 (Consent Management)**|❌|Does not address **how consent is managed**.|
|**CQ17 (SAR Response in One Month)**|❌|No mention of **response timelines**.|
|**CQ29 (Retention Policies)**|❌|No discussion of **retention procedures**.|
|**CQ39 (Supplier Agreements)**|❌|Does not analyze **contractual GDPR obligations**.|

### **Conclusion**

While the study helps understand **legal complexity**, it does **not explicitly address compliance processes**.

---

# References

- [[bonatti2020a]]