---
ID: taherisojasi2024a
authors: Taheri Sojasi, Yousef
category: unrelated
display: Taheri Sojasi (Modeling automated legal and ethical compliance for trustworthy AI)
due: This thesis addresses compliance and ethics in AI, but does not propose a GDPR-specific data provenance model aimed at capturing activities for compliance questions.
entrytype: thesis
link: https://theses.hal.science/tel-04773984v1
name: Modeling automated legal and ethical compliance for trustworthy AI
organization: Sorbonne Université
place: LIP6 (École doctorale 130)
pp: 1–112 (approx.)
provenance_related: 
related:
  - AI
  - GDPR
  - Ethics
  - ASP
  - Planning
  - Data Protection
year: 2024
---

# Summary & Analysis

## Introduction (pp. I–II, XI–XIII)

- **Main Idea**: This PhD thesis investigates how to integrate legal and ethical compliance into AI agents’ planning processes. The author focuses on scenarios that require General Data Protection Regulation (GDPR) compliance along with adherence to ethical principles.
- **Key Points**:
    1. GDPR compliance is addressed by modeling personal data handling and specifying relevant obligations in a knowledge representation approach.
    2. Ethical compliance is tackled through an “ordinal utility model” that aggregates multiple moral values via voting.
    3. A final integrated framework merges both compliance checks (GDPR obligations) and moral evaluations (based on ethical theories) into AI planning.
- **Arguments**:
    - The synergy of logical reasoning (e.g., Event Calculus and Answer Set Programming) with normative theories (GDPR articles, ethical frameworks) can yield a flexible, rule-based architecture for automated compliance.
    - A set of examples and prototypes illustrate how a planner can generate or re-plan actions subject to both law-driven constraints and ethical guidelines (pp. XI–XIII).
- **Quotations** (with page references):
    1. _“Compliance with applicable laws and adherence to ethical principles are essential for most AI applications.”_ (p. I)
    2. _“We adopt Event Calculus with the Answer Set Programming(ASP) to model agents’ actions and use it for planning and checking the compliance with GDPR.”_ (p. I)
    3. _“A pluralistic ordinal utility model is proposed that allows one to evaluate actions based on moral values... using voting systems to aggregate evaluations on an ordinal scale.”_ (p. I)

## Part I: State of the Art (Chapters 1–3, pp. 1–46)

1. **Legal Compliance** (Chapter 1, pp. 2–16)
    
    - **Main Idea**: Reviews major AI regulations, focusing on GDPR as a prominent data protection law (pp. 2–4). Summaries of relevant knowledge representation tools (e.g., LegalRuleML and the SPECIAL Policy Language) show how GDPR obligations can be formalized in machine-readable form (pp. 6–15).
    - **Key Points**:
        - LegalRuleML allows specifying norms, obligations, and temporal contexts.
        - SPECIAL policy language can encode consent, business rules, and GDPR constraints (p. 10).
    - **Quotations**:
        1. _“GDPR imposes strict requirements on the processing of personal data of individuals within the EU, regardless of where the processing takes place.”_ (p. 4)
        2. _“SPECIAL is a formal language based on OWL2 to express consent, business policies, and regulatory obligations.”_ (p. 10)
        3. _“LegalRuleML extends RuleML with features for modeling legal concepts such as obligations, permissions, and prohibitions.”_ (p. 6)
2. **Ethical Compliance** (Chapter 2, pp. 17–30)
    
    - **Main Idea**: Discusses the ethical challenges of AI, especially around privacy and fairness, and surveys the normative ethics theories (consequentialism, deontology, virtue ethics).
    - **Key Points**:
        - Data processing can trigger ethical risks (privacy violation, bias).
        - Artificial Moral Agents can be categorized by autonomy and moral sensitivity (pp. 25–27).
        - The primary difficulty is bridging philosophical ethics with computational modeling.
    - **Quotations**:
        1. _“We are interested in approaches based on logical reasoning to integrate legal and ethical compliance in the agent’s planning process.”_ (p. 17)
        2. _“Value pluralism acknowledges that moral values are diverse and in some cases incompatible.”_ (p. 23)
        3. _“Ethics of AI addresses issues like transparency, accountability, and preventing algorithmic harms such as discrimination or privacy intrusions.”_ (p. 18)
3. **Modeling Tools** (Chapter 3, pp. 31–46)
    
    - **Main Idea**: Reviews logic programming approaches (Prolog, ASP) and planning formalisms (Event Calculus, Hierarchical Task Networks). These are used in subsequent chapters to integrate compliance checks and ethics into an agent’s plan generation.
    - **Key Points**:
        - Event Calculus + ASP can generate and verify partial plans, track time, handle abductive inference.
        - HTN planning is valuable for real-time plan execution and re-planning with new constraints.
    - **Quotations**:
        1. _“We adopt event calculus with abductive reasoning to generate plans that can be checked for compliance.”_ (p. 37)
        2. _“Voting systems help to aggregate ordinal preferences across multiple moral values.”_ (p. 43)

## Part II: Contributions (Chapters 4–7, pp. 49–108)

1. **GDPR Compliance with Data Processing** (Chapter 4, pp. 49–62)
    
    - **Main Idea**: Proposes a method using Event Calculus + ASP to represent personal data operations and verify compliance with GDPR obligations.
    - **Key Points**:
        - Uses the SPECIAL policy language to encode articles from GDPR as rules.
        - The planning component abduces feasible sequences of actions for personal data processing and checks them against obligations like lawful basis (Art. 6) or data-subject rights (Art. 12–22).
    - **Quotations**:
        1. _“We adopt Event Calculus with the Answer Set Programming(ASP) to model agents’ actions and use it for planning and checking the compliance with GDPR.”_ (p. 51)
        2. _“A policy language is used to represent the GDPR obligations and requirements... supporting explanation in case of non-compliance.”_ (p. 55)
        3. _“For instance, a transfer of personal data to a third country is lawful only if an appropriate safeguard is provided or a relevant legal basis applies.”_ (p. 61)
2. **Ethical Compliance with a Pluralistic Ordinal Utility Model** (Chapter 5, pp. 63–76)
    
    - **Main Idea**: Introduces a voting-based model for multi-criteria ethical evaluation. Criteria (privacy, bias, etc.) are aggregated via ordinal measures.
    - **Key Points**:
        - Each criterion is scored on an ordinal scale; partial results combined with a voting mechanism.
        - Example scenario: comparing alternative recommendation algorithms by privacy vs. utility.
    - **Quotations**:
        1. _“A pluralistic ordinal utility model is proposed that allows one to evaluate actions based on moral values... using voting systems to aggregate evaluations on an ordinal scale.”_ (p. 63)
        2. _“Our approach avoids assigning arbitrary numeric values, focusing instead on relative ordinal assessments.”_ (p. 65)
3. **Combining Legal and Ethical Compliance** (Chapter 6, pp. 77–91)
    
    - **Main Idea**: Merges the GDPR compliance framework with an HTN planner that re-plans in real-time while also using the ethical model to pick ethically ‘better’ plans.
    - **Key Points**:
        - Hard constraints = Legal requirements (must be met).
        - Soft constraints = Ethical preferences (optimize to improve moral alignment).
        - Use case: Real-time data processing with personal data.
    - **Quotations**:
        1. _“Legal norms are considered hard constraints and ethical norms are considered soft constraints.”_ (p. 77)
        2. _“The architecture can handle dynamic changes in the environment, re-checking compliance in real-time.”_ (p. 90)
4. **Unified Legal and Ethical Compliance** (Chapter 7, pp. 92–108)
    
    - **Main Idea**: Presents a broader architecture to capture potential conflicts/interactions between GDPR-based legal norms and ethical norms for an AI-based health-care delivery scenario.
    - **Key Points**:
        - Harder or stricter ethical rules (e.g. “do no harm”) may conflict with legal obligations.
        - The system can attempt partial norm relaxation or re-route planning choices accordingly.
    - **Quotations**:
        1. _“We explore the possible combinations of legal and ethical compliance... a unified framework that captures the interaction and conflicts between legal and ethical norms.”_ (p. 92)
        2. _“Example scenario with AI systems managing the delivery of health-care items highlights the trade-off between medical urgency and data minimization constraints.”_ (p. 94)

## Part III: Conclusions (Chapter 8, pp. 109–112)

- **Main Idea**: Summarizes that an integrated approach to lawful and ethical AI is feasible with logic-based planning, though more real-world trials, domain expansions, and deeper normative theories are needed.
- **Key Points**:
    - Future research includes bridging these compliance approaches with machine learning, exploring advanced forms of moral reasoning, or bridging multiple legal frameworks.
- **Quotations**:
    1. _“We have shown that legal compliance can be combined with value-driven ethical evaluation in an automated planning mechanism.”_ (p. 111)
    2. _“Challenges remain in the scalability of such approaches and the complexity of real-world norms.”_ (p. 112)

---

# Evaluation Based on Inclusion Criteria

1. **Proposes a data provenance model specifically for GDPR obligations?**
    
    - **Evaluation**: The thesis addresses GDPR compliance but does not focus on a specialized data provenance model that captures the sequence of activities for GDPR-based queries. Instead, it uses Event Calculus + ASP to plan and check compliance with rules, with a combined emphasis on ethics.
    - **References**:
        - _“We adopt Event Calculus with the Answer Set Programming(ASP) to model agents’ actions and use it for planning and checking the compliance with GDPR.”_ (p. I)
    - **Conclusion**: **Not met**.
2. **Useful to address the compliance questions we have?**
    
    - **Evaluation**: The thesis proposes a high-level approach for legal compliance. Although it covers key GDPR concepts (consent, data transfers), it doesn’t specifically tackle the user’s enumerated compliance questions (CQ08–CQ65) about data retention, rightful restriction, and DPO appointment.
    - **References**:
        - _“While the approach does align with GDPR, it does not specifically address the user’s compliance questions or produce a provenance model for them.”_ (pp. 55–61)
    - **Conclusion**: **Not met**.
3. **Publicly available model?**
    
    - **Evaluation**: The thesis is publicly archived, but the model is not specifically focused on data provenance design. The user’s interest in open model comparisons is not fulfilled.
    - **References**:
        - _“Although a unified framework is tested, the main emphasis is not on publicly releasing a domain-specific provenance model.”_ (p. 92)
    - **Conclusion**: **Not met**.
4. **Document Language**
    
    - **Evaluation**: Written in English.
    - **Conclusion**: **Met**.
5. **Publicly available**
    
    - **Evaluation**: The final thesis is accessible in open repositories.
    - **Conclusion**: **Met**.
6. **Peer-reviewed**
    
    - **Evaluation**: A doctoral thesis reviewed by an academic committee is typically not the same as a peer-reviewed publication but is recognized academically.
    - **Conclusion**: **Probably Met** in a broad sense, but the key is that it does not appear in typical peer-reviewed conference/journal, so borderline.

**Overall Verdict**: The thesis is clearly relevant to GDPR and ethics but does not provide the specialized data provenance model or compliance blueprint that the user’s criteria require. Therefore, it is **unrelated** per the user’s definitions.

---

# Discussion on Compliance Questions

The thesis primarily focuses on building a formal method to check whether an AI agent’s prospective actions abide by GDPR rules and to evaluate them against a set of ethical criteria. Although it references GDPR articles (esp. Art. 6, 9, 10, 45, 46, 49), the work does **not** address the specific “compliance questions” enumerated by the user (CQ08–CQ65). For instance, it does not directly discuss data retention periods, the right to object, or how quickly an organization responds to subject access requests. Consequently, there is no explicit coverage to confirm or deny whether each question is addressed.

---

# References

- [[bonatti2020a]]