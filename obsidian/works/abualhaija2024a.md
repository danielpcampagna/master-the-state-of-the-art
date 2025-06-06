---
ID: abualhaija2024a
authors: Abualhaija, Sallam and Ceci, Marcello and Briand, Lionel
category: unrelated
display: "abualhaija (Legal Requirements Analysis: A Regulatory Compliance Perspective)"
due: This paper surveys existing approaches and explains the process behind the materialization of regulation towards software requirements that achieve compliance. It does not introduce or propose a new ontology model. However it serves as a middle of the path for explain the entirely process involved.
entrytype: chapter
link: https://arxiv.org/abs/2311.13871
name: "Chapter 11: Legal Requirements Analysis: A Regulatory Compliance Perspective"
organization: arXiv
place: ""
pp: 1–29
provenance_related: false
related:
  - legal compliance
  - AI-based question answering
  - GDPR
  - NLP-based compliance checking
year: "2024"
forward_steps: 2
---

# Summary & Analysis

## Abstract

This chapter offers a thorough overview of methods for legal requirements analysis in the context of regulatory compliance – mainly taking GDPR as an example. It depicts how software engineers can interpret regulations to extract compliance requirements (norms), represent them (via conceptual models, ontologies, or formal logic), and then perform automation-supported compliance checking.  
**Quotations**

1. “Software systems that collect, process, or share personal data are subject to compliance with such regulations [GDPR]. Developing compliant software depends heavily on addressing legal requirements.” (p. 1)
2. “In this chapter, we explore a variety of methods for analyzing legal requirements and exemplify them on GDPR.” (p. 1)

## Introduction

The chapter highlights the importance of legal requirements derived from relevant regulations (like GDPR) and how these can be systematically identified and managed during requirements engineering. The authors note that regulations are typically large and written in natural language, making them difficult to operationalize. They define key terminology such as “legal requirement,” “compliance checking,” “breach,” and introduce a simple example from GDPR Art. 33 on notifying supervisory authorities of personal data breaches.  
**Quotations**

1. “Legal requirements analysis entails creating machine-analyzable representations of legal text based on which automated analysis technologies can be developed.” (p. 2)
2. “We define compliance as the relationship between the specification of the system-to-be and the set of relevant legal norms.” (p. 2)

## From Regulations to Representation

This main part of the chapter delves into how to extract norms (or rules) from regulatory text and model them, be it with conceptual modeling, ontologies, or formal logic. They also discuss interpretative challenges (like bridging the gap between legal text and software requirements) and mention advanced modeling tools such as LegalRuleML for specifying compliance rules.  
**Quotations**

1. “Norms describe a desired reality... compliance means that the facts are aligned with these norms.” (p. 4)
2. “Representing legal provisions as norms is a complex activity, since it involves legal interpretation and unavoidably requires the disambiguation of legal concepts.” (p. 6)
3. “We can represent the same provision in different formats: e.g., natural language, UML-based conceptual models, or logic-based rule languages.” (p. 10)

## From Representation to Compliance

Having built a machine-readable representation, the chapter next shows how to perform automated question answering (QA) on the regulation using large language models. For compliance checking, the text discusses various strategies including semantic similarity measurements, classification-based approaches, rule-based matching, or verifying text-level “semantic roles” extracted from the input document against the representation of the regulation’s requirements.  
**Quotations**

1. “Navigating through regulations manually is time-consuming... we describe a recent approach, COREQQA, which leverages large language models for question answering.” (p. 15)
2. “A straightforward method is to measure semantic similarity between each legal requirement and each text segment in the input document.” (p. 24)

## Challenges

Finally, the authors point out open challenges: 1) Handling multiple regulations or cross-references, 2) Dealing with changes over time (legal temporal dimensions), 3) Balancing different representation approaches, 4) Achieving explainability. They note that these topics are all ripe for further research in the intersection of RE and legal informatics.  
**Quotations**

1. “The regulatory framework changes over time, and capturing this change is a prerequisite for ensuring the continuity of the system’s compliance.” (p. 28)
2. “Despite advances in AI, formal representations of the law must still be developed manually since it is a highly complex activity.” (p. 28)

# Evaluation Based on Inclusion Criteria

1. **Data Provenance Model for GDPR?**
    
    - The chapter mostly focuses on representation of GDPR obligations via conceptual models and formal logic. While it’s not strictly about “data provenance” models, it does propose how one might represent the flows or usage of personal data to ensure compliance, which is relevant.
2. **Useful for addressing compliance questions?**
    
    - Yes, it’s about systematically ensuring compliance with GDPR.
    - “We can represent data breach notification obligations, how data is processed, who is the actor, etc.” (p. 7)
3. **Publicly Available Model?**
    
    - The work provides several examples of conceptual models and a partial ontology for legal norms, but it’s mainly examples in the text. Not an entire publicly shared data model.
4. **Language**
    
    - In English.
5. **Is the Document Publicly Available?**
    
    - Yes, on arXiv.
6. **Peer-Reviewed?**
    
    - Not entirely clear. It's posted as a chapter on arXiv, so it might be in revision or appear in a published volume later. For the user’s selection, it’s presumably an academic text.

Hence, it’s relevant to compliance analysis but does not propose a data provenance model specifically.

# Discussion on Compliance Questions

- The chapter is about compliance with GDPR, so it touches on many obligations. But it doesn’t systematically address user’s “compliance questions” (CQ08, CQ09, etc.). Instead, it provides a general framework for bridging the gap between legal text and software requirements, mention that e.g. data breach obligations are from GDPR’s Art. 33.

It can help reason about those compliance questions but does not directly answer them.

# References

- [[torre2021a]]