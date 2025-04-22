---
ID: birrell2024a
authors: Birrell, Eleanor; Rodolitz, Jay; Ding, Angel; Lee, Jenna; McReynolds, Emily; Hutson, Jevan; Lerner, Ada
category: unrelated
display: "birrell (SoK: Technical Implementation and Human Impact of Internet Privacy Regulations)"
due: This paper analyzes privacy regulations worldwide, but does not propose a data provenance model for GDPR obligations.
entrytype: inproceedings
link: ""
name: "SoK: Technical Implementation and Human Impact of Internet Privacy Regulations"
organization: IEEE
place: IEEE Symposium on Security and Privacy
pp: ""
provenance_related: false
related: 
year: 2024
forward_steps: 2
---

# Summary & Analysis

## Summary

**“SoK: Technical Implementation and Human Impact of Internet Privacy Regulations” (S&P 2024) by Birrell, Rodolitz, Ding, Lee, McReynolds, Hutson, and Lerner** offers a systematization of knowledge about the global landscape of Internet privacy regulations. The authors examine 24 laws from around the world (including GDPR and CCPA), comparing features such as rights conferred to individuals, obligations on organizations, and enforcement mechanisms. From these, they distill a taxonomy of rights and obligations (e.g., right to access, right to portability, data minimization, security requirements) and evaluate how each has been addressed in 270 existing computer science research papers. The analysis indicates an overwhelming focus in CS literature on European (GDPR) and Californian (CCPA) laws, as well as on “privacy self-management” mechanisms like cookie banners or data subject access requests. The paper concludes that certain aspects of privacy regulations (e.g., data minimization, fundamental rights not to be subject to automated decisions, non-discrimination) have received little attention from technical researchers, and calls for more cross-cultural, longitudinal, and forward-looking studies that can complement or shape future privacy regulations.

## Key Points

1. **24 Global Laws** – The paper surveys privacy regulations from countries with large populations or large GDP. Similarities and differences in rights and obligations are examined, forming a taxonomy that includes definitions (e.g., personal data, anonymization), self-managed rights (access, deletion, consent), fundamental prohibitions (e.g., automated decisions, certain technologies), business obligations (notice/transparency, data minimization, privacy by design), scope (individuals and organizations), and enforcement.
    
2. **Reviewing 270 Papers** – The authors systematically gathered papers from top security, privacy, and HCI venues, eventually settling on 270 relevant works since 2017. Most prior CS research focuses on GDPR (87% of the 270 papers). Key hotspots of inquiry include the usability and manipulation of cookie banners, subject access requests, opt-out processes, compliance measurements, and so forth. Meanwhile, many other regulation features remain rarely studied.
    
3. **Findings** – Research around self-management and transparency largely finds that existing “notice-and-consent” models create user fatigue and rely heavily on manipulative design patterns (dark patterns). Evidence shows that many organizations do not fully comply with transparency or user rights. Some aspects (e.g., the right to correct, non-discrimination obligations, privacy by design) have comparatively little coverage in the computer science literature.
    
4. **Recommendations** – The authors propose more emphasis on fundamental rights (that do not hinge on user self-management), deeper cross-jurisdictional studies, more longitudinal research extending well after new laws come into force, and study of alternative regulatory models (e.g., data fiduciaries).
    

## Evaluation Against Inclusion Criteria

- **Data Provenance Model for GDPR?** – The paper focuses on analyzing privacy laws and how they have been studied by computer scientists, not on building a data provenance model. Hence, it does **not** fulfill the requirement for proposing “a strict data provenance model to represent GDPR obligations.”
- **Addressing Specific GDPR Compliance Questions?** – While the paper touches on many GDPR rights and obligations, it does not systematically address the enumerated compliance questions (like data retention periods or DSAR timelines). Instead, it provides an overall SoK of how laws have been studied.
- **Category** – Because it does not propose a specific data provenance solution or address the user’s enumerated compliance questions, it’s deemed “unrelated” to that narrower requirement.

## Discussion on Compliance Questions

The authors highlight broad, real-world privacy compliance issues but do not offer discrete solutions to user queries, e.g., “how to store personal data to fulfill GDPR data retention?” Instead, they give a comprehensive view of the academic state-of-the-art in analyzing privacy laws. They do not directly tackle the compliance questions from the user’s list.

## Conclusion

The authors present a thorough “SoK” of privacy law research within computer science, with calls for more varied future work, especially beyond “privacy self-management.” However, they do not propose a dedicated data provenance model for GDPR compliance. As per the user’s strict criteria, the paper is **unrelated**.

---

# References

- [[bonatti2020a]]