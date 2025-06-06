---
ID: cambronero2024a
authors: Cambronero, M. Emilia and Martínez, Miguel A. and Llana, Luis and Rodríguez, Ricardo J. and Russo, Alejandro
category: unrelated
display: cambronero (Towards a GDPR-compliant cloud architecture with data privacy controlled through sticky policies)
due: The paper proposes a UML-based approach for cloud data tracking and privacy using sticky policies, which can be compared against other data provenance models. However, it does not improve the semantic model or
entrytype: article
link: https://peerj.com/articles/cs-1898.pdf
name: Towards a GDPR-compliant cloud architecture with data privacy controlled through sticky policies
organization: PeerJ Computer Science
place: PeerJ Computer Science
pp: 1-44
provenance_related: true
related:
  - UML profiling
  - sticky policies
  - GDPR compliance
  - cloud architecture
  - data tracking
  - Implementation
year: "2024"
forward_steps: 2
---

# Summary & Analysis

## Abstract

The paper addresses the challenge of designing a cloud architecture that complies with the General Data Protection Regulation (GDPR) by introducing a model-driven engineering framework called MDCT. This framework relies on a UML profile to guide the design of GDPR-compliant cloud systems, integrates sticky policies for data privacy and tracking, and uses OCL rules to validate compliance.  
**Quotations**

1. “In this article, we want to help cloud providers comply with the GDPR by proposing a GDPR-compliant cloud architecture.” (p. 1)
2. “For this purpose, sticky policies associated with the data are incorporated to define permission for third parties to access the data and track instances of data access.” (p. 1)
3. “Our tool models key GDPR points such as user consent/withdrawal, the purpose of access, and data transparency and auditing, and considers data privacy and data tracking with the help of sticky policies.” (p. 1)

## Introduction

The introduction discusses the increasing need for data privacy in cloud environments, particularly when adhering to the GDPR. It highlights how the GDPR affects organizations inside and outside the EU, forcing cloud providers to adapt their offerings to ensure compliance. The authors outline the major contributions of the work, including how the solution incorporates UML profiling for modeling GDPR interactions.  
**Quotations**

1. “Data privacy was a major concern among scientists before the publication of the General Data Protection Regulation (GDPR).” (p. 2)
2. “In 2021, the European Commission identified cloud computing as a key vulnerability area.” (p. 2)
3. “Understanding how cloud providers comply with the GDPR represents a key challenge for established and newly emerging providers.” (p. 2)

## Literature Review

The authors provide a survey of related approaches that either model privacy and GDPR aspects or study compliance in cloud scenarios. They emphasize how their work is distinct in that it specifically uses UML profiling plus sticky policies to track data usage and enforce compliance in a systematic manner.  
**Quotations**

1. “Some other works only focus on some specific aspects of the GDPR.” (p. 4)
2. “Our profile covers SaaS and IaaS by using UML sequence and component diagrams to model the cloud infrastructure and cloud interactions, respectively.” (p. 6)
3. “In summary, none of the cited works model the cloud system using UML or incorporate data tracking as we do in our work.” (p. 7)

## Background

This section outlines the relevant concepts of GDPR, sticky policies, and UML. The GDPR portion explains the roles (data subject, controller, processor), as well as the lawful basis of personal data processing, data subject rights, and the idea of privacy by design. Sticky policies are introduced as mechanisms to attach usage permissions and obligations directly to the data. The overview of UML underscores the usage of sequence diagrams, component diagrams, profiling, and OCL for specifying and validating constraints.  
**Quotations**

1. “The GDPR is a regulation, which means that it applies directly to its recipients ... it also affects any non-EU organization that handles the data of European citizens.” (p. 9)
2. “A sticky policy defines a set of conditions and restrictions attached to data that describe how the data should be treated.” (p. 10)
3. “OCL provides a precise textual language for model validation by expressing constraints that cannot be shown diagrammatically in UML.” (p. 11)

## Running Example

A motivating example describes how a business consultancy, GestF, accesses user data stored in a GDPR-compliant cloud architecture, using sticky policies to grant or restrict access. They illustrate how data ownership and permissions evolve when combining personal data from multiple sources for distinct purposes (e.g. statistical vs. tax).  
**Quotations**

1. “We consider five main fields in the sticky policies: permission, owner, purpose, controller, and accessHistory.” (p. 14)
2. “Once GestF has permission to access the data, it can access it for two different purposes: statistical or tax.” (p. 14)
3. “In this case, GestF reads the data of the interested party and calculates the average of the salaries of the employees, which is aggregated data.” (p. 15)

## Methodology

The methodology describes the three main phases of the MDCT framework: (1) Modeling phase—defining the cloud architecture and UML profile, (2) Validation phase—enforcing constraints via OCL rules, and (3) Recommendation phase—finalizing the GDPR-compliant cloud design for providers.  
**Quotations**

1. “The main objective of our framework is to define recommendations that allow cloud providers to create a stateless computing architecture in the cloud that complies with the GDPR.” (p. 17)
2. “For this purpose, we have had the support of expert GDPR consultants.” (p. 18)
3. “If errors are detected, they must be corrected, and we return to the previous phase (Phase 1. Modeling phase) to correct them.” (p. 18)

## Modeling Data Tracking in Cloud Systems

Here the authors define the UML sequence diagrams that capture user and third-party interactions, data combination rules, and the role of sticky policies. A specific UML profile (Model4_DataCTrack) includes stereotypes for capturing privacy constraints, machine types, and compliance parameters.  
**Quotations**

1. “We first look at the interaction model, showing the UML sequence diagrams that allow us to model the interaction between the different roles in the system.” (p. 19)
2. “Permissions are DC labels: tuples of the form ⟨S, I⟩, where S and I are conjunctive normal forms on entities without negative literals.” (p. 27)
3. “This section resulting describes Model4_DataCTrack and its validation in detail.” (p. 19)

## Validation and Threat Model

The authors introduce OCL constraints that ensure models comply with GDPR obligations, e.g., verifying that data purpose fields are properly specified or that user consent is present before third-party access. They also discuss threats to validity, such as subjective interpretation of certain GDPR articles.  
**Quotations**

1. “We define a set of OCL (Object Management Group (OMG), 2014) rules, which allows us to detect errors and warnings in the model.” (p. 18)
2. “A potential threat to internal validity is that we have interpreted the text of the GDPR provisions to create a cloud architecture.” (p. 38)
3. “Our model is publicly available.” (p. 38)

## The MDCT Tool

This section introduces a Papyrus-based software tool that supports the proposed approach. It enables practitioners to build UML diagrams, apply the specialized stereotypes, and run the OCL validation. The code is open source and hosted on GitHub.  
**Quotations**

1. “Our tool is publicly available, and its source code has been released under the GNU/GPLv3 license.” (p. 3)
2. “We have also implemented a software tool that supports MDCT.” (p. 3)
3. “The UML profile and the OCL rules have been integrated into a complete framework named Modeling Data Cloud Tracking (MDCT).” (p. 3)

## Discussion

The paper discusses how the proposed cloud architecture accommodates privacy by design, ensures GDPR compliance, and addresses potential challenges for real-world adoption. The authors also mention possible integration with other regulatory domains.  
**Quotations**

1. “In this article, we do not explicitly model the supervisory authority as a role in the system as we consider it to be an element outside our cloud architecture.” (p. 38)
2. “Thus, we can conclude that certain recommendations be given to the entity responsible for data security (the controller) to define its architecture in the cloud.” (p. 38)
3. “We cannot rule out subjectivity, but we do provide our interpretation accurately and explicitly.” (p. 38)

## Conclusions and Future Work

The authors conclude that their approach is a step towards embedding GDPR compliance into cloud designs by default. Their toolset (MDCT) allows for implementing sticky policies and verifying compliance. Future directions include exploring additional GDPR requirements, real-world pilot programs, and expansions to handle other regulatory regimes.  
**Quotations**

1. “This article introduces the MDCT computer-aided design framework.” (p. 39)
2. “The profile models key GDPR considerations such as user consent/withdrawal, the purpose of access, and data transparency and auditing.” (p. 39)
3. “Future studies exemplifying our model in different cloud domains ... will be critical in deciding the completeness and applicability of our framework in real-world scenarios.” (p. 38)

# Evaluation Based on Inclusion Criteria

1. **Proposes a Data Provenance Model to Represent Activities Information Related to GDPR Obligations**
    
    - The paper presents a UML-based model architecture that focuses on data privacy and data tracking in the cloud, employing sticky policies to track how data is accessed and used. This indeed represents user activities related to GDPR obligations, including data subject rights and the roles of controller and processor.
    - “This profile covers SaaS and IaaS by using UML sequence and component diagrams to model the cloud infrastructure and cloud interactions, respectively.” (p. 6)
    - “Our proposal addresses data privacy by introducing sticky policies, allowing third-party access control through precise data permissions.” (p. 3)
2. **Model Useful to Address the Compliance Questions**
    
    - The authors systematically incorporate aspects such as user consent, data transparency, purpose specification, and auditing through OCL rules. This alignment directly speaks to many of the GDPR compliance questions about retention, restriction, erasure, etc.
    - “In addition, the use of sticky policies allows our framework to track user data throughout their entire life-cycle.” (p. 17)
3. **Model is Publicly Available**
    
    - The UML profile and the tool (MDCT) are publicly available in an open-source repository.
    - “Our tool is publicly available, and its source code has been released under the GNU/GPLv3 license.” (p. 3)
4. **Document in English or Portuguese**
    
    - The paper is in English and is published in a peer-reviewed venue (PeerJ Computer Science).
5. **Publicly Accessible Document**
    
    - The paper is available under PeerJ, an open-access publisher.
    - “Distributed under Creative Commons CC-BY 4.0.” (p. 2)
6. **Peer-reviewed Document**
    
    - Published in PeerJ Computer Science, indicating peer review.

Hence, it meets the inclusion criteria.

# Discussion on Compliance Questions

Below is a brief discussion of how the paper addresses each compliance question (CQ). The paper’s approach is mostly about a UML-based model for data tracking and privacy; it does not explicitly enumerate the compliance questions, but we can assess if the approach can incorporate each:

## CQ08: Retention Period for Personal Data

- The proposed model includes a maximum time for storing data in the SLA and sticky policy fields. “In particular, we develop a complete framework ... to define permission for third parties to access the data and track instances of data access.” (p. 1) This sets an expiration time for data in the system, helping manage data retention.

## CQ09: Identify Actions for Compliance (e.g., Deleting Data)

- The framework allows user-initiated deletion of data and an enforced time-based deletion. “The user can order the removal of its data ... the controller searches for all the possible machines ... to erase them.” (p. 23) This covers data removal obligations.

## CQ11: Re-sought Consent if Not Up to GDPR Standard

- Consent is a key component of the architecture: “In our architecture, when a third party wants to access the data and does not have permission to do so, the user’s consent must be requested.” (p. 38) The model can be updated if older consent does not meet standards.

## CQ17: Respond to Subject Access Requests (SARs) within One Month

- The paper highlights user rights to rectification, erasure, and consent withdrawal. The architecture includes a dedicated log to quickly retrieve data usage details. “We have a log that saves all data accesses, and this log contains the actions on the user’s data.” (p. 7)

## CQ20: Halt Processing if Restriction is Valid

- By updating the sticky policy with new restrictions, the framework can effectively suspend or limit further processing. “The user wants to add new restrictions to its data policy (the user wants to add new restrictions condition).” (p. 23)

## CQ21: Right to Object

- The user can disallow further processing by removing or restricting access to their data in the sticky policy. “The user can withdraw consent at any moment ... to change their access permissions.” (p. 23)

## CQ25: Document Circumstances of Lawful Restrictions

- The model does not explicitly mention if these circumstances are recorded, but sticky policies can define constraints for lawful access. “We define ... specific permission for third-party access and the path followed by data.” (p. 1)

## CQ28/CQ35: Procedures to Keep Data Accurate

- Data can be rectified: “The user sends the message rectifyData ... the data must be updated on all the machines where it is stored.” (p. 23)

## CQ29/CQ30: Retention Policies and Minimum Retention Requirements

- As with CQ08, the model sets maximum storage time. Any minimum retention required by sectoral regulations can also be integrated into the sticky policy logic.

## CQ32: Avoid Unnecessary Duplication

- The usage of a “controller log” and standardized approach to data flows fosters consistency. Redundant copies can be tracked and removed when not necessary.

## CQ33: Transparent, Plain-Language Data Usage Info

- The architecture uses UML diagrams to specify how data is processed. The authors mention that the user is informed about the controller’s identity and the data’s retention time. “...the controller must inform the user (info message) about the period for which data will be stored.” (p. 19)

## CQ37/CQ38: Proactive Information on GDPR Rights; Easy Accessibility

- The paper models user interactions to retrieve info about their data and who is accessing it: “The user wants information about the data management.” (p. 22)

## CQ39: Third-Party Agreements

- The SLA is used between the controller and the processor for compliance. Sticky policies ensure that third parties must request permission. “Hence, the data will be stored and processed on that machine. These contracts are defined according to Article 13.2 GDPR.” (p. 19)

## CQ40–CQ44: Data Protection Officer (DPO) Requirements

- The paper does not explicitly mention the DPO role or contact details, focusing on the cloud architecture perspective. The model can be extended to incorporate such roles.

## CQ47–CQ49, CQ50–CQ52: Security Safeguards, Encryption, Incident Handling

- The approach focuses on data usage and tracking more than internal security controls. However, the design fosters “safe and secure data management and tracking in the context of the cloud.” (p. 1) Sticky policies can incorporate encryption or security obligations.

## CQ56–CQ58: Reviewing Plans, Documenting Breaches

- The architecture includes a subscription mechanism for breach notifications but does not detail deep incident management. “We propose a controlled cloud architecture ... to ensure an adequate level of protection according to the GDPR.” (p. 3)

## CQ63–CQ65: International Transfers

- The paper references that the architecture can handle machines “that may or may not be in members of the EU” (p. 38). The authors rely on the GDPRCompliance field to ensure non-EU machines meet adequate protection standards. That said, it is not an exhaustive solution for all cross-border data transfer obligations.

Overall, the MDCT approach can be extended or specialized to address each compliance question, mainly through the sticky policy mechanism, user consent flows, and OCL-based validations.

# Results

- The document is relevant to data provenance / data tracking for GDPR compliance.
- Publication year: 2024, PeerJ Computer Science.
- Authors: “Cambronero, M. Emilia and Martínez, Miguel A. and Llana, Luis and Rodríguez, Ricardo J. and Russo, Alejandro”
- The approach is indeed publicly available, in English, peer-reviewed, and can be used as a model for provenance-like tracking.

---

# References

- [[matulevicius2020a]]