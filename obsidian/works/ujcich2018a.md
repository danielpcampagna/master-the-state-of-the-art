---
ID: ujcich2018provenance
authors: Ujcich, Benjamin E and Bates, Adam and Sanders, William H
category: ok
cluster_id: '4068207568007502254'
display: Ujcich et al. Model 3
due: This paper present a data provenance model that aims to support legal reasoning
  and compliance checking. Additionally, this approach represents the data lifecycle,
  processing, legal base for a process.
entrytype: inproceedings
link: https://par.nsf.gov/servlets/purl/10087201
name: A provenance model for the European union general data protection regulation
organization: Springer
place: IPAW
pp: 45--57
scholar: https://scholar.google.com.br/scholar?cites=4068207568007502254&as_sdt=2005&sciodt=0,5&hl=en
scholar_id: rpmkkzotdTgJ
scholar_ok: true
start_set: true
summary: Based on a set of rights and obligations the authors have identified, it
  is proposed a data provenance model for representing GDPR concepts and activities
  related to the GDPR. This approach extends PROV concepts by proposing a set of classes
  and relations. The use of the approach takes place in three use cases based on a
  retail shop. The auors identifies some vunerabiities such approach might be subjected.
year: 2018

---
# Ujcich, Benjamin E and Bates, Adam and Sanders, William H. A provenance model for the European union general data protection regulation. 2018.

## Approach and Motivations

The European Union (EU) General Data Protection Regulation (GDPR) has significantly expanded regulations regarding the storage and processing of personal data. This regulation mandates that organizations demonstrate compliance with data privacy laws, which includes showing how data were generated and used. The authors, Benjamin E. Ujcich, Adam Bates, and William H. Sanders, propose a data provenance model specifically tailored to the GDPR. This model aims to help organizations track the processing of personal data and ensure compliance with the regulation.

The proposed model captures data provenance, which involves the history and lifecycle of data, including its origins, transformations, and usage. The model includes high-level classes such as agents, activities, and entities, represented by house symbols, rectangles, and ellipses, respectively. Additionally, it incorporates relations and other properties essential for understanding data processing workflows. The authors emphasize the importance of temporal reasoning in determining the lawfulness of data processing, particularly concerning data consent validity over time.

## Approach Contribution For The Compliance Questions

### Question 8

The model includes temporal notions and timestamps for data activities, which can partially address the requirement to list the data retention period. By tracking when data were collected and processed, the model can help ensure that data are retained only as long as necessary.

### Question 28

The model's design patterns for data collection and consent can help track when corrections to personal data are made. By capturing timestamps and the provenance of data changes, the model supports the requirement to keep data up to date and accurate.

### Question 29

The model's emphasis on temporal reasoning and data retention periods can contribute to establishing retention policies. By tracking the lifecycle of data, the model helps ensure data are held no longer than necessary.

### Question 51

The model's provenance tracking can help document when data are destroyed, erased, or anonymized. By maintaining a record of these actions, the model supports the systematic handling of data no longer legally required.

### Question 63

The model includes components for tracking data transfers, including the origins and destinations of data. This can help list all transfers and answer questions about the nature and purpose of data processing.

### Question 64

The model does not explicitly address the legal basis for data transfers. While it can track data origins and destinations, it lacks components to document the legal justifications for these transfers.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8

While the model includes temporal components, it does not explicitly provide a mechanism for specifying data retention periods for different categories of personal data. Additional components may be needed to define and enforce retention policies.

### Question 28

The model can track updates to personal data, but it does not provide specific mechanisms for ensuring data accuracy and making necessary corrections without delay. This may require integration with other data quality management systems.

### Question 29

Although the model tracks data lifecycles, it does not include explicit retention policies or procedures. Organizations may need to develop additional policies and integrate them with the model to ensure compliance.

### Question 51

The model supports documenting data destruction, but it does not include specific procedures for systematically handling data when it is no longer required. Additional processes and controls may be needed to ensure compliance.

### Question 64

The model lacks components to document the legal basis for data transfers. This information is crucial for GDPR compliance but is not covered by the current model.

## Key Contributions

- **Data Provenance Model:** A model to track the history and lifecycle of personal data.
- **Temporal Reasoning:** Incorporation of temporal components to determine the lawfulness of data processing.
- **Design Patterns:** Patterns for modeling common events such as data collection, consent, and updates.
- **Compliance Support:** Helps organizations demonstrate GDPR compliance through data provenance tracking.
    - **Components:**
        - Agents (house symbols)
        - Activities (rectangles)
        - Entities (ellipses)
        - Relations (arrows)
        - Properties (notes)

- **Evaluation:** Analysis of GDPR text to identify compliance challenges and how data provenance can address them.

## State-of-the-Art

This approach advances the state-of-the-art by providing a structured model for tracking data provenance in the context of GDPR compliance. It builds on previous work by Pandit and Lewis and Bartolini et al., who developed GDPR ontologies. By incorporating temporal reasoning and design patterns, the model offers a practical tool for organizations to manage and document their data processing activities.

The model's emphasis on temporal aspects and compliance verification distinguishes it from prior research, which may not have focused as explicitly on these areas. Additionally, the model's alignment with the GDPR's requirements provides a robust framework for organizations seeking to ensure compliance and avoid significant penalties for non-compliance.

Related work includes the GDPR ontologies by Pandit and Lewis, and Bartolini et al., which structure the regulation's concepts. The current model extends these efforts by providing a practical tool for tracking data processing activities and ensuring compliance with the regulation's temporal and documentation requirements.
# References

[[bonatti2017a|7. P. Bonatti, S. Kirrane, A. Polleres, and R. Wenning, “Transparent personal data processing: The road ahead,” in Proceedings of Computer Safety, Reliability, and Security. Springer, 2017, pp. 337–349.]]
[[tankard2016a|2. C. Tankard, “What the GDPR means for businesses,” Network Security, vol. 2016, no. 6, pp. 5–8, 2016.]]
[[basin2018a|11. D. Basin, S. Debois, and T. Hildebrandt, “On purpose and by necessity: Compliance under the GDPR,” in Proceedings of Financial Cryptography and Data Security ’18, Mar. 2018.]]
[[bartolini2015b|3. C. Bartolini, R. Muthuri, and C. Santos, “Using ontologies to model data protection requirements in workflows,” in Proceedings of New Frontiers in Artificial Intelligence. Springer, 2017, pp. 233–248.]]
- [[bartolini2015b]]
[[bates2017a|17. A. Bates, W. U. Hassan, K. Butler, A. Dobra, B. Reaves, P. Cable, T. Moyer, and N. Schear, “Transparent web service auditing via network provenance functions,” in Proceedings of the 26th International Conference on World Wide Web, 2017, pp. 887–8]]
[[pasquier2015a|16. T. Pasquier, J. Singh, D. Eyers, and J. Bacon, “CamFlow: Managed data-sharing for cloud services,” IEEE Transactions on Cloud Computing, vol. 5, no. 3, pp. 472–484, July 2017.]]
[[pandit2017a|8. H. J. Pandit and D. Lewis, “Modelling provenance for GDPR compliance using linked open data vocabularies,” in Proceedings of Society, Privacy and the Semantic Web - Policy and Technology ’17, 2017.]]
[[bier2013a|14. C. Bier, “How usage control and provenance tracking get together - A data protection perspective,” in Proceedings of IEEE 4th International Workshop on Data Usage Management, May 2013, pp. 13–17.]]
[[directive1995a|10. Council of the European Union, “Directive 95/46/EC of the European Parliament and of the Council of 24 October 1995 (Data Protection Directive),” in Official Journal of the European Union, vol. L 281, Nov. 1995, pp. 31–50.]]
[[aldeco2008a|13. R. Aldeco-P´erez and L. Moreau, “Provenance-based auditing of private data use,” in Proceedings of Visions of Computer Science ’08, 2008, pp. 141–152.]]
[[moreau2013a|9. World Wide Web Consortium, “PROV-DM: The PROV data model,” https://www.w3.org/TR/prov-dm/, Apr. 2013.]]
[[gjermundrød2016a|12. H. Gjermundrød, I. Dionysiou, and K. Costa, “privacyTracker: A privacy-by-design GDPR-compliant framework with verifiable data traceability controls,” in Proceedings of Current Trends in Web Engineering. Springer, 2016, pp. 3–15.]]
[[martin2012a|6. A. Martin, J. Lyle, and C. Namilkuo, “Provenance as a security control,” in Proceedings of the Theory and Practice of Provenance ’12. USENIX, 2012.]]
[[bates2015a|15. A. Bates, D. Tian, K. R. B. Butler, and T. Moyer, “Trustworthy whole-system provenance for the Linux kernel,” in Proceedings of USENIX Security ’15, 2015, pp. 319–334.]]
