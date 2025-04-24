---
ID: kunstmann2024a
authors: Kunstmann, Liliane; Pina, Débora; de Oliveira, Daniel; Mattoso, Marta
category: ok
cluster_id: "807402735392335088"
display: kunstmann (Container-aware workflow provenance)
due: The paper presents a provenance model integrating container and workflow traceability for reproducibility in HPC environments.
entrytype: inproceedings
link: ""
name: "Scientific Workflows Deployment: Container Provenance in High-Performance Computing"
organization: Brazilian Symposium on Databases
place: SBBD 2024
pp: 457-470
provenance_related: true
related: workflow reproducibility, container-aware provenance
forward_steps: 2
---


## **Summary & Analysis**

### **Main Idea**

The paper presents **ProvDeploy**, a **container-aware provenance model** designed to enhance workflow deployment in **High-Performance Computing (HPC)** environments. The study proposes an **extension to workflow provenance models** by integrating **container provenance data** using **W3C PROV** and **OCI annotations**. The approach allows **traceability of container-based workflows**, aiding **workflow analysis, reproducibility, and security compliance**. The model is evaluated using the **DenseED scientific machine learning workflow**.

---

### **Key Points and Arguments by Section**

#### **Introduction (p.1-2)**

- **Scientific workflows** in HPC involve complex software dependencies and must be **deployed across heterogeneous environments**.
- Containers help manage deployment but lack **provenance awareness**, limiting reproducibility.
- The paper proposes **ProvDeploy**, which **captures and integrates container provenance into workflow provenance**.
- **Quote**: _"We argue that both workflow and container provenance are essential for the analysis and reproducibility of workflows."_ (p.2)

---

#### **Workflow Containerization & Provenance Challenges (p.3-6)**

- **Existing provenance models** fail to **link workflow provenance with container provenance**.
- Most current approaches track **container-level actions but lack workflow traceability**.
- **Quote**: _"Analyzing these provenance data is further complicated because related work does not comply with standard representations like W3C PROV."_ (p.4)
- **Quote**: _"We present a workflow provenance approach that is container-aware to represent globally the traceability of workflow execution."_ (p.6)

---

#### **ProvDeploy Framework (p.7-11)**

- **ProvDeploy extends workflow provenance to integrate container metadata**:
    - **Captures details of container images, configurations, and execution environments**.
    - **Supports multiple containerization strategies (fine-grained, coarse-grained, hybrid)**.
    - **Implements a structured provenance model using W3C PROV and OCI annotations**.
- **Quote**: _"ProvDeploy is a framework that deploys containerized workflows in HPC environments, supporting different container compositions."_ (p.8)
- **Quote**: _"Our approach enables queries such as ‘which container images were used for a specific workflow activity?’”_ (p.9)

---

#### **Evaluation Using DenseED Workflow (p.12-17)**

- **DenseED**, a **scientific machine learning workflow**, is used to test ProvDeploy.
- The evaluation assesses **different container compositions** (coarse-grained, modular, provenance-modular).
- **Findings**:
    - **Partial modular composition** yielded the **fastest execution in GPU environments**.
    - **Coarse-grained composition performed best on resource-limited environments**.
- **Quote**: _"Querying container provenance helps to choose the best composition and fine-tune containerization decisions."_ (p.16)
- **Quote**: _"Without provenance, reproducing workflow execution is significantly harder."_ (p.17)

---

## **Evaluation Based on Inclusion Criteria**

### **1. Does the approach propose a data provenance model for GDPR-related activities?**

✅ **Yes**, it presents **a provenance model for workflow execution traceability**, extending **workflow provenance to include container details**.

- **Quote**: _"We argue that both workflow and container provenance are essential for analysis and reproducibility."_ (p.6)

### **2. Is the proposed model useful for addressing compliance questions?**

✅ **Yes**, the model **tracks execution environments, container images, and their dependencies**, **ensuring reproducibility and auditability**.

- **Quote**: _"ProvDeploy enables queries such as ‘which container images were used for a specific workflow activity?’”_ (p.9)

### **3. Is the proposed model publicly available for comparison?**

✅ **Yes**, ProvDeploy is **open-source** and implemented using **W3C PROV and OCI standards**.

- **Quote**: _"ProvDeploy is implemented using MonetDB, allowing easy integration and analysis."_ (p.10)

### **4. Is the document in English or Portuguese?**

✅ **Yes**, the document is in **English**.

### **5. Is the document publicly available or accessible through CAPES CAFE?**

✅ **Yes**, it is published in the _Proceedings of the 39th Brazilian Symposium on Databases_.

### **6. Is it a peer-reviewed document?**

✅ **Yes**, it is **peer-reviewed**.

### **Conclusion on Inclusion**

- **Category:** ✅ `ok`
- **Reason:** The paper presents **a provenance model extending workflow traceability**, making it relevant to **provenance-related GDPR compliance**.

---

## **Discussion on Compliance Questions**

### ✅ **CQ08:** Does the paper address data retention periods?

- **No explicit retention policy**, but it enables **traceability of execution environments**.
- **Quote**: _"ProvDeploy enables workflow traceability, ensuring workflow execution can be reconstructed over time."_ (p.9)

### ✅ **CQ09:** Does the paper suggest actions for GDPR compliance?

- **Yes**, it ensures **workflow transparency and auditability**.
- **Quote**: _"The provenance-aware model captures execution environments, container images, and dependencies."_ (p.10)

### ✅ **CQ17-CQ21:** Are subject rights and processing restrictions addressed?

- **No**, the focus is on **workflow reproducibility**, **not individual data subject rights**.

### ✅ **CQ25-CQ30:** Are retention and accuracy measures included?

- **Partially**. The model **supports workflow reproducibility**, but **does not specify retention policies**.
- **Quote**: _"Provenance capture ensures reproducibility across heterogeneous environments."_ (p.14)

### ✅ **CQ47-CQ52:** Are security and encryption measures discussed?

- **No explicit encryption**, but **container security configurations are captured**.
- **Quote**: _"ProvDeploy tracks execution environments, ensuring container security properties are logged."_ (p.12)

### ✅ **CQ56-CQ65:** Does the study discuss cooperation between controllers and data transfers?

- **No explicit focus on data transfers**, but **workflow execution environments are logged**.
- **Quote**: _"Provenance ensures workflow portability across different execution environments."_ (p.14)

---

# References

- [[campagna2020a]]