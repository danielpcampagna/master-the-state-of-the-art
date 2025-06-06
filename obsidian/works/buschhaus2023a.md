---
ID: buschhaus2023a
authors: Buschhaus, Constantin and Butting, Arvid and Michael, Judith and Nitsch, Verena and Pütz, Sebastian and Rumpe, Bernhard and Stellmacher, Carolin and Theis, Sabine
category: unrelated
display: "buschhaus (Overcoming the Hurdle of Legal Expertise: A Reusable Model for Smartwatch Privacy Policies)"
due: Although this paper proposes a conceptual model for smartwatch privacy policies, which can be compared against other approaches dealing with data provenance and compliance, it does not directly connected with GDPR, which made difficult to compare the proposed model against the existing in literature.
entrytype: article (preprint)
link: https://ssrn.com/abstract=4701295
name: "Overcoming the Hurdle of Legal Expertise: A Reusable Model for Smartwatch Privacy Policies"
organization: SSRN
place: ""
pp: 1–19
provenance_related: false
related:
  - privacy policy conceptual model
  - GDPR compliance
  - smartwatch data
  - model-driven software engineering
year: "2023"
forward_steps: 2
---

# Summary & Analysis

## Overview

This paper tackles the issue of simplifying and structuring privacy policies for smartwatches in a machine-readable and developer-friendly format. The authors introduce a conceptual model, tested with a model-driven software engineering approach, that focuses on bridging the complexity gap between legal experts, software developers, and end users.  
**Quotations**

1. “To better communicate privacy policies for smartwatches, we need an in-depth understanding of their concepts and provide better ways to enable developers to integrate them when engineering systems.” (p. 1)
2. “We have analyzed the privacy policies of various manufacturers and extracted the relevant concepts.” (p. 1)
3. “This reusable privacy policy model can enable developers to easily represent privacy policies in their systems.” (p. 1)

## Introduction

The introduction situates the challenge: privacy statements for wearable devices are long, often confusing, and misaligned with user needs. Traditional privacy regulations (e.g., GDPR) describe many requirements at a high level, leaving open how to actually present them to developers and end users.  
**Quotations**

1. “It is necessary to provide privacy policies in a structured way, mainly when health-related data is collected, e.g. using smartwatches or other types of wearables.” (p. 1)
2. “There is a need for a conceptual model that captures relevant concepts from privacy policies and can be easily integrated into applications by developers.” (p. 1)

## Related Work

The authors highlight existing approaches to conceptual modeling of GDPR obligations but note a gap in terms of a structured model specifically targeting smartwatch privacy policies. They also bring in the concept of model-driven software engineering (MDSE) with MontiGem to demonstrate how these policies can be integrated as part of system generation.  
**Quotations**

1. “Existing work focuses either solely on the GDPR without considering privacy policies of smartwatches, e.g., for checking GDPR compliance.” (p. 2)
2. “We have used the generator framework MontiGem ... to create a platform for data visualization of wearable privacy policies from different smartwatch manufacturers.” (p. 3)

## Methodology

A five-step process was used to develop the conceptual model: analyzing actual smartwatch policies, aligning them with GDPR articles, verifying with lawyers, creating a class diagram, and instantiating it with Garmin and Fitbit data as a validation step.  
**Quotations**

1. “We applied a five-step process to identify and collect concepts from privacy policies and to better understand the characteristics of data processing that a conceptual model must consider.” (p. 5)
2. “Findings from the analysis were then evaluated ... with lawyers specialized in data protection.” (p. 5)

## The Proposed Conceptual Model

A UML-based conceptual model organizes data processing scenarios into classes: user region, contact persons, data categories vs. data entries, processing types (collecting, storing, transmitting, deleting, further processing), and legal basis. The structure also includes attributes such as timing, location, actor, and purpose.  
**Quotations**

1. “We do not guarantee that all instances of the model are legally compliant ... it is not in the focus of this conceptual model to be able to check individual instances against any legislation.” (p. 6)
2. “One big challenge for fitting the privacy policies of the various manufacturers into instances of the PPM was that they all differed in structure.” (p. 10)

### Model Highlights

- **PrivacyPolicy** object: Name, text, manufacturer, URL, date of effect, version, minimum user age, update policies.
- **Region**: Ties in contact persons (controllers, data protection officer), user rights.
- **DataProcessing** (abstract): Actor, location, data involved, purpose, legal basis, form of agreement, revocation info.
- **Subclasses**: CollectingData, StoringData, TransmittingData, DeletingData, and FurtherProcessingData.

**Quotations**

1. “Each privacy policy in the conceptual model has a name, a full text, the name of the manufacturer, etc.” (p. 6)
2. “When StoringData, data can be stored either for a fixed period or until an event occurs.” (p. 8)

## Example Application

They demonstrate how the conceptual model is used within MontiGem to generate a web-based platform for visualizing privacy policies. Users (e.g., data protection officers or developers) fill in forms reflecting the model; end users then see an interactive display of how their data is handled, for what purposes, on what legal basis, etc.  
**Quotations**

1. “Using input forms, smartwatch vendors can add their privacy policy to the platform. This privacy policy information is then visualized.” (p. 11)
2. “While this reduces the effort of managing rigid textual privacy policies, the given structure in our model also supports stakeholders’ compliance with the GDPR’s requirements.” (p. 11)

## Discussion

The authors point out that the biggest challenge is that actual text-based privacy policies do not always neatly map to these structures. Some details required by law or by user expectations aren’t always given or are found in separate sections. Furthermore, the model captures some optional or advanced concepts (e.g., encryption details) that may not always appear. Finally, the approach is best used with the cooperation of the companies behind these smartwatch solutions.  
**Quotations**

1. “Privacy policies only contain information about legal data transmissions and not technical ones ... privacy policies hardly contain information about how and where data is stored.” (p. 10)
2. “In addition to the preparatory functionalities for technical implementation, the conceptual model ... has the power to convey processes and interrelationships of data protection and raise awareness.” (p. 12)

## Conclusion

This work formalizes and validates a conceptual model for smartwatch privacy policies, showing how it can be used to store, compare, and present user data in a more standardized manner. The authors stress it’s not a compliance checker but a “foundation for more structured and understandable privacy policies,” hopefully leading to better user data sovereignty and developer clarity.  
**Quotations**

1. “The conceptual model can be used by other developers to handle information in privacy policies in a structured way in their development processes.” (p. 13)
2. “We have defined the concepts ... based on an analysis of the privacy policies of seven smartwatch manufacturers. ... The textual version of the conceptual model is then used in a MDSE approach to create a platform for further visualization.” (p. 13)

# Evaluation Based on Inclusion Criteria

1. **Data Provenance Model for GDPR Obligations?**
    
    - The paper provides a model to structure data flows and processing descriptions in privacy policies. While “provenance” is not the main term, the model indeed addresses who collects data, how it’s processed or transmitted, and for what purpose – much like a simplified provenance chain for personal data.  
        **Conclusion**: It’s relevant if your inclusion criteria can be extended to the modeling of data uses and flows under GDPR, though not a strict “data provenance” approach.
2. **Useful to Address Compliance Questions?**
    
    - The model focuses on structuring privacy policy content. It references GDPR articles and helps ensure certain GDPR items get covered. However, it doesn’t directly answer compliance questions (like retention or re-sought consent) except by letting the developer specify them in the model.  
        **Conclusion**: Could be used to help highlight compliance points, but does not directly solve them.
3. **Publicly Available Model**
    
    - The conceptual model is described in the paper and is presumably open to reuse. The authors mention a Zenodo link with the model.  
        **Conclusion**: Yes, it’s publicly shared.
4. **Language**
    
    - The paper is in English.
5. **Publicly Available?**
    
    - The preprint is on SSRN, presumably publicly available.
6. **Peer-Reviewed Document?**
    
    - Indicated as a preprint on SSRN. Possibly not peer-reviewed yet. Still, it’s an academic work, so it might not meet the “peer-reviewed” criterion strictly.

Hence, the paper can be classified as relevant to GDPR, but it doesn’t strictly propose an enforceable data provenance approach. It’s more of a conceptual structuring for privacy policies, so it’s borderline if you want a strict data provenance model for compliance. However, it’s definitely in the realm of privacy compliance modeling.

# Discussion on Compliance Questions

**CQ08 (Retention Period)**  
They allow for storing data with either a fixed time or until a certain event. So the model can capture retention periods, but the text acknowledges that many actual policies do not specify them clearly.

**CQ09 (Actions for Compliance, e.g., Deleting Data)**  
The model’s DeletingData object can represent data erasure in the policy. So it helps represent the user’s right to erasure.

**CQ11 (Re-sought Consent)**  
The model references optional, mandatory, or function-based agreements, but doesn’t extensively detail re-seeking consent. Developers can still add text about re-consent in the “revocation” fields.

**CQ17, etc.**  
They do not systematically address every compliance question in detail but do note that their model covers contact persons, user rights, and other relevant data.

In short, it’s consistent with general GDPR requirements (like legal basis, data subject rights, and so forth). However, it’s a high-level foundation rather than a question-by-question compliance check.

---

# References

- [[torre2021a]]