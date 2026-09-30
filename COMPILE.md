# GNU Radio Compile Report

Compiler: GNU Radio Companion Compiler 3.8.5.0 from `/opt/local/bin/grcc`.

Validation status: 1/1 modernized flowgraphs validate OK.

Python generation was verified in the source monorepo before splitting. To regenerate locally, run:

```sh
mkdir -p generated
for f in modern/*; do /opt/local/bin/grcc -o generated "$f"; done
```

The local macOS environment may print PyQt5 duplicate-class warnings because both user-site PyQt5 and MacPorts Qt/PyQt are visible. Those warnings did not prevent validation or generation.
