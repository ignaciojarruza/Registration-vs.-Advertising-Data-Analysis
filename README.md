# Registration-vs.-Advertising-Data-Analysis

This program takes registration sheets, event data including attendance/registration numbers, and advertising data as input. It outputs a graph for each event where the registration data is plotted with the advertisement dates represented as vertical lines on the graphs.

## Project Background

I developed this tool in my role as a `Data Administrator` for the ADVANCE Office of Faculty Development at Northeastern University. This project was created to visualize the impact of advertisement campaigns on registration and attendance numbers for the 2023-2024 academic year (ongoing). This tool helps in analyzing and understanding the effectiveness of various advertising efforts for events our office hosts.

## Installation and Requirements

Before running the program, ensure you have the following dependencies installed:

- Python 3.x
- pandas
- matplotlib
  You can install these dependencies using pip:

```
pip install pandas matplotlib
```

## Usage

1. Clone the repository or downlaod the source code files.
2. Place your registration sheets in the `registration-sheets` directory.
3. Prepare your event and advetising data in Excel format. Ensure you have columns named appropriately.
4. Run the program.

```
python registration-data-analysis.py
```

## Input Data

`Registration Sheets`

- The program reads registration sheets from the `registration-sheets` directory.
- Each registration sheet should be in Excel format with appropriate columns for registration data.
- The program iterates through each registration sheet to gather data for plotting.

## Event Data

- Event data is read from an Excel file specified by `registration-data.xlsx`.
- It should contain information about events including their name, number of participants registered, number of attendees, and modality.

## Advertising Data

- Advertising data is read from an Excel file specified by `advertising-data.xlsx`.
- It contains information about advertising dates for each event.

## Output

The program generates a graph for each event. Each graph displays the following:

- Registration data plotted against the date of registration
- Vertical lines representing advertising dates (in red) and newsletter advertised dates (in purple).
  - In my office, we count advertisements with flyers and advertisements through our monthly newsletter separately.
- Event date indicated by a vertical line in black.
- Event title, modality, registered attendees, attended, and attendance rate displayed as the graph title.

## Example Outputs

The graphs provided under the `/sample-outputs` folder are created from real data collected by our office. These graphs illustrate the visualization of registration and attendance trends alongside advertising efforts for various events during the 2023-2024 academic year. These examples demonstrate how the program can be used to analyze the impact of advertisement campaigns on event participation and inform future advertising strategies.
