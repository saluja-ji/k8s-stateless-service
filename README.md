# Kubernetes Production Blueprint

A production-oriented Kubernetes blueprint for deploying, scaling, and operating a stateless web service using native Kubernetes primitives.

---

## Overview

This repository demonstrates how a stateless application is deployed and operated in Kubernetes **with production concerns in mind**.  
The focus is on **operational correctness**, not application complexity.

The blueprint emphasizes:
- predictable deployments
- safe scaling
- health-based traffic management
- configuration isolation
- reproducible infrastructure behavior

This repository is intentionally minimal in business logic and explicit in infrastructure design.

---

## Architecture

**High-level flow**

Client
↓
Ingress
↓
Service
↓
Deployment
↓
Pods (stateless application)


All resources are deployed into a dedicated namespace to ensure logical isolation.

---

## Design Principles

### Stateless by default
The application maintains no local state, enabling safe horizontal scaling and deterministic rollouts.

### Explicit health signaling
Readiness and liveness probes are defined separately:
- readiness gates traffic
- liveness enforces container restarts

This prevents degraded pods from receiving traffic while avoiding unnecessary restarts.

### Resource-aware scheduling
CPU and memory requests and limits are explicitly defined to:
- inform scheduler placement
- support autoscaling decisions
- prevent resource starvation

### Zero-downtime deployments
Rolling updates are configured to ensure continuous availability during releases.

### Configuration isolation
Runtime configuration and secrets are externalized using Kubernetes-native mechanisms.

---

## Kubernetes Resources

| Resource | Purpose |
|--------|--------|
| Namespace | Logical isolation |
| Deployment | Declarative lifecycle management |
| Service | Stable internal networking |
| Ingress | External traffic routing |
| ConfigMap | Non-sensitive configuration |
| Secret | Sensitive configuration placeholders |
| HPA | Horizontal scaling |

---

## Deployment Strategy

- Rolling update strategy:
  - `maxUnavailable: 0`
  - `maxSurge: 1`
- Traffic is routed only to ready pods
- Failed containers are restarted automatically
- Rollbacks are achieved by reverting deployment changes

This mirrors common production deployment defaults for stateless workloads.

---

## Scaling Model

The service uses a **Horizontal Pod Autoscaler** based on CPU utilization.

- Minimum replicas ensure baseline availability
- Maximum replicas cap uncontrolled growth
- Resource requests provide accurate scaling signals

This approach is suitable for CPU-bound stateless services.

---

## Failure Handling

- Unhealthy pods are removed from service via readiness probes
- Crashed containers are restarted automatically
- Misconfigured deployments fail fast rather than degrade silently
- Kubernetes reconciliation ensures desired state convergence

---

## Repository Structure

.
├── app/ # Minimal stateless application
├── docker/ # Container build configuration
├── k8s/ # Kubernetes manifests
├── scripts/ # Operational scripts
├── diagrams/ # Architecture diagrams
└── README.md






