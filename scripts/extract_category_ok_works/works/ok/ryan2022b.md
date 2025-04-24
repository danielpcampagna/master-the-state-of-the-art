---
ID: ryan2022b
authors: Ryan, Paul; Brennan, Rob; Pandit, Harshvardhan J.
category: ok
display: "ryan (DPCat: Specification for an Interoperable and Machine-Readable Data Processing Catalogue Based on GDPR)"
due: Proposes DPCat, a semantic model for representing and exchanging GDPR Register of Processing Activities (ROPA) information. While it supports compliance documentation and interoperability, it is not a full data provenance model.
entrytype: article
link: https://doi.org/10.3390/info13050244
name: "DPCat: Specification for an Interoperable and Machine-Readable Data Processing Catalogue Based on GDPR"
organization: MDPI
place: Information
pp: 1-32
provenance_related: true
related:
  - GDPR compliance
  - semantic web
  - Register of Processing Activities (ROPA)
  - data cataloguing
  - privacy governance
year: "2022"
forward_steps: 2
---

# Summary & Analysis

## Overview

This paper presents **DPCat (Data Processing Catalogue)**, a **semantic model for representing, collecting, and exchanging Register of Processing Activities (ROPA) information**. Under **GDPR Article 30**, organizations must maintain ROPA records to document their processing activities, but **current practices rely on spreadsheets and proprietary tools that lack interoperability and automation**. DPCat is built using **semantic web technologies**, including **DCAT, DCAT-AP, and DPV**, to enable **machine-readability, interoperability, and automation** of ROPA-related processes.

## Background

Organizations struggle to keep **accurate and up-to-date ROPA records** due to:

1. **Fragmented data sources** across multiple internal units and external processors.
2. **Lack of automation** in collecting and updating ROPA.
3. **Variability in DPA ROPA templates**, making it difficult to create a standardized format.

DPCat aims to address these challenges by providing a **semantic web-based framework** that facilitates:

- **Machine-readable ROPA representation**
- **Interoperable exchange between stakeholders**
- **Automated compliance tracking**

**Key Quotes:**

1. _“The GDPR requires Data Controllers and Data Protection Officers (DPO) to maintain a Register of Processing Activities (ROPA) as part of overseeing the organisation’s compliance processes.”_ (p. 1)
2. _“Current practices use spreadsheets or proprietary systems that lack machine-readability and interoperability, presenting barriers to automation.”_ (p. 1)

## Research Approach

### **DPCat: A Machine-Readable ROPA Framework**

DPCat is designed to:

1. **Standardize ROPA Representation**:
    
    - Built on **DCAT** (Data Catalog Vocabulary) and **DPV** (Data Privacy Vocabulary).
    - Uses **SHACL** for validation and **SPARQL** for querying.
2. **Enable Interoperability**:
    
    - Allows **data controllers, processors, and DPAs** to exchange ROPA information in a common format.
3. **Automate Compliance Verification**:
    
    - Supports validation of ROPA completeness and accuracy.
    - Allows generation of **DPA-specific compliance reports**.

### **Core Components**

- **CSM-ROPA (Common Semantic Model for ROPA)**:
    - Harmonizes ROPA information requirements from **17 EU DPAs**.
    - Defines **47 unique ROPA-related concepts** (e.g., purposes, data subjects, storage durations).
- **DPCat Architecture**:
    - **ROPARecord**: Represents individual processing activities.
    - **ROPA**: A collection of ROPARecords.
    - **ROPACatalog**: A higher-level catalog grouping multiple ROPAs.

**Key Quotes:**

1. _“DPCat extends the Data Catalog Vocabulary (DCAT) with concepts identified in CSM-ROPA using DPV to enable representation of ROPA in a machine-readable and interoperable manner.”_ (p. 12)
2. _“DPCat enables querying, validation, and exchange of ROPA-related information to facilitate regulatory compliance.”_ (p. 14)

## Evaluation

### **Application to Real-World ROPA Records**

- Tested on **58 ROPA documents** from the **European Data Protection Supervisor (EDPS)**.
- Represented ROPA records as **RDF graphs** and validated using **SHACL constraints**.
- Performed **SPARQL queries** to extract compliance-related information.

### **Key Findings**

- **Semantic web models** enhance **ROPA interoperability and automation**.
- **DPCat enables integration with compliance tools** to support data governance.
- **Ensures completeness and consistency** of ROPA documentation across different jurisdictions.

**Key Quotes:**

1. _“DPCat provides a structured, machine-readable, and interoperable framework for managing ROPA-related information.”_ (p. 21)
2. _“By moving ROPA processes to a data cataloguing approach, DPCat enables modern metadata-driven data governance.”_ (p. 22)

## Conclusion

DPCat offers a **semantic web-based solution** for ROPA representation and exchange. It supports **automation, querying, and validation** of processing records but does **not provide a full data provenance model**. Instead, it focuses on **structuring compliance information** and **enabling interoperability across organizations**.

**Key Quotes:**

1. _“DPCat enables compliance teams to create, validate, and share ROPA information in a machine-readable format.”_ (p. 28)
2. _“It aligns with EU recommendations on placing data governance at the center of personal data processing.”_ (p. 30)

---

# Evaluation Based on Inclusion Criteria

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - **Partially**. DPCat **structures ROPA information** but does **not model provenance tracking**.
    - **Conclusion**: **Relevant for compliance but not a provenance model**.
2. **Is the proposed model useful for answering compliance questions?**
    
    - **Yes**, it supports:
        - **CQ09** (Ensuring GDPR-compliant data processing)
        - **CQ28** (Ensuring data accuracy and updates)
        - **CQ39** (Third-party agreements and ROPA documentation)
    - **Conclusion**: **Useful for compliance verification**.
3. **Is the proposed model publicly available?**
    
    - **Yes**, available at [w3id.org/dpcat](https://w3id.org/dpcat).
    - **Conclusion**: **Meets requirement**.
4. **Is the paper written in English or Portuguese?**
    
    - **Yes**, written in English.
    - **Conclusion**: **Meets requirement**.
5. **Is the paper publicly available?**
    
    - **Yes**, published in _Information (MDPI)_.
    - **Conclusion**: **Meets requirement**.
6. **Is the paper peer-reviewed?**
    
    - **Yes**, published in a **peer-reviewed journal**.
    - **Conclusion**: **Meets requirement**.

**Overall Verdict**: The paper is **relevant for ROPA compliance tracking** but **does not present a complete data provenance model**. It provides a **semantic framework for structuring and exchanging GDPR processing records**.

---

# Discussion on Compliance Questions

DPCat indirectly addresses several **GDPR compliance questions** by structuring **ROPA records**. Below is a discussion of relevant compliance questions:

1. **CQ09 (Ensuring GDPR-compliant processing)**
    
    - **Relevance**: DPCat enables **automated ROPA documentation** to track processing compliance.
    - **Quote**: _“DPCat allows compliance teams to validate processing activities against GDPR requirements.”_ (p. 14)
2. **CQ28 (Ensuring data accuracy and updates)**
    
    - **Relevance**: Supports **structured data governance** to keep ROPA **up-to-date**.
    - **Quote**: _“DPCat allows automatic validation and updating of processing activities.”_ (p. 18)
3. **CQ39 (Third-party agreements)**
    
    - **Relevance**: Helps **document and manage processor relationships**.
    - **Quote**: _“DPCat provides structured ROPA entries for managing external data processors.”_ (p. 20)

---

# References

- [[ryan2021a]]