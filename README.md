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

---

## Why this project exists

Many beginner Kubernetes projects stop at *“it runs”*.  
This project goes one step further and focuses on:

- how Kubernetes decides when traffic should reach a pod  
- how applications scale safely  
- how failures are handled automatically  
- how configuration is separated from application code  

These are the basics of **real-world DevOps and platform engineering**.

---

## Repository structure







