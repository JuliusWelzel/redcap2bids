import json
from pathlib import Path
from redcap import Project

from src.prep import filter_rc


# Define the root directory for BIDS data
dir_root_bids = Path(r'W:\data\bids_data\juw_rc2bids')

####
# Retreive RedCap data
####

api_url = 'https://redcapdev.uol.de/api/'
api_key = 'F6CDD83AB8AD6A3CC105D51CBB9907D4'
rc_project = Project(api_url, api_key)

# get data and all fields as pd.DataFrame
rc_data = rc_project.export_records(format_type="df")

# filter the data to include only relevant columns
relevant_columns = [
    'participant_id', 'age', 'happiness_vas', 'data_orga', 'facit_f_total'
]
participants_data = filter_rc(rc_data, relevant_columns)

# save as participants.tsv
participants_data.to_csv(
    dir_root_bids.joinpath('participants.tsv'),
    sep='\t', index=False, na_rep='n/a'
)

####
# Provide descriptions of the columns in the participants.tsv file
####
 
rc_metadata = rc_project.export_metadata(format_type="df")

# Sample .json description for the participants.tsv columns
json_description = {
    "participant_id": {
        "Description": "Unique participant identifier"
    },
    "age": {
        "Description": "Age of the participant",
        "Units": "years"
    },
    "happiness_vas": {
        "Description": "Group to which the participant belongs",
    },
    "data_orga": {
        "Description": "How much do you like data organization?",
        "Levels": {
            "1" : "Yes",
            "2" : "Much",
            "3" : "I <3 BIDS",
        }
    },
    "facit_f_total": {
        "Description": "Total score for the FACIT-Fatigue Scale",
        "Units": "points"
    }
}

# check if all columns in participants_data are described
for col in participants_data.columns:
    if col not in json_description:
        raise ValueError(f"Column '{col}' in participants.tsv is not described in the JSON description.")
    
# Save the .json description to a file
with open(dir_root_bids.joinpath('participants.json'), 'w') as f:
    json.dump(json_description, f, indent=4)
    print(f'Created participants.tsv and participants.json in {dir_root_bids}')