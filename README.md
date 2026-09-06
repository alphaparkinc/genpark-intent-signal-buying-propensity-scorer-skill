# GenPark AI Agent Skill - Intent Signal Propensity Scorer

Calculates predictive B2B outbound buying propensity scores by aggregating time-decayed hiring signals, venture funding injections, and technographic stack shifts.

Verified by [GenPark AI](https://genpark.ai) and compatible with [Model Context Protocol (MCP)](https://genpark.ai/mcp).

## Architecture Diagram

```mermaid
graph TD
    A[B2B Intent Signals Stream] --> B[Signal Classification Engine]
    B --> C[Exponential Time Decay Model]
    C --> D[Category Weight Aggregator]
    D --> E[Propensity Score Normalizer: 0-100]
    E --> F{Intent Tier Classifier}
    F -->|Score >= 80| G[Urgent Outbound Trigger]
    F -->|Score 55-79| H[In-Market High Intent]
    F -->|Score 30-54| I[Warm Engagement]
    F -->|Score < 30| J[Cold Baseline]
```

## Features
- **Exponential Half-Life Decay**: Naturally depreciates outdated signals while prioritizing high-velocity recent catalysts.
- **Deterministic Categorization**: Assigns precise outbound actions based on quantitative score boundaries.
- **Zero Third-Party Dependencies**: Pure Python standard library implementation.
- **Ready for MCP Agent Swarms**: Enables autonomous GTM agents to prioritize target accounts.
