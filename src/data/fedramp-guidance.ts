export interface FedrampTopic {
  slug: string;
  code: string;
  title: string;
  summary: string;
  implementation: string[];
  evidence: string[];
  metrics: string[];
}

export const fedrampTopics: FedrampTopic[] = [
  {
    slug: 'system-boundary-and-inheritance',
    code: 'FG-01',
    title: 'System Boundary and Control Inheritance',
    summary: 'Define in-scope systems, trust boundaries, and inherited/shared responsibilities.',
    implementation: [
      'Maintain boundary diagrams and in-scope component inventory.',
      'Map inherited, shared, and customer-responsible controls.',
      'Require boundary impact analysis before major architecture changes.'
    ],
    evidence: ['Boundary diagrams', 'Shared responsibility matrix', 'Boundary change records'],
    metrics: ['Boundary docs updated on schedule', 'Open responsibility mapping gaps']
  },
  {
    slug: 'security-plan-and-control-implementation',
    code: 'FG-02',
    title: 'Security Plan and Control Implementation',
    summary: 'Build complete and testable control implementation narratives.',
    implementation: [
      'Document control statements with implementation references.',
      'Assign owners and operating frequency by control.',
      'Review control narratives on a defined lifecycle.'
    ],
    evidence: ['System security plan artifacts', 'Control implementation matrix', 'Owner attestations'],
    metrics: ['Controls with complete owner/evidence linkage', 'Control narrative currency rate']
  },
  {
    slug: 'assessment-testing-and-poam-management',
    code: 'FG-03',
    title: 'Assessment Testing and POA&M Management',
    summary: 'Coordinate assessment readiness, findings management, and validated remediation.',
    implementation: [
      'Prepare control evidence in an assessor-friendly structure.',
      'Track findings with severity, milestones, and owner accountability.',
      'Re-test remediations and record closure evidence.'
    ],
    evidence: ['Assessment evidence index', 'POA&M register', 'Retest/closure records'],
    metrics: ['POA&M aging by severity', 'Retest pass rate']
  },
  {
    slug: 'continuous-monitoring-operations',
    code: 'FG-04',
    title: 'Continuous Monitoring Operations',
    summary: 'Run recurring security monitoring with consistent reporting discipline.',
    implementation: [
      'Define monthly and periodic monitoring schedule.',
      'Run vulnerability scans and triage workflows with SLA targets.',
      'Track and escalate overdue high-risk items.'
    ],
    evidence: ['Continuous monitoring schedule', 'Scan and triage reports', 'Escalation logs'],
    metrics: ['Monitoring task completion rate', 'Critical remediation SLA attainment']
  },
  {
    slug: 'incident-response-and-configuration-governance',
    code: 'FG-05',
    title: 'Incident Response and Configuration Governance',
    summary: 'Coordinate incident response with change and configuration control rigor.',
    implementation: [
      'Integrate incident workflows with emergency change controls.',
      'Maintain secure baseline governance and drift response process.',
      'Run post-incident and post-change retrospectives.'
    ],
    evidence: ['Incident playbooks and records', 'Configuration management plan', 'Post-event retrospectives'],
    metrics: ['Containment time', 'Change-induced incident rate']
  },
  {
    slug: 'evidence-packaging-and-reporting-discipline',
    code: 'FG-06',
    title: 'Evidence Packaging and Reporting Discipline',
    summary: 'Keep documentation complete, coherent, and continuously audit-ready.',
    implementation: [
      'Standardize evidence taxonomy and naming conventions.',
      'Automate repeatable evidence collection where possible.',
      'Run quality checks before reporting cycles.'
    ],
    evidence: ['Evidence inventory index', 'Reporting templates', 'Quality-control checklist'],
    metrics: ['Evidence completeness score', 'Documentation rework rate']
  }
];
