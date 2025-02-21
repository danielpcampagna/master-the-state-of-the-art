---
ID: campagna2020achieving
authors: Campagna, Daniel Prett and da Silva, Altigran Soares and Braganholo, Vanessa
category: ok
cluster_id: '15772782772141981403'
display: campagna
due: This contribution extends prior data provenance model in the literature by providing
  new concepts that capable this model to represent new requisites stipulated by GDPR
entrytype: inproceedings
link: https://sbbd.org.br/2020/wp-content/uploads/sites/13/2020/09/Archieving-GDPR-ST1.pdf
name: 'Achieving GDPR Compliance through Provenance: An Extended Model.'
place: SBBD
pp: 13--24
scholar: https://scholar.google.com.br/scholar?cites=15772782772141981403&as_sdt=2005&sciodt=0,5&hl=en
scholar_id: 237sDF0u5NoJ
scholar_ok: true
start_set: true
year: 2020

---
# Campagna, Daniel Prett, da Silva, Altigran Soares, and Braganholo, Vanessa. Achieving GDPR Compliance through Provenance: An Extended Model. 2020.

> https://dew-uff.github.io/gdpr-data-provenance-model/

## Approach and Motivations

The paper "Achieving GDPR Compliance through Provenance: An Extended Model" by Campagna, da Silva, and Braganholo introduces an enhanced data provenance model aimed at achieving compliance with the General Data Protection Regulation (GDPR). The motivation for this work arises from the significant changes brought by GDPR in handling data produced in digital media, emphasizing transparency and the involvement of individuals in data treatment processes. However, existing provenance models fall short of being fully compliant with GDPR requirements.

The authors build upon the GDPR data provenance model proposed by Ujcich et al., suggesting eleven new changes to make the model more transparent and compliant with the GDPR text. These changes are categorized into three types: plumbing extensions, porcelain extensions, and wallpaper extensions. Plumbing extensions affect the functionality of the model by appending new elements, while porcelain and wallpaper extensions aim to enrich the model by clarifying semantic meanings and adding further information as detailed in the law. The paper also introduces two design patterns to guide the implementation of these changes in real-world contexts.

## Approach Contribution For The Compliance Questions

### Question 8

The model addresses the need to inform data subjects about the period for which their data will be stored. This is represented using the `startedAtTime` and `endedAtTime` relations in the provenance graph. These elements can be used to answer Question 8 by specifying the duration for which each category of personal data will be retained.

## Approach Insufficiencies For Fulfill The Compliance Questions

### Question 28, 29, 51, 63, 64

The current model does not fully address the remaining compliance questions due to various limitations:

- **Question 28**: The model lacks components to ensure personal data is kept up to date and accurate, and to handle corrections without delay.
- **Question 29**: There are no specific elements in the model to enforce retention policies and procedures that ensure data is held no longer than necessary.
- **Question 51**: The model does not cover systematic destruction, erasing, or anonymization of data when it is no longer legally required.
- **Question 63**: Comprehensive tracking of data transfers, including the nature, purpose, origin, destination, and recipients of the data, is not fully represented.
- **Question 64**: The model does not document the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses.

## Key Contributions

- Introduction of eleven new changes to the existing GDPR data provenance model.
  - **Plumbing extensions**: Enhance the functionality by adding new elements.
  - **Porcelain extensions**: Clarify semantic meanings of GDPR text components.
  - **Wallpaper extensions**: Append further legal information to the model.
- Presentation of two design patterns to guide real-world implementation.
- Analysis of GDPR text to evolve the provenance model.

## State-of-the-Art

The approach advances the state-of-the-art by addressing some of the gaps in existing GDPR data provenance models. By introducing new elements and design patterns, the model enhances transparency and compliance with GDPR requirements. The work builds on previous models proposed by Ujcich et al., Bartolini et al., and Pandit and Lewis, extending their ideas and addressing some of their limitations.

However, the model still has insufficiencies in fully covering all compliance questions, indicating areas for future research and development. Competing approaches might address these gaps differently, potentially incorporating more comprehensive solutions for data accuracy, retention policies, and legal documentation of data transfers.

# References

[[ujcich2018a]]
[[regulation2016a|Council of European Union (2016). Council regulation (EU) no 2016/679. https://eur-lex.europa.eu/eli/reg/2016/679/oj.]]
[[kuner2012a|Kuner, C. (2012). The european commission’s proposed data protection regulation: A copernican revolution in european data protection law. Bloomberg BNA Privacy and Security Law Report (2012) February, 6(2012):1–15.]]
[[bonatti2017a|Bonatti, P., Kirrane, S., Polleres, A., and Wenning, R. (2017). Transparent personal data processing: The road ahead. In International Conference on Computer Safety, Reliability, and Security, pages 337–349. Springer.]]
[[tankard2016a|Tankard, C. (2016). What the gdpr means for businesses. Network Security, 2016(6):5–8.]]
[[basin2018a|Basin, D., Debois, S., and Hildebrandt, T. (2018). On purpose and by necessity: compliance under the gdpr. In International Conference on Financial Cryptography and Data Security, pages 20–37. Springer.]]
[[bartolini2015b|Bartolini, C., Muthuri, R., and Santos, C. (2015). Using ontologies to model data protection requirements in workflows. In JSAI International Symposium on Artificial Intelligence, pages 233–248. Springer]]
[[pasquier2015a|Pasquier, T. F.-M., Singh, J., Eyers, D., and Bacon, J. (2015). Camflow: Managed datasharing for cloud services. IEEE Transactions on Cloud Computing, 5(3):472–484.]]
[[pandit2019b|Pandit, H. J., O’Sullivan, D., and Lewis, D. (2019). Test-driven approach towards gdpr compliance. In Acosta, M., Cudré-Mauroux, P., Maleshkova, M., Pellegrini, T., Sack, H., and Sure-Vetter, Y., editors, Semantic Systems. The Power of AI and Knowledge ]]
[[belhajjame2013a|Garijo, D. and Gil, Y. (2013). P-Plan: The P-Plan ontology. W3C recommendation, W3C. https://www.opmw.org/model/p-plan17092013/.]]
[[wang2019a|Wang, L., Near, J. P., Somani, N., Gao, P., Low, A., Dao, D., and Song, D. (2019). Data capsule: A new paradigm for automatic compliance with data privacy regulations. In Heterogeneous Data Management, Polystores, and Analytics for Healthcare, pages 3–23. Springer.]]
[[pohly2012a|Pohly, D. J., McLaughlin, S., McDaniel, P., and Butler, K. (2012). Hi-fi: collecting highfidelity whole-system provenance. In Proceedings of the 28th Annual Computer Security Applications Conference on, pages 259–268.]]
[[bier2013a|Bier, C. (2013). How usage control and provenance tracking get together-a data protection perspective. In 2013 IEEE Security and Privacy Workshops, pages 13–17. IEEE.]]
[[shastri2019a|Shastri, S., Banakar, V., Wasserman, M., Kumar, A., and Chidambaram, V. (2019). Understanding and benchmarking the impact of gdpr on database systems. arXiv preprint arXiv:1910.00728.]]
[[aldeco2008a|Aldeco Perez, R. and Moreau, L. (2008). Provenance-based auditing of private data use. In BCS International Academic Conference.]]
[[gjermundrød2016a|Gjermundrød, H., Dionysiou, I., and Costa, K. (2016). privacytracker: a privacy-bydesign gdpr-compliant framework with verifiable data traceability controls. In International Conference on Web Engineering, pages 3–15. Springer.]]
[[martin2012a|Martin, A. P., Lyle, J., and Namiluko, C. (2012). Provenance as a security control. In TaPP.]]
[[bates2015a|Bates, A., Tian, D. J., Butler, K. R., and Moyer, T. (2015). Trustworthy whole-system provenance for the linux kernel. In 24th {USENIX} Security Symposium ({USENIX} Security 15), pages 319–334.]]
[[ozsoyoglu1995a|Ozsoyoglu, G. and Snodgrass, R. T. (1995). Temporal and real-time databases: A survey. IEEE Transactions on Knowledge and Data Engineering, 7(4):513–532.]]
- [[ujcich2018a]]