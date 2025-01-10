from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from utils import load_dataset, save_joblib, is_exists
from app import logger


class ModelBuilding:

    def setup_pipeline(self) -> bool:
        try:
            df = load_dataset("cleaned/transformed.csv")

            # X , Y split
            X = df.drop(columns=["churn"])
            Y = df["churn"]
            logger.info("feature/target split completed")

            x_train, x_test, y_train, y_test = train_test_split(
                X, Y, random_state=9374, shuffle=True, test_size=0.2
            )
            logger.info("train/test split completed")

            best_params: dict = {
                "n_estimators": 200,
                "max_depth": 15,
                "min_samples_split": 6,
            }

            estimator: RandomForestClassifier = RandomForestClassifier(**best_params)
            model = estimator.fit(x_train, y_train)
            logger.info("model trained successfully")
            save_joblib(model, "random_forest_model.joblib")
            return True

        except Exception as e:
            logger.error(f"exception occured: {e}")
            return False

    def run(self) -> bool:
        if is_exists("MODEL_PATH", "random_forest_model.joblib"):
            logger.info("model already exists")
            return True
        pipeline_status = self.setup_pipeline()
        if pipeline_status:
            logger.info("model training pipeline run successfully")
            return True
        logger.error("model training pipeline failed!")
        return False
