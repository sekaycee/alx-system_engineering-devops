# Postmortem

## Format

### Issue Summary

* Duration of outage
    + Start time: Wednesday, May 10th 2023. 10:30pm (GMT+1)
    + End time: Wednesday, May 10th 2023. 11:00pm (GMT+1)
* Impact
* Root cause

### Timeline

* Issue detection time:
* Issue detection method: Monitoring alert
* Actions taken:
* Misleading investigation(debugging) paths taken:
* Team(individuals) the incident escalated to:
* Incident resolution method:



## Actual postmortem

### Issue Summary

This is a postmortem created for an issue that occured between 10:30 pm and 11pm on Wednesday, the 10th of May 2023 (GMT+1). It effectively led to the shutdown of our services witgin that time interval. About an estimated 30% of our userbase was affected by it. The root cause of the issue was found to be in a misconfiguration of our Nginx server after an upgrade.

The issue was detected by our monitoring service Datadog, some ten seconds after it occurred. An alert was consequently sent to Mercy Jay our on-call software engineer, who after trying to resolve it to no effect, escalated it to Kay Cee and Prince Josh.


