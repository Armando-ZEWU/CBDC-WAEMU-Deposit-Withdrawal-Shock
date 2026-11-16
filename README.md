# Simulation de l'impact sur le crédit d'un choc de retrait en présence d'une MNBC dans la zone UEMOA

*Simulating the credit impact of a deposit-withdrawal shock in the presence of a CBDC in the WAEMU*

> A conditional threshold exercise: under which conditions does a migration of deposits to a hypothetical central bank digital currency (CBDC, "MNBC" in French) turn into a contraction of bank credit in the West African Economic and Monetary Union (WAEMU/UEMOA)?

**Status: working paper, independent undergraduate research (University of Lomé, November 2026).** The article is written in French. This is a calibration followed by a simulation on published bank balance sheets, not an econometric estimation, and its results are conditional on the assumptions listed below.

## Why this project

No CBDC exists in the WAEMU, so there is no data on its real effect. Instead of forecasting adoption, the paper asks a conditional question and answers it with a threshold:

- **Q1.** Is the withdrawal rate at which credit starts to fall reachable in a plausible range, or do banks absorb the shock with their current liquidity?
- **Q2.** Does the threshold depend more on banks' liquidity buffer or on how funds are recycled back to banks (hence on CBDC design and central bank policy)?
- **Q3.** Does the union-wide threshold hide countries that cross their own threshold much earlier?

## The model in brief

Static, one-period model with K = 8 countries. A share ζ of deposits is converted into CBDC; a share λ of those funds returns to the banking system (central bank refinancing, redeposit).

| Object | Definition |
|---|---|
| Net resource loss of country *k* | ΔF_k = (1 − λ) ζ D_k |
| Liquidity buffer | b_k = B_k / D_k, central bank money banks already hold |
| Credit contraction (country) | ΔL_k / L_k = min{1, φ · max{0, (1 − λ)ζ − b_k} / ρ_k} |
| **Critical threshold** | **ζ\*_k = b_k / (1 − λ)** |

Banks first absorb the outflow with their buffer, and cut credit only beyond the threshold. Three uncertainty parameters are tested: φ (pass-through to credit), κ (share of the measured buffer that is really usable) and π (share of CBDC funded by deposits rather than cash). Two aggregation views are shown: the union as a single balance sheet (perfect liquidity circulation) and eight separate countries (no circulation).

## Main results (baseline: strict buffer, λ = 0, range over 2021–2025)

| Result | Value |
|---|---|
| Union threshold (one balance sheet) | **7.7 % to 13.3 %** of deposits (about 3,500 to 7,500 bn FCFA) |
| Weakest country's threshold (Benin in every year except 2021) | **3.9 % to 8.8 %** of deposits |
| Union credit drop at 10 % withdrawal | 0 % to 3.0 % |
| Union credit drop at 15 % / 20 % withdrawal | 2.5 % to 9.4 % / 9.7 % to 15.8 % |
| Recycling λ = 0.5 | Doubles the thresholds (union 15.4 % to 26.5 %) |
| Holding cap of 2 % of deposits | Exposes no country in any year |
| Holding cap of 10 % | Exposes at least one country every year |
| Buffer overstated by half (κ = 0.5) | All thresholds are halved |

Reading: the strongest lever is not in banks' balance sheets but in the central bank's hands (refinancing commitment), and a low holding cap protects even the most fragile countries. The charge of a shock is concentrated on a few countries, which the union average hides.

## Data

- Source: annual reports of the Commission Bancaire de l'UMOA for 2021, 2023, 2024 and 2025 (aggregate balance sheets of credit institutions for the eight member states). The 2022 report was only available as a scan and was not used; 2022 values come from the 2023 and 2024 reports. 2025 figures are provisional.
- Extractions were automated and checked: the sum of the eight countries reproduces the published union deposits, credit and balance-sheet total for 2023–2025 (gaps below 0.05 bn FCFA).

## Reproducibility

Results are produced by `simulation_choc_retrait.py` from the workbook `Données Extrait.xlsx` (sheet `Données_pays`). The script stops with an error message if any of eleven built-in checks fails:

| Check | What it verifies |
|---|---|
| G1 | Worked example (100 deposits, 80 loans, 10 % outflow, 6 % buffer) gives exactly a 5 % drop |
| G2 | No contraction anywhere when λ = 1 |
| G3 | The contraction never decreases when the outflow increases |
| G4 | Zero contraction below the critical threshold (all countries, all years) |
| G5 | The aggregate never exceeds the sum of countries (Jensen inequality) |
| G6 | The eight country weights sum to 100 % each year |
| G7 | Every drop is between 0 and 100 %, with no missing value |
| G8 | The union buffer equals the one computed independently in the data workbook |
| G9 | κ = 1 reproduces the baseline exactly |
| G10 | The threshold is proportional to κ |
| G11 | All announced figures exist |

The article contains 20 figures (thresholds by country and year, contraction curves, role of recycling, holding-cap diagnostics, robustness to φ and to the buffer measurement error).

## Limitations

- **Upper bound on credit.** The baseline (φ = 1) rations quantities, harsher than the second-round price mechanism described in the literature; results for φ < 1 are smaller in the same proportion.
- **Gradual migration only.** No bank run (Diamond and Dybvig, 1983) and no dynamics.
- **Buffer measurement.** The buffer includes foreign and interbank balances that cannot be separated in the reports, so it is an upper bound on central bank money. The 3 % reserve requirement used in the measurement comes from a secondary source and has to be checked against the BCEAO text.
- **The outflow is not necessarily a deposit outflow.** Where cash dominates, a CBDC may first draw on banknotes; π is not estimated here.
- **Common parameters.** ζ and λ are assumed identical across the eight countries; dispersion between banks inside a country is not modelled.
- **No estimation.** Thresholds are consequences of a model applied to balance-sheet data, not empirical findings. Past the threshold the linear slope comes from the chosen functional form, not from the data.

## Citation

ZEWU, Y. A. I. (2026). *Simulation de l'impact sur le crédit d'un choc de retrait en présence d'une MNBC dans la zone UEMOA*. Working paper, Université de Lomé.

## Author

ZEWU Yawo Armand Isaac, undergraduate student in International Economics, FASEG, University of Lomé.
