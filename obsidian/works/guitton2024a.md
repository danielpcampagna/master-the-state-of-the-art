---
ID: guitton2024a
authors: Guitton, Clement and Mayer, Simon and Tamò-Larrieux, Aurelia and Garcia, Kimberly and Fornara, Nicoletta
category: unrelated
display: guitton (A Proxy for Assessing the Automatic Encodability of Regulation)
due: This paper proposes a method to measure feasibility of automated encoding of regulations; it does not present a GDPR data provenance model. Hence it is not included.
entrytype: inproceedings
link: https://doi.org/10.1145/3614407.3643697
name: A Proxy for Assessing the Automatic Encodability of Regulation
organization: ACM (CSLAW '24)
place: Boston
pp: 1-11
provenance_related: false
related:
  - APR
  - NLP
  - Sentence complexity
  - Word complexity
  - Encodability
year: 2024
forward_steps: 2
---

# Summary & Analysis

## Introduction & Motivation

This paper examines whether, and how, regulatory texts such as laws or articles of the GDPR can be automatically encoded into “automatically processable regulation” (APR). The authors observe that while manual efforts to encode certain rules into machine-understandable formats have succeeded in limited contexts, many parts of legal texts contain open-textured or vague language that is difficult for machines to interpret unambiguously. They propose a novel approach that uses **natural language processing** (NLP) pipelines to compute two metrics – _sentence complexity_ and _word complexity_ – with the aim of approximating how feasible it is to turn a particular clause (or entire piece of legislation) into APR.

**Key Points**

1. **Automatic Encodability of Regulation**. Although pockets of research and pilot projects have tried to create APR manually, a key open question is whether an automated pipeline could do this at scale.
2. **Two-Dimensional Measure**. The feasibility measure is twofold:
    - **Sentence Complexity** attempts to determine how difficult it is to parse each legal clause into syntactically simpler sub-sentences that can be mapped to ontology-like triples.
    - **Word Complexity** evaluates how many terms in the text can be mapped, with relatively high confidence, to known concepts in public legal ontologies or domain vocabularies.
3. **Methodology**.
    - **Relation Extraction** (Graphene). The authors use an NLP system (Graphene) to simplify sentences into <subject, relation, object> components and measure ratio-based features of the parse result.
    - **Entity Linking** uses a curated set of legal ontologies (e.g., LKIF, ELI, IATE) and general knowledge bases (Wikidata) to see if tokens have recognized definitions.
    - **Heuristics**. The paper defines custom heuristics to flag if/then terms (e.g., “provided that”), legal effect terms (e.g., “shall”), references, or open-textured/vague tokens (e.g., “reasonable,” “periodically”).
    - **Combining Metrics**. Each clause is assigned a “sentence complexity” score (the ratio of how easily sub-sentences can be extracted) and a “word complexity” score (the fraction of tokens not confidently recognized). These two values are plotted in a 2D space to classify whether a clause is likely “encodable,” “difficult,” or “uncertain.”
4. **Empirical Results**.
    - The authors illustrate the system on the GDPR, on multiple additional regulations, and on short legislative acts that were successfully encoded manually by state agencies. They show that the method aligns broadly with how experts might judge the presence of open-textured language in, e.g., a “Charter of Fundamental Rights.”
    - Overall, even in well-defined regulations, only a modest fraction of clauses fell into the “encodable” region of the two-axis measure, suggesting that automated derivation of machine-executable rules from typical laws is still limited.

---

# Evaluation Based on Inclusion Criteria

1. **Strictly propose a data provenance model for GDPR obligations?**
    
    - **No.** The paper does _not_ introduce a data provenance or lineage model. It presents a measure of how automatically “encodable” a legal text is by analyzing textual complexity and referencing external ontologies.
    - **Reference**: “We propose an algorithm that first gauges sentence complexity [...] in addition, the algorithm assesses word complexity by attempting to link terms to supposed functional requirements [...]” (p. 1)
2. **Useful to address the user’s compliance questions?**
    
    - The paper focuses on measuring how feasible it is to automatically turn legal text into machine-processable format. While it mentions some references to GDPR articles, it does _not_ detail how to answer questions about data retention, user rights, or DPO appointment.
    - **Reference**: “We apply our methodology to several legislations [...] with the assumption that they are less encodable due to the many open-textured terms.” (p. 1)
3. **Proposed model publicly available?**
    
    - The authors mention an implementation in Java is available on GitHub. They do not publish a stable “data provenance” model nor do they specify an official release for regulatory compliance.
    - **Reference**: “The algorithm is implemented in Java and [...] the implementation is available [...].” (p. 6)
4. **Document in English or Portuguese?**
    
    - The paper is written in English.
5. **Publicly accessible from digital libraries?**
    
    - The reference says it is from the “Symposium on Computer Science and Law (CSLAW ’24), Boston, MA, USA.” It likely is accessible via the ACM library.
6. **Peer-reviewed?**
    
    - Yes, it appears in a formal proceedings of CSLAW, an ACM conference, so presumably peer-reviewed.

**Conclusion**  
The paper is a technical study on using NLP to compute an “automated encodability score” of legal texts. It does _not_ propose or present a data provenance model for GDPR obligations. Hence, it is **unrelated** under the user’s strict “provenance model” criterion.

---

# Discussion on Compliance Questions

The paper’s approach or method does not specifically handle the user’s compliance queries such as data retention (CQ08), data subject rights, or DPO appointment. It focuses on analyzing the raw text of regulations for complexity in terms of potential automation. The authors do reference the GDPR (Article 7(1)) as an example, but they do not systematically address the user’s enumerated compliance questions (CQ08–CQ65). They do not mention direct solutions or explicit coverage of those queries.

---

# References

- [[bonatti2020a]]