# Research Gap Analysis

## Identified Research Gap

### Limited Generalisation of SQL Injection Detection Across Different Datasets

The main research gap identified from the reviewed literature is the limited evaluation of SQL Injection detection approaches across different datasets.

Many of the existing studies report high detection performance using a particular dataset. For example, Pansare et al. (2025) achieved 99.37% accuracy and 99.36% F1-score using a dataset containing 30,000 SQL queries. Other studies also report high accuracy or F1-score using datasets with different characteristics.

However, SQL Injection datasets can differ in:

- Number of SQL queries
- Ratio of malicious and legitimate queries
- SQL Injection attack types
- Payload structures
- Feature representations
- Sources of the collected data

These differencesof datasets may affect the performance of a detection model when it is applied to another dataset.

## Problem with Existing Research

A model that performs well on one dataset may not necessarily maintain the same performance when tested using another dataset.

Although some studies have included external validation, cross-dataset evaluation is not consistently performed across the reviewed research. Therefore, there is still a need to investigate whether an ML-based SQL Injection detection approach can provide consistent results across different datasets.

## Proposed Research Response

To address this gap, the proposed research will:

1. Develop an ML-based SQL Injection detection approach using Random Forest.
2. Apply the model to different SQL Injection datasets.
3. Compare detection performance across the datasets.
4. Evaluate the model using Accuracy, Precision, Recall, F1-score, and Processing Time.
5. Analyse whether the model maintains consistent performance across different datasets.

## Research Gap Summary

| Aspect | Existing Research | Identified Gap | Proposed Research |
|---|---|---|---|
| Detection approach | Traditional ML and DL approaches | Generalisation remains insufficiently evaluated | Random Forest |
| Dataset | Often dataset-specific | Different dataset characteristics may affect performance | Multiple SQL Injection datasets |
| Evaluation | Commonly reports Accuracy/F1 | Cross-dataset consistency is less frequently investigated | Cross-dataset evaluation |
| Performance | Many studies report high scores | High performance may be dataset-dependent | Compare performance across datasets |
| Practicality | Some approaches are computationally complex | Need for a relatively straightforward ML approach | Random Forest |

## Research Gap Statement

The identified gap is the limited evaluation of SQL Injection detection models across different datasets. Therefore, this research investigates whether a Random Forest-based SQL Injection detection approach can maintain good detection performance when evaluated using different SQL Injection datasets.
