---
ID: leone2020a
authors: Leone, Valentina and Di Caro, Luigi
category: unrelated
display: leone (The Role of Vocabulary Mediation to Discover Relevant Information in Privacy Policies)
due: This paper focuses on mapping privacy policy text to DPV concepts, not on a data provenance model. It is peer-reviewed, in English, but does not meet the stated inclusion criteria.
entrytype: inproceedings
link: 
name: The Role of Vocabulary Mediation to Discover and Represent Relevant Information in Privacy Policies
organization: IOS Press (Legal Knowledge and Information Systems, FAIA-334)
place: JURIX or related workshop
pp: 73-82
provenance_related: false
related:
  - Data Privacy Vocabulary
  - Privacy Policy Analysis
  - Semantic Web
  - Text Classification
  - Ontology Design Patterns
year: 2020
forward_steps: 2
---

# Summary & Analysis

## Introduction & Motivation (Sections 1–2)

This paper explores how to leverage a domain-specific vocabulary—namely the Data Privacy Vocabulary (**DPV**)—to help automate discovery of relevant information in website privacy policies. Existing approaches to analyzing privacy policies, e.g., using machine learning, rarely exploit formal or Semantic-Web-based vocabularies. Conversely, knowledge-centric initiatives (like DPV) have not been broadly applied in text-mining approaches to real policies. The work proposes a method that uses the DPV to detect textual fragments in policies corresponding to relevant data-processing concepts.

**Key Points**

1. **Objective**: Map text in privacy policies to appropriate DPV classes (particularly focusing on “Personal Data Category” and “Purpose”).
2. **Mapping Steps**:
    - Identify relevant noun chunks and match them to DPV _modules_ via specific “descriptor” words.
    - Refine the matches to find more specific DPV classes by using synonyms (BabelNet) and a vector-similarity approach.
    - Generate results as a machine-readable RDF representation using an ontology design pattern.
3. **Evaluation**: Uses the OPP-115 dataset (115 annotated US website privacy policies). The authors compare auto-extracted text chunks against the gold-standard attribute-value annotations (e.g., personal information types, data uses).
4. **Observations**:
    - The DPV-based approach can find relevant text segments, though some mismatch arises from either broad labeling in OPP-115 or unannotated text.
    - Approximately half of the DPV classes in the relevant modules were successfully matched.

**Quotations**

1. “This is the first approach to the automatic processing of privacy policies that relies on the DPV.” [p. 73]
2. “The text of privacy policies without [...] taking advantage of existing vocabularies to provide those documents with a shared semantic superstructure.” [p. 73]
3. “We present a machine-readable representation of this information to bridge the unstructured textual information to the formal taxonomy modelled in it.” [p. 73]
4. “Many works in the data protection field applied NLP techniques to the text of privacy policies for labelling their paragraphs [...] These two lines of research do not seem to pursue a common goal.” [p. 74]

---

## Methodology (Sections 3–4)

The authors focus on two DPV modules—(i) **Personal Data Category** and (ii) **Purpose**—and only the “First Party Collection/Use” paragraphs of the OPP-115 corpus. The system proceeds in three steps:

1. **Initial Module-Level Mapping**:
    
    - Lists of “descriptors” (frequent words) are compiled from DPV class labels and short descriptions.
    - For each sentence, the algorithm extracts noun chunks and checks if their root matches a module-specific descriptor.
    - Those chunks are preliminarily assigned to the relevant module(s).
2. **Candidate Classes**:
    
    - When a chunk matches a module, possible DPV classes are retrieved by matching synonyms or sub-strings from BabelNet.
    - For example, “mobile device ID” might map to dpv:DeviceBased or dpv:Identifying.
3. **Choosing the Best Class**:
    
    - A vector-based approach calculates cosine similarities between the chunk and each candidate class.
    - The class with the highest similarity is selected, so “customer service” might link to dpv:CustomerCare.

---

## Results & Discussion (Sections 5–6)

1. **Extraction Statistics**:
    
    - Over 4,800 text chunks assigned to 102 out of 192 classes in the two DPV modules.
    - Classes like dpv:DeviceBased, dpv:EmailAddress, and dpv:CommercialInterest appear frequently; some fine-grained classes appear rarely or not at all.
2. **Evaluation**:
    
    - Compared to OPP-115’s attribute-value pairs, 30% of chunk-level matches overlapped with the same label, about 24% outright mismatched, and 46% had no corresponding annotation in OPP-115.
    - Some OPP-115 labels are very coarse (like “Other”), so the DPV-based approach might be more precise.
3. **RDF Representation**:
    
    - The authors propose an Ontology Design Pattern (ODP) using isMemberOf to link text chunks to semantic domains (i.e. DPV classes).
    - This clarifies the “chunk belongs to this domain (class)” rather than claiming a direct equivalence.
4. **Limitations & Future Work**:
    
    - Many OPP-115 policies predate the GDPR, so references to certain “modern” DPV concepts may be missing.
    - Next steps involve applying the approach to more GDPR-oriented policies, refining the method, and possibly covering other DPV modules.

**Quotations**

1. “An unstructured delivery of the results could erroneously suggest that [...] there is a close match between their meanings.” [p. 81]
2. “This first evaluation approach [...] provided promising insights that encourage the refinement of the evaluation approach, that could involve manual expert evaluation.” [p. 80]

---

## Conclusion (Section 7)

The paper’s main novelty is bridging NLP-based text segment discovery with a specialized data protection vocabulary. By aligning relevant textual segments in privacy policies to DPV concepts, the approach potentially enhances interoperability and reusability of the extracted information. Future extensions include a broader scope of DPV modules, more advanced text similarity models, and improved evaluation on a corpus of GDPR-compliant policies.

**Key Takeaway**:  
This work is a prototype demonstrating how a domain vocabulary (DPV) can guide the automated extraction and machine-readable structuring of policy content, thus supporting transparency and compliance in data protection documentation.

---

# Evaluation Based on Inclusion Criteria

1. **Strictly propose a data provenance model for GDPR obligations?**
    
    - No. The paper uses the Data Privacy Vocabulary (DPV) to classify text in privacy policies into certain concepts (like categories of personal data or purpose). It does not present a _data provenance_ or lineage model.
    - **Reference**: “In this paper we show how a recently released domain-specific vocabulary, i.e. the Data Privacy Vocabulary, can be used [...] We also provide a machine-readable representation [...].” [p. 73]
2. **Useful to address the user’s compliance questions (CQ08–CQ65)?**
    
    - While the approach improves semantic clarity of policy text, it does _not_ explicitly address the user’s specific compliance queries (e.g., data retention times, subject access requests, or DPO appointment).
    - **Reference**: The text focuses on automated classification, not on answering compliance questions or enumerating data management obligations (pp. 73–82).
3. **Proposed model publicly available for comparison?**
    
    - The authors use the existing DPV, which is publicly available. However, they do not release a stable repository of their extracted “machine-readable representation” for broad re-use.
    - **Reference**: They mention “We also provide a machine-readable representation [...] to bridge the unstructured textual information,” but do not cite a public code repository (pp. 81–82).
4. **Document is in English or Portuguese?**
    
    - It is in English.
    - **Reference**: Entire text [pp. 73–82].
5. **Publicly available or accessible in digital libraries (CAPES CAFE, etc.)?**
    
    - The paper is published in “Legal Knowledge and Information Systems” (FAIA 2020, IOS Press) and presumably accessible in some digital libraries.
    - **Reference**: “Published online with Open Access by IOS Press.” [p. 73]
6. **Peer-reviewed?**
    
    - Yes. This is a conference proceeding in the “Legal Knowledge and Information Systems” track associated with JURIX or similar.
    - **Reference**: “In: Legal Knowledge and Information Systems. S. Villata et al. (Eds.) [...] published by IOS Press.” [p. 73]

**Conclusion**  
While peer-reviewed and in English, the paper does _not_ present a data provenance model that addresses the user’s inclusion requirements. Instead, it’s about text extraction/classification using DPV. Therefore, it should be categorized as **unrelated**.

---

# Discussion on Compliance Questions

The user’s compliance questions (CQ08–CQ65) relate to retention periods, data subject rights, security measures, etc. This paper does not methodically address or answer those. It focuses on mapping textual fragments in privacy policies to conceptual labels from the DPV. Even though that might help structure policy content, no direct or exhaustive coverage of items like data retention, objection rights, or DPO appointment is provided.

---

# References

- [[bonatti2020a]]