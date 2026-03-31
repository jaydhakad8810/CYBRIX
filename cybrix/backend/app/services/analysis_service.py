from urllib.parse import urlparse

from app.models.analysis import AnalysisResponse


class AnalysisService:
    """Service layer for rule-based analysis behavior."""

    SUSPICIOUS_KEYWORDS = ("login", "verify", "secure", "account", "bank")
    MESSAGE_RULES = (
        (
            ("urgent", "immediately", "now", "action required"),
            25,
            "Urgency language detected",
        ),
        (
            ("bank", "account", "payment", "credit card"),
            20,
            "Financial terms detected",
        ),
        (
            ("click here", "verify now", "login now", "claim reward"),
            25,
            "Suspicious call-to-action detected",
        ),
        (
            ("account blocked", "legal action", "suspended"),
            20,
            "Threat or fear-based language detected",
        ),
    )

    def analyze_link(self, url: str) -> AnalysisResponse:
        """Analyze a URL using simple deterministic rules."""
        normalized_url = url.strip()
        parsed_url = self._parse_url(normalized_url)
        reasons: list[str] = []
        risk = 0

        domain = parsed_url.netloc or parsed_url.path
        if domain:
            reasons.append(f"Domain extracted: {domain}")

        lowered_url = normalized_url.lower()
        for keyword in self.SUSPICIOUS_KEYWORDS:
            if keyword in lowered_url:
                risk += 15
                reasons.append(f"Suspicious keyword detected: {keyword}")

        if parsed_url.scheme.lower() == "http":
            risk += 20
            reasons.append("URL uses http instead of https")

        if len(normalized_url) > 50:
            risk += 10
            reasons.append("URL length is greater than 50 characters")

        risk = min(risk, 100)

        if risk >= 60:
            action = "High Risk"
        elif risk > 0:
            action = "Suspicious"
        else:
            action = "Safe"
            reasons.append("No suspicious rules were triggered")

        return AnalysisResponse(
            risk=risk,
            reason=reasons,
            action=action,
        )

    def analyze_message(self, message: str) -> AnalysisResponse:
        """Analyze a message using deterministic phishing and scam rules."""
        normalized_message = message.strip()
        lowered_message = normalized_message.lower()
        reasons: list[str] = []
        risk = 0

        for keywords, score, category in self.MESSAGE_RULES:
            matches = self._find_keyword_matches(lowered_message, keywords)
            if matches:
                risk += score
                joined_matches = ", ".join(matches)
                reasons.append(f"{category}: {joined_matches}.")

        if "http" in lowered_message:
            risk += 15
            reasons.append("A link was detected in the message, which is commonly used in phishing attempts.")

        risk = min(risk, 100)

        if risk >= 60:
            action = "High Risk"
        elif risk > 0:
            action = "Suspicious"
        else:
            action = "Safe"
            reasons.append("No common phishing or scam patterns were detected.")

        return AnalysisResponse(risk=risk, reason=reasons, action=action)

    def _parse_url(self, url: str):
        """Parse URLs safely and support inputs without an explicit scheme."""
        parsed_url = urlparse(url)
        if parsed_url.scheme or parsed_url.netloc:
            return parsed_url
        return urlparse(f"https://{url}")

    def _find_keyword_matches(self, text: str, keywords: tuple[str, ...]) -> list[str]:
        """Return the matched keywords for a rule without duplicating entries."""
        return [keyword for keyword in keywords if keyword in text]
