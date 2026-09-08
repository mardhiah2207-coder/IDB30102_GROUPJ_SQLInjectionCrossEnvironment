# Evaluation Metrics

The proposed research will evaluate the Random Forest SQL Injection detection approach using five main metrics:

## 1. Accuracy

Accuracy measures the proportion of correctly classified samples among all samples.

Formula:

Accuracy = (TP + TN) / (TP + TN + FP + FN)

## 2. Precision

Precision measures how many queries classified as malicious are actually malicious.

Formula:

Precision = TP / (TP + FP)

High precision indicates that the model produces fewer false positive classifications.

## 3. Recall

Recall measures the proportion of actual SQL Injection attacks that are correctly detected.

Formula:

Recall = TP / (TP + FN)

High recall is important because failing to detect malicious SQL Injection queries may create security risks.

## 4. F1-Score

F1-score provides a balance between precision and recall.

Formula:

F1 = 2 × (Precision × Recall) / (Precision + Recall)

F1-score is useful when both false positives and false negatives need to be considered.

## 5. Processing Time

Processing time measures the time required by the model to process and classify the SQL query data.

Processing time is included to evaluate not only detection effectiveness but also the practical efficiency of the proposed approach.

## Evaluation Summary

| Metric | Purpose |
|---|---|
| Accuracy | Overall classification performance |
| Precision | Ability to avoid false positive classifications |
| Recall | Ability to detect actual SQL Injection attacks |
| F1-score | Balance between precision and recall |
| Processing Time | Computational efficiency |

Using multiple evaluation metrics provides a more comprehensive assessment than relying on accuracy alone. The results from different datasets will be compared to determine whether the model maintains consistent performance.
