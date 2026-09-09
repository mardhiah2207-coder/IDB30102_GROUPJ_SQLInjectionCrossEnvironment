# Dataset Sources

This research uses two different datasets to evaluate the cross-environment generalisation of the proposed SQL Injection detection model.

## Environment A: SQL Injection Dataset

**Source:** Kaggle  
**Dataset Provider:** syedsaqlainhussain  
**Dataset Link:** https://www.kaggle.com/datasets/syedsaqlainhussain/sql-injection-dataset

**Purpose:**  
Environment A will be used as the primary dataset for model training and within-environment baseline testing. The dataset provides SQL query data for distinguishing between normal and SQL Injection inputs.

**Research Usage:**  
- Model training
- TF-IDF feature extraction
- Within-environment baseline testing

---

## Environment B: HttpParamsDataset

**Source:** GitHub - Morzeux/HttpParamsDataset  
**Dataset Link:** https://github.com/Morzeux/HttpParamsDataset

**Purpose:**  
Environment B will be used as the unseen dataset for cross-environment generalisation testing. The dataset contains values that can appear as parameters in HTTP requests.

For this research, only benign (`norm`) and SQL Injection (`sqli`) samples will be used. Other attack categories such as XSS, Command Injection, and Path Traversal will not be included because this research focuses only on SQL Injection detection.

**Research Usage:**  
- Unseen cross-environment testing
- Generalisation performance evaluation
- Comparison with Environment A

The Random Forest model trained using Environment A will be tested on Environment B without retraining or further tuning.
