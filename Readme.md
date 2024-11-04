# EventStreamX
This project simulates an AI based Compliance checker.

## Installation

Running the System:

- Step 1: Clone the repository.

```
git clone https://github.com/sanjanakansal/compliance_checker.git
cd compliance_checker
```
- Step 2: Create a .env file in the root of the project directory and add the OPENAI_API_KEY variable with its value.
```
OPENAI_API_KEY=your_openai_api_key_here
```
- Step 3: Install Python Requirements.
```
pip install -r requirements.txt
```
- Start the Django Server.

```
python manage.py runserver
```


## Future Enhancements
- Analyze incoming content in real-time, providing immediate feedback and alerts for non-compliance.
- Set up automated alerts via email, SMS, or Slack when non-compliant content is detected.
- Develop a real-time dashboard that displays live updates on compliance checks, recent violations, and resolution status.
- Expand compliance checking capabilities to multiple languages by leveraging multilingual NLP models or integrating translation APIs.
