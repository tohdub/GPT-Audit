# GPT Audit — Quick Start Audit Template (v1.0)

This template is designed to help you run your **first audits** quickly, while remaining aligned with the **GPT Audit Charter v1.0**. Use it as a starting point in your GitHub repo. Over time, expand with sector-specific checklists, detailed ADRs, and automation.

---

## 1. Project Overview

```yaml
project:
  name: <string>
  vision: <1–2 sentences>
  success_criteria: [<KPI or acceptance tests>]
audience: {non_technical | mixed | technical}
priorities: <rank latency, cost, quality, safety, UX>
```

---

## 2. Artifacts to Audit

```yaml
artifacts:
  prompts: [<files/links>]
  evals: [<design docs, datasets, dashboards>]
  apis: [<OpenAPI/specs, code refs>]
  automations: [<workflows, CI/CD, infra>]
  ux: [<flows, screenshots, prototypes>]
```

---

## 3. Standards & Compliance

```yaml
standards:
  writing: [IEEE, ISO, or company style guide]
  compliance: [SOC2, ISO 27001, GDPR, WCAG 2.2]
ssot:
  repos: [<GitHub URLs with commit SHAs>]
```

---

## 4. Specialist Panel Review (skeleton)

```yaml
reviews:
  - role: Lead Auditor
    findings: <scope, missing artifacts, SSOT check>
  - role: Technical Writer
    findings: <clarity, style adherence, completeness>
  - role: UX Reviewer
    findings: <journeys, accessibility, onboarding>
  - role: Optimization Engineer
    findings: <latency, cost, token use>
  - role: Reasoning & Evaluation Scientist
    findings: <metrics, dataset validity>
  - role: Safety & Compliance Officer
    findings: <privacy, risk, alignment to standards>
  - role: Tooling & Automation Engineer
    findings: <APIs, retries, observability>
  - role: Model Ops Specialist (Claude)
    findings: <context, cost>
  - role: Model Ops Specialist (Gemini)
    findings: <multimodal, QPS>
  - role: Business Use Case Analyst
    findings: <ROI, adoption>
  - role: Data & Analytics Auditor
    findings: <pipelines, BI integrations>
```

---

## 5. Debate & Decision Record

```yaml
decision_record:
  context: <why this decision matters>
  options:
    - name: Option A
      pros: [...]
      cons: [...]
    - name: Option B
      pros: [...]
      cons: [...]
  decision: <chosen option>
  rationale: <why chosen>
  consequences: <risks + follow-ups>
```

---

## 6. Compliance Gate & Checklist

```yaml
compliance:
  verdict: {Pass | Fail}
  severity: {Blocker | Major | Minor | Info}
  checklist:
    technical_writing: <0–2>
    ux: <0–2>
    optimization: <0–2>
    reasoning_eval: <0–2>
    api_automation: <0–2>
    compliance_safety: <0–2>
    business_analytics: <0–2>
```

---

## 7. Good / Better / Best Recommendations

```yaml
recommendations:
  area: Security
  good: SOC2 reporting
  better: Partial ISO 27001 alignment
  best: Full ISO 27001 certification + external audit
```

---

## 8. Remediation Plan

```yaml
remediation:
  owner: <name>
  actions: [<fix steps>]
  due_date: <date>
```

---

# Builder Instructions for Custom GPT

To deploy **GPT Audit** as a custom GPT:

1. **System Prompt**: Paste the **Charter v1.0** into the *System Instructions* field of your custom GPT.
2. **Startup Greeting**: Configure to say:
   *“Hello, I’m GPT Audit — a multi-expert audit council. I will help you audit your project against industry standards, explain trade-offs in plain language, and give you good/better/best recommendations.”*
3. **File Input**: Connect to your GitHub repo (read-only) to fetch SSOT artifacts and standards docs.
4. **Output Modes**: Default to **Full Audit Report**, but allow user to request **Quick Gate** or **Change Review**.
5. **Templates**: Store this file (`audit_template.yaml`) in `/templates` within the repo.

---

✅ With this skeleton, you can start running **audits today** by filling in the YAML sections. The GPT Audit council will take care of reasoning, debate, and reporting.
