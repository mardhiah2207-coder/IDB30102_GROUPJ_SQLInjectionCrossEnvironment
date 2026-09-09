# References Supporting the Proposed Methodology

The following studies support the development and evaluation of the proposed machine learning-based SQL Injection detection approach.

## 1. Kini et al. (2022)

Kini et al. investigated SQL Injection detection and prevention using the Aho-Corasick pattern matching algorithm. Their study used 860 malicious SQL Injection query patterns and reported 90.23% detection accuracy.

**Relevance:** Provides a traditional pattern-based approach that can be used as a baseline for comparison with machine learning-based SQL Injection detection.

Reference: Kini, S., Patil, A. P., Pooja, M., & Balasubramanyam, A. (2022). *SQL injection detection and prevention using Aho-Corasick pattern matching algorithm*. 3rd International Conference for Emerging Technology (INCET), 1–6.

---

## 2. Ibrohim and Suryani (2023)

Ibrohim and Suryani investigated SQL Injection classification using TF-IDF with SVM and Naïve Bayes ensemble learning. Their study reported 92.9% accuracy.

**Relevance:** Supports the use of machine learning and feature-based classification for SQL Injection detection.

Reference: Ibrohim, M. M., & Suryani, V. (2023). Classification of SQL Injection Attacks using ensemble learning 
SVM and Naïve Bayes. 2023 International Conference on Data Science and Its Applications 
(ICoDSA), 230–236.

DOI: 10.1109/ICODSA58501.2023.10277436

---

## 3. Okesola et al. (2023)

Okesola et al. investigated the prevention of SQL Injection attacks from a parameterised query perspective. The study focused on using parameterised queries to reduce the risk of SQL Injection in web applications.

**Relevance:** Provides a conventional SQL Injection prevention approach and establishes a comparison point between secure coding techniques and machine learning-based detection.

Reference: J. O. Okesola, A. S. Ogunbanwo, A. Owoade, E. O. Olorunnisola and K. Okokpuji. (2023) Securing web 
applications against SQL injection attacks - A Parameterised Query perspective. 2023 
International Conference on Science, Engineering and Business for Sustainable Development 
Goals (SEB-SDG), Omu-Aran, Nigeria, 2023, pp. 1-6, doi: 10.1109/SEB
SDG57117.2023.10124613.

---

## 4. Shah et al. (2024)

Shah et al. proposed a machine learning approach for classifying malicious SQL Injection code. Their study used feature selection with Extra Trees and applied Random Forest for classification, reporting 98.9% accuracy on Kaggle query logs.

**Relevance:** Directly supports the selection of Random Forest as a practical machine learning technique for SQL Injection detection.

Reference: Shah, I., Jhanjhi, N., & Brohi, S. (2024). Proposing Model for Classification of Malicious SQLi Code 
Using Machine Learning Approach.

DOI: 10.1109/ICIESTR60916.2024.10798230

---

## 5. Falowo et al. (2025)

Falowo et al. investigated SQL Injection detection and classification using a stacking ensemble model. The approach combined Decision Tree, Random Forest and Logistic Regression as base learners with a meta-classifier using approximately 33,000 SQL queries.

**Relevance:** Demonstrates the effectiveness of ensemble machine learning techniques and shows that Random Forest can contribute to SQL Injection detection.

Reference: Falowo, G., Olorunfemi, B. O., Adeniyi, A. E., Abosede, O. B., & Ogbuju, E. (2025). *Machine learning-based detection and classification of SQL injection attacks using a stacking ensemble model*. 2025 International Conference on Technology, Applied Science and Computing (ICTAS), 1-6.

---

## 6. Pansare et al. (2025)

Pansare et al. applied TF-IDF and XGBoost for SQL Injection detection using 30,000 SQL queries, consisting of 15,000 benign and 15,000 malicious queries. The study reported 99.37% accuracy, 99.41% precision, 99.31% recall and 99.36% F1-score.

**Relevance:** Demonstrates strong machine learning performance and highlights the importance of dataset characteristics when evaluating SQL Injection detection models.

Reference: Pansare, S. S., Nimbalkar, P. S., Mhaske, P. P., Kadam, S. P., Patil, G. P., & Angadi, S. (2025). *Preventing SQL Injection Attacks with Machine Learning: A TF-IDF + XGBoost Approach*. 2nd International Conference on Computational and Data Science (ICCDS), 1-6.

---

## 7. Hosen et al. (2026)

Hosen et al. investigated lightweight SQL Injection detection using Decision Trees, TF-IDF and SHAP-based explainability. Their study reported 98.31% training accuracy and 97.52% accuracy on external data.

**Relevance:** Particularly relevant to the proposed research because the difference between training and external evaluation demonstrates the importance of testing machine learning models on data beyond the original training dataset.

Reference: Hosen, S., Zihan, A. A. M., & Mamun, N. (2026). Interpretable SQL Injection Detection: Lightweight 
Decision Trees with SHAP-Enhanced Deployment. 2026 IEEE 2Nd International Conference on 
Quantum Photonics, Artificial Intelligence &Amp; Networking (QPAIN), 1–5.

---

## 8. Toktassyn and Al-Hubaishi (2026)

Toktassyn and Al-Hubaishi investigated SQL Injection detection using advanced feature engineering and machine learning ensemble methods. Their study used 244,068 SQL queries and evaluated multiple machine learning models. Random Forest achieved 99.3% accuracy using an 80:20 split and 99.1% using a 50:50 split.

**Relevance:** Strongly supports the use of Random Forest for SQL Injection detection while highlighting the limitation of evaluation using a single dataset.

Reference: Toktassyn, & Al-Hubaishi. (2026). *Enhanced SQL Injection Detection Using Advanced Feature Engineering and Machine Learning Ensemble Methods*. 4th International Conference on Data Intelligence and Computing Technologies (IDCIoT), 914–921.

---

## 9. Arif et al. (2022)

Arif et al. investigated SQL Injection detection and prevention for MySQL databases using input categorization and an input verifier. The study evaluated the approach using 15 web applications with five different database characteristics. The method categorized user input and verified whether the input was safe or malicious before blocking potential SQL Injection attempts.

**Relevance:** Provides a traditional input validation and verification approach that supports comparison between conventional SQL Injection prevention techniques and machine learning-based detection.

Reference: Arif, A. A. S., Purwoko, R., Qomariasih, N., & Setiawan, H. (2022). *Analysis of SQL Injection Attack Detection and Prevention on MySQL Database Using Input Categorization and Input Verifier*. 2022 IEEE 8th Information Technology International Seminar (ITIS), 190–194.

---

## 10. Qbea’h et al. (2022)

Qbea’h et al. reviewed different SQL Injection attack types and mitigation techniques. The study compared machine learning approaches with static and dynamic methods and discussed tools such as SQLBlock, DIAVA, SQLMap and Acunetix. The review highlighted that existing machine learning techniques may not cover all SQL Injection attack types.

**Relevance:** Provides an overview of existing SQL Injection detection and mitigation approaches and highlights the need for more comprehensive solutions that can handle different attack types and environments.

Reference: M. Qbea'h, S. Alrabaee, M. Alshraideh and K. E. Sabri. (2022) Diverse Approaches Have Been 
Presented To Mitigate SQL Injection Attack, But It Is Still Alive: A Review. 2022 International 
Conference on Computer and Applications (ICCA), Cairo, Egypt, 2022, pp. 1-5, doi: 
10.1109/ICCA56443.2022.10039611. 

DOI: 10.1109/ICCA56443.2022.10039611

---

## 11. Bouafia et al. (2023)

Bouafia et al. investigated the automatic detection and exploitation of SQL Injection vulnerabilities using Acunetix, Burp Suite and SQLMap. The study followed a practical workflow involving scanning, interception, command generation and exploitation using the Damn Vulnerable Web Application (DVWA).

**Relevance:** Demonstrates the use of automated security testing tools for SQL Injection vulnerability detection and provides a practical perspective that complements machine learning-based detection approaches.

Reference: R. Bouafia, H. Benbrahim and A. Amine. (2023) Automatic Protection of Web Applications Against SQL 
Injections: An Approach Based On Acunetix, Burp Suite and SQLMAP. 2023 9th International 
Conference on Optimization and Applications (ICOA), AbuDhabi, United Arab Emirates, 2023, 
pp. 1-6.

DOI: 10.1109/ICOA58279.2023.10308827

---

## 12. Muliono et al. (2022)

Muliono et al. investigated the prediction of the impact of SQL Injection attacks on confidentiality, integrity and availability. The study used the CSIC 2010 dataset and SQLMap payloads and applied an SVM classifier integrated with a Security Information and Event Management (SIEM) system. The study achieved more than 94% accuracy in classifying SQL Injection attack types and intentions.

**Relevance:** Demonstrates how machine learning can be used not only to detect SQL Injection attacks but also to classify their potential security impact, while highlighting the importance of training data quality.

Reference: Y. Muliono, M. Y. Darus, C. R. Pardomuan, M. A. M. Ariffin and A. Kurniawan. (2022) Predicting 
Confidentiality, Integrity, and Availability from SQL Injection Payload. 2022 International 
Conference on Information Management and Technology (ICIMTech), Semarang, Indonesia, 
UniKL CDDH v4 Appendix N - Assessment Coversheet v3 (2025-12-03)  
2022, pp. 600-605.

DOI: 10.1109/ICIMTech55957.2022.9915227

---

## 13. Zhang et al. (2022)

Zhang et al. proposed a deep neural network-based SQL Injection detection method called SQLNN. The approach converted SQL statements into numerical representations using TF-IDF and used a multi-hidden-layer neural network with ReLU and Dropout. The model was evaluated against KNN, Decision Tree and LSTM approaches using a Kaggle dataset containing 30,919 SQL records.

The proposed model maintained an accuracy above 96% and performed better than the compared models across accuracy, precision, recall and F1-score.

**Relevance:** Provides evidence that deep learning can achieve strong SQL Injection detection performance and provides a comparison with conventional machine learning models. It also demonstrates the importance of evaluating models using multiple performance metrics.

Reference: Zhang, W., Li, Y., Li, X., Shao, M., Mi, Y., Zhang, H., & Zhi, G. (2022). Deep neural network-based SQL 
injection detection method. Security and Communication Networks, 2022, Article 4836289.

DOI: 10.1155/2022/4836289

---

## 14. Zulu et al. (2024)

Zulu et al. investigated the use of contextualized word embeddings for machine learning-based SQL Injection detection. The study compared contextualized and non-contextualized embeddings with several classification approaches, including neural networks, K-nearest neighbors, Random Forest and Logistic Regression. The study reported accuracy above 99% across different classification algorithms and found that contextualized embeddings could substantially reduce model training time while improving model calibration.

**Relevance:** Demonstrates that feature representation can influence SQL Injection detection performance and that Random Forest can be evaluated together with different query representation techniques. The study also supports the importance of examining model performance beyond accuracy alone.

Reference: Zulu, J., Han, B., Alsmadi, I., & Liang, G. (2024). Enhancing machine learning based SQL injection 
detection using contextualized word embedding. Proceedings of the 2024 ACM Southeast 
Conference, 211–216.

DOI: 10.1145/3603287.3651187

---

# Methodological Implication

The reviewed studies demonstrate that both traditional and machine learning approaches can be applied to SQL Injection detection and prevention. Traditional approaches such as Aho-Corasick pattern matching and parameterised queries provide established methods for identifying or preventing SQL Injection attacks, while machine learning approaches such as SVM, Naïve Bayes, Random Forest, XGBoost and ensemble models have reported strong detection performance.

However, the high performance reported in individual studies does not necessarily establish strong generalisation across different SQL Injection datasets. Several studies evaluate their models using specific datasets, while Hosen et al. (2026) demonstrate that performance can differ when external data is used.

Therefore, the proposed research uses Random Forest to investigate whether a machine learning-based SQL Injection detection approach can maintain consistent performance across different SQL Injection datasets. Accuracy, Precision, Recall, F1-score, and Processing Time will be used to evaluate both detection effectiveness and practical efficiency.
