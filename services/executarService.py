
import numpy as np
import joblib
import xgboost as xgb


class DiagnosticoIA:
    def __init__(
        self,
        model_path: str = "model/modelo_HealthIA.json",
        vectorizer_path: str = "model/vetorizador_HealthIA.pkl",
        encoder_path: str = "model/encoderY_HealthIA.pkl",
    ):
        self.vet = joblib.load(vectorizer_path)
        self.enc = joblib.load(encoder_path)

        self.model = xgb.Booster()
        self.model.load_model(model_path)

    def predict_simples(self, sintomas_list):
        """
        Retorna Top-2 hipóteses com percentuais (probabilidades reais do modelo).
        """
        sintomas_list = [str(s).strip() for s in (sintomas_list or []) if str(s).strip()]
        if not sintomas_list:
            return {
                "sintomas_recebidos": [],
                "diagnostico_provavel": "Nenhum sintoma informado",
                "top2": [],
                "acuracia_modelo": 83.67,
                "modelo": "XGBoost",
            }

        texto = ", ".join(sintomas_list)
        X_vec = self.vet.transform([texto])

        pred = self.model.predict(xgb.DMatrix(X_vec))
        if pred.ndim == 1:
            pred = pred.reshape(1, -1)

        probs = pred[0]
        top_idx = np.argsort(probs)[::-1][:2]  # Top-2

        # índice -> nome da classe
        if hasattr(self.enc, "inverse_transform"):
            top_labels = self.enc.inverse_transform(top_idx)
        else:
            top_labels = [self.enc[i] for i in top_idx]

        top2 = []
        for lbl, i in zip(top_labels, top_idx):
            top2.append({
                "doenca": str(lbl),
                "prob_percent": round(float(probs[i]) * 100, 2)
            })

        diagnostico_previsto = top2[0]["doenca"] if top2 else "Classe desconhecida"

        return {
            "sintomas_recebidos": sintomas_list,
            "diagnostico_provavel": str(diagnostico_previsto),
            "top2": top2,
            "acuracia_modelo": 83.67,
            "modelo": "XGBoost",
        }
