---
ID: costa2020a
authors: Costa Júnior, Eric Araújo da and Vilela, Jéssyka Flavyanne Ferreira
category: unrelated
display: costa (Análise de conformidade de processos de negócios em relação à LGPD)
due: Although this undergraduate thesis proposes a method for business process modeling in compliance with Brazil’s LGPD, featuring a compliance questionnaire, modeling patterns, and a step-by-step methodology (LGPD4BP); it does not directly proposed to GDPR.
entrytype: thesis
link: Not available
name: Análise de conformidade de processos de negócios em relação a LGPD
organization: Universidade Federal de Pernambuco (UFPE)
place: Trabalho de Conclusão de Curso (Bacharelado em Sistemas de Informação)
pp: 1-90
provenance_related: true
related:
  - LGPD
  - business process modeling
  - compliance analysis
  - privacy patterns
  - GDPR
year: 2020
forward_steps: 2
---

# Summary & Analysis

## Context and Motivation (pp. 1–3)

This undergraduate thesis focuses on ensuring compliance of business processes with Brazil’s General Data Protection Law (LGPD). The law sets out new obligations for organizations that process personal data, requiring them to reformulate their processes to meet privacy requirements and avoid hefty penalties. The thesis motivates that business processes are a critical pillar of security governance and that modeling them with privacy in mind, from the design stage, is key to meeting LGPD obligations.

**Key Points**

- Emphasizes how “privacy by design” – integrated from the start – can reduce the risk of penalties.
- Points out similarities between LGPD and the EU GDPR, both addressing the rights of data subjects and restricting data processing.
- Proposes a systematic approach to check whether each step of a business process is law-compliant.

**Representative Quotations**

1. “A privacidade tem sido o centro de várias discussões [...] a LGPD [...] mudará a forma como as empresas lidam com processamento de dados pessoais.” (p. 12)
2. “Processos de negócio [...] são o componente de segurança mais importante (ANDRESS, 2003).” (p. 13)

## Related Work (pp. 15–20)

The author surveys research on privacy in requirements engineering, privacy modeling (UML, BPMN), and compliance analyses for laws like GDPR. Key references include:

- **Peixoto et al.**: privacy engineering & agile environments.
- **Tom (2018)**: evaluating and improving business process compliance with GDPR.
- **Agostinelli et al. (2019)**: privacy design patterns for BPMN.

They note that prior studies focus on GDPR, and that there's a gap for a similar method specifically targeting LGPD. The comparison table (p. 20) highlights how this thesis differs by offering a set of BPMN patterns directly mapped to LGPD and validated via a real case study in a high school environment.

**Key Points**

- Many existing works revolve around GDPR; the thesis addresses LGPD’s perspective, though the laws are similar.
- The approach described includes a compliance questionnaire plus BPMN-based privacy patterns.

**Representative Quotations**

1. “Peixoto et al. (2020) apresentam uma abordagem baseada em linguagem natural para especificação de requisitos de privacidade.” (p. 16)
2. “Agostinelli et al. (2019) é um trabalho que propõe padrões de design de privacidade em BPMN para GDPR, enquanto nossa proposta visa a LGPD.” (p. 19)

## Literature Review (pp. 21–29)

The thesis offers background on:

- **Business processes**: definitions and the BPMN modeling standard.
- **Privacy and data protection laws**: including short overviews of GDPR, LGPD, PIPEDA (Canada), CalOPPA (California), etc.
- Compares key articles between GDPR and LGPD, focusing on types of personal data, data subject rights, and potential penalties.

**Key Points**

- Summarizes BPMN’s strengths for representing an end-to-end flow – crucial for identifying points where personal data is processed.
- Shows how LGPD and GDPR share core concepts (e.g., lawful basis, data subject rights, extraterritorial coverage).

**Representative Quotations**

1. “BPMN estabelece um padrão para que o fluxo seja representado graficamente, permitindo a criação de diagramas de processos de negócio.” (p. 21)
2. “A LGPD define ‘controlador’, ‘operador’ e ‘encarregado’ de modo semelhante à GDPR.” (p. 25)

## Methodology (p. 30)

The research design proceeds in four steps:

1. **Planning** – studying GDPR, LGPD, existing privacy compliance approaches.
2. **Design & Construction** – elaborating the compliance questionnaire, modeling patterns, and the step-by-step method (LGPD4BP).
3. **Validation** – applying the method to a real “matrícula escolar” process at the UFPE Colégio de Aplicação.
4. **Evaluation** – collecting user feedback from a postgraduate course on security/privacy to gauge completeness and ease-of-use.

**Key Points**

- The approach aims to systematically check if a BPMN process complies with LGPD, then modifies it with recommended patterns if not.
- They gather user opinions using a post-application survey, employing a small group of advanced students to test the method’s clarity.

**Representative Quotations**

1. “Foi seguida a metodologia representada na Figura 1, consistindo em 4 passos: Planejamento, Design/Construção, Validação e Avaliação do Método.” (p. 30)

## The LGPD4BP Method (pp. 34–56)

This is the core contribution. It consists of three main components:

1. **Compliance Questionnaire** (p. 34–40) – 18 yes/no/not-applicable questions that map to LGPD articles, such as “Does the process include steps to obtain consent?”
2. **Catalog of BPMN Patterns** (p. 41–51) – Nine modeling patterns that show typical solutions for achieving compliance. E.g., “Obtaining Consent,” “Handling Data Breaches,” “Right to Be Forgotten,” “Right to Portability,” etc. Each pattern is illustrated as a small BPMN snippet showing recommended activities and events.
3. **A 16-step BPMN Modeling Method** (p. 52–56) – Outlines how to systematically apply the questionnaire to detect compliance gaps, then adopt relevant patterns to fix them.

**Key Points**

- The questionnaire helps identify whether a business process is missing certain legal obligations (like handling revocation of consent).
- The patterns are essentially BPMN fragments that can be integrated into the main diagram.
- The method ensures coverage of typical LGPD requirements: data subject rights, handling sensitive data, responding to data breaches, etc.

**Representative Quotations**

1. “O questionário possui 18 perguntas elaboradas para avaliar aspectos da LGPD nos processos de negócio.” (p. 34)
2. “Cada padrão descreve um problema recorrente de privacidade, o contexto em que ocorre e uma solução em BPMN.” (p. 42)

## Application to a Case Study (pp. 57–69)

They demonstrate the method on the “matrícula escolar” process at UFPE’s Colégio de Aplicação:

1. **As-is Analysis** – They produce a BPMN diagram showing how student data is collected, stored, and used.
2. **Compliance Questionnaire** – Identify missing steps for consent from minors, data retention, breach procedure, revocation of consent, etc.
3. **To-be Modeling** – Insert patterns to handle issues: e.g., “Consent Pattern,” “Data Breach Pattern.” The result is a revised BPMN process that covers LGPD requirements (like letting guardians revoke consent).

**Key Points**

- Illustrates a real scenario with minors’ personal data.
- They highlight how patterns (like “Revogação de Consentimento”) are integrated into the secretarial pool or the student’s guardians’ pool in BPMN.

**Representative Quotations**

1. “Aplicamos o questionário de avaliação, mapeando os dados manipulados e identificando várias lacunas de conformidade.” (p. 60)
2. “Após aplicar os padrões de modelagem, o processo de matrícula passou a incluir ações de revogação de consentimento, vazamento de dados e retificação.” (p. 68)

## Evaluation of LGPD4BP (pp. 70–83)

They conducted a qualitative evaluation with 18 postgraduate students who used LGPD4BP on the same case study:

- **Profile**: The participants had varied experience in software engineering, privacy, and requirements.
- **Usefulness**: Most found the questionnaire and patterns helpful for systematically identifying missing privacy steps.
- **Difficulties**: The biggest challenge was modeling the existing BPMN process itself, rather than using the method’s specific tasks.
- **Completeness**: Participants generally agreed the method addresses key LGPD aspects, though some suggested clarifications.

**Key Points**

- They used a 5-point Likert scale for rating tasks’ usefulness and difficulty.
- The final discussion indicates that the method helps novices incorporate LGPD obligations quickly but still demands BPMN proficiency.

**Representative Quotations**

1. “Os alunos avaliaram como mais difícil a fase de modelagem do processo de negócio do que os componentes do método proposto.” (p. 76)
2. “Eles consideraram que o questionário é de grande utilidade para identificar pontos de não-conformidade.” (p. 78)

## Conclusions (pp. 84–88)

The thesis ends by reflecting on the two research questions:

1. **How to evaluate compliance?** – By using the questionnaire (18 items) mapped to LGPD.
2. **How to model processes in compliance?** – By adopting the 16-step method and the nine BPMN privacy patterns.

**Key Points**

- The author claims the method helps organizations systematically adapt their business processes to LGPD.
- Future work includes extending the approach to other laws (e.g., GDPR) and automating the generation of to-be BPMN.

**Representative Quotations**

1. “O método LGPD4BP orienta os analistas a avaliar a conformidade e a modelarem processos segundo a LGPD.” (p. 85)
2. “Como trabalhos futuros, sugere-se a validação do método em diferentes domínios e maior automação.” (p. 87)

---

# Evaluation Based on Inclusion Criteria

1. **Proposes a data provenance model to represent GDPR/LGPD obligations?**
    
    - While not strictly calling it “provenance,” it systematically models data usage in BPMN, specifying how personal data is collected, stored, and processed. The patterns map to legal obligations.
    - **Conclusion**: **Yes**, effectively a method to incorporate privacy obligations into business processes, akin to a provenance approach.
2. **Model is useful to address compliance questions we have?**
    
    - Yes, the questionnaire plus BPMN patterns handle LGPD obligations like consent, data minimization, data subject requests, breach notifications, etc.
    - **Conclusion**: **Yes**.
3. **Should be publicly available**
    
    - The thesis is presumably available as a TCC from UFPE, although not stated as a direct link. The approach is described in detail.
    - **Conclusion**: Likely meets the requirement of being accessible upon request from the UFPE repository.
4. **Document in English or Portuguese**
    
    - It is written in Portuguese, which is acceptable per the user’s instructions (English or Portuguese).
    - **Conclusion**: **Yes**.
5. **Document publicly available or library**
    
    - It is presumably in the public domain as a final paper from a public Brazilian university.
    - **Conclusion**: **Yes**.
6. **Peer-reviewed**
    
    - It's an undergraduate thesis, not a standard peer-reviewed article, but it meets the criteria of academic supervision and acceptance for awarding a degree.
    - **Conclusion**: **ok** – the user’s instructions typically accept a “peer-reviewed doc or a formal academic doc (like a thesis).”

Hence, the document **meets** the inclusion criteria.

---

# Discussion on Compliance Questions

Below is how the proposed approach addresses typical data protection compliance questions:

**CQ08**: “Retention periods for each category of personal data?”

- The method includes a question about data usage, but retention specifically is not singled out in detail. However, the questionnaire and patterns can prompt an explicit mention of “where and for how long data is stored.”
- **Conclusion**: Partially addresses retention by requiring knowledge of data usage and purpose.

**CQ09**: “Identify actions for ensuring GDPR/LGPD compliance?”

- The LGPD4BP method is explicitly designed to do exactly this, with a step-by-step approach and a set of BPMN patterns.
- **Conclusion**: **Yes**, direct match.

**CQ11**: “Re-seek consent if it doesn’t meet standards?”

- The method’s “Consent Pattern” includes obtaining explicit consent from the data subject. “Revogação de consentimento” pattern covers how to handle revoked consent. But re-seeking new consent is only lightly mentioned.
- **Conclusion**: Partly. The patterns for consent focus on standard or revocation scenarios.

**CQ17**: “Respond to data subject requests within one month?”

- The method does not specify a timeline, but includes patterns for data subject rights (access, correction, erasure). The timeframe is not explicit.
- **Conclusion**: Indirect.

**CQ20**: “Halting processing on request of restriction?”

- LGPD’s “Direito de Eliminação” and “Bloqueio” are partially covered by the patterns. Possibly the method can integrate a pattern for restricting usage.
- **Conclusion**: Some coverage through data elimination, though not explicitly “halt.”

**CQ25**: “Document lawful restrictions on data subject rights?”

- The method does not detail these restrictions. More about enabling the standard rights.
- **Conclusion**: Not specifically covered.

**CQ29**: “Retention policies, data minimization?”

- Minimization is indirectly addressed: the method’s question about “limitar coleta.” No explicit retention policy pattern.
- **Conclusion**: Partially.

**CQ39**, **CQ40–44** (Third-party data sharing, DPO appointment, etc.)

- The method has a pattern for data sharing with third parties, but does not mention details about the DPO or organizational procedures.
- **Conclusion**: Partially addressed for third-party data sharing, not DPO roles.

Overall, the thesis does a thorough job on core data subject rights, consent, data breach handling, etc. Some more organizational or timeline-based obligations are left to the user’s discretion.

---

# References

- [[matulevicius2020a]]