---
ID: chapman2022a
authors: Chapman, Adriane and Elliot, Mark and Jarwar, Muhammad Aslam and Raji, Fatemeh and Blount, Tom and Smith, Duncan and O'Hara, Kieron
category: unrelated
cluster_id: "807402735392335088"
display: Chapman et al. (2022)
due: The paper does not present a GDPR-specific provenance model, nor is the RP4 model publicly available. It focuses on anonymisation and provenance integration, rather than compliance tracking.
entrytype: article
link: https://doi.org/10.1145/nnnnnnn.nnnnnnn
name: Anonymisation and Provenance Expressing Data Environments with PROV - Turing Pilot Project Final Report
organization: ACM
place: Turing Pilot Project
pp: 1--34
provenance_related: true
related: use SemanticWeb;
forward_steps: 2
---
# Summary & Analysis

## **1. Project Overview (Page 1-3)**

### **Main Ideas:**

- The paper focuses on **the intersection of the provenance interoperability standard (W3C PROV) and the information needed for data sharing and anonymisation decisions**.
- **Functional Anonymisation** is introduced, which considers data risk in relation to its environment, rather than as an isolated dataset.
- A data environment is defined by four parameters: **agents, supplementary data, infrastructure, and governance**.

### **Representative Quotes:**

1. _“Choosing which technique to use requires understanding of the attacker threat, what the shared data is to be used for, and the context in which it was both gathered and released.”_ (Page 2)
2. _"Anonymity is not therefore solely a property of the data, but a function of the data environment(s) in which it is held."_ (Page 2)
3. _"Understanding the complexity of data environments is challenging, and requires an awareness of data flows."_ (Page 3)

## **2. Foundations (Page 3-8)**

### **Main Ideas:**

- The **Anonymisation Decision-Making Framework (ADF)** is introduced to help quantify the risks of data sharing.
- **W3C PROV** is identified as a possible means of capturing and documenting data provenance.
- **Existing anonymisation techniques are insufficient** due to a lack of environmental context.

### **Representative Quotes:**

4. _“What is needed to move this on further is a representational formalism which can capture the necessary features of the environment to allow more principled analysis of risk.”_ (Page 5)
5. _"Using provenance (as described by PROV), it is possible to trace where data came from, and how it was processed."_ (Page 6)
6. _“The development of the Anonymisation Decision-Making Framework (ADF), which captures risk by mapping data flows, has been a step forward.”_ (Page 7)

## **3. Mapping ADF Requirements to PROV (Page 9-14)**

### **Main Ideas:**

- The paper evaluates whether **W3C PROV can fully model the data governance concepts** required by ADF.
- PROV's **core components (agents, entities, activities, and relationships)** are examined for suitability in mapping anonymisation decisions.
- Certain concepts, like **nested environments and governance instruments, require extensions** beyond standard PROV.

### **Representative Quotes:**

7. _“Looking at Tables 3-7, only one field is covered with a (✓), indicating that the information required by the ADF is natively supported in PROV.”_ (Page 11)
8. _"Using bundles, we cannot represent this nesting because PROV does not allow the nesting of bundles."_ (Page 13)
9. _"PROV-based provenance model uses the PROV data model and data protection ontologies to express the provenance for the purposes of compliance with the European Union (EU) General Data Protection Regulation (GDPR)."_ (Page 12)

## **4. Extending PROV (Page 14-18)**

### **Main Ideas:**

- The paper introduces **new extensions to PROV** to capture **nested environments** and **data governance policies**.
- Introduces **RP4 Provenance**: Retrospective, Prospective, Permitted, Prescriptive, and Proscriptive provenance.
- **Data Governance Instruments (DGIs)** are proposed as a framework for **automated decision-making**.

### **Representative Quotes:**

10. _"RP4 provides the conceptual architecture that enables the user to address the essential questions (WHO-WHAT-HOW-WHEN-WHERE) about the data and their environments that the ADF requires."_ (Page 17)
11. _“Data Governance Instruments (DGIs) formalise the constraints, permissions, and policies that govern data usage.”_ (Page 16)
12. _"We propose that P3 provenance should be created through analysis of the relevant DGIs."_ (Page 18)

## **5. Use Cases and Industrial Application (Page 18-24)**

### **Main Ideas:**

- The authors analyze **two real-world use cases**:
    1. **Government Office for National Data (GOND)** - data sharing between national agencies.
    2. **Pharma-based Clinical Trial Data** - protecting participant confidentiality.
- Both cases **demonstrate the need for extended PROV models** to ensure anonymisation.

### **Representative Quotes:**

13. _“A seemingly simple data flow between environments can in fact be complex depending on the nature of the data, the data environment(s), the intended data use and the responsibilities of the data stakeholders.”_ (Page 19)
14. _"Explicit consent has been given by trial participants for secondary research using anonymised versions of their data."_ (Page 21)
15. _"One of the goals of anonymisation decision-making is to ensure that when data that has been derived from the same original data, are released, inadvertent disclosures of personal information do not happen as a consequence."_ (Page 20)

## **6. Summary and Future Work (Page 24-30)**

### **Main Ideas:**

- The study provides a **blueprint for incorporating provenance into anonymisation**.
- **PROV requires additional extensions** to fully meet GDPR and ADF requirements.
- The authors call for **further research into provenance-based compliance frameworks**.

### **Representative Quotes:**

16. _"This work demonstrates that a provenance-based approach can significantly enhance the decision-making process in data anonymisation."_ (Page 27)
17. _"More work is required to refine the model and integrate it with existing privacy-preserving technologies."_ (Page 28)
18. _"Anonymisation and provenance must be considered jointly, rather than as separate concerns."_ (Page 29)

# **Evaluation Based on Inclusion Criteria:**

| **Criterion**                                                                                                   | **Evaluation**                                                                                                                                                               | **Supporting Quote (with Page Number)**                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. The approach should propose a data provenance model to represent activities related to GDPR obligations.** | **Partially met** – The paper presents an extended PROV-based model for anonymisation but does not explicitly define a **data provenance model** solely for GDPR compliance. | _"A W3C PROV-based provenance model uses the PROV data model and data protection ontologies to express the provenance for the purposes of compliance with the European Union (EU) General Data Protection Regulation (GDPR)."_ (Page 12) |
| **2. The proposed model should be useful to address compliance questions.**                                     | **Partially met** – The PROV extensions improve **provenance tracking**, but the paper does not explicitly map these to GDPR compliance questions.                           | _"This work demonstrates that a provenance-based approach can significantly enhance the decision-making process in data anonymisation."_ (Page 27)                                                                                       |
| **3. The proposed model should be publicly available.**                                                         | **Not met** – There is no indication that the proposed **RP4 model** is publicly available for comparison.                                                                   | _No direct mention of public access to the model._                                                                                                                                                                                       |
| **4. The document should be written in English or Portuguese.**                                                 | **Met** – The paper is written in English.                                                                                                                                   | _Paper is published in English (verified throughout document)._                                                                                                                                                                          |
| **5. The document should be publicly available or accessible through CAPES CAFE libraries.**                    | **Met** – The document is publicly available in the ACM Digital Library.                                                                                                     | _"ACM Reference Format: Chapman et al. 2022."_ (Page 1)                                                                                                                                                                                  |
| **6. It should be a peer-reviewed document.**                                                                   | **Met** – The paper is published in ACM, indicating peer review.                                                                                                             | _"© 2022 Association for Computing Machinery."_ (Page 1)                                                                                                                                                                                 |

## **Conclusion on Inclusion/Exclusion Criteria:**

- **Category: `Unrelated`**
- **Due:** The paper does not explicitly **propose a GDPR compliance-specific provenance model**, and its **RP4 model is not publicly available**. While the paper does reference GDPR, it focuses more on anonymisation and provenance integration, rather than compliance-specific provenance tracking.

# **Discussion on Compliance Questions**

This section analyzes whether the paper provides insights into the **GDPR compliance questions (CQ)** listed in the request.

|**Compliance Question**|**Addressed in the Paper?**|**Supporting Quote (with Page Number)**|
|---|---|---|
|**CQ08: Retention periods for personal data.**|**Not explicitly addressed** – The paper discusses data provenance but does not focus on retention periods.|_No reference found in the document regarding retention periods._|
|**CQ09: Identifying required actions for GDPR compliance.**|**Partially addressed** – The **ADF framework** supports data-sharing decisions but does not prescribe compliance actions.|_"The ADF tool poses around thirty questions to data controllers in order to determine the data situation sensitivity and summary risk."_ (Page 10)|
|**CQ21: Informing individuals of the right to object to certain processing.**|**Not addressed** – The paper focuses on **data tracking and anonymisation**, not individual rights.|_No references found related to individual rights notifications._|
|**CQ29: Ensuring data is retained only as necessary.**|**Not explicitly addressed** – The document focuses on **data provenance** rather than retention policies.|_No mention of retention policies related to GDPR._|
|**CQ32: Preventing unnecessary duplication of records.**|**Partially addressed** – Provenance tracking **could** help prevent duplication, but this is not directly discussed.|_"Using provenance (as described by PROV), it is possible to trace where data came from, and how it was processed."_ (Page 6)|
|**CQ47: Documenting security safeguards.**|**Not addressed** – The focus is on provenance and anonymisation rather than security protocols.|_No explicit mention of security documentation._|
|**CQ51: Ensuring data is destroyed/anonymised when no longer required.**|**Partially addressed** – The **RP4 model** includes guidelines for anonymisation, but not destruction policies.|_"Proscriptive provenance specifies the set of activities or processes that should not happen when data in question are processed."_ (Page 17)|

## **Conclusion on Compliance Questions:**

- The paper does **not explicitly** address most **GDPR compliance questions**.
- It provides **partial** insights into **data anonymisation**, which is relevant for GDPR but does not fully meet the **specific compliance questions required**.

# References

- [[pandit2018g]]
- [[ujcich2018a]]