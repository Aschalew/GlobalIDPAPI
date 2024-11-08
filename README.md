# Code Description

---

# DTM Global API Data Fetcher

This Python script allows you to fetch and save data from the Displacement Tracking Matrix (DTM) Global API in multiple formats (CSV, XLSX, JSON). The DTM is managed by the International Organization for Migration (IOM) to monitor displacement and population movements. This script provides a convenient way to retrieve and save data in various formats for analysis and reporting.

## Features

- Fetches data from DTM API with customizable parameters.
- Supports saving data in JSON, CSV, or XLSX formats.
- Allows specifying output directory and file names for easy data organization.

## Requirements

- Python 3.x
- `requests`
- `pandas`
  
You can install the required packages via pip:

```bash
pip install requests pandas
```

## Usage

### Configuration

1. **API URL**: The API URL is set to fetch Admin 0 level data by default. Change the URL in the script for different administrative levels:
   - Admin 0: `https://dtmapi.iom.int/api/idpAdmin0Data/GetAdmin0Datav2`
   - Admin 1: `https://dtmapi.iom.int/api/IdpAdmin1Data/GetAdmin1Datav2`
   - Admin 2: `https://dtmapi.iom.int/api/IdpAdmin2Data/GetAdmin2Datav2`

2. **Parameters**: Adjust the parameters in the `params` dictionary to filter data by country code, administrative level, reporting dates, and other optional fields.
   
   Example `params`:
   ```python
   params = {
       'CountryName': '',
       'Admin0Pcode': 'AFG',  # Example for Afghanistan
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
   ```

3. **Output Format**: Set the `format_type` variable to specify the output format (`'json'`, `'csv'`, or `'xlsx'`).

4. **Output Location**: By default, files are saved to a folder named `api_data` on your desktop. Change the `output_dir` variable to a different path if desired.

### Running the Script

Execute the script by running:

```bash
python script_name.py
```

The script will:

1. Fetch data from the DTM API using specified parameters.
2. Save the data in the selected format at the chosen output location.
3. Print a success message with the output file path or display any errors encountered.

### Example

To fetch and save data as a CSV file:

```python
params = {
    'Admin0Pcode': 'AFG'  # Specify the country or any other required parameters
}
format_type = 'csv'
```

## Functions

### `fetch_data(api_url, params)`
- **Description**: Sends a GET request to the specified API with the given parameters.
- **Parameters**:
  - `api_url`: API endpoint URL.
  - `params`: Dictionary of query parameters for API request.
- **Returns**: JSON data if the request is successful.

### `save_data(data, format_type, output_filename, output_dir=None)`
- **Description**: Saves the fetched data in the specified format (`json`, `csv`, or `xlsx`).
- **Parameters**:
  - `data`: Data retrieved from the API.
  - `format_type`: Output format (`json`, `csv`, or `xlsx`).
  - `output_filename`: Base name of the output file.
  - `output_dir`: Directory to save the file.

## Error Handling

If a required parameter (such as `CountryName`, `Admin0Pcode`, or `Operation`) is missing, the script will raise a `ValueError`. Additionally, any issues during the API request or file saving process will be caught and printed.
