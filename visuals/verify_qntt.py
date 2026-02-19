# Author: Sunil Jain and Punya Jain
# Affiliation: CyberinQ LLC / EmpowerAi
# Description: Independent verification script for QNTT Benchmarks on IBM Heron r2.

from qiskit_ibm_runtime import QiskitRuntimeService
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

def verify_and_plot_job():
    print("⏳ Initializing Qiskit Runtime Service for public verification...")
    # Initializing service for public verification
    service = QiskitRuntimeService(
        channel='ibm_quantum_platform',
        instance='crn:v1:bluemix:public:quantum-computing:us-east:a/e66db19aee9b4e6aa5ff8497cea834ed:26478c31-7fc7-49c0-ba86-f05f3680e349::'
    )

    # Accessing the specific job used in the arXiv paper
    job_id = 'd6aaursnsg9c7397m2h0'
    print(f"🔍 Fetching Job ID: {job_id} from backend: ibm_fez (Heron r2)...")
    
    job = service.job(job_id)
    job_result = job.result()

    # Verification output
    print(f"📊 Job {job_id} successfully retrieved.")
    print(f"✅ Status: {job.status()}")

    # Extracting the execution time metrics to verify the 10.8 us claim
    metadata = job.metrics()
    print(f"⏱️ Job Execution Metrics: {metadata}")

    # Extracting counts for the SamplerV2 primitive result
    try:
        # For SamplerV2, data is accessed via pub results
        pub_result = job_result[0]
        counts = pub_result.data.meas.get_counts()
        
        print(f"📈 Successfully extracted {len(counts)} unique measurement outcomes.")
        
        # Plotting the histogram
        fig = plot_histogram(counts, title=f"QNTT Measurement Results (Job: {job_id})")
        plt.tight_layout()
        plt.savefig(f"Histogram_job_{job_id}_reproduced.png", dpi=300)
        print(f"💾 Histogram saved locally as 'Histogram_job_{job_id}_reproduced.png'.")
        plt.show()

    except Exception as e:
        print(f"❌ Error extracting measurement counts: {e}")

if __name__ == "__main__":
    verify_and_plot_job()