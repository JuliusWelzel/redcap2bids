import pandas as pd
from redcap import Project
import os

from rcol.instruments import fal, moca


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
