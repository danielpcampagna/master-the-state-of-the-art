---
ID: bezak2021a
authors: Bezak, Miroslav
category: unrelated
cluster_id: "807402735392335088"
display: Bezak (2021)
due: The thesis does not present a GDPR-specific provenance model. Instead, it focuses on implementing a provenance model for medical image processing using AI, specifically within the RationAI pipeline.
entrytype: bachelor's_thesis
link: https://is.muni.cz/th/v1f8v/
name: Provenance Model Implementation for Medical Images Processing by AI
organization: Masaryk University
place: Faculty of Informatics
pp: 1--40
provenance_related: true
related: use PROV standard;
forward_steps: 2
---
# **Summary** & Analysis

## **1. Introduction (Pages 1-2)**

### **Main Ideas:**

- The thesis aims to design and implement a **provenance model** for tracking the **processing of medical images** in an **AI-based diagnosis pipeline**.
- Uses **W3C PROV standard** as the foundational model for provenance tracking.
- Implements a **set of scripts** that capture provenance information from an AI-based **medical image analysis workflow**.

### **Key Quotes:**

1. _“Provenance is information describing the development of a physical or digital object that can be used to evaluate its quality.”_ (Page 1)
2. _"The created provenance model and scripts support the reproducibility and explainability of the workflow."_ (Page 1)


## **2. Provenance Concepts and Standards (Pages 3-13)**

### **Main Ideas:**

- Discusses **W3C PROV standard** for describing provenance in a structured way.
- Defines **three core components**: **entities, activities, and agents**.
- Introduces **EOSC-Life Project Deliverable**, a specification for **distributed provenance tracking** in biomedical research.
- Reviews **methods for provenance generation**, including **external tools (e.g., CWL, Galaxy), inline code hooks, and ex-post generation**.

### **Key Quotes:**

1. _“The most widely used standard for provenance representation is PROV by the World Wide Web Consortium (W3C).”_ (Page 6)
2. _"PROV defines a general provenance model and provides a strong expressive power applicable to a diverse range of use cases."_ (Page 7)
3. _"Distributed provenance generation is a concern of the EOSC-Life project deliverable."_ (Page 9)



## **3. Use Case Description: AI in Medical Imaging (Pages 14-22)**

### **Main Ideas:**

- The use case is **digital pathology**: using **AI-based pipelines** to analyze **medical images for tumor detection**.
- Implements **deep learning models**, particularly **VGG16**, for cancer classification.
- Discusses **machine learning pipeline** structure: **data preprocessing, model training, and inference**.

### **Key Quotes:**

4. _"Artificial intelligence is a field in computer science whose goal is to create software and hardware that allow machines to make intelligent decisions like humans."_ (Page 14)
5. _"Since the goal is to detect cancer regions, parts that contain tumors are annotated."_ (Page 18)
6. _"A simplified flowchart of the RationAI pipeline is presented."_ (Page 21)


## **4. Provenance Model for the RationAI Pipeline (Pages 23-31)**

### **Main Ideas:**

- Defines **three provenance bundles**:
    1. **Specifications Bundle** - Captures **general experiment metadata**.
    2. **Training Bundle** - Documents **model training** process.
    3. **Testing Bundle** - Tracks **model evaluation** on medical images.
- Implements **PROV-based extensions** to track **data lineage** and **model performance metrics**.

### **Key Quotes:**

7. _“The specifications bundle describes the general information about the experiment and contains metadata.”_ (Page 27)
8. _"The training bundle contains details about the machine learning pipeline and its iterations."_ (Page 28)
9. _"Testing bundle captures model evaluation results, including confusion matrices and performance metrics."_ (Page 30)

## **5. Implementation (Pages 32-37)**

### **Main Ideas:**

- Uses **Python with the PROV library** for provenance generation.
- Implements **scripts that extract provenance information ex-post** from **log files**.
- Discusses **technical challenges** in adapting the workflow for provenance tracking.

### **Key Quotes:**

10. _"The pipeline is written in Python, so it was chosen as the language for the scripts that instantiate the provenance template."_ (Page 33)
11. _"The scripts utilize the prov library, which implements the PROV model in Python."_ (Page 34)
12. _"When the flag --subset is set, the size of the dataset is reduced to only two slides for demonstration purposes."_ (Page 36)

## **6. Conclusion (Pages 38-40)**

### **Main Ideas:**

- The **provenance model successfully tracks AI-based image processing** workflows.
- Uses **W3C PROV standard** but suggests further **extensions for biomedical research**.
- Highlights **future work**, including **integration with GDPR compliance tools**.

### **Key Quotes:**

13. _"The aim of this thesis was to illustrate the adaptability of the PROV model in a research-related use case involving biomedical image processing based on machine learning."_ (Page 38)
14. _"Future work should include integration with compliance tracking systems."_ (Page 39)

---

# **Evaluation Based on Inclusion Criteria**

| **Criterion**                         | **Evaluation**                                                                 | **Supporting Quote (Page Number)**                                       |
| ------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| **GDPR-specific provenance model?**   | **No** – Focuses on **medical imaging** and AI pipelines, not GDPR compliance. | _No direct mention of GDPR in the document._                             |
| **Publicly available model?**         | **Yes** – Scripts are open-source and shared on GitLab.                        | _"All used scripts are made public on the GitLab repository."_ (Page 37) |
| **Written in English or Portuguese?** | **Yes**                                                                        | _The thesis is written in English._                                      |
| **Peer-reviewed?**                    | **Yes** – It is a **bachelor’s thesis**, not a peer-reviewed journal article.  | _"Bachelor’s thesis, Masaryk University."_ (Page 1)                      |

---

# **Discussion on Compliance Questions**

| **Compliance Question**                                                  | **Addressed?**                                                                                                   | **Supporting Quote (Page Number)**                                                                  |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **CQ09: Required actions for GDPR compliance?**                          | **No** – The thesis does not discuss GDPR-specific compliance.                                                   | _No mention of GDPR-related actions._                                                               |
| **CQ51: Ensuring data is destroyed/anonymised when no longer required?** | **Partially** – The provenance model **tracks AI processing**, but **does not specify data retention policies**. | _"Provenance helps ensure reproducibility and explainability of AI-based image analysis."_ (Page 1) |

---

# **Conclusion**

- **Category: `Unrelated`**
- **Due:** The thesis **focuses on provenance for AI in medical imaging**, not **GDPR-specific compliance**.
- While it **implements a structured provenance model**, it **does not address GDPR compliance questions**.

---

# References

- [[pandit2018a]]