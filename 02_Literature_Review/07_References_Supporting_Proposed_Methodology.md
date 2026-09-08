# References Supporting the Proposed Methodology

The following studies support the development and evaluation of the proposed machine learning-based SQL Injection detection approach.

## 1. Ibrohim and Suryani (2023)

Ibrohim and Suryani investigated SQL Injection classification using TF-IDF with SVM and Naïve Bayes. Their study demonstrates that conventional machine learning algorithms can be applied to SQL Injection detection.

**Relevance:** Supports the use of machine learning for SQL Injection classification.

DOI: 10.1109/ICODSA58501.2023.10277436

---

## 2. Shah et al. (2024)

Shah et al. investigated a machine learning-based approach for SQL Injection detection and reported high detection performance.

**Relevance:** Provides evidence that ML approaches can achieve strong SQL Injection detection performance.

DOI: 10.1109/ICIESTR60916.2024.10798230

---

## 3. Pansare et al. (2025)

Pansare et al. applied TF-IDF and XGBoost for SQL Injection detection using 30,000 SQL queries. The study reported 99.37% accuracy and 99.36% F1-score.

**Relevance:** Demonstrates strong ML performance and provides evidence that dataset characteristics are important when evaluating SQL Injection detection.

---

## 4. Hosen et al. (2026)

Hosen et al. investigated Decision Tree-based SQL Injection detection with SHAP explainability. The study reported 98.31% training accuracy and 97.52% external accuracy.

**Relevance:** Particularly relevant to the proposed research because external evaluation demonstrates the importance of testing models beyond the original training data.

---

## 5. Zulu et al. (2024)

Zulu et al. investigated contextualised embeddings using RoBERTa for SQL Injection detection and reported approximately 99% accuracy.

**Relevance:** Provides comparison with a more complex deep learning approach and demonstrates that high performance has been achieved using advanced models.

---

## Methodological Implication

The reviewed studies demonstrate that machine learning can be effectively applied to SQL Injection detection. However, the high performance reported in individual studies does not necessarily establish strong generalisation across different SQL Injection datasets.

Therefore, the proposed research uses Random Forest and evaluates its performance across different datasets. Accuracy, Precision, Recall, F1-score, and Processing Time will be used to assess both detection effectiveness and practical efficiency.
