# Summary of Methods and Algorithms Identified from Previous Studies

The reviewed literature identifies several techniques used for SQL Injection detection and prevention.

| Method / Algorithm | Type | Example Study | Main Purpose |
|---|---|---|---|
| Aho-Corasick | Pattern Matching | Kini et al. (2022) | Detect known SQL Injection patterns |
| Parameterised Queries | Prevention | Okesola et al. (2023) | Prevent malicious input from being executed as SQL |
| SVM | Machine Learning | Ibrohim & Suryani (2023) | Classify SQL queries |
| Naïve Bayes | Machine Learning | Ibrohim & Suryani (2023) | Classify legitimate and malicious queries |
| Random Forest | Machine Learning | Previous ML literature | Classification using multiple decision trees |
| RoBERTa | Deep Learning | Zulu et al. (2024) | Capture contextual information in SQL queries |
| BERT-LSTM | Deep Learning | Liu & Dai (2024) | Capture contextual and sequential patterns |
| AST-based Trident | Structural Analysis | Li et al. (2024) | Analyse SQL query structures |
| XGBoost | Machine Learning | Pansare et al. (2025) | Classify SQL Injection queries |
| Decision Tree + SHAP | Machine Learning / Explainable AI | Hosen et al. (2026) | Detection with model interpretation |

## Selected Algorithm

Random Forest is selected for the proposed research as a practical machine learning classification approach.

The selection is based on:

- Relatively straightforward implementation
- Ability to perform classification using multiple decision trees
- Suitability for tabular and feature-based datasets
- Relatively manageable computational requirements
- Easier interpretation compared with more complex deep learning architectures

The research does not state that Random Forest is the best SQL Injection detection algorithm. Instead, the study focuses on evaluating whether Random Forest can generalise effectively across different SQL Injection datasets.
