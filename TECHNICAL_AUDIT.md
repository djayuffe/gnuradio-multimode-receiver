# Technical Audit

This audit covers the modern-only public repository `gnuradio-multimode-receiver`.

## Scope

- Modern flowgraphs audited: 1.
- Outdated public XML removed from the repo.
- Repo-local file paths used for samples/captures.
- GNU Radio Companion validation target: 3.8.5.0.

## Tooling Review

- `tools/audit_flows.py` parses GRC XML, hashes each file, reports block/connection counts, hardware endpoints, transmit-capable sinks, file paths, duplicate IDs, and exact duplicate payloads.
- `tools/validate_grc.py` uses GNU Radio Companion's Python API to load, rewrite, and validate each modern `.grc`; it does not rely on ad hoc text matching.
- Setup scripts, where present, create safe placeholder local files only. They do not run SDR hardware.

## Feature and Parameter Coverage

| Flowgraph | Blocks | Connections | Key Parameters | Hardware/Audio Blocks | Transmit Blocks |
| --- | ---: | ---: | --- | --- | --- |
| `multimode.grc` | 100 | 31 | freq=150.0e6; srate=1.0e6; arate=48.0e3; bw=mbw; samp_rate=int(mh.get_good_rate(devinfo,srate)); mode=dmode | audio_sink_0 (audio_sink); osmosdr_source_0 (osmosdr_source) | - |

## File Path Coverage

- `multimode.grc`: blocks_wavfile_sink_0.file=recfn; blocks_file_sink_0.file=aout; blocks_file_sink_1.file=digifn

## Remaining Runtime Responsibilities

- GRC validation and `grcc` generation do not prove connected SDR/audio hardware behavior.
- Users must configure local devices, antennas, sample files, and gains.
- Transmit-capable graphs require RF isolation and authorization before any runtime use.

## Verification Checklist

- `VALIDATION.md` contains no `Result: FAILED` entries.
- `SHA256SUMS.txt` verifies all committed files.
- Generated Python and runtime captures remain ignored by git.
