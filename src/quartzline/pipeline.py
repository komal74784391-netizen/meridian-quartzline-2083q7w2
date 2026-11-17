"""Composable feature pipeline used by Quartzline."""

from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List


@dataclass
class FeatureStep:
    name: str
    fn: Any


@dataclass
class Pipeline:
    steps: List[FeatureStep] = field(default_factory=list)

    def add(self, name: str, fn) -> "Pipeline":
        self.steps.append(FeatureStep(name=name, fn=fn))
        return self

    def run(self, rows: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
        result = []
        for row in rows:
            features = dict(row)
            for step in self.steps:
                features[step.name] = step.fn(features)
            result.append(features)
        return result
