import os
import json
import time
import sklearn
from sklearn.datasets import make_classification
from sklearn.frozen import FrozenEstimator
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import FixedThresholdClassifier

print(sklearn.__version__)

X, y = make_classification(n_samples=1000, random_state=0)

start_sgd = time.time()
classifier = SGDClassifier().fit(X, y)
end_sgd = time.time()
print(f"Fitting the classifier took {(end_sgd - start_sgd) * 1_000:.2f} milliseconds")

start = time.time()
threshold_classifier = FixedThresholdClassifier(
    estimator=FrozenEstimator(classifier), threshold=0.9
).fit(X, y)
end = time.time()
print(f"Fitting the threshold classifier took {(end - start) * 1_000:.2f} milliseconds")

msg = (
    f"Fitting the SGDClassifier took {(end_sgd - start_sgd) * 1_000:.2f} milliseconds\n"
    f"Fitting the FixedThresholdClassifier took {(end - start) * 1_000:.2f} milliseconds\n"
)

# Write only the final accuracy to result.txt
output_directory = os.environ["IEXEC_OUT"]
output_path = os.path.join(output_directory, "result.txt")

with open(output_path, "w") as f:
    f.write(msg)

with open(os.path.join(output_directory, 'computed.json'), 'w') as f:
        json.dump({"deterministic-output-path": output_path}, f)
