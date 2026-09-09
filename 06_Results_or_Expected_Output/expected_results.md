# Expected Results and Evaluation Output

This folder presents the expected outputs of the proposed machine learning-based SQL Injection (SQLi) detection research. The expected outputs are aligned with the three Research Objectives (RO1, RO2, and RO3). Since the project is currently at the proposal stage, actual experimental results will be added after model development and testing are completed.

## RO1: SQL Injection Characteristics and Patterns

The first expected output is a comparison of SQL Injection characteristics found in Environment A and Environment B. The analysis will examine differences in query structure, common SQLi patterns, tokens, special characters, and other characteristics found in both datasets.

The comparison may be presented using a table similar to the following:

| Characteristic | Environment A | Environment B |
|---|---|---|
| Data structure | To be analysed | To be analysed |
| Common SQLi patterns | To be analysed | To be analysed |
| Common tokens/keywords | To be analysed | To be analysed |
| Special characters | To be analysed | To be analysed |

This analysis will help identify similarities and differences between SQL Injection samples across the two environments.

## RO2: SQL Injection Detection Model

The second expected output is a machine learning-based SQL Injection detection prototype. The proposed model will use data preprocessing, TF-IDF feature extraction, and a Random Forest classifier.

The model will perform binary classification where input data will be classified as either:

- Normal / Benign
- SQL Injection

A sample of the expected classification output is provided in `sample_classification_output.csv`.

## RO3: Cross-Environment Evaluation

The model will be evaluated in two stages. First, Environment A will be divided into 80% training data and 20% testing data to establish baseline performance. After that, the same trained model will be tested on Environment B without retraining or further tuning.

| Evaluation | Training Data | Testing Data | Purpose |
|---|---|---|---|
| Within-Environment Testing | Environment A (80%) | Environment A (20%) | Establish baseline performance |
| Cross-Environment Testing | Environment A (80%) | Environment B | Evaluate generalisation |

## Evaluation Metrics

The model will be evaluated using:

- **Accuracy** – Overall classification correctness.
- **Precision** – Correct SQLi predictions among all SQLi predictions.
- **Recall** – Ability to detect actual SQL Injection samples.
- **F1-score** – Balance between Precision and Recall.
- **False Positive Rate (FPR)** – Normal inputs incorrectly classified as SQL Injection.
- **Processing Time** – Time required to process and classify the input.

## Proposed Results

| Metric | Environment A | Environment B |
|---|---|---|
| Accuracy | TBD | TBD |
| Precision | TBD | TBD |
| Recall | TBD | TBD |
| F1-score | TBD | TBD |
| False Positive Rate | TBD | TBD |
| Processing Time | TBD | TBD |

**TBD** means that the actual value will be obtained during the experimental stage.

The final results will compare the performance between Environment A and Environment B. This comparison will show whether the proposed model can maintain its SQL Injection detection performance when applied to a different and unseen data environment.
