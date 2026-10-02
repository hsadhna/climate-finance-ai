# Climate Finance AI

An evolving climate-finance analytics project designed to connect corporate greenhouse gas emissions with financial risk and sustainability reporting.

## Project Goal

The long-term goal is to build a tool that can:

- Calculate corporate Scope 1, Scope 2, and eventually Scope 3 GHG emissions
- Maintain a transparent audit trail of activity data and emission factors
- Translate emissions into potential financial impacts
- Perform carbon-price scenario analysis
- Assess climate-related financial risks
- Support sustainability and climate reporting frameworks
- Generate decision-useful dashboards and company-level insights

## Current Version — Phase 1

The first prototype contains a Python carbon accounting engine that:

1. Stores activity data and emission factors
2. Calculates emissions by source
3. Aggregates emissions by GHG Protocol scope
4. Calculates carbon-cost scenarios
5. Expresses potential carbon cost as a percentage of EBITDA

### Core calculation

Emissions (tCO2e) = Activity Data × Emission Factor

### Important

The current activity data, emission factors, carbon prices, and financial figures are illustrative placeholders used to test the model architecture. They should not be interpreted as actual company or regulatory data.

## Planned Development

Future phases will incorporate:

- Authoritative Canadian emission factors
- Scope 3 categories
- Company data inputs
- Carbon pricing and scenario analysis
- Climate-related financial risk metrics
- Sustainability reporting framework mapping
- Data visualizations and dashboards
- Automated report generation
- AI-assisted analysis

## Technologies

- Python
- pandas
- Git / GitHub

## Status

Work in progress.