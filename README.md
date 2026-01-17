# Kubernetes Stateless Service Blueprint

A beginner-friendly but production-oriented example of how to deploy and operate a stateless service on Kubernetes using core Kubernetes primitives.

---

## What is this project?

This repository is a **practical Kubernetes blueprint** that shows how a simple stateless application is deployed, scaled, and managed in a way that resembles real production setups.

The goal is not to build a complex application, but to focus on **how applications should behave and be operated inside Kubernetes**.

---

## What this project demonstrates

- Containerizing a simple stateless application
- Deploying it using a Kubernetes Deployment
- Managing configuration with ConfigMaps and Secrets
- Handling health checks using readiness and liveness probes
- Scaling the application using a Horizontal Pod Autoscaler (HPA)
- Exposing the service internally and externally using Service and Ingress
- Applying safe, zero-downtime rolling updates

---

## High-level architecture

Client → Ingress → Service → Deployment → Pods


All resources are deployed inside a dedicated Kubernetes namespace for isolation.


## Repository structure
.
├── app/ # Minimal stateless application
├── docker/ # Dockerfile for the application
├── k8s/ # Kubernetes manifests
├── scripts/ # Deployment helper scripts
├── diagrams/ # Architecture diagram
└── README.md

---

## Notes & limitations

- Autoscaling is CPU-based and reactive
- No persistent storage (by design)
- Secrets are handled using Kubernetes Secrets only
- TLS and advanced routing depend on the ingress controller

These choices are intentional to keep the project simple and focused.

---







