import os
import pickle
import tensorflow as tf
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


EMBEDDINGS_PATH = "./data/embeddings.pkl"
MODEL_PATH = "./models/model_lstm_v2.keras"
ENCODED_LABELS_PATH = "./data/encoded_to_label.pkl"
LABELS_ENCODED_PATH = "./data/label_to_encoded.pkl"
TRAMITS_MAP = "./data/tramits_map.pkl"


class ActionsPredictor:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, model=None):
        if not hasattr(self, "_initialized"):  # Avoid re-initialization
            self._initialized = True
            self._load_embeddings()
            self._load_model()
            self._load_encoded_mappings()
        self._input_labels = []

    def _load_embeddings(self):
        """Load embeddings from file (if available)."""
        if os.path.exists(EMBEDDINGS_PATH):
            with open(EMBEDDINGS_PATH, "rb") as f:
                self._embeddings = pickle.load(f)
        else:
            raise Exception("Embeddings file not found.")

    def _load_model(self):
        """Load model from file (if available)."""
        if os.path.exists(MODEL_PATH):
            self._model = tf.keras.models.load_model(MODEL_PATH)
        else:
            raise Exception("Model file not found.")

    def _load_encoded_mappings(self):
        """Load encoded mappings from file (if available)."""
        if os.path.exists(ENCODED_LABELS_PATH):
            with open(ENCODED_LABELS_PATH, "rb") as f:
                self._encoded_to_labels = pickle.load(f)
        else:
            raise Exception("Encoded labels file not found.")
        if os.path.exists(LABELS_ENCODED_PATH):
            with open(LABELS_ENCODED_PATH, "rb") as f:
                self._labels_to_encoded = pickle.load(f)
        else:
            raise Exception("Labels encoded file not found.")
        if os.path.exists(TRAMITS_MAP):
            with open(TRAMITS_MAP, "rb") as f:
                self._tramits_id_to_name = pickle.load(f)
                self._tramits_name_to_id = {
                    v: k for k, v in self._tramits_id_to_name.items()
                }

    def clean_input(self, input):
        """Clean input before processing."""

        def remove_repeated_actions():
            """Remove repeated actions."""
            i = 0
            while i < len(input) - 1:
                if input[i][0] == input[i + 1][0] and input[i][1] == input[i + 1][1]:
                    del input[i]
                else:
                    i += 1

        def add_generic():
            """Add generic action if less than 3 actions."""
            generic_action = ("Sol·licitud genèrica", "AFIT")
            for _ in range(3 - len(input)):
                input.insert(0, generic_action)

        remove_repeated_actions()
        if len(input) < 3:
            add_generic()
        print(input)
        return input[-3:]

    def _parse_input(self, input):
        """Parse input to embeddings."""
        parsed_input = []
        for action in input:
            tramit_id = self._tramits_name_to_id[action[0]]
            joint_action = "_".join([action[1], tramit_id])
            encoded_action = self._labels_to_encoded[joint_action]
            self._input_labels.append(encoded_action)
            if encoded_action in self._embeddings:
                parsed_input.append(self._embeddings[encoded_action])
            else:
                raise Exception(f"Action '{encoded_action}' not found in embeddings.")
        return parsed_input

    def _get_n_closest_actions(self, prediction, n=6):
        """Get the n closest actions to the prediction."""
        similarities = []
        for action_id, embedding in self._embeddings.items():
            embedding = embedding.reshape(1, -1)
            similarity = cosine_similarity([prediction], embedding)[0][0]
            similarities.append((action_id, similarity))
        similarities.sort(key=lambda x: x[1], reverse=True)
        top_n_similar = similarities[:n]
        return top_n_similar

    def _parse_output(self, output, n=3):
        """Parse output to human-readable format."""
        parsed_output = []
        for action_label, similarity in output:
            if action_label in self._input_labels:
                continue
            action_id = self._encoded_to_labels[action_label]
            action_name, tramit_id = action_id.split("_")
            tramit_name = self._tramits_id_to_name[tramit_id]
            parsed_output.append(tramit_name)
        return parsed_output[:n]

    def predict_action(self, actions):
        """Predict action using the loaded embeddings."""
        clean_input = self.clean_input(actions)
        # PREDICT WITH MODEL
        parsed_input = self._parse_input(clean_input)
        # print(parsed_input)
        prediction = self._model.predict(np.expand_dims(parsed_input, axis=0))
        # print(prediction)
        actions_to_recommend = self._get_n_closest_actions(prediction[0])
        # Parse ouput
        actions = self._parse_output(actions_to_recommend)
        print(actions)

        return actions[0]
