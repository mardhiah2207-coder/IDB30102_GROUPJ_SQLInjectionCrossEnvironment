# Summary of Methods and Algorithms Identified from Previous Studies

The reviewed literature identifies several techniques used for SQL Injection detection and prevention.

# Summary of Methods and Algorithms

| Method / Algorithm | Supporting Paper(s) | Purpose | Strength | Limitation |
|---|---|---|---|---|
| Aho-Corasick | Kini et al. (2022) | Pattern matching for SQLi detection | Simple and effective for known patterns | Dependent on predefined patterns and weak against new mutations |
| Parameterised Queries | Okesola et al. (2023) | Prevent malicious input from changing SQL query structure | Effective preventive development practice | Does not perform ML-based SQLi classification |
| SVM | Ibrohim & Suryani (2023) | Classify SQL queries | Effective classification when combined with suitable features | Performance depends on feature representation and dataset |
| Naïve Bayes | Ibrohim & Suryani (2023) | Classify SQL queries | Simple and suitable for text-based classification | Dependent on feature representation and dataset |
| Random Forest | Shah et al. (2024); Falowo et al. (2025); Toktassyn & Al-Hubaishi (2026) | Classify malicious and legitimate SQL queries | Strong classification performance and relatively interpretable | Performance may depend on training dataset and features |
| XGBoost | Pansare et al. (2025) | Classify SQL queries using TF-IDF features | Very high reported classification performance | Performance may be dataset-dependent and can involve greater model complexity |
| Decision Tree | Hosen et al. (2026); Falowo et al. (2025) | SQLi classification | Lightweight and interpretable | May have limitations when handling more complex patterns |
| Stacking Ensemble | Falowo et al. (2025) | Combine several ML classifiers | Combines strengths of multiple models | More complex and may require additional processing |
| TF-IDF | Ibrohim & Suryani (2023); Pansare et al. (2025); Hosen et al. (2026); Toktassyn & Al-Hubaishi (2026) | Convert SQL query text into numerical features | Useful for representing query terms | Fixed representation may not fully capture unseen or complex patterns |
| SHAP | Hosen et al. (2026) | Explain ML predictions | Improves interpretability | Adds an additional explanation component |

## Selected Algorithm

Random Forest is selected for the proposed research as a practical machine learning classification approach.

The selection is based on:

- Relatively straightforward implementation
- Ability to perform classification using multiple decision trees
- Suitability for tabular and feature-based datasets
- Relatively manageable computational requirements
- Easier interpretation compared with more complex deep learning architectures

The research does not state that Random Forest is the best SQL Injection detection algorithm. Instead, the study focuses on evaluating whether Random Forest can generalise effectively across different SQL Injection datasets.
