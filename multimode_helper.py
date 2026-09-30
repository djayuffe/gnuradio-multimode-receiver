"""Compatibility helper for the modernized legacy multimode GNU Radio flowgraph."""

_LAST_RETURNED = None

_MODES = {
    "NFM1": ("NFM 12.5 kHz", "FM", 5.0e3),
    "NFM2": ("NFM 25 kHz", "FM", 7.5e3),
    "WFM": ("Wide FM", "FM", 75.0e3),
    "AM": ("AM", "AM", 5.0e3),
    "USB": ("USB", "SSB", 2.7e3),
    "LSB": ("LSB", "SSB", 2.7e3),
    "DIG": ("Digital", "DIG", 2.4e3),
}


def get_modes_values():
    return list(_MODES)


def get_modes_names():
    return [label for label, _mode_type, _deviation in _MODES.values()]


def get_mode_type(mode):
    return _MODES.get(mode, _MODES["NFM1"])[1]


def get_mode_deviation(mode, bandwidth):
    if mode in {"AM", "USB", "LSB"} and bandwidth:
        return float(bandwidth)
    return float(_MODES.get(mode, _MODES["NFM1"])[2])


def get_good_rate(_devinfo, requested_rate):
    return float(requested_rate)


def get_last_returned(default):
    return default if _LAST_RETURNED is None else _LAST_RETURNED


def scan_freq_out(enabled, low, high, current, ifreq, power, threshold, increment, _rate, _list_mode, scan_list):
    global _LAST_RETURNED
    if not enabled or power >= threshold:
        _LAST_RETURNED = current
        return current

    frequencies = _parse_scan_list(scan_list)
    if frequencies:
        try:
            index = frequencies.index(current)
            _LAST_RETURNED = frequencies[(index + 1) % len(frequencies)]
        except ValueError:
            _LAST_RETURNED = frequencies[0]
        return _LAST_RETURNED

    next_freq = current + increment
    if next_freq > high:
        next_freq = low
    if next_freq < low:
        next_freq = high
    _LAST_RETURNED = next_freq + ifreq
    return _LAST_RETURNED


def _parse_scan_list(scan_list):
    if not scan_list:
        return []
    if isinstance(scan_list, (list, tuple)):
        return [float(item) for item in scan_list]
    return [float(item.strip()) for item in str(scan_list).replace(";", ",").split(",") if item.strip()]
