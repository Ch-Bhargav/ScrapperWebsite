# HelloWorld Scrapper

## Overview

**HelloWorld Scrapper** is a web application built with Flask that allows users to retrieve and display their Codeforces and CodeChef profiles. Users can enter their usernames, and the application fetches and displays their current and historical ratings, global ranks, and other relevant profile information.

## Features

- **User-friendly Interface:** Simple and clean web interface for entering usernames and displaying results.
- **Profile Data Display:** Displays user profiles with current ratings, titles, and ranks from Codeforces and CodeChef.
- **Responsive Design:** Ensures a good user experience across various devices.

## Technologies Used

- **Flask:** A micro web framework for Python.
- **BeautifulSoup:** A library for web scraping in Python.
- **HTML/CSS:** For structuring and styling the web pages.

## Getting Started

### Prerequisites

- Python 3.7 or later
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/helloworld-scrapper.git
   cd helloworld-scrapper
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask application:**

   ```bash
   python app.py
   ```

2. **Open your web browser and go to:**

   ```
   http://127.0.0.1:1234/
   ```

   The main page should load, and you can enter your Codeforces and CodeChef usernames to retrieve and view your profile information.

## Project Structure

```plaintext
.
├── app.py                 # Main application file
├── README.md              # Project readme file
├── requirements.txt       # Dependencies list
├── static
│   ├── css
│   │   └── index.css      # CSS file for styling
├── templates
│   ├── index.html         # Main HTML template
│   ├── codechef.html      # CodeChef profile template
│   └── codeforces.html    # Codeforces profile template
└── venv                   # Virtual environment
```

## Usage

- Navigate to the main page and enter a Codeforces and/or CodeChef username.
- Click the **Get Rank** button to fetch and display the profile data.
- View the current and maximum ratings, titles, and other relevant information.

## Code Explanation

### `app.py`

- **`codeforcesRating(username)`**: Fetches and parses the Codeforces profile data for the given username.
- **`codechefRating(username)`**: Fetches and parses the CodeChef profile data for the given username.
- **Flask routes**:
  - `/`: Renders the main page.
  - `/submit`: Handles form submissions and renders profile data on the main page.
  - `/codechef`: Renders the CodeChef profile page.
  - `/codeforces`: Renders the Codeforces profile page.
  - `/codeforcesprofile` and `/codechefprofile`: Handle specific profile data fetching and rendering.

### `templates/index.html`

- The main template that includes the form for entering usernames and sections for displaying Codeforces and CodeChef profiles side by side.

### `templates/codechef.html` and `templates/codeforces.html`

- Templates for displaying the respective user profiles with all fetched data.

### `static/css/index.css`

- CSS for styling the HTML templates, ensuring a consistent and responsive layout.

## Future Improvements

- **Enhanced Data Display**: Add more profile information and improve visual representation.
- **Error Handling**: Enhance error messages and handling for cases where usernames are invalid or data cannot be fetched.
- **APIs Integration**: Integrate official APIs (if available) for more reliable data retrieval.
- **User Authentication**: Allow users to save and manage their profiles for quick access.

