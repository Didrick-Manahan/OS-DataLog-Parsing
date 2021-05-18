# Import local files
import Common_Params

# Import packages
import re
from collections import OrderedDict

# Perform mappings on log given a mapping dictionary
def replace_with_tokens(log, mapping):
    # Iterate over log rows
    for i in range(0, len(log)):
        line = log[i]

        # Iterate over mappings
        for regex_str in mapping.keys():
            line = re.sub(regex_str, mapping[regex_str], line)
        log[i] = line

# Perform preprocessing on the given log. The log should be list of strings.
def preprocess(log):
    # Get regexes from file
    common_params = Common_Params.common_params
    
    # Perform substitution
    replace_with_tokens(log, common_params)

    return log