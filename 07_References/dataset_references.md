# Dataset References

This research uses two datasets representing different data environments for training, baseline testing, and cross-environment evaluation.

## Environment A: SQL Injection Dataset

**Platform:** Kaggle  
**Dataset Provider:** syedsaqlainhussain  
**Dataset Name:** SQL Injection Dataset  
**Dataset Link:** https://www.kaggle.com/datasets/syedsaqlainhussain/sql-injection-dataset

**Use in this research:**  
Environment A will be used as the primary dataset for model training and within-environment baseline testing. The dataset will be divided into 80% training data and 20% testing data.

## Environment B: HttpParamsDataset

**Platform:** GitHub  
**Repository Owner:** Morzeux  
**Dataset Name:** HttpParamsDataset  
**Dataset Link:** https://github.com/Morzeux/HttpParamsDataset

**Use in this research:**  
Environment B will be used for cross-environment generalisation testing. Only benign (`norm`) and SQL Injection (`sqli`) samples will be selected because the proposed research focuses on binary SQL Injection detection.

The trained model from Environment A will be evaluated on Environment B without retraining or further tuning. This allows the research to compare model performance across two different data environments.
