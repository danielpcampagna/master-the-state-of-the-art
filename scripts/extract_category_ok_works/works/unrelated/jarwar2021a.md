---
ID: jarwar2021a
authors: Jarwar, Muhammad Aslam; Chapman, Adriane; Elliot, Mark; Raji, Fatemeh
category: unrelated
cluster_id: "210709966"
display: jarwar (Provenance, Anonymisation and Data Environments)
due: This paper discusses the use of W3C PROV in anonymization decision-making but does not present a GDPR-specific data provenance model.
entrytype: article
link: http://arxiv.org/abs/2107.09966v1
name: Improving Data Value and its Influence on Decision Making through Better Data Frameworks and Management
place: arXiv
pp: 1--21
provenance_related: true
related: use W3C PROV
forward_steps: 2
---

### Summary & Analysis

#### **Main Idea**

The paper, _Provenance, Anonymisation and Data Environments: a Unifying Construction_, explores how _provenance_ information can be used within the **Anonymisation Decision-making Framework (ADF)** to manage data risks when exchanging data across environments. It proposes **integrating W3C PROV-DM** to track data flows and model _data environments_ to automate risk assessment for anonymization.

#### **Key Points by Section**

##### **1. Introduction**

- **Key Idea:** The paper introduces the **Anonymisation Decision-making Framework (ADF)** as a method for assessing disclosure risks in data sharing. It highlights the challenge of mapping **data environments** to track anonymization needs dynamically.
- **Quotations:**
    - "The second edition of ADF has increased its emphasis on modeling data flows, highlighting a potential new use of provenance information to support anonymisation decision-making." (_p.1_)
    - "Understanding contextual risk, and how to manage that risk through anonymisation, requires an awareness of, and capacity to map, the data flows between environments." (_p.2_)

##### **2. An ADF Use Case**

- **Key Idea:** The authors present a use case involving the **Government Office for National Data (GOND)**, which shares datasets with the **National Research Data Service (NRDS)** under contractual agreements. The complexities of data control, anonymization, and provenance tracking are examined.
- **Quotations:**
    - "A seemingly simple data flow between environments can in fact be complex depending on the nature of the data and the environment(s), the intended data use and the responsibilities of the data situation’s stakeholders." (_p.4_)
    - "NRDS has direct responsibility and operational control over the data release from the output of publications." (_p.4_)

##### **3. Supporting Data Environments with W3C PROV**

- **Key Idea:** The authors evaluate four different methods to model **data environments** in W3C PROV, including **Namespaces and Bundles**, as potential solutions to integrate provenance into the **ADF**.
- **Quotations:**
    - "A critical element in the feasibility of linking provenance to the ADF is the representation of data environments." (_p.3_)
    - "The namespace is a candidate for use as an identifier to capture the idea of multiple data environments (including data environments within data environments) and their associated entities, activities, agents, etc." (_p.8_)

##### **4. Comparative Analysis**

- **Key Idea:** The paper evaluates **how well different models fit the requirements of data environments**, comparing them based on completeness, ability to express **access control and governance**, and their suitability for anonymization processes.
- **Quotations:**
    - "The nesting of data environments is one of the important features. However, with bundles we cannot represent nested data environments because PROV does not allow the nesting of bundles." (_p.14_)
    - "The ability to attach attributes to a data environment is also an important feature for the ADF. Neither bundles nor namespaces support attachment of attributes." (_p.15_)

##### **5. Related Work**

- **Key Idea:** The authors discuss prior work on **PROV extensions for privacy and security** and highlight **gaps** that their model addresses.
- **Quotations:**
    - "A W3C PROV-based provenance model has been proposed by Benjamin et al. that uses the PROV data model ontology and data protection ontology to express the provenance for compliance with the European Union (EU) General Data Protection Regulation (GDPR)." (_p.17_)
    - "The PROV data model has also been extended with new relationship properties in order to supervise the security of data streaming." (_p.18_)

##### **6. Conclusion**

- **Key Idea:** The authors conclude that while **W3C PROV** can be adapted to **model data environments**, modifications are needed for **full support of anonymisation frameworks**.
- **Quotations:**
    - "We identified four different candidate mechanisms within the W3C PROV and evaluated each with respect to trade-offs of cost, maintenance and suitability for the problem." (_p.19_)
    - "While two obviously do not pass muster, the other two are viable solutions, with one Namespaces+ that utilises existing W3C PROV structures but requires an additional management, and the second Bundles+ which requires an extension to PROV." (_p.19_)

---

### Evaluation Based on Inclusion Criteria

|**Criterion**|**Evaluation**|**Supporting Quotation (Page #)**|
|---|---|---|
|**1. Proposes a data provenance model for GDPR activities**|✅ Yes, the paper discusses how W3C PROV could be extended to represent data environments for anonymization within ADF.|"By integrating provenance with the ADF, we will be able to track the flows of data and recognize the upstream and downstream data situations." (_p.2_)|
|**2. Model must be useful for compliance questions**|⚠️ Partially, the paper discusses anonymization strategies and risk assessment but does not explicitly link to compliance questions.|"One of the goals of the ADF is to ensure that when data that has been derived from the same original data, are released by different organisations, inadvertent disclosures of personal information do not happen as a consequence." (_p.5_)|
|**3. Model should be publicly available**|❌ No direct mention of making the proposed modifications to PROV publicly available.|Not stated in the document.|
|**4. Written in English or Portuguese**|✅ Yes, the paper is in English.|Entire document.|
|**5. Publicly accessible (Capes Cafe, open access, etc.)**|✅ Yes, available on arXiv.|"[http://arxiv.org/abs/2107.09966v1](http://arxiv.org/abs/2107.09966v1)" (_p.1_)|
|**6. Peer-reviewed (excluding arXiv, etc.)**|❌ No, arXiv is a preprint server and is not peer-reviewed.|Not peer-reviewed.|

**Final Inclusion Verdict:** ❌ **Unrelated (Does Not Fully Meet Inclusion Criteria)**  
While the paper discusses **data provenance in anonymization**, it **does not propose a publicly available model** for **GDPR compliance tracking**.

---

### Discussion on Compliance Questions

|**Compliance Question**|**Does the Paper Address It?**|**Explanation & Supporting Quotation (Page #)**|
|---|---|---|
|**CQ08: Data retention periods**|❌ No|The paper does not discuss data retention policies.|
|**CQ09: Actions to ensure GDPR compliance**|⚠️ Partially|It discusses anonymization but not specific actions for GDPR.|
|**CQ11: Re-seeking consent**|❌ No|No mention of consent handling.|
|**CQ17: Responding to SARs within a month**|❌ No|No discussion on subject access requests.|
|**CQ29: Retention policies**|❌ No|The focus is on anonymization, not retention.|
|**CQ51: Data destruction policies**|❌ No|No mention of data deletion or destruction.|

**Conclusion:** ❌ **Does Not Address Compliance Questions**  
The paper **focuses on anonymization within data environments**, but **does not address GDPR compliance questions explicitly**.

---

### **Final Verdict:** ❌ **Does Not Fit Inclusion Criteria**

This paper is **relevant to provenance and anonymization** but **not directly applicable to GDPR compliance modeling**.

---

# References

- [[pandit2018a]]