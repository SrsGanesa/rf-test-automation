
"""Standalone ADALM-Pluto receive test.

Tests connectivity, receiver configuration, and acquisition of
real complex I/Q samples. This script does not transmit RF signals.
"""

import sys

import adi
import numpy as np


# Pluto connection and receive configuration
PLUTO_URI = "ip:192.168.2.1"

RX_FREQUENCY_HZ = 900_000_000       # 900 MHz
SAMPLE_RATE_HZ = 1_000_000           # 1 MS/s
RX_BANDWIDTH_HZ = 1_000_000          # 1 MHz
RX_GAIN_DB = 10                      # Manual RX gain
NUMBER_OF_SAMPLES = 1024             # Initial hardware test size


def main() -> int:
    try:
        print(f"Connecting to Pluto at {PLUTO_URI}...")
        sdr = adi.Pluto(uri=PLUTO_URI)

        print("Configuring receiver...")
        sdr.rx_lo = RX_FREQUENCY_HZ
        sdr.sample_rate = SAMPLE_RATE_HZ
        sdr.rx_rf_bandwidth = RX_BANDWIDTH_HZ
        sdr.gain_control_mode_chan0 = "manual"
        sdr.rx_hardwaregain_chan0 = RX_GAIN_DB
        sdr.rx_buffer_size = NUMBER_OF_SAMPLES

        print("Acquiring I/Q samples...")
        samples = np.asarray(sdr.rx())

        print("\n--- Pluto acquisition results ---")
        print(f"Requested samples : {NUMBER_OF_SAMPLES}")
        print(f"Received shape    : {samples.shape}")
        print(f"Received count    : {samples.size}")
        print(f"Data type         : {samples.dtype}")
        print(f"All values finite : {np.isfinite(samples).all()}")

        if samples.size > 0:
            # Digital I/Q magnitude RMS, not calibrated voltage.
            rms = np.sqrt(np.mean(np.abs(samples.astype(np.complex128)) ** 2))
            print(f"Digital I/Q RMS   : {rms:.6g}")
            print("First five samples:")
            print(samples[:5])
        else:
            print("FAIL: Pluto returned no samples.")
            return 2

        if samples.size != NUMBER_OF_SAMPLES:
            print("FAIL: Received sample count differs from the request.")
            return 2

        if not np.isfinite(samples).all():
            print("FAIL: I/Q data contains NaN or infinity.")
            return 2

        print("\nPASS: Pluto connection and sample acquisition succeeded.")
        return 0

    except Exception as exc:
        print(f"\nFAIL: {type(exc).__name__}: {exc}", file=sys.stderr)
        print(
            "Check the Pluto connection, URI, firmware, and libiio setup.",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
