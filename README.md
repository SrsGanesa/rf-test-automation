# RF Test Automation Project

An end-to-end RF test automation project built around the
Analog Devices ADALM-Pluto SDR.

The project is designed to reproduce an industrial-style RF
test workflow combining instrument control, automated measurement,
signal processing, reporting, and lightweight machine learning.

## Project Goals

- Automate RF measurement workflows using LabVIEW
- Use a state-machine architecture for test execution
- Integrate Python with LabVIEW for SDR and signal-processing tasks
- Interface with the ADALM-Pluto through libiio / pyadi-iio
- Generate and analyze OFDM waveforms
- Calculate RF and communication metrics such as EVM and BER
- Build automated measurement sweeps and reporting
- Apply a lightweight ML model to captured RF data
- Compare ML performance against a classical baseline
- Maintain the complete project using Git and structured version control

## Planned Architecture

ADALM-Pluto SDR
        |
        v
RF Measurement / Capture
        |
        v
LabVIEW Test Orchestrator
(State Machine)
        |
        v
Python Bridge
        |
        v
Python Signal Processing
        |
        +--> OFDM Analysis
        |
        +--> EVM / BER
        |
        +--> Channel Estimation
        |
        +--> ML Analysis
        |
        v
Results / Logging / Reporting

## Technology Stack

### Hardware

- Analog Devices ADALM-Pluto SDR

### LabVIEW / NI

- LabVIEW
- NI TestStand
- VISA where applicable
- LabVIEW State Machine architecture
- LabVIEW Python Node

### Python

- Python
- NumPy
- SciPy
- pyadi-iio
- libiio
- scikit-learn
- Matplotlib

### Development

- Git
- GitHub
- Visual Studio Code

## Repository Structure

```text
labview/    LabVIEW project, VIs and test-control logic
bridge/     LabVIEW-Python integration layer
python/     Signal processing, OFDM and ML
tests/      Automated tests
docs/       Architecture and technical documentation
data/       Local RF measurement data (not committed)