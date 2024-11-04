import openai
import requests
from bs4 import BeautifulSoup


def validate_urls(policy_url, target_url):
    return bool(policy_url and target_url)


def fetch_and_clean_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    text = " ".join(soup.stripped_strings)

    text = text.replace("\n", " ").replace("\r", "").strip()

    return text


def generate_prompt(policy_content, target_content):
    return (
        f"Check if the following webpage content adheres to this compliance policy:\n"
        f"Compliance Policy:{policy_content}\n"
        f"Webpage Content:{target_content}\n"
        f"List any non-compliant issues you find and explain why."
    )


def get_compliance_findings(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a compliance checker AI."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
    )
    return response.choices[0].message['content'].strip()
