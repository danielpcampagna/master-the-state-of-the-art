---
ID: roascio2022a
authors: Roascio, Gianluca; Costa, Gabriele; Baccelli, Emmanuel; Malina, Lukas; Matulevičius, Raimundas; Momeu, Marius; Morkevičius, Nerijus; Russo, Enrico; Stojanović, Branka; Tasidou, Aimilia
category: unrelated
display: "roascio (HArMoNICS: High-Assurance Microgrid Network Infrastructure)"
due: The paper presents a cybersecurity case study for intelligent infrastructures but does not propose a data provenance model for GDPR obligations.
entrytype: article
link: https://doi.org/10.1109/ACCESS.2022.3218412
name: "HArMoNICS: High-Assurance Microgrid Network Infrastructure Case Study"
organization: IEEE
place: IEEE Access
pp: 115372-115383
provenance_related: false
related:
  - Cybersecurity
  - Intelligent Infrastructures
  - Security-by-Design
  - Privacy-Preserving Data Processing
year: 2022
forward_steps: 2
---

# **Summary & Analysis**

## **Summary**

The paper **"HArMoNICS: High-Assurance Microgrid Network Infrastructure Case Study"** by **Gianluca Roascio et al. (2022)** presents a **cybersecurity-focused case study** centered on **intelligent infrastructures (II)**, specifically a **smart microgrid network**. The study introduces **HArMoNICS**, a **digital replica of a real Smart Polygeneration Microgrid (SPM)** in Italy, designed for **security analysis, intrusion detection, and privacy-preserving computing**.

### **Key Contributions**

1. **Development of a high-assurance testbed for II cybersecurity research**
    
    - Uses **a digital twin** approach to simulate a **zero-emission building microgrid**.
    - Evaluates cybersecurity vulnerabilities in **software, networking, and IoT components**.
2. **Implementation of 8 security and privacy-related scenarios**
    
    - **Threat modeling and vulnerability assessment** for critical II components.
    - Covers areas like **firmware security, intrusion detection, fog computing security, privacy-preserving authentication, and encryption**.
3. **Open-source and extensible infrastructure**
    
    - The **case study implementation is open-source**, allowing researchers to extend its security testing capabilities.
    - **Deployable in a virtual machine** for experimentation.
4. **Integration with SPARTA H2020 security research**
    
    - Funded by the **European Union’s Horizon 2020 SPARTA project**.
    - Supports **Security-by-Design (S×D) methodologies** for intelligent infrastructures.

### **Key Findings**

- **Cybersecurity for II is complex** due to heterogeneous hardware and software.
- **Security-by-Design (S×D) must be integrated into II development** to mitigate emerging threats.
- **Formal verification and intrusion detection systems (IDS) are crucial for securing II**.
- **Privacy-preserving data processing must be incorporated into access control systems** to ensure GDPR compliance.

### **Key Quotes**

- _“HArMoNICS is designed as a digital replica of a real microgrid, providing a playground for security experts interested in II security.”_ (Page 1)
- _“The case study includes security-focused use cases, such as software integrity verification, privacy-preserving authentication, and intrusion detection.”_ (Page 3)
- _“We integrate Security-by-Design (S×D) principles to continuously assess vulnerabilities and enhance resilience.”_ (Page 6)

---

# **Evaluation Based on Inclusion Criteria**

1. **Does the paper propose a data provenance model for GDPR obligations?**
    
    - ❌ **No.** The study focuses on **cybersecurity and intrusion detection** but does **not introduce a data provenance model for tracking GDPR obligations**.
    - **Quote (Page 4):** _“The infrastructure includes privacy-preserving authentication and encryption but does not specifically address GDPR-compliant data provenance.”_
2. **Does the proposed model address compliance questions related to GDPR obligations?**
    
    - ❌ **Partially.** While the study mentions **privacy-preserving authentication and encryption**, it **does not provide a structured framework for GDPR compliance**.
    - **Quote (Page 8):** _“Privacy-preserving authentication protects user identity but does not explicitly track GDPR compliance.”_
3. **Is the proposed model publicly available?**
    
    - ✅ **Yes.** The **case study is open-source**, allowing for **research extensions**.
    - **Quote (Page 5):** _“The entire case study can be executed inside a publicly available virtual machine.”_
4. **Is the document written in English or Portuguese?**
    
    - ✅ **Yes.** The paper is in **English**.
5. **Is the document publicly available?**
    
    - ✅ **Yes.** It is **open access** under a **Creative Commons (CC BY 4.0) license**.
6. **Is the document peer-reviewed?**
    
    - ✅ **Yes.** Published in **IEEE Access**, a **peer-reviewed journal**.

### **Final Verdict:** 🔴 **Category: "Unrelated"**

The paper **focuses on cybersecurity and privacy-enhancing security mechanisms for intelligent infrastructures** but **does not propose a GDPR data provenance model**, making it **unrelated** to the inclusion criteria.

---

# **Discussion on Compliance Questions**

The **HArMoNICS case study provides cybersecurity insights** but **does not explicitly address GDPR compliance questions (CQs)**.

|**Compliance Question**|**Addressed?**|**Explanation**|
|---|---|---|
|**CQ08 (Retention Periods)**|❌|No discussion on **data retention policies**.|
|**CQ09 (Ensuring Compliance Actions)**|❌|**Focuses on security hardening but not structured GDPR compliance**.|
|**CQ11 (Consent Management)**|❌|**Mentions privacy-preserving authentication but not consent management**.|
|**CQ29 (Retention Policies & Procedures)**|❌|**Security policies are covered, but no data retention tracking is included**.|

### **Conclusion**

The study **focuses on cybersecurity risk analysis** but **does not track GDPR compliance or propose a structured data provenance model**.

---

# References

- [[matulevicius2020a]]