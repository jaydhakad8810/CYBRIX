from urllib.parse import urlparse

from app.models.analysis import AnalysisResponse


class AnalysisService:
    """Service layer for rule-based analysis behavior."""

    SUSPICIOUS_KEYWORDS = ("login", "verify", "secure", "account", "bank")

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

    def analyze_message(self, _: str) -> AnalysisResponse:
        return AnalysisResponse(
            risk=0,
            reason=["Not implemented yet"],
            action="Pending analysis",
        )

    def _parse_url(self, url: str):
        """Parse URLs safely and support inputs without an explicit scheme."""
        parsed_url = urlparse(url)
        if parsed_url.scheme or parsed_url.netloc:
            return parsed_url
        return urlparse(f"https://{url}")
