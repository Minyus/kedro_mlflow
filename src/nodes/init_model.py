from sklearn.linear_model import LogisticRegression


def init_model():
    return LogisticRegression(C=1.23456, max_iter=987, random_state=42,)
