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

DOI: 10.1109/ICODSA58501.2023.10277436

---

## 3. Okesola et al. (2023)

Okesola et al. investigated the prevention of SQL Injection attacks from a parameterised query perspective. The study focused on using parameterised queries to reduce the risk of SQL Injection in web applications.

**Relevance:** Provides a conventional SQL Injection prevention approach and establishes a comparison point between secure coding techniques and machine learning-based detection.

DOI: 10.1109/SEB-SDG57117.2023.10124613

---

## 4. Shah et al. (2024)

Shah et al. proposed a machine learning approach for classifying malicious SQL Injection code. Their study used feature selection with Extra Trees and applied Random Forest for classification, reporting 98.9% accuracy on Kaggle query logs.

**Relevance:** Directly supports the selection of Random Forest as a practical machine learning technique for SQL Injection detection.

DOI: 10.1109/ICIESTR60916.2024.10798230

---

## 5. Falowo et al. (2025)

Falowo et al. investigated SQL Injection detection and classification using a stacking ensemble model. The approach combined Decision Tree, Random Forest and Logistic Regression as base learners with a meta-classifier using approximately 33,000 SQL queries.

**Relevance:** Demonstrates the effectiveness of ensemble machine learning techniques and shows that Random Forest can contribute to SQL Injection detection.

Reference: Falowo, G., Olorunfemi, B. O., Adeniyi, A. E., Abosede, O. B., & Ogbuju, E. (2025). *Machine learning-based detection and classification of SQL injection attacks using a stacking ensemble model*. 2025 International Conference on Technology, Applied Science and Computing (ICTAS).

---

## 6. Pansare et al. (2025)

Pansare et al. applied TF-IDF and XGBoost for SQL Injection detection using 30,000 SQL queries, consisting of 15,000 benign and 15,000 malicious queries. The study reported 99.37% accuracy, 99.41% precision, 99.31% recall and 99.36% F1-score.

**Relevance:** Demonstrates strong machine learning performance and highlights the importance of dataset characteristics when evaluating SQL Injection detection models.

Reference: Pansare, S. S., Nimbalkar, P. S., Mhaske, P. P., Kadam, S. P., Patil, G. P., & Angadi, S. (2025). *Preventing SQL Injection Attacks with Machine Learning: A TF-IDF + XGBoost Approach*. 2nd International Conference on Computational and Data Science (ICCDS).

---

## 7. Hosen et al. (2026)

Hosen et al. investigated lightweight SQL Injection detection using Decision Trees, TF-IDF and SHAP-based explainability. Their study reported 98.31% training accuracy and 97.52% accuracy on external data.

**Relevance:** Particularly relevant to the proposed research because the difference between training and external evaluation demonstrates the importance of testing machine learning models on data beyond the original training dataset.

Reference: Hosen, S., Zihan, A. A. M., & Mamun, N. (2026). *Interpretable SQL Injection Detection: Lightweight Decision Trees with SHAP-Enhanced Deployment*. IEEE 2nd QPAIN.

---

## 8. Toktassyn and Al-Hubaishi (2026)

Toktassyn and Al-Hubaishi investigated SQL Injection detection using advanced feature engineering and machine learning ensemble methods. Their study used 244,068 SQL queries and evaluated multiple machine learning models. Random Forest achieved 99.3% accuracy using an 80:20 split and 99.1% using a 50:50 split.

**Relevance:** Strongly supports the use of Random Forest for SQL Injection detection while highlighting the limitation of evaluation using a single dataset.

Reference: Toktassyn, & Al-Hubaishi. (2026). *Enhanced SQL Injection Detection Using Advanced Feature Engineering and Machine Learning Ensemble Methods*. 4th International Conference on Data Intelligence and Computing Technologies (IDCIoT), 914–921.

---

# Methodological Implication

The reviewed studies demonstrate that both traditional and machine learning approaches can be applied to SQL Injection detection and prevention. Traditional approaches such as Aho-Corasick pattern matching and parameterised queries provide established methods for identifying or preventing SQL Injection attacks, while machine learning approaches such as SVM, Naïve Bayes, Random Forest, XGBoost and ensemble models have reported strong detection performance.

However, the high performance reported in individual studies does not necessarily establish strong generalisation across different SQL Injection datasets. Several studies evaluate their models using specific datasets, while Hosen et al. (2026) demonstrate that performance can differ when external data is used.

Therefore, the proposed research uses Random Forest to investigate whether a machine learning-based SQL Injection detection approach can maintain consistent performance across different SQL Injection datasets. Accuracy, Precision, Recall, F1-score, and Processing Time will be used to evaluate both detection effectiveness and practical efficiency.
