import pandas as pd

def count_characters_in_dataframe(df):
    # Initialize an empty list to store the results
    results = []
    
    # Initialize the start position with "000"
    start = "000"
    
    # Iterate through the columns of the DataFrame
    for column in df.columns:
        # Get the field name (column name)
        field_name = column

        # Calculate the character count for each cell in the column
        character_counts = df[column].astype(str).apply(len)

        # Calculate the end position based on the start position and character counts
        end = str(int(start) + character_counts.sum() - 1).zfill(3)

        # Append the results to the list
        results.append([field_name, start, end])

        # Update the start position for the next field
        start = str(int(end) + 1).zfill(3)

    # Create a new DataFrame from the results list with the specified headers
    result_df = pd.DataFrame(results, columns=["Field Name", "Start", "End"])

    return result_df

# Example usage:
data = {'Field1': ['Hello', 'World', 'Python'],
        'Field2': [123, 456, 789],
        'Field3': ['Data', 'Science', 'Rules']}
df = pd.DataFrame(data)

character_count_df = count_characters_in_dataframe(df)
print(character_count_df)
