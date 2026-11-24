# End-to-End DevOps Automation Platform (Capstone Project)
**Author:** Krish Agarwal (2301730146) — B.Tech CSE (AI & ML), K.R. Mangalam University

## Architecture & Pillars
1. **CI/CD Pipeline (`.github/workflows/capstone-cicd.yml`):** Automated Pytest & DevSecOps security gates.
2. **Containerization (`app/Dockerfile`):** Hardened non-root Alpine Python container with healthchecks.
3. **Kubernetes Orchestration (`k8s/`):** Declarative Deployment & NodePort Service manifests.
4. **Infrastructure as Code (`infra/main.tf`):** Reproducible Terraform provisioning configuration.
5. **Observability (`observability/prometheus.yml`):** Prometheus `/metrics` endpoint & structured JSON logs.
6. **Security (`security/secret_guard.py`):** Vault secret injection & log masking (`***MASKED***`).
7. **Canary & DR (`deploy/`, `dr/`):** 90/10 progressive rollout & automated snapshot backups.
