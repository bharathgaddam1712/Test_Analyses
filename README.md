# Student Performance Feedback System

## Overview

An AI-powered system to analyze student test data from JSON files, generate personalized feedback using the Gemini Pro model, and produce styled PDF reports with charts and insights. The system now includes a web interface for user-friendly input and analysis, allowing users to upload test data, view detailed performance reports, and download PDFs.

## Tech Stack

- **Language**: Python 3.9+
- **LLM**: Gemini Pro (via Google Generative AI API)
- **Backend**: Flask (for web interface)
- **Frontend**: React, Tailwind CSS (CDN-hosted)
- **Libraries**:
  - pandas: Data processing
  - matplotlib, seaborn: Charts
  - google-generativeai: LLM integration
  - reportlab: PDF generation
  - flask, flask-cors: Web server and CORS handling

## API Used

- **Google Generative AI API (Gemini Pro)**: Generates personalized, human-like feedback based on student performance data.

## Prompt Logic

- **Context**: Student name, test stats (time, marks, questions), subject-wise and chapter-wise metrics (accuracy, time, difficulty, concepts).
- **Instruction**: Generate:
  1. Motivating, personalized intro message.
  2. Detailed subject and chapter breakdown.
  3. Time vs. accuracy insights.
  4. 2-3 actionable suggestions.
- **Tone**: Warm, encouraging, constructive.
- **Approach**: Structured prompt with clear sections, tailored to performance (e.g., celebrate high Chemistry accuracy, address slow Physics timing).

## Report Structure

- **Header**: Student name, exam title, date, "Performance Feedback Report".
- **Intro**: Personalized, motivating message from Gemini.
- **Summary**: Test stats (time, marks, attempted, accuracy).
- **Breakdown**: Subject-wise and chapter-wise stats (table).
- **Insights**: Time vs. accuracy analysis (scatter plot + text).
- **Suggestions**: 2-3 actionable steps with bolded sub-headings.
- **Visuals**: Bar chart (subject accuracy), scatter plot (time vs. accuracy).
- **Styling**: Helvetica font, embedded charts, clean layout.

## Web Interface

- **Page 1: Input Form**
  - Input fields: Student name, examination title, exam date, JSON file upload.
  - Button: "Analyze Your Test" to process data and navigate to the analysis page.
- **Page 2: Analysis Report**
  - Displays the full PDF content: cover page, introduction, performance breakdown, insights, suggestions, and encouragement.
  - Charts: Subject-wise accuracy and individual subject performance.
  - Button: "Download the PDF" to save the generated report locally.
- **Tech**: React for dynamic UI, Tailwind CSS for styling, Flask backend for API endpoints (`/api/analyze`, `/api/download`).

## Project Structure

```
student-feedback-system/
├── data/
│   ├── submission1.json        # Sample test data JSON
│   ├── submission2.json
│   ├── submission3.json
│   ├── submission4.json
├── src/
│   ├── data_processing.py      # Parse JSON, compute metrics
│   ├── ai_feedback.py          # Prompt Gemini, generate feedback
│   ├── visualization.py        # Create charts and tables
│   └── pdf_generator.py        # Generate styled PDF report
├── static/
│   └── index.html              # React-based frontend
├── output/
│   ├── charts/                # Store generated chart images
│   └── reports/               # Store generated PDF reports
├── config/
│   └── config.py              # API keys, constants, file paths
├── tests/
│   ├── test_data_processing.py # Unit tests for data parsing
│   └── test_feedback.py       # Unit tests for feedback generation
├── app.py                     # Flask backend with API endpoints
├── main.py                    # Main script for CLI workflow
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup

1. Clone the repository: `git clone <repo-link>`

2. Create a virtual environment: `python -m venv venv`

3. Activate the virtual environment:

   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. Install dependencies: `pip install -r requirements.txt`

5. Update `config/config.py` with your Gemini API key and directory paths:

   ```python
   GEMINI_API_KEY = 'your-api-key'
   OUTPUT_REPORTS_DIR = 'output/reports'
   OUTPUT_CHARTS_DIR = 'output/charts'
   ```

6. Place JSON files in `data/` for CLI processing or upload via the web interface.

### CLI Workflow

- Run: `python main.py`
- Processes JSON files in `data/`, generates charts in `output/charts/`, and PDFs in `output/reports/`.

### Web Interface Workflow

1. Run the Flask server: `python app.py`
2. Access the interface at `http://localhost:5000`
3. Enter student details, exam title, date, and upload a JSON file.
4. Click "Analyze Your Test" to view the report.
5. Click "Download the PDF" to save the analysis report locally.

## Output

- **CLI**: Charts in `output/charts/`, PDF reports in `output/reports/`.
- **Web**: Interactive report displayed in the browser, downloadable PDF saved locally.
- Public link: \[Upload to Google Drive or GitHub Pages and insert link\]

## Development Notes

- Ensure `visualization.py` saves charts with accessible paths (e.g., `/output/charts/`).
- Secure the Flask backend by sanitizing inputs and limiting file uploads to `.json`.
- Add tests for the web interface in `tests/` if needed.
- For production, use a WSGI server (e.g., Gunicorn) and configure CORS appropriately.

## Contributing

- Fork the repository and submit pull requests for new features or bug fixes.
- Report issues via GitHub Issues.

