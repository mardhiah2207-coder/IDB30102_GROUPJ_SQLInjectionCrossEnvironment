import urllib.parse
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def preprocess_query(query: str) -> str:
    """Clean and normalize raw SQL query string."""
    if not isinstance(query, str):
        return ""
    # URL decoding and lowercasing
    decoded_query = urllib.parse.unquote(query)
    normalized_query = decoded_query.lower().strip()
    return normalized_query


def run_cross_environment_experiment():
    print("=" * 60)
    print("  Group J: Cross-Environment SQLi Detection Prototype")
    print("=" * 60 + "\n")

    # 1. Baseline Training Dataset (Environment A: Kaggle Benchmark Queries)
    env_a_queries = [
        "SELECT * FROM users WHERE id = 1",
        "SELECT username, password FROM accounts WHERE active = 1",
        "SELECT * FROM products WHERE category = 'electronics'",
        "INSERT INTO audit_logs (action) VALUES ('user_login')",
        "UPDATE users SET email = 'user@example.com' WHERE id = 5",
        "SELECT * FROM users WHERE username = 'admin' AND '1'='1'",
        "SELECT * FROM products WHERE cat = 'books' UNION SELECT username, password FROM users--",
        "SELECT * FROM accounts WHERE id = 1 OR 1=1--",
        "1' OR 'a'='a",
        "SELECT * FROM members WHERE name = '' OR '1'='1' --"
    ]
    env_a_labels = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]  # 0: Benign, 1: Malicious SQLi

    # 2. Unseen Test Dataset (Environment B: Web Application Logs / Obfuscated Injections)
    env_b_queries = [
        "SELECT name, price FROM items WHERE status = 'active'",
        "SELECT id FROM employees WHERE department = 'IT'",
        "INSERT INTO comments (post_id, text) VALUES (10, 'Great post!')",
        "admin' OR '1'='1'/*",
        "1'; DROP TABLE users;--",
        "SELECT * FROM orders WHERE user_id = 10 UNION ALL SELECT null, null--",
        "SELECT * FROM credit_cards WHERE card_num = '4111' OR 2>1--",
        "SELECT title FROM articles WHERE published = true"
    ]
    env_b_labels = [0, 0, 0, 1, 1, 1, 1, 0]  # Ground truth labels for Env B

    df_env_a = pd.DataFrame({'query': env_a_queries, 'label': env_a_labels})
    df_env_b = pd.DataFrame({'query': env_b_queries, 'label': env_b_labels})

    # Preprocessing
    df_env_a['clean_query'] = df_env_a['query'].apply(preprocess_query)
    df_env_b['clean_query'] = df_env_b['query'].apply(preprocess_query)

    # Feature Extraction: Character n-gram TF-IDF Vectorization
    vectorizer = TfidfVectorizer(ngram_range=(1, 3), analyzer='char_wb')
    X_train = vectorizer.fit_transform(df_env_a['clean_query'])
    y_train = df_env_a['label']

    X_test_b = vectorizer.transform(df_env_b['clean_query'])
    y_test_b = df_env_b['label']

    # Model Training on Environment A
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train, y_train)

    # Inference on Environment B (Cross-Environment Evaluation)
    y_pred_b = clf.predict(X_test_b)
    y_proba_b = clf.predict_proba(X_test_b)[:, 1]

    # Evaluation Metrics Calculation
    acc = accuracy_score(y_test_b, y_pred_b)
    prec = precision_score(y_test_b, y_pred_b)
    rec = recall_score(y_test_b, y_pred_b)
    f1 = f1_score(y_test_b, y_pred_b)

    print("[+] Model Training Completed on Environment A (Baseline Dataset)")
    print("[+] Evaluating Generalization on Environment B (Secondary Web Logs):\n")

    for i, (q, label, pred, proba) in enumerate(zip(env_b_queries, y_test_b, y_pred_b, y_proba_b)):
        status = "MALICIOUS [BLOCKED]" if pred == 1 else "BENIGN [ALLOWED]"
        actual = "Malicious" if label == 1 else "Benign"
        print(f"Query {i+1}: {q[:55]}")
        print(f"   -> True Label: {actual} | Predicted: {status} (Probability SQLi: {proba:.2f})\n")

    print("-" * 60)
    print("CROSS-ENVIRONMENT PERFORMANCE METRICS (Environment B):")
    print(f"  - Accuracy : {acc * 100:.2f}%")
    print(f"  - Precision: {prec * 100:.2f}%")
    print(f"  - Recall   : {rec * 100:.2f}%")
    print(f"  - F1-Score : {f1 * 100:.2f}%")
    print("=" * 60)


if __name__ == "__main__":
    run_cross_environment_experiment()
