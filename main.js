// Trigger the Outcome-First Wizard
import { OutcomeFirstWizard } from './modules/outcome-first-wizard.js';
const wizard = new OutcomeFirstWizard();
wizard.execute();
import { ResilienceMonitor, slackAlerter, AIWrapper, UnifiedSyncBridge } from './modules/index.js';

// 1. Initialize Monitor
const monitor = new ResilienceMonitor({ 
  alerters: [slackAlerter(process.env.SLACK_WEBHOOK_URL)],
  alertOnRecovery: true 
});

// 2. Configure Endpoints
monitor.register('anthropic-api', {
  url: 'https://api.anthropic.com/health',
  intervalMs: 10000,
  thresholds: { p95LatencyMs: 1500, errorRatePct: 5 }
});

monitor.register('linear-api', {
  url: 'https://linear.app/api/health',
  intervalMs: 15000,
  thresholds: { p95LatencyMs: 2000, errorRatePct: 5 }
});

// 3. Start Lifecycle
monitor.start();

// 4. Verification Logging
console.log('--- StreamlineAI System Active ---');
console.log('Status Snapshot:', JSON.stringify(monitor.getStatus(), null, 2));

process.on('SIGINT', () => {
  monitor.stop();
  process.exit();
});
