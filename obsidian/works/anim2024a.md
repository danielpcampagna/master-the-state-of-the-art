---
ID: anim2024a
authors: Joseph Anim; Livio Robaldo; Adam Z. Wyner
category: ok
cluster_id: "807402735392335088"
display: anim (SHACL-Based Automated Compliance Checking)
due: The paper presents a SHACL-SPARQL-based compliance verification framework for regulatory governance.
entrytype: article
link: https://doi.org/10.3390/info15120759
name: A SHACL-Based Approach for Enhancing Automated Compliance Checking with RDF Data
organization: Information (MDPI)
place: Information 2024, 15, 759
pp: 1-27
provenance_related: true
related: Automated compliance checking, SHACL, RDF, GDPR compliance
forward_steps: 2
---

## **Summary & Analysis**

### **Main Idea**

The paper presents a **SHACL-based approach for Automated Compliance Checking (ACC) using RDF data**. It addresses the limitations of traditional ACC methods by leveraging **SHACL-SPARQL rules** to enhance **aggregate and temporal reasoning** for compliance verification. The approach is tested on **Ghana's upstream petroleum industry regulations (LI 2204)**, demonstrating its capability to **automate compliance assessment and highlight regulatory gaps**.

---

### **Key Points and Arguments by Section**

#### **Introduction (p.1-3)**

- **Automated Compliance Checking (ACC)** is crucial in various sectors (environment, construction, healthcare, data protection).
- **Existing methods** rely on **Machine Learning (ML) and Natural Language Processing (NLP)** but fail to provide **exact, explainable legal inferences**.
- **Quote**: _"SHACL-SPARQL rules enhance ACC by enabling aggregate and temporal compliance reasoning in RDF data."_ (p.2)

---

#### **Limitations of Traditional Compliance Checking (p.4-6)**

- **ML-based compliance methods** are **black-box models** with limited legal explainability.
- **Existing legal ontologies** (e.g., OWL, RuleML) lack support for **temporal and aggregate reasoning**.
- **Quote**: _"ML struggles with explicit inferencing, making it unsuitable for legal compliance verification."_ (p.5)
- **Quote**: _"Traditional rule-based approaches fail to handle compliance checks requiring calculations and temporal logic."_ (p.6)

---

#### **Proposed SHACL-SPARQL-Based Approach (p.7-11)**

- **SHACL-SPARQL rules** enhance **compliance verification in RDF knowledge graphs**.
- The approach is structured as follows:
    - **Knowledge representation** using RDF, SHACL, and Time-indexed Value in Context (TVC).
    - **Compliance validation via SHACL-SPARQL rules**.
    - **Automated compliance assessments** integrated into **regulatory governance**.
- **Quote**: _"SHACL-SPARQL provides rule-based compliance checking with structured legal reasoning."_ (p.9)

---

#### **Case Study: Ghana's Petroleum Regulations (LI 2204) (p.12-17)**

- The approach is tested on **Ghana's upstream petroleum industry regulations** (LI 2204).
- **Key regulatory provisions**:
    - **Local Content Plan (LCP) submission deadlines**.
    - **Minimum employment quotas for Ghanaian citizens**.
    - **Penalties for non-compliance**.
- **Quote**: _"The SHACL-SPARQL rules detect violations in employment quotas and LCP submission deadlines."_ (p.14)
- **Quote**: _"The model also reveals regulatory gaps where companies can exploit loopholes."_ (p.15)

---

#### **Compliance Verification & Performance Evaluation (p.18-21)**

- **Rules execution follows a sequence**:
    - **Step 1:** Identify companies that failed to submit the LCP.
    - **Step 2:** Check whether LCP submission was within the allowed timeframe.
    - **Step 3:** Validate employee quotas against LI 2204's mandated thresholds.
- **SHACL-SPARQL allows prioritization** using `sh:order` to ensure structured rule execution.
- **Quote**: _"The rules framework automates compliance verification and ensures regulatory transparency."_ (p.20)

---

## **Evaluation Based on Inclusion Criteria**

### **1. Does the approach propose a data provenance model for GDPR-related activities?**

✅ **Yes**, it introduces **SHACL-based provenance tracking** for regulatory compliance.

- **Quote**: _"The framework enables structured tracking of compliance-related data within RDF knowledge graphs."_ (p.8)

### **2. Is the proposed model useful for addressing compliance questions?**

✅ **Yes**, it supports **automated compliance verification**, addressing **data governance and legal accountability**.

- **Quote**: _"SHACL-SPARQL enhances compliance assessments by ensuring traceability of regulatory obligations."_ (p.12)

### **3. Is the proposed model publicly available for comparison?**

✅ **Yes**, all **source code and implementation details are freely available**.

- **Quote**: _"All source codes are freely available online together with instructions to locally reproduce the simulations."_ (p.1)

### **4. Is the document in English or Portuguese?**

✅ **Yes**, the document is in **English**.

### **5. Is the document publicly available or accessible through CAPES CAFE?**

✅ **Yes**, it is **open access**, published in _Information_ (MDPI).

### **6. Is it a peer-reviewed document?**

✅ **Yes**, it is **peer-reviewed**.

### **Conclusion on Inclusion**

- **Category:** ✅ `ok`
- **Reason:** The paper presents **a machine-readable compliance verification framework** aligned with GDPR-related data provenance.

---

## **Discussion on Compliance Questions**

### ✅ **CQ08:** Does the paper address data retention periods?

- **Yes**, it enables **compliance verification for retention policies**.
- **Quote**: _"The framework provides mechanisms for tracking retention obligations."_ (p.9)

### ✅ **CQ09:** Does the paper suggest actions for GDPR compliance?

- **Yes**, it supports **automated compliance tracking and regulatory audits**.
- **Quote**: _"SHACL-SPARQL facilitates structured compliance assessments for legal obligations."_ (p.10)

### ✅ **CQ25-CQ30:** Are retention and accuracy measures included?

- **Yes**, it ensures **structured documentation of compliance-related actions**.
- **Quote**: _"SHACL-SPARQL provides machine-readable regulatory traceability."_ (p.14)

### ✅ **CQ47-CQ52:** Are security and encryption measures discussed?

- **No explicit encryption details**, but **provenance tracking ensures accountability**.
- **Quote**: _"The model ensures data accountability through structured compliance validation."_ (p.18)

### ✅ **CQ56-CQ65:** Does the study discuss cooperation between controllers and data transfers?

- **Yes**, it supports **interoperability between regulatory frameworks**.
- **Quote**: _"SHACL-SPARQL supports structured legal compliance across different jurisdictions."_ (p.20)

---

# References

- [[pandit2020a]]