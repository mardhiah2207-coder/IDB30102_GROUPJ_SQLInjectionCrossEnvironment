# SQL Injection Detection in Web Applications for Improved Cross-Environment Performance

## 1. Research Project Information

- **Group Number:** Group J
- **Group Members:**
  - Person 1: NUR AINUL MARDHIAH BINTI AZRIL – 52215124223
  - Person 2: NUR AFIQAH SHAZWANI BT ASMARIRAMZI – 52215124775
  - Person 3: NUR AINNA AFINA BINTI HAMZAH – 52215124331
  - Person 4: NURFATIMAH HUSNA BINTI AHMAD ZAFFRI – 52215124246
- **Assigned Research Area:** Website Security
- **Research Topic:** SQL Injection

---

## 2. Research Problem

Current SQL Injection detection methods have shown encouraging results when tested with particular datasets, web applications, databases, or controlled environments. Nonetheless, there is limited evidence of their ability to generalise across different environments. A detection method that performs well on one dataset or application may not achieve the same performance when applied to different SQL Injection patterns, datasets, or application environments. This makes it difficult to assess the reliability and consistency of current detection methods across different environments.

Variations in datasets and application environments can influence the performance of SQL Injection detection methods. Differences in SQL query formats, attack patterns, database configurations, and application characteristics may affect detection outcomes. Therefore, a systematic evaluation across different selected environments is necessary to determine whether a SQL Injection detection method can maintain consistent detection performance beyond the environment in which it was initially tested.

### Research Gap

**Limited Generalisation Across Different SQL Injection Datasets**

Existing SQL Injection detection studies often evaluate models using a specific dataset or controlled environment. Limited evidence is available regarding whether the same detection model can maintain consistent performance across different SQL Injection datasets with different SQL syntax, attack patterns, and data characteristics.

---

## 3. Research Aim

The aim of this research is to investigate the cross-environment generalisation of an SQL Injection detection approach by evaluating its detection performance across different selected datasets and environments.

---

## 4. Research Objectives

1. To identify the characteristics and patterns of SQL Injection attacks across different selected datasets and environments.

2. To implement a machine learning-based approach for detecting SQL Injection attacks.

3. To evaluate the generalisation performance of the proposed SQL Injection detection approach across different selected datasets and environments using appropriate performance metrics.

---

## 5. Proposed Solution

The proposed research will implement a **Random Forest-based machine learning approach** for detecting SQL Injection attacks.

The system will use **Term Frequency-Inverse Document Frequency (TF-IDF)** to transform processed SQL query text into numerical features for machine learning classification.

The Random Forest model will be trained using a selected SQL Injection dataset and evaluated using a different unseen dataset. This cross-dataset evaluation will be used to determine whether the model can maintain consistent detection performance when applied to different types of SQL Injection data.

The proposed detection approach will classify input data into two categories:

- **Normal / Benign Query**
- **Malicious SQL Injection**

The research will focus on examining the generalisation capability of the Random Forest detection model rather than evaluating its performance only within the dataset used for training.

---

## 6. Research Methodology

The research will use the **Cross-Industry Standard Process for Data Mining (CRISP-DM)** as the main research methodology.

An **Iterative Prototyping** development model will also be adopted to support the development and improvement of the machine learning-based detection prototype.

### 6.1 CRISP-DM

CRISP-DM provides a structured approach for conducting the data-driven research process. The methodology will cover the following activities:

1. Research problem and SQL Injection threat understanding
2. Data collection and understanding
3. Data preprocessing and feature engineering
4. Machine learning model development
5. Model evaluation
6. Generalisation analysis

### 6.2 Iterative Prototyping

The Iterative Prototyping model will support incremental development and improvement of the detection prototype. This allows the preprocessing, feature extraction, and machine learning components to be refined based on the results obtained during development and validation.

### 6.3 Research Phases

#### Phase 1: Security and Threat Model Definition

This phase focuses on identifying SQL Injection characteristics, attack patterns, and differences between SQL Injection data from different environments.

#### Phase 2: Query Preprocessing and Feature Engineering

The collected data will be cleaned and prepared through processes such as:

- Removing duplicate records
- Removing invalid or empty records
- Standardising labels
- Converting query text to lowercase
- Decoding URL-encoded characters
- Tokenisation
- TF-IDF feature extraction

#### Phase 3: Machine Learning Detection Engine Prototyping

The prepared data will be used to develop a Random Forest-based SQL Injection detection prototype using Python and Scikit-learn.

Environment A will be used for model training and baseline testing.

#### Phase 4: Cross-Environment Evaluation and Generalisation Analysis

The trained model will be tested using Environment B without retraining or further tuning. The performance between the original and unseen environments will then be compared to determine the model's generalisation capability.

---

## 7. Proposed Evaluation Plan

The proposed evaluation will be conducted in two stages.

### 7.1 Baseline Evaluation

The Random Forest model will be trained using **80% of Environment A** and tested using the remaining **20%**.

This evaluation will establish the baseline performance of the model within the original dataset environment.

### 7.2 Cross-Environment Evaluation

The same trained Random Forest model and TF-IDF vectoriser will then be applied directly to **Environment B** without retraining or further tuning.

The performance obtained from Environment A and Environment B will be compared to determine whether the model can maintain its detection performance when applied to unseen data.

### 7.3 Environment A: Kaggle SQL Injection Dataset

Environment A uses the Kaggle SQL Injection Dataset created by user `sajid576`.

The dataset contains:

- **30,919** total SQL query entries
- **11,330** malicious SQL Injection entries
- **19,589** benign entries

The dataset contains different SQL Injection attack patterns, including:

- Union-based SQL Injection
- Error-based SQL Injection
- Time-based SQL Injection
- Boolean-based blind SQL Injection

### 7.4 Environment B: HttpParams Dataset

Environment B uses the **HttpParams Dataset**, an open-source dataset hosted on GitHub by `Morzeux/HttpParamsDataset`.

The dataset contains:

- **30,156** total entries
- **10,852** malicious SQL Injection payloads
- **19,304** normal web requests

Unlike Environment A, which mainly consists of standalone SQL query strings, Environment B contains HTTP GET and POST request parameters and web page payloads.

The differences between Environment A and Environment B provide a basis for cross-environment evaluation. :contentReference[oaicite:2]{index=2}

### 7.5 Evaluation Metrics

The model will be evaluated using:

- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**
- **False Positive Rate (FPR)**
- **Processing Time**

These metrics provide a broader evaluation of classification performance, SQL Injection detection capability, false alarms, and processing efficiency. :contentReference[oaicite:3]{index=3}

### 7.6 Generalisation Analysis

The results from Environment A will be compared with the results from Environment B.

A smaller decrease in F1-score and Recall, together with a low False Positive Rate, will indicate better cross-environment generalisation.

Processing time will also be considered to determine whether the model can classify queries efficiently.

The comparison will help identify the strengths and limitations of the model when applied to unseen data. :contentReference[oaicite:4]{index=4}

---

## 8. Proposed System Architecture

The proposed SQL Injection detection system consists of three main layers:

### 8.1 Data Input Layer

This layer receives the input data used for SQL Injection detection and cross-environment evaluation.

The input may include:

- SQL query strings
- HTTP query parameters
- Form parameters
- Benchmark SQL Injection datasets
- Web application request data

The two main environments are:

- **Environment A:** Kaggle SQL Injection Dataset
- **Environment B:** HttpParams Dataset

### 8.2 Processing Layer

The Processing Layer functions as the machine learning middleware.

The main processes include:

1. Query preprocessing
2. Lowercase conversion
3. URL decoding
4. Special character normalisation
5. Tokenisation
6. TF-IDF feature extraction
7. Random Forest classification

### 8.3 Output and Action Layer

The system provides a binary security decision based on the classification result.

- **Normal Query → Allow / Pass to Database**
- **Malicious SQL Injection → Block and Log Security Alert**

Attack metadata can also be recorded for further performance and generalisation analysis.

The proposed three-layer architecture is based on the architecture developed in Chapter 3, consisting of the Data Input Layer, Processing Layer, and Output & Action Layer. :contentReference[oaicite:5]{index=5}

### 8.4 System Flow


Start
  ↓
Receive SQL Query / HTTP Request
  ↓
Decode & Preprocess
  ↓
TF-IDF Feature Extraction
  ↓
Random Forest Classifier
  ↓
Is the Query Malicious?
       ↓
   ┌───┴────┐
  Yes       No
   ↓         ↓
Block &    Allow
Log Alert  Query
   ↓         ↓

## 9. Technical Components

### 9.1 Programming Language

- Python

### 9.2 Machine Learning Algorithm

- Random Forest Classifier
- Binary Classification

### 9.3 Feature Extraction

- TF-IDF (Term Frequency-Inverse Document Frequency)

### 9.4 Machine Learning Library

- Scikit-learn

### 9.5 Data Processing

The system will perform:

- Data cleaning
- Duplicate removal
- Invalid record removal
- Label standardisation
- Lowercase conversion
- URL decoding
- Tokenisation
- Feature filtering
- TF-IDF vectorisation

### 9.6 Input Data

The proposed system will process:

- SQL query strings
- SQL Injection payloads
- Normal SQL queries
- HTTP GET parameters
- HTTP POST parameters
- Web application request data

### 9.7 Evaluation Components

The system will use:

- Accuracy
- Precision
- Recall
- F1-score
- False Positive Rate
- Processing Time


## 10. Preliminary Code Instructions

The proposed implementation will be developed using Python.

The preliminary implementation pipeline will follow these steps:

1. Load the selected SQL Injection datasets.
2. Inspect and understand the dataset structure.
3. Remove duplicate, empty, and invalid records.
4. Standardise the classification labels:
   - `0` = Normal
   - `1` = SQL Injection
5. Convert query text to lowercase.
6. Decode URL-encoded characters.
7. Remove unnecessary URL information while retaining relevant SQL characters and operators.
8. Tokenise the processed query text.
9. Apply TF-IDF vectorisation.
10. Split Environment A into 80% training data and 20% testing data.
11. Train the Random Forest classifier using the training data.
12. Evaluate the baseline performance using the Environment A test data.
13. Apply the same trained model and TF-IDF vectoriser to Environment B.
14. Do not retrain or further tune the model during the Environment B evaluation.
15. Calculate the selected evaluation metrics.
16. Compare the performance between Environment A and Environment B.
17. Analyse the model's cross-environment generalisation performance.

### Preliminary Software Environment

```text
Python
Scikit-learn
TF-IDF Vectorizer
Random Forest Classifier
   └────┬────┘
        ↓
       End
