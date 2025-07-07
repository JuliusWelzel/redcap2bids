# Redcap2BIDS

A Python tool for converting RedCap data to BIDS (Brain Imaging Data Structure) format.

## Overview

This project provides scripts to extract participant data from RedCap and format it according to BIDS specifications, creating the necessary `participants.tsv` and `participants.json` files.

## Scripts

### redcap2participants.py

This script connects to a RedCap project, extracts participant data, and creates BIDS-compliant participant files.

#### How it works:

1. **RedCap Connection**: 
   - Connects to a RedCap instance using the API URL and API key
   - Exports all records as a pandas DataFrame

2. **Data Filtering**:
   - Filters the RedCap data to include only relevant columns:
     - `participant_id`: Unique participant identifier
     - `age`: Participant age in years
     - `happiness_vas`: Random made-up variable for happiness
     - `data_orga`: Data organization preference rating
     - `facit_f_total`: Total score for the FACIT-Fatigue Scale

3. **BIDS Output Generation**:
   - Creates `participants.tsv`: A tab-separated file containing the filtered participant data
   - Creates `participants.json`: A JSON file with column descriptions, units, and value mappings

4. **Data Validation**:
   - Ensures all columns in the TSV file have corresponding descriptions in the JSON file
   - Raises an error if any column lacks documentation

#### Configuration:

Before running the script, you need to:

1. Set your RedCap API credentials:
   ```python
   api_url = 'https://redcapdev.uol.de/api/'
   api_key = 'YOUR_ACTUAL_API_KEY'  # Replace with your API key
   ```

2. Set the BIDS root directory:
   ```python
   dir_root_bids = Path(r'W:\data\bids_data\juw_rc2bids')
   ```

#### Output:

The script generates two files in the specified BIDS directory:
- `participants.tsv`: Contains the participant data in BIDS format
- `participants.json`: Contains metadata descriptions for each column

#### Usage:

```bash
python scripts/redcap2participants.py
```

The script will output a confirmation message when the files are successfully created.