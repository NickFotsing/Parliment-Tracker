# UK Parliament Visualization Tool

## Overview

The **UK Parliament Visualization Tool** is a dynamic and interactive solution designed to visualize and explore data about the Members of UK Parliament (MPs). Leveraging real-time data from the UK Parliament API, this project provides users with an intuitive graphical user interface (GUI) to access detailed information about MPs, including their name, title, party affiliation, gender, and more.

This tool aims to enhance accessibility, engagement, and transparency by bridging the gap between large datasets and user-friendly visualizations. It is ideal for citizens, journalists, educators, policymakers, and civic tech developers seeking insights into the composition and structure of Parliament.

---

## Features

- **Dynamic Visualization**: MPs are represented as clickable buttons, color-coded by party affiliation for easy identification.
- **Interactive Details**: Clicking on an MP's button opens a detailed pop-up displaying their name, title, party, gender, and profile photo.
- **Real-Time Updates**: Data is dynamically fetched from the UK Parliament API, ensuring users always have the latest information.
- **Scrollable Interface**: A scrollable layout makes all 650 MPs easily accessible, regardless of screen size.
- **Future Enhancements**:
  - Search and filtering capabilities.
  - Advanced data analytics for visualizing trends (e.g., gender balance, party composition).
  - Data export functionality for further analysis.

---

## Use Cases

1. **General Public**: Easily explore your representatives and understand Parliament's structure.
2. **Journalists**: Access up-to-date data for accurate reporting on political developments.
3. **Educators and Students**: Use the tool as an engaging resource for learning about government systems.
4. **Policymakers and Analysts**: Analyze trends in Parliament to support data-driven decision-making.
5. **Civic Tech Enthusiasts**: Build upon this project to create broader civic engagement platforms.

---

## Project Structure

The project is divided into three main components:

1. **Data Retrieval and Parsing**:
   - Fetches real-time data from the UK Parliament API using HTTP requests.
   - Parses JSON responses into Python dictionaries for efficient handling.

2. **Graphical User Interface (GUI)**:
   - Built with `customtkinter` to provide a modern and responsive design.
   - Displays MPs in a grid layout with interactive buttons.

3. **Interactive Features**:
   - Provides a pop-up window with detailed information about each MP.
   - Supports dynamic updates and responsive design for accessibility.

---

## Getting Started

### Prerequisites

- Python 3.10 or higher.
- Libraries:
  - `customtkinter`
  - `requests`
  - `Pillow`

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/uk-parliament-visualization.git
   cd uk-parliament-visualization
