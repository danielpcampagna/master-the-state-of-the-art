---
ID: kurteva2024a
authors: Kurteva, Anelia and Chhetri, Tek Raj and Pandit, Harshvardhan J and Fensel, Anna
category: unrelated
due: This paper surveys semantic technologies for consent representation and management but does not propose a data provenance model for GDPR compliance activities.
entrytype: article
link: https://doi.org/10.3233/SW-210438
name: "Consent through the lens of semantics: State of the art survey and best practices"
organization: University of Innsbruck, Trinity College Dublin
place: Semantic Web Journal
pp: 647–673
year: 2024
forward_steps: 2
---

# Kurteva, Anelia et al. Consent through the lens of semantics: State of the art survey and best practices. 2024.

## Approach and Motivations

This paper provides a **state-of-the-art survey** of existing **semantic web technologies** that implement **consent mechanisms** under GDPR. The authors analyze how **ontologies** and **knowledge graphs** are used for **consent representation, visualization, and management**, particularly focusing on solutions incorporating **blockchain technology**.

While this survey explores methods for **structuring and reasoning over consent records**, it does **not propose a provenance model** that systematically captures and represents **activities information** related to **GDPR obligations**.

## Approach Contribution For The Compliance Questions

The paper does not provide a **direct answer** to GDPR **compliance questions (CQ08 - CQ65)**, as it does not propose a provenance model. However, some of its insights on **semantic models** and **consent ontologies** may be indirectly relevant to **GDPR accountability and transparency**.

### **Question 11**: Re-seeking Consent for GDPR Compliance
- The paper discusses **models** for tracking **consent revocation and re-authorization** (p. 650).
- Various **ontologies** (e.g., GConsent, PrOnto) provide **machine-readable structures** for consent records.

### **Question 20**: Halting Data Processing upon User Request
- The reviewed semantic models facilitate **automated policy enforcement** for consent withdrawal (p. 653).
- However, the paper does not address how data **processing activities are tracked over time**.

### **Question 33**: Transparent and Accessible Consent Information
- A key contribution of this work is its review of **graphical consent visualization tools** (p. 657).
- The study highlights tools such as **CoRe and CURE**, which aim to improve user understanding of consent mechanisms.

### **Question 51**: Systematic Erasure of Personal Data
- Some of the discussed solutions integrate **blockchain-based compliance tracking** (p. 662).
- However, **immutability of blockchain contradicts the GDPR right to erasure**, which remains an unresolved issue.

### **Question 63**: Listing All Data Transfers
- The study reviews **knowledge graphs** that can **track** data-sharing activities (p. 664).
- However, it does not **propose a specific framework** to ensure **comprehensive tracking of data flows**.

## Approach Insufficiencies For Fulfilling The Compliance Questions

The paper does **not** propose a **data provenance model**, which limits its direct applicability for GDPR **compliance tracking**.

### **Key Deficiencies:**
1. **No provenance model** for capturing **activity logs** related to GDPR obligations.
2. **Focuses on consent**, but **not on the complete data lifecycle**.
3. **Limited discussion** on **GDPR-mandated retention policies** (CQ08, CQ29).
4. **No implementation of a structured compliance framework**.
5. **No discussion of provenance in a legal or regulatory context**.

## Key Contributions

- **Survey of Consent Ontologies:** Evaluates existing **semantic models** for tracking **consent records**.
- **Review of Consent Visualization Tools:** Explores **graphical representations** that improve **user awareness**.
- **Discussion of Blockchain for GDPR:** Identifies **conflicts** between **blockchain immutability** and **GDPR compliance**.

## State-of-the-Art

This paper consolidates prior research on **GDPR-compliant consent tracking** and provides insights into emerging trends in **semantic technologies** for legal compliance. However, it **lacks a concrete model** for addressing **GDPR provenance requirements**.

## Conclusion

While this paper offers valuable insights into **semantic models for consent**, it does not meet the **inclusion criteria** for a **data provenance model** that explicitly supports **GDPR compliance tracking**. Consequently, it has been categorized as **"unrelated"**.

# References

- [[bartolini2015b]]
- Kurteva, A., Chhetri, T. R., Pandit, H. J., & Fensel, A. (2024). Consent through the lens of semantics: State of the art survey and best practices. *Semantic Web*, 15, 647–673. https://doi.org/10.3233/SW-210438
- [[fatema2017a]]