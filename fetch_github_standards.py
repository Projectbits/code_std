"""
Module: fetch_github_standards.py
Created: 2025-04-23
Creator: Don Lovett
Purpose: Fetches coding standards from a public GitHub repository.
Version: 2.0
Last Modified: 2025-04-23
Changelog:
    - v2.0: Initial version with Version 2 standards
"""

import logging
import os
import requests
from colorama import init, Fore
from typing import Optional

init(autoreset=True)

logging.basicConfig(
    filename="logs/fetch_github_standards.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_message(message: str, level: str = "INFO") -> None:
    """Log a message with color-coded output."""
    colors = {"INFO": Fore.GREEN, "WARNING": Fore.YELLOW, "ERROR": Fore.RED}
    print(f"{colors.get(level, Fore.WHITE)}--> {message}")
    getattr(logging, level.lower())(message)

def fetch_standards(url: str) -> Optional[str]:
    """Fetch a file from a public GitHub repository."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        log_message("Successfully fetched standards")
        return response.text
    except Exception as e:
        log_message(f"Error fetching standards: {e}. Ensure the URL is correct and public.", "ERROR")
        return None

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    log_message("Script started")
    url = "https://raw.githubusercontent.com/Projectbits/code_std/main/Coding%20Standards.md"
    content = fetch_standards(url)
    if content:
        log_message("Standards content (first 500 chars):")
        print(content[:500])
    log_message("Script completed")

# Instructions:
# Save: Save as `fetch_github_standards.py` in `/home/user/scripts`.
# Run: Install requests and colorama (`pip install requests colorama`), then run: `python fetch_github_standards.py`.
# Prerequisites: Python 3.6+, requests, colorama.
# Troubleshooting: Check `logs/fetch_github_standards.log`. Red output indicates errors (e.g., "Ensure the URL is public"). Verify the URL or network.
