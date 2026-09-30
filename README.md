# GNU Radio Multimode Receiver

Modernized multimode SDR receiver with helper functions restored for GNU Radio validation.

Multimode receiver with AM/FM/SSB/DIG mode helper logic and scanning compatibility functions. The repository is modern-only: runnable GNU Radio Companion files live in `modern/`, use repo-local paths, and validate with GNU Radio Companion 3.8.5.0.

## Features

- Modern GNU Radio Companion XML only; outdated source XML was removed from the public repo.
- Qt GUI blocks replace old WX GUI patterns where applicable.
- Machine-specific paths were replaced with repo-local `samples/` and `captures/` paths.
- `tools/audit_flows.py` and `tools/validate_grc.py` provide repeatable checks.
- `SHA256SUMS.txt` tracks committed-file integrity.

## Flowgraphs

- `modern/multimode.grc`

## Technical Inventory

| Flowgraph | Blocks | Connections | Key Parameters | Hardware/Audio Blocks | Transmit Blocks |
| --- | ---: | ---: | --- | --- | --- |
| `multimode.grc` | 100 | 31 | freq=150.0e6; srate=1.0e6; arate=48.0e3; bw=mbw; samp_rate=int(mh.get_good_rate(devinfo,srate)); mode=dmode | audio_sink_0 (audio_sink); osmosdr_source_0 (osmosdr_source) | - |

## Standards and Frequencies

- GNU Radio Companion target validated locally: 3.8.5.0.
- Frequency, sample-rate, and mode values are shown in the inventory table above from the actual `.grc` XML.
- Transmit-capable repositories include explicit RF safety text and keep transmit examples isolated.

## Repo-Local File Paths

- `multimode.grc`: blocks_wavfile_sink_0.file=recfn; blocks_file_sink_0.file=aout; blocks_file_sink_1.file=digifn

## Setup Helpers

- No setup scripts needed.

Run setup helpers only if you need placeholder files for local graph loading or non-radiating tests.

## Usage Examples

```sh
/opt/local/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9 tools/validate_grc.py modern/* --report VALIDATION.md
mkdir -p generated
for f in modern/*; do /opt/local/bin/grcc -o generated "$f"; done
shasum -a 256 -c SHA256SUMS.txt
```

Open a flowgraph interactively:

```sh
gnuradio-companion modern/<flowgraph>.grc
```

Inspect generated Python before running it. Confirm hardware, frequency, gain, sample rate, and paths every time.

## Safety

Receive-oriented flow. Confirm local frequency authorization and update output filenames before recording.

## Audit Status

- Modern flowgraph audit: `AUDIT.md`.
- GNU Radio validation: `VALIDATION.md`.
- Generation summary: `COMPILE.md`.
- Technical review: `TECHNICAL_AUDIT.md`.

## License

No new license is asserted for the original flowgraph design lineage. Review provenance before redistribution in other projects.
