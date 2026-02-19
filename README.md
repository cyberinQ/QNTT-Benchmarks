# QNTT Benchmarks: Verification Supplement

This repository contains the physical verification data, circuit logic, and measurement outputs for the arXiv preprint: 
**"On the Parallelized Decomposition of Number Theoretic Transforms via NISQ-Era Quantum Fourier Gates"**.

## Physical Hardware Execution Details
- **Job ID**: `d6aaursnsg9c7397m2h0`
- **Backend Architecture**: `ibm_fez` (156-qubit IBM Heron r2)
- **Instance**: `crn:v1:bluemix:public:quantum-computing:us-east:a/e66db19aee9b4e6aa5ff8497cea834ed:26478c31-7fc7-49c0-ba86-f05f3680e349::`
- **Execution Date**: February 17, 2026
- **Measured Circuit Depth**: 23 layers

## Repository Structure
- `verify_qntt.py`: Python script utilizing `qiskit-ibm-runtime` to programmatically retrieve, verify, and plot the job results directly from the IBM Quantum Platform.
- `/visuals/Metadata_job-d6aaursnsg9c7397m2h0-info.json`: Raw execution metadata including spans and hardware overhead metrics.
- `/visuals/QASM_Logic_job-d6aaursnsg9c7397m2h0-result.json`: Transpiled SamplerV2 primitive output.
- `/visuals/Histogram_job_d6aaursnsg9c7397m2h0_results_meas.png`: Visual distribution of the QNTT execution measurement outcomes.

## Reproduction Instructions
To independently verify the results published in the paper:
1. Ensure you have Qiskit and the IBM Runtime installed: `pip install qiskit qiskit-ibm-runtime matplotlib`
2. Run the verification script: `python verify_qntt.py`
3. The script will output the execution spans confirming the 10.8 μs physical execution latency and generate the measurement histogram.

## Citation
If you utilize this benchmark data or the QNTT decomposition method in your research, please cite our arXiv paper:
*(Update with arXiv BibTeX once published)*

## Authors
Sunil Jain and Punya Jain (CyberinQ LLC / EmpowerAi)