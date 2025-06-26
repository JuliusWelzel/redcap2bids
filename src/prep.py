def filter_rc(rc_data, relevant_columns):
    """    Filters the RedCap data to include only relevant columns.
    Also run some basic checks on the data.
    Calcualte or derive columns where necessary.
    """
    # Filter the DataFrame to include only relevant columns
    filtered_data = rc_data.copy()

    # Rename columns for consistencywithin the lab
    filtered_data.rename(columns={
        'neuropsych_id': 'participant_id',
        'age_years': 'age',
        'happiess_vas': 'happiness_vas'
    }, inplace=True)

    # Check for missing values in critical columns
    if filtered_data['participant_id'].isnull().any():
        raise ValueError("Missing participant IDs in the data.")
    
    # Ensure participant_id is unique
    if not filtered_data['participant_id'].is_unique:
        raise ValueError("Participant IDs are not unique.")
    
    missing_age_ids = filtered_data.loc[filtered_data['age'].isnull(), 'participant_id'].tolist()
    if missing_age_ids:
        raise ValueError(f"Missing ages for participant IDs: {missing_age_ids}")


    # calculate additional values

    # FACIT-Fatigue Scale (FACIT-F) score
    filtered_data = calc_facit_total_score(filtered_data)

    # Filter to keep only the relevant columns
    filtered_data = filtered_data[relevant_columns]


    return filtered_data.reset_index(drop=True)

def calc_facit_total_score(df):
    """Calculate the total score for the FACIT-Fatigue Scale."""
    # Assuming the columns for the FACIT-Fatigue Scale are named 'facit_f_1', 'facit_f_2', ..., 'facit_f_n'
    facit_columns = [col for col in df.columns if col.startswith('facit_f_')]
    
    if not facit_columns:
        raise ValueError("No FACIT-Fatigue Scale columns found in the DataFrame.")
    
    # Calculate the total score by summing the relevant columns
    df['facit_f_total'] = df[facit_columns].sum(axis=1)
    
    return df