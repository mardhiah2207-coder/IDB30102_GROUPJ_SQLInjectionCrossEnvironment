# Expected Results

The proposed SQL Injection detection model will be evaluated using both within-environment and cross-environment testing.

## Proposed Evaluation

| Evaluation | Training Data | Testing Data | Purpose |
|---|---|---|---|
| Within-Environment | Environment A | Environment A (20% test set) | Establish baseline performance |
| Cross-Environment | Environment A | Environment B | Evaluate model generalisation |

The model performance will be measured using Accuracy, Precision, Recall, F1-score, False Positive Rate (FPR), and Processing Time.

## Expected Results Table

| Metric | Environment A | Environment B |
|---|---|---|
| Accuracy | TBD | TBD |
| Precision | TBD | TBD |
| Recall | TBD | TBD |
| F1-score | TBD | TBD |
| False Positive Rate | TBD | TBD |
| Processing Time | TBD | TBD |

**TBD** indicates that the actual values will be obtained during the experimental stage.

The results from Environment A and Environment B will be compared to determine whether the Random Forest model can maintain its SQL Injection detection performance when tested on an unseen environment. A decrease in performance on Environment B will also be considered an important finding because it may indicate limitations in cross-environment generalisation.
