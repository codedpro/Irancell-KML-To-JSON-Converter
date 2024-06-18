# Irancell KML to JSON Converter

## Overview

The **Irancell KML to JSON Converter** is a tool designed to facilitate the conversion of KML data related to FTTH and FTTX of MTN Irancell into a GeoJSON format. This conversion allows for easy visualization and analysis of fiber optic services on monitoring tools such as LNM.

## Features

- **Convert KML to GeoJSON**: Seamlessly convert KML files into GeoJSON format.
- **Progress Bar**: Real-time progress display using a progress bar.
- **Error Handling**: Robust error handling to manage and report issues during the conversion process.

## Requirements

To run this project, you will need to have Python installed along with the following libraries:

- `pykml`
- `lxml`
- `tqdm`

You can install these dependencies using the provided `requirements.txt` file.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/codedpro/Irancell-KML-To-JSON-Converter.git
   cd Irancell-KML-To-JSON-Converter
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Place Your KML File**: Ensure your KML file (e.g., `input.kml`) is in the project directory.

2. **Run the Converter**:
   ```bash
   python main.py
   ```

3. **Output**: The converted GeoJSON file (e.g., `output.json`) will be created in the project directory.

## Contributing

We welcome contributions to enhance the functionality and usability of this tool. Feel free to open issues or submit pull requests on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

This tool was developed to streamline the process of converting KML data for MTN Irancell's FTTH and FTTX services, enabling efficient visualization and monitoring using tools like LNM.