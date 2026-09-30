# Technical Audit

This audit summarizes code, functions, and feature coverage for `gnuradio-multimode-receiver`.

## Scope

- Flowgraphs audited: 1 modern files plus archived originals in `flows/`.
- Tools audited: `tools/audit_flows.py` and `tools/validate_grc.py`.
- Reports regenerated locally before publication.

## Code and Function Review

- `tools/audit_flows.py` parses XML with `xml.etree.ElementTree`, hashes each file, lists block counts, connection counts, hardware endpoints, transmit-capable sinks, explicit file paths, duplicate block IDs, and exact duplicate payloads.
- `tools/validate_grc.py` uses the installed GNU Radio Companion core API, not text matching, to load, rewrite, and validate each modern `.grc` file.
- Shell examples avoid executing generated RF graphs automatically; generation and validation are separate from runtime operation.

## Feature Coverage

- NFM, WFM, AM, USB, LSB, and digital-mode selector helper table
- Frequency scanning helper compatibility layer
- osmocom SDR source input
- Audio, WAV, and file output paths
- Original `profile.fuzz` preserved as archive data

## Technical Parameters

| Flowgraph | Blocks | Connections | Key Parameters | Hardware/Audio Blocks | Transmit Blocks |
| --- | ---: | ---: | --- | --- | --- |
| `multimode.grc` | 100 | 31 | freq=150.0e6; srate=1.0e6; arate=48.0e3; bw=mbw; samp_rate=int(mh.get_good_rate(devinfo,srate)); mode=dmode | audio_sink_0 (audio_sink); osmosdr_source_0 (osmosdr_source) | - |

## Known Operational Gaps

- Runtime hardware behavior is not asserted by validation; actual SDR/audio devices must be configured locally.
- External sample/capture files named in legacy graphs are not bundled unless present in `flows/`.
- Transmit-capable graphs require separate RF lab controls and legal authorization.

## Verification

- `VALIDATION.md` has no `Result: FAILED` entries.
- `SHA256SUMS.txt` verifies all committed files.
