# GNU Radio Multimode Receiver

Modernized multimode SDR receiver with helper functions restored for GNU Radio validation.

This repository is split from the audited `modern-gnuradio-sdr-flows` workspace. It keeps a focused GNU Radio Companion flow family with archived originals in `flows/` and validated modern ports in `modern/`.

## Features

- NFM, WFM, AM, USB, LSB, and digital-mode selector helper table
- Frequency scanning helper compatibility layer
- osmocom SDR source input
- Audio, WAV, and file output paths
- Original `profile.fuzz` preserved as archive data

## Standards and Signal Context

- General-purpose multimode SDR receiver experiment
- Mode table implemented in `multimode_helper.py`
- GNU Radio Companion XML validated with GNU Radio 3.8.5.0

## Flowgraph Inventory

| Flowgraph | Blocks | Connections | Key Parameters | Hardware/Audio Blocks | Transmit Blocks |
| --- | ---: | ---: | --- | --- | --- |
| `multimode.grc` | 100 | 31 | freq=150.0e6; srate=1.0e6; arate=48.0e3; bw=mbw; samp_rate=int(mh.get_good_rate(devinfo,srate)); mode=dmode | audio_sink_0 (audio_sink); osmosdr_source_0 (osmosdr_source) | - |

## File and Capture Paths

- `multimode.grc`: blocks_wavfile_sink_0.file=recfn; blocks_file_sink_0.file=aout; blocks_file_sink_1.file=digifn

Update these paths before running graphs on a different machine. Generated files, captures, recordings, and raw samples are intentionally ignored by git.

## Usage Examples

```sh
# Validate modernized flowgraphs
/opt/local/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9 tools/validate_grc.py modern/* --report VALIDATION.md

# Generate Python without running RF hardware
mkdir -p generated
for f in modern/*; do /opt/local/bin/grcc -o generated "$f"; done

# Verify committed file integrity
shasum -a 256 -c SHA256SUMS.txt
```

To open a graph interactively:

```sh
gnuradio-companion modern/<flowgraph>.grc
```

To run generated Python, inspect the generated script first and confirm hardware, frequency, gain, sample rate, and file paths. Do not run transmit-capable graphs directly from generated code without RF isolation and legal authorization.

## Safety

Receive-oriented flow. Confirm local frequency authorization and update output filenames before recording.

## Audit Status

- Archived originals parse as XML. See `AUDIT.md`.
- Modernized flowgraphs validate OK. See `VALIDATION.md`.
- Python generation was verified with GNU Radio Companion Compiler 3.8.5.0. See `COMPILE.md`.
- Checksums are tracked in `SHA256SUMS.txt`.

## Repository Layout

- `flows/` - archived original flowgraphs and related data files.
- `modern/` - modernized GNU Radio Companion flowgraphs for normal use.
- `tools/` - repeatable audit and validation helpers.
- `README.md` - usage and technical overview.
- `DESCRIPTION.md` - short project description.
- `AUDIT.md`, `VALIDATION.md`, `COMPILE.md` - generated audit/verification reports.

## License

No new license is asserted for the archived flowgraphs. Preserve original ownership/history before redistribution or publication.
