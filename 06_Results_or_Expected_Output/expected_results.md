# Expected Results and Evaluation Output

This folder presents the expected results and evaluation output for the proposed machine learning-based SQL Injection (SQLi) detection model. Since the project is currently at the proposal stage, the actual experimental results have not yet been obtained. The final results will be added after model development and testing are completed.

## Evaluation Approach

The proposed Random Forest model will be evaluated in two stages. First, within-environment testing will be conducted using Environment A to establish the baseline performance of the model. Environment A will be divided into 80% training data and 20% testing data.

After baseline testing, the same trained model will be tested on Environment B without retraining or further tuning. This cross-environment evaluation will be used to determine how well the model can detect SQL Injection when applied to a different and unseen data environment.

| Evaluation | Training Data | Testing Data | Purpose |
|---|---|---|---|
| Within-Environment Testing | Environment A (80%) | Environment A (20%) | Establish baseline performance |
| Cross-Environment Testing | Environment A (80%) | Environment B | Evaluate cross-environment generalisation |

## Evaluation Metrics

The performance of the model will be evaluated using the following metrics:

- **Accuracy** – Measures the overall percentage of correctly classified queries.
- **Precision** – Measures how many queries predicted as SQL Injection are actually malicious.
- **Recall** – Measures how many actual SQL Injection queries are successfully detected.
- **F1-score** – Provides a balance between Precision and Recall.
- **False Positive Rate (FPR)** – Measures how often normal queries are incorrectly classified as SQL Injection.
- **Processing Time** – Measures the time required by the model to process and classify the input.

## Proposed Results Table

The actual values will be recorded after the experiments are completed.

| Metric | Environment A | Environment B |
|---|---|---|
| Accuracy | TBD | TBD |
| Precision | TBD | TBD |
| Recall | TBD | TBD |
| F1-score | TBD | TBD |
| False Positive Rate | TBD | TBD |
| Processing Time | TBD | TBD |

**TBD** means that the value will be determined during the experimental stage.

## Expected Outcome

The results from both environments will be compared to evaluate the generalisation ability of the proposed model. A small difference in performance between Environment A and Environment B would indicate better cross-environment generalisation. However, a decrease in performance on Environment B would also provide useful findings by showing the limitations of the model when dealing with unseen SQL Injection data.

The final results may be presented using performance tables, graphs, and a confusion matrix to provide a clear comparison between the two environments.
