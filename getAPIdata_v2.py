import os
import requests
import pandas as pd
import json

def fetch_data(api_url, params):
    # SEND a GET request to the API with the given parameters
    response = requests.get(api_url, params=params)
    
    # Check if the request was successful or not
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def save_data(data, format_type, output_filename, output_dir=None):
    
    # Determine the full path for the output file
    if output_dir:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)  # Create the directory if it doesn't exist
        output_filename = os.path.join(output_dir, output_filename)
    else:
        output_filename = output_filename

    if format_type == 'json':        
        print(data)
        
    elif format_type == 'csv':
        result_data = data['result']

        # Convert the list of dictionaries to DataFrame
        df = pd.DataFrame(result_data)
        output_filename = output_filename+".csv"

        # Save the DataFrame to an Excel file
        df.to_csv(output_filename, index=False)
        print(f"Data saved as {output_filename}")
        
    elif format_type == 'xlsx':
        # Save data as Excel
        result_data = data['result']

        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(result_data)
        output_filename = output_filename+".xlsx"

        # Save the DataFrame to an Excel file
        df.to_excel(output_filename, index=False)
        print(f"Data saved as {output_filename}")
        
    else:
        raise ValueError("Invalid format_type. Choose 'json', 'csv', or 'xlsx'.")

def main():
    # API URL
    api_url = "https://dtmapi.iom.int/api/idpAdmin0Data/GetAdmin0Datav2"
    #Change the url to get Admin 1 or Admin 2 level data
    #For admin 1:https://dtmapi.iom.int/api/IdpAdmin1Data/GetAdmin1Datav2?
    #For admin 2:https://dtmapi.iom.int/api/IdpAdmin2Data/GetAdmin2Datav2?
    
    # Parameters for the API request
    params = {
        'CountryName': '',
        'Admin0Pcode':'AFG',
        'Operation': '',
        'FromReportingDate': '',
        'ToReportingDate': '',
        'Admin1Name': '',
        'Admin1Pcode': '',
        'Admin2Name': '',
        'Admin2Pcode': '',
        'FromRoundNumber': '',
        'ToRoundNumber': ''
    }
    
    # Format of the output (json, csv, or xlsx)
    format_type = 'csv'  # Change this to 'json' or 'xlsx' as needed
    
    # Output filename (without extension)
    output_filename = 'api_result'
    
    # Output directory (set to save to Desktop/api_data)
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    output_dir = os.path.join(desktop_path, 'api_data')  # Change this to your desired directory
    
    # Ensure at least one of the required parameters is provided
    if not (params['CountryName'] or params['Admin0Pcode'] or params['Operation']):
        raise ValueError("At least one of 'CountryName', 'Admin0Pcode', or 'Operation' must be provided")
    
    try:
        # Fetch data from API
        data = fetch_data(api_url, params)
        
        # Call Save the data in the desired format function
        save_data(data, format_type, output_filename, output_dir)
        
    except Exception as e:
        print(f"An error occurred: {e}")


main()