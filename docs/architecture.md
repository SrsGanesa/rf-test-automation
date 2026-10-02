# System Architecture

This document describes the architecture of the RF Test Automation Project.

## Planned Components

1. LabVIEW test orchestrator
2. LabVIEW state machine
3. Python bridge
4. libiio / pyadi-iio interface
5. ADALM-Pluto SDR
6. Python RF / OFDM processing
7. TestStand sequence
8. Data logging
9. Reporting
10. ML analysis

## High-Level Flow

Configuration
→ Measurement
→ Capture
→ Processing
→ Decision
→ Logging
→ Reporting