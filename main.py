import torch
from src.auditor_logic import ScientificAuditor

# Check for GPU
device = 0 if torch.cuda.is_available() else -1

# Initialize and run
auditor = ScientificAuditor('data/advanced_physics_kb.csv', device=device)
audit_results = auditor.run_audit('reports')

# Save and print results
audit_results.to_csv('audit_summary.csv', index=False)
print("🛡️ Audit Complete. Summary saved to audit_summary.csv")
print(audit_results.head(10))