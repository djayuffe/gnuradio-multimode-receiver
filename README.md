# GNU Radio Multimode Receiver

A legacy multimode SDR receiver modernized for GNU Radio Companion, including the missing compatibility helper needed for validation.

This private repository is split from `modern-gnuradio-sdr-flows` and keeps a focused subset of related GNU Radio Companion flowgraphs. Files in `flows/` are archived originals. Files in `modern/` are the working GNU Radio Companion ports.

## Contents

- `flows/` - original archived flowgraphs and related source files.
- `modern/` - modernized `.grc` files validated with GNU Radio Companion 3.8.5.0 on this Mac.
- `AUDIT.md` - structural audit of the archived originals.
- `VALIDATION.md` - validation result for modernized files.
- `COMPILE.md` - compiler/generation result summary.
- `tools/` - repeatable audit and validation helpers.
- `SHA256SUMS.txt` - integrity hashes for committed files.

## Modern Flowgraphs

- `modern/multimode.grc`

## Archived Originals

- `flows/multimode.grc`
- `flows/profile.fuzz`

## Notes

- Adds `multimode_helper.py`, replacing the missing helper dependency referenced by the archived flowgraph.
- Supports mode table/helper functions used by the original scanner and demodulation controls.
- `profile.fuzz` is preserved as archive data but is not a GRC flowgraph.

## Verify

```sh
python3 tools/audit_flows.py flows --report AUDIT.md
/opt/local/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9 tools/validate_grc.py modern/* --report VALIDATION.md
shasum -a 256 -c SHA256SUMS.txt
```

To generate Python from the modernized flowgraphs:

```sh
mkdir -p generated
for f in modern/*; do /opt/local/bin/grcc -o generated "$f"; done
```

`generated/` is intentionally ignored. Commit the `.grc` sources and reports, not generated Python output.

## License

No new license is asserted for the archived flowgraphs in this private repository. Preserve any original ownership/history before redistribution or publication.
