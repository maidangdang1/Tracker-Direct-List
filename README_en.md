# Tracker-Direct-List

Automatically fetch the latest BT tracker list from [ngosang/trackerslist](https://github.com/ngosang/trackerslist) and convert it to OpenClash rules format.

## Introduction

This project uses GitHub Actions to automatically update the tracker list every hour, converting it to OpenClash-compatible Direct rules format for users who need proxy/VPN access.

## Features

- 🚀 Auto-fetch latest public trackers
- ⏰ Hourly auto-update
- 📝 OpenClash rules format
- ✅ Only commit when content changes

## Generated Rules File

The generated rules file is located at [`rule/Torrent_Tracker_Direct.yaml`](rule/Torrent_Tracker_Direct.yaml), formatted as follows:

```yaml
# Generated from rule/Custom_Direct.yaml
# REPO: https://github.com/ngosang/trackerslist
# SOURCE: https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt
# TOTAL: xxx
# UPDATED: YYYY-MM-DD HH:MM:SS UTC

payload:
  - DOMAIN-SUFFIX:tracker1.example.com
  - DOMAIN-SUFFIX:tracker2.example.com
  # ...
```

## Usage in OpenClash

1. Download the `Custom_Direct.yaml` file from this repository
2. Add it in OpenClash's "Config File Management"
3. Select it in the rules settings

## How It Works

1. GitHub Actions triggers every hour
2. Fetch tracker list from `trackers_all.txt`
3. Extract domain from each tracker
4. Convert to OpenClash's `DOMAIN-SUFFIX` rules format
5. Commit to repository if content changed

## Directory Structure

```
Tracker-Direct-List/
├── .github/
│   └── workflows/
│       └── update-trackers.yml    # GitHub Actions workflow
├── scripts/
│   └── convert.py                 # Conversion script
├── rule/
│   └── Torrent_Tracker_Direct.yaml        # Generated rules file
├── README.md                      # Chinese README
└── README_en.md                   # English README
```

## License

MIT License

## Credits

- [ngosang/trackerslist](https://github.com/ngosang/trackerslist) - Tracker list data source
- [Aethersailor/Custom_OpenClash_Rules](https://github.com/Aethersailor/Custom_OpenClash_Rules) - Format reference