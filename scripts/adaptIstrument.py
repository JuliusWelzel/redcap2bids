import os
import pandas as pd
from rcol.instruments import fal, ehi, moca
from redcap import Project

# Get REDCap API credentials
api_key = os.getenv("REDCAP_API_KEY")
api_url = "https://redcapdev.uol.de/api/"  # Replace with your actual REDCap API URL

# Use individual instruments
print(f"FAL has {len(fal)} fields")
print(f"EHI has {len(ehi)} fields")
print(f"BDI-II has {len(moca)} fields")

# Stack multiple instruments for REDCap upload
all_instruments = pd.concat([fal, ehi, moca], ignore_index=True)

# Create a custom instrument
custom_instrument = pd.DataFrame({
	'field_name': ['custom_field_1', 'custom_field_2'], 
	'field_label': ['Custom Field 1', 'Custom Field 2'], 
	'field_type': ['text', 'radio'], 
	'choices': ['', 'A, Choice A | B, Choice B']
})

# Add instrument name
custom_instrument['form_name'] = 'custom_form'

# Add a new question to FAL instrument
fal_new_question = pd.DataFrame({
	'field_name': ['fal_like_redcap'], 
	'field_label': ['Do you like RedCap?'], 
	'field_type': ['radio'], 
	'form_name': ['fal'], 
	'choices': ['1, Yes | 0, No']
})

# add questions to FAL
fal = pd.concat([fal, fal_new_question], ignore_index=True)

####
# Update RedCap project structure
####
RC_API_KEY = os.getenv("RC_API_KEY")
api_url = 'https://redcapdev.uol.de/api/'
rc_project = Project(api_url, RC_API_KEY)

# stack all intruments pandas dfs
# Example: stacking rc_data on top of itself
all_instruments = pd.concat([fal, 
                             moca], 
                             ignore_index=True)

# upload instruments to RedCap using the import_metadata method
rc_project.import_metadata(all_instruments, import_format='df')
