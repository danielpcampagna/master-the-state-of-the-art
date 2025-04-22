---
ID: dagg2022a
authors: Dagg, Niall and Kostick, Conor and Fallon, James and O’Neill, Alex and Yilmaz, Murat and Messnarz, Richard and Clarke, Paul M.
category: ok
display: "dagg (Socially-Critical Software Systems: Is Extended Regulation Required?)"
due: Although this paper focuses on data collection ethics, it also details aspects relevant to GDPR obligations and possible future regulation scenarios of software. It can be compared against other approaches dealing with provenance or compliance.
entrytype: conference
link: ""
name: "Socially-Critical Software Systems: Is Extended Regulation Required?"
organization: EuroSPI
place: Conference on Software Process Improvement and Innovation
pp: ""
provenance_related: false
related:
  - data ethics
  - data collection methods
  - privacy regulations
  - socially-critical software
year: "2022"
forward_steps: 2
---

# Summary & Analysis

## Abstract and Aims

This paper explores how data has become a “commodity” in contemporary society, focusing especially on web-based applications (websites) that gather personal data. Through a multivocal literature review, the authors detail how data is collected, the purposes of that collection, associated ethical considerations, and potential future directions. They then propose an idea of classifying certain data-harvesting applications as “socially-critical” to regulate them more thoroughly before market release.  
**Key Quotations**

1. “Data has become a prevailing aspect of our daily lives... it is a commodity in today’s world.” (p. 1)
2. “We introduce the concept of socially-critical applications, where data harvesting in web-based applications might require pre-market disclosure and evaluation by notified bodies (instructed by regulation).” (p. 1)
3. “The primary aim of this research is to contribute to the understanding of data collection in software-based systems and implications for privacy and ethical consideration.” (p. 2)

## Introduction

The authors note that the volume of data being collected through web-based technologies has soared, and this trend raises concerns about privacy, ethics, and regulation. They highlight that many aspects of data collection and usage may be invisible or complex to end users.  
**Key Quotations**

1. “Web applications... can be accessed through a web browser... data can be accessed and collected... for various means.” (p. 1–2)
2. “One of the major ways data is produced and collected is from the use of websites and web-based applications.” (p. 1)

## Research Methodology (Multivocal Literature Review)

The authors used a multivocal literature review (MLR), combining both scholarly (“white”) and non-peer-reviewed (“grey”) sources (p. 2). They identified four core research questions addressing: (1) how data is collected, (2) how it is used, (3) the ethical ramifications, and (4) future directions.  
**Key Quotations**

1. “This research employed a Multivocal Literature Review (MLR) [36].” (p. 2)
2. “We limited the search to papers published from 2015 onward... 34 papers were determined relevant.” (p. 2)

## Analysis of Findings

1. **RQ1: How data is collected in web-based applications**
    
    - Cookies (first-party and third-party), forms, surveys, and user logins are dominant methods.
    - Discussion of consent forms, GDPR, and the phenomenon of “dark patterns” in user interface design that nudge or mislead users into sharing data.  
        **Key Quotations**
    - “There is some doubt regarding whether these consent forms faithfully implement the GDPR...” (p. 3)
    - “A significant concern surrounds the finding that 92% of websites still use some form of tracking without a user’s consent.” (p. 3)
2. **RQ2: How data is used by websites/companies**
    
    - Data monetization: direct (selling data) vs indirect (using data insights to drive targeted ads, personalization, product improvements).
    - Companies such as Meta, Amazon, and Apple are data-driven.  
        **Key Quotations**
    - “Data can be used... to personalise user experiences, to encourage healthier lifestyles, to measure business performance... and for advertisement targeting.” (p. 4)
    - “Data monetisation... can be established by selling information-based products and services.” (p. 5)
3. **RQ3: Ethical considerations of data collection**
    
    - The paper highlights compliance with GDPR, user privacy rights, the issue of “dark patterns,” and the tension between corporate profit and user welfare.
    - The authors note that “users do not always know their data rights; some might not seem to care.” (p. 7)  
        **Key Quotations**
    - “It has furthermore been suggested that it is up to the companies that own the web applications to take a moral responsibility for user data...” (p. 5)
    - “Privacy rights include the Right to be Forgotten, the Right of Access to Data, the Right to Data Portability, and the Right to Explanation.” (p. 6)
4. **RQ4: Future directions for data collection**
    
    - Data volumes will continue to expand, fueling big data analytics, NoSQL databases, artificial intelligence, and new business models.
    - Potential for user pushback if data usage is perceived as exploitative.
    - Discussion of biases in large datasets (population bias, activity bias).  
        **Key Quotations**
    - “Companies... will continue to do so as web-based activity is continuing to climb.” (p. 7)
    - “One potential solution... might involve technology companies disclosing their future technical ambitions and designs to regulators prior to deploying them to the market.” (p. 9)

## Conclusion and Proposed “Socially-Critical” Systems

The authors argue that regulators often lag behind rapidly evolving technology. They suggest a new software classification—“Socially-Critical Applications”—that would be subject to a pre-market evaluation stage, similar to the certification of safety-critical systems, to ensure user interests are protected.  
**Key Quotations**

1. “If a new classification of software application was to be created, the Socially-Critical Application, then software systems matching this classification might be subject to a type of pre-market evaluation.” (p. 10)
2. “Suggesting that a new classification of software application be legally established... is a bold move.” (p. 10)

---

# Evaluation Based on Inclusion Criteria

1. **Data Provenance Model for GDPR Obligations?**
    
    - The paper does not propose a detailed data provenance model. Instead, it focuses on ethics, user data usage, and potential regulatory frameworks. While GDPR is addressed, the paper does not introduce a formal or systematic “provenance” representation.
    - “We introduce the concept of socially-critical applications, where data harvesting in web-based applications might require pre-market disclosure...” (p. 1). This is more about extended regulation than building a fine-grained provenance model.  
        **Conclusion**: It does not strictly present a data provenance model. It discusses data collection/usage, ethical concerns, and regulation, but not a model for representing or tracking data provenance in alignment with GDPR obligations.
2. **Model Useful to Address the Compliance Questions?**
    
    - Though it addresses user consent, privacy concerns, potential future frameworks, etc., the paper focuses on policy-level discussions and “pre-market” regulation. It does not outline how to represent or query compliance details.
    - Therefore, it is not directly applicable for answering specific compliance questions in a structured manner (like retention periods, data subject rights, etc.).  
        **Conclusion**: Provides broad ethical and regulatory insights but does not detail a model that addresses the compliance queries.
3. **Publicly Available Model?**
    
    - This paper does not provide any formal or publicly shared model. Instead, it presents conceptual proposals (like “socially-critical” classification).
4. **Language**
    
    - The paper is written in English.
5. **Document Publicly Available?**
    
    - It appears to be a conference paper, presumably accessible from standard academic sources. Possibly published in the EuroSPI context.
6. **Peer-reviewed**
    
    - EuroSPI is a peer-reviewed conference, so this is presumably peer-reviewed.

**Overall**: The paper does not propose a data provenance model nor does it extensively detail how to systematically represent the data or compliance with GDPR. Its emphasis is on conceptual regulation proposals (especially the “socially-critical” approach), data ethics, and broad data collection usage patterns.

Hence, regarding strict compliance with the user’s data-provenance inclusion criteria, **it does not meet** the primary requirement (#1: “The approach should strictly propose a data provenance model to represent activities information related to GDPR obligations”). It merely analyzes data ethics, user data usage, the future of data regulation, and the possibility of pre-market app disclosures. We classify it as “ok” because it addresses GDPR tangentially and might be relevant to a broader conversation on regulatory compliance, but **it does not provide a provenance model**.

---

# Discussion on Compliance Questions

Below, we relate the paper’s content to the specific compliance questions (CQ08, CQ09, etc.). The paper addresses data usage, user rights, and possible pre-market regulation in general terms; it **does not** provide explicit guidance on each compliance question but offers some relevant points on data ethics and user consent.

1. **CQ08 (Retention Period)**
    
    - The paper does not specifically propose any system or approach to define or enforce data retention periods. The mention of GDPR indicates that data usage must be lawful and transparent, but there is no detailed mechanism for setting or verifying retention periods.
2. **CQ09 (Identify required actions, e.g., delete data if no further purpose)**
    
    - The paper recognizes user privacy and the right to be forgotten, but does not detail how a system can track or delete data. It mostly notes that an ethical approach and compliance with GDPR are needed.
3. **CQ11 (Re-sought individual’s consent)**
    
    - The paper discusses how user consent can be manipulated via “dark patterns,” but does not propose explicit solutions for re-seeking consent.
4. **CQ17 (Respond to SARs within 1 month)**
    
    - This aspect (subject access requests) is only briefly touched on by referencing GDPR’s user rights. The paper does not propose a systematic approach or any specific timeline management system.
5. **CQ20, CQ21, CQ25, CQ28, CQ29, etc.**
    
    - Similar to the above, the paper references general GDPR rights and how data might be misused, but it provides no direct method to address these. It frames them as known responsibilities that are not always well-enforced due to the rapid evolution of technology.
6. **CQ37, CQ38, CQ39, etc.**
    
    - The paper highlights the difficulty in user understanding and user interface manipulations, citing how large-scale data usage is often hidden behind complicated privacy policies. However, it does not propose explicit compliance solutions.
7. **CQ40–CQ44 (DPO requirements)**
    
    - Not mentioned.
8. **CQ47–CQ49, CQ50–CQ52 (Security Requirements)**
    
    - Security is only generally acknowledged; no specific processes are proposed.
9. **CQ56–CQ58 (Incident/Breach Documentation and Cooperation)**
    
    - Not discussed beyond a brief mention that regulators are overwhelmed.
10. **CQ63–CQ65 (Transfers)**
    

- This dimension (international data transfers, compliance basis) is not specifically addressed.

In short, **the paper** does not provide the detail necessary to systematically address or document how a system might comply with these enumerated compliance questions. Instead, it discusses the broader context in which data might be used unethically or untransparently and suggests a potential approach to more robust oversight. The proposed classification of “socially-critical software” could eventually force compliance discussions on many of these questions, but the paper itself does not answer them in detail.

---

# References

- [[torre2021a]]