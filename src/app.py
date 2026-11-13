"""Meter ingest for Faircurrent Energy"""

class MeterIngest:
    """Internal service for meter-ingest."""

    def status(self) -> str:
        return "ok"


if __name__ == "__main__":
    print(MeterIngest().status())
