# Comparison of Existing SQL Injection Detection Techniques

## 1. Overview

Existing SQL Injection detection and prevention techniques can be divided into traditional approaches, machine learning (ML), and deep learning (DL). Each approach provides different advantages in terms of detection capability, computational requirements, complexity, and adaptability.

## 2. Traditional Approaches

Traditional SQL Injection approaches commonly include predefined rules, pattern matching, input validation, and parameterised queries.

Kini et al. (2022) applied the Aho-Corasick algorithm to identify SQL Injection patterns and achieved 90.23% detection accuracy. Parameterised queries have also been investigated as a prevention mechanism because they separate user input from SQL commands.

The main advantage of traditional approaches is their simplicity and relatively low computational requirements. However, pattern-based techniques may have difficulties identifying modified, obfuscated, or previously unseen SQL Injection payloads.

## 3. Machine Learning Approaches

Machine learning approaches classify SQL queries or payloads based on patterns learned from datasets.

Ibrohim and Suryani (2023) used TF-IDF with SVM and Naïve Bayes and achieved 92.9% accuracy. Pansare et al. (2025) used TF-IDF with XGBoost and achieved 99.37% accuracy and 99.36% F1-score using 30,000 SQL queries.

ML approaches can automatically learn patterns from data and provide strong classification performance. They are also generally less complex than large deep learning architectures.

## 4. Deep Learning Approaches

Deep learning approaches have also been investigated for SQL Injection detection. Zulu et al. (2024) used contextualised embeddings with RoBERTa and reported approximately 99% accuracy, while Liu and Dai (2024) used BERT-LSTM and achieved an F1-score of 95.8%.

These approaches can capture complex contextual and sequential patterns. However, they generally require greater computational resources and have higher model complexity compared with conventional ML approaches.

## 5. Comparative Analysis

| Approach | Strength | Limitation |
|---|---|---|
| Pattern-based | Simple and efficient | Limited against unseen or modified attacks |
| Parameterised queries | Effective prevention technique | Focuses mainly on secure query construction |
| Conventional ML | Good performance with relatively manageable complexity | Performance may depend on dataset characteristics |
| Deep Learning | Can capture complex patterns and contextual information | Higher computational and implementation complexity |

## 6. Synthesis

Overall, the reviewed studies demonstrate that ML and DL techniques can achieve high SQL Injection detection performance. However, the reported performance is often associated with the datasets used for training and evaluation.

Therefore, high accuracy on a single dataset does not necessarily demonstrate that a model can generalise effectively to other SQL Injection datasets. This observation motivates further investigation into cross-dataset evaluation.

For the proposed research, Random Forest is selected as a practical ML approach because it provides a relatively straightforward model structure and is easier to interpret and implement. The research does not assume that Random Forest is universally superior to other ML or DL techniques. Instead, its ability to maintain detection performance across different SQL Injection datasets will be investigated.
