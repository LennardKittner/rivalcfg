from .. import usbhid


profile = {
    "name": "SteelSeries Prime",
    "models": [
        {
            "name": "SteelSeries Prime",
            "vendor_id": 0x1038,
            "product_id": 0x182E,
            "endpoint": 0,
        },
        {
            "name": "SteelSeries Prime Rainbow 6 Siege Black Ice Edition",
            "vendor_id": 0x1038,
            "product_id": 0x182A,
            "endpoint": 0,
        },
        {
            "name": "SteelSeries Prime CS:GO Neo Noir Edition",
            "vendor_id": 0x1038,
            "product_id": 0x1856,
            "endpoint": 0,
        },
    ],
    "settings": {
        "sensitivity": {
            "label": "Sensitivity presets",
            "description": "Set sensitivity preset (DPI)",
            "cli": ["-s", "--sensitivity"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x61],
            "value_type": "multidpi_range",
            "input_range": [50, 18000, 50],
            "output_range": [1, 0x0168, 1],
            "dpi_length_byte": 2,
            "count_mode": "number",
            "first_preset": 0,
            "max_preset_count": 5,
            "default": "400, 800, 1200, 2400, 3200",
        },
        "polling_rate": {
            "label": "Polling rate",
            "description": "Set polling rate (Hz)",
            "cli": ["-p", "--polling-rate"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x5D],
            "value_type": "choice",
            "choices": {
                125: 0x04,
                250: 0x03,
                500: 0x02,
                1000: 0x01,
            },
            "default": 1000,
        },
        "color": {
            "label": "Wheel LED color",
            "description": "Set the color of the wheel LED",
            "cli": ["-c", "--color"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x62, 0x01],
            "command_suffix": [
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0xFF,
            ],
            "value_type": "rgbcolor",
            "default": "#FF5200",
        },
        "led_brightness": {
            "label": "Wheel LED brightness",
            "description": "Set the brightness of the wheel LED",
            "cli": ["-l", "--led-brightness"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x5F],
            "value_type": "range",
            "input_range": [0, 256, 1],
            "output_range": [0, 256, 1],
            "range_length_byte": 2,
            "default": 256,
        },
        "default_lighting": {
            "label": "Default lighting",
            "description": "Set default lighting at mouse startup",
            "cli": ["-d", "--default-lighting"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x27],
            "value_type": "choice",
            "choices": {
                "off": 0x00,
                "rainbow": 0x01,
            },
            "default": "rainbow",
        },
    },
    "save_command": {
        "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
        "command": [0x59],
    },
}
