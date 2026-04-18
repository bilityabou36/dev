# AWS DOP-C02 DevSecOps Lab

This project is a hands-on AWS lab designed to cover the six domains of the AWS Certified DevOps Engineer - Professional (DOP-C02) exam:

1. SDLC Automation
2. Configuration Management and IaC
3. Resilient Cloud Solutions
4. Monitoring and Logging
5. Incident and Event Response
6. Security and Compliance

## Objective

Build an end-to-end DevSecOps pipeline on AWS that:
- pulls code from GitHub
- builds and tests an application
- deploys infrastructure with CloudFormation
- runs security checks
- enables monitoring and tracing
- automates remediation events
- demonstrates resilience and high availability

## Initial Scope

Phase 1:
- GitHub repository
- Python sample application
- BuildSpec for AWS CodeBuild
- CloudFormation starter template

## Planned AWS Services

- AWS CodePipeline
- AWS CodeBuild
- AWS CodeConnections
- AWS CloudFormation
- Amazon EC2
- Elastic Load Balancing
- Amazon CloudWatch
- AWS Lambda
- Amazon EventBridge
- AWS Systems Manager
- AWS IAM
- AWS KMS
- AWS CloudTrail

## Repo Structure

```text
architecture/
app/
infrastructure/cloudformation/
pipeline/
scripts/
monitoring/
incident-response/
security/
evidence/