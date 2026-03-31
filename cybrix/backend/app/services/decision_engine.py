class DecisionEngine:
    """Combine multiple analysis results into one user-facing decision."""

    def generate_decision(self, results: dict) -> dict:
        available_results = {
            name: result
            for name, result in results.items()
            if result is not None
        }

        risks = [
            int(result.get("risk", 0))
            for result in available_results.values()
        ]
        final_risk = round(sum(risks) / len(risks)) if risks else 0

        if len(available_results) >= 2:
            confidence = "High"
        elif len(available_results) == 1:
            confidence = "Medium"
        else:
            confidence = "Low"

        if final_risk <= 30:
            classification = "Safe"
        elif final_risk <= 70:
            classification = "Suspicious"
        else:
            classification = "High Risk"

        summary = self._build_summary(classification, available_results)
        recommended_action = self._build_recommended_action(classification)

        return {
            "final_risk": final_risk,
            "confidence": confidence,
            "summary": summary,
            "details": available_results,
            "recommended_action": recommended_action,
        }

    def _build_summary(self, classification: str, results: dict) -> str:
        message_result = results.get("message")
        link_result = results.get("link")

        if classification == "High Risk":
            if message_result and link_result:
                return "This appears to be a phishing attempt using suspicious message patterns and a risky link."
            if message_result:
                return "This message shows strong signs of a phishing or scam attempt."
            if link_result:
                return "This link shows strong signs of phishing or malicious activity."

        if classification == "Suspicious":
            if message_result and link_result:
                return "Some warning signs were found in both the message and link, so caution is recommended."
            if message_result:
                return "The message contains some suspicious patterns that may indicate fraud."
            if link_result:
                return "The link contains some suspicious indicators and should be treated carefully."

        return "The content looks safe with no strong indicators of phishing or fraud."

    def _build_recommended_action(self, classification: str) -> str:
        if classification == "High Risk":
            return "Do not click, reply, or share any personal information. Block and report the sender if possible."
        if classification == "Suspicious":
            return "Avoid interacting until you verify the sender or link through a trusted source."
        return "No immediate action is needed, but continue following normal online safety practices."
