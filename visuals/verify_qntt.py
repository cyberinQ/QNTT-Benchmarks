# Author: Sunil Jain and Punya Jain
from qiskit_ibm_runtime import QiskitRuntimeService

# Initializing service for public verification
service = QiskitRuntimeService(
    channel='ibm_quantum_platform',
    instance='crn:v1:bluemix:public:quantum-computing:us-east:a/e66db19aee9b4e6aa5ff8497cea834ed:26478c31-7fc7-49c0-ba86-f05f3680e349::'
)

# Accessing the specific job used in the arXiv paper
job_id = 'd6aaursnsg9c7397m2h0'
job = service.job(job_id)
job_result = job.result()

# Verification output
print(f"📊 Job {job_id} successfully retrieved.")
print(f"Status: {job.status()}")

# To get counts for a particular pub result:
# pub_result = job_result[0].data.meas.get_counts()