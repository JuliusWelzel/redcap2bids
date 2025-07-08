from pathlib import Path
from redcap import Project

from src.instruments.ehi import ehi
from src.instruments.fal import fal
import pandas as pd


####
# Update RedCap project structure
####

api_url = 'https://redcapdev.uol.de/api/'
api_key = '4A9DC1177762A57F4E3514B89F1D6F32'  # Replace with your actual API key
rc_project = Project(api_url, api_key)

# stack all intruments pandas dfs
# Example: stacking rc_data on top of itself
all_instruments = pd.concat([fal, 
                             ehi], 
                             ignore_index=True)

# upload instruments to RedCap using the import_metadata method
rc_project.import_metadata(all_instruments, import_format='df')
