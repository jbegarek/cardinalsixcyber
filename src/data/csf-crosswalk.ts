export type NistFamilyRef = {
  code: string;
  title: string;
};

export type CsfCrosswalkEntry = {
  nistFamilies: NistFamilyRef[];
  cisCodes: string[];
};

export const csfCrosswalk: Record<string, CsfCrosswalkEntry> = {
  'gv-oc': { nistFamilies: [{ code: '3.15', title: 'Planning' }, { code: '3.1', title: 'Access Control' }, { code: '3.11', title: 'Risk Assessment' }], cisCodes: ['CIS 1', 'CIS 2', 'CIS 15'] },
  'gv-rm': { nistFamilies: [{ code: '3.11', title: 'Risk Assessment' }, { code: '3.12', title: 'Security Assessment and Monitoring' }, { code: '3.15', title: 'Planning' }], cisCodes: ['CIS 7', 'CIS 15', 'CIS 18'] },
  'gv-rr': { nistFamilies: [{ code: '3.1', title: 'Access Control' }, { code: '3.6', title: 'Incident Response' }, { code: '3.12', title: 'Security Assessment and Monitoring' }], cisCodes: ['CIS 5', 'CIS 6', 'CIS 17'] },
  'gv-po': { nistFamilies: [{ code: '3.15', title: 'Planning' }, { code: '3.4', title: 'Configuration Management' }, { code: '3.13', title: 'System and Communications Protection' }], cisCodes: ['CIS 4', 'CIS 6', 'CIS 15'] },
  'gv-ov': { nistFamilies: [{ code: '3.12', title: 'Security Assessment and Monitoring' }, { code: '3.3', title: 'Audit and Accountability' }, { code: '3.14', title: 'System and Information Integrity' }], cisCodes: ['CIS 8', 'CIS 7', 'CIS 17'] },
  'gv-sc': { nistFamilies: [{ code: '3.1', title: 'Access Control' }, { code: '3.11', title: 'Risk Assessment' }, { code: '3.13', title: 'System and Communications Protection' }], cisCodes: ['CIS 15', 'CIS 12', 'CIS 13'] },
  'id-am': { nistFamilies: [{ code: '3.4', title: 'Configuration Management' }, { code: '3.1', title: 'Access Control' }, { code: '3.11', title: 'Risk Assessment' }], cisCodes: ['CIS 1', 'CIS 2', 'CIS 4'] },
  'id-ra': { nistFamilies: [{ code: '3.11', title: 'Risk Assessment' }, { code: '3.12', title: 'Security Assessment and Monitoring' }, { code: '3.14', title: 'System and Information Integrity' }], cisCodes: ['CIS 7', 'CIS 18', 'CIS 13'] },
  'id-im': { nistFamilies: [{ code: '3.12', title: 'Security Assessment and Monitoring' }, { code: '3.14', title: 'System and Information Integrity' }, { code: '3.6', title: 'Incident Response' }], cisCodes: ['CIS 7', 'CIS 17', 'CIS 18'] },
  'pr-aa': { nistFamilies: [{ code: '3.1', title: 'Access Control' }, { code: '3.5', title: 'Identification and Authentication' }, { code: '3.3', title: 'Audit and Accountability' }], cisCodes: ['CIS 5', 'CIS 6', 'CIS 8'] },
  'pr-at': { nistFamilies: [{ code: '3.2', title: 'Awareness and Training' }, { code: '3.6', title: 'Incident Response' }, { code: '3.12', title: 'Security Assessment and Monitoring' }], cisCodes: ['CIS 14', 'CIS 17', 'CIS 9'] },
  'pr-ds': { nistFamilies: [{ code: '3.8', title: 'Media Protection' }, { code: '3.13', title: 'System and Communications Protection' }, { code: '3.14', title: 'System and Information Integrity' }], cisCodes: ['CIS 3', 'CIS 11', 'CIS 8'] },
  'pr-ps': { nistFamilies: [{ code: '3.4', title: 'Configuration Management' }, { code: '3.14', title: 'System and Information Integrity' }, { code: '3.7', title: 'Maintenance' }], cisCodes: ['CIS 4', 'CIS 7', 'CIS 12'] },
  'pr-ir': { nistFamilies: [{ code: '3.11', title: 'Risk Assessment' }, { code: '3.6', title: 'Incident Response' }, { code: '3.13', title: 'System and Communications Protection' }], cisCodes: ['CIS 11', 'CIS 12', 'CIS 17'] },
  'de-cm': { nistFamilies: [{ code: '3.3', title: 'Audit and Accountability' }, { code: '3.14', title: 'System and Information Integrity' }, { code: '3.12', title: 'Security Assessment and Monitoring' }], cisCodes: ['CIS 8', 'CIS 13', 'CIS 7'] },
  'de-ae': { nistFamilies: [{ code: '3.3', title: 'Audit and Accountability' }, { code: '3.6', title: 'Incident Response' }, { code: '3.14', title: 'System and Information Integrity' }], cisCodes: ['CIS 8', 'CIS 13', 'CIS 17'] },
  'rs-ma': { nistFamilies: [{ code: '3.6', title: 'Incident Response' }, { code: '3.3', title: 'Audit and Accountability' }, { code: '3.15', title: 'Planning' }], cisCodes: ['CIS 17', 'CIS 8', 'CIS 11'] },
  'rs-an': { nistFamilies: [{ code: '3.6', title: 'Incident Response' }, { code: '3.3', title: 'Audit and Accountability' }, { code: '3.14', title: 'System and Information Integrity' }], cisCodes: ['CIS 17', 'CIS 8', 'CIS 13'] },
  'rs-co': { nistFamilies: [{ code: '3.6', title: 'Incident Response' }, { code: '3.12', title: 'Security Assessment and Monitoring' }, { code: '3.15', title: 'Planning' }], cisCodes: ['CIS 17', 'CIS 14', 'CIS 8'] },
  'rs-mi': { nistFamilies: [{ code: '3.6', title: 'Incident Response' }, { code: '3.14', title: 'System and Information Integrity' }, { code: '3.4', title: 'Configuration Management' }], cisCodes: ['CIS 17', 'CIS 7', 'CIS 13'] },
  'rs-im': { nistFamilies: [{ code: '3.6', title: 'Incident Response' }, { code: '3.12', title: 'Security Assessment and Monitoring' }, { code: '3.11', title: 'Risk Assessment' }], cisCodes: ['CIS 17', 'CIS 18', 'CIS 7'] },
  'rc-rp': { nistFamilies: [{ code: '3.6', title: 'Incident Response' }, { code: '3.11', title: 'Risk Assessment' }, { code: '3.8', title: 'Media Protection' }], cisCodes: ['CIS 11', 'CIS 17', 'CIS 12'] },
  'rc-co': { nistFamilies: [{ code: '3.6', title: 'Incident Response' }, { code: '3.15', title: 'Planning' }, { code: '3.12', title: 'Security Assessment and Monitoring' }], cisCodes: ['CIS 17', 'CIS 14', 'CIS 15'] },
  'rc-im': { nistFamilies: [{ code: '3.11', title: 'Risk Assessment' }, { code: '3.12', title: 'Security Assessment and Monitoring' }, { code: '3.6', title: 'Incident Response' }], cisCodes: ['CIS 11', 'CIS 17', 'CIS 18'] }
};
