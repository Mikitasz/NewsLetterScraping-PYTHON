# Newsletter Scraping Project

## Project Overview

Newsletter Scraping is an educational initiative designed to facilitate the learning and application of web scraping techniques. The primary focus of this project is to extract articles related to cybersecurity from prominent websites such as:
- [The Hacker News](https://thehackernews.com/)
- [Bleeping Computer](https://www.bleepingcomputer.com/)

The collected data is then utilized to generate a newsletter in Microsoft Word format.

## Installation

The project uses libraries: `python-docx` for creating Microsoft Word documents, `pillow` for image processing, `tldextract` fot extracting domain name from the link, `googletrans` for google translating and `bs4`.

### Install Dependencies

```bash
pip install python-docx
pip install tldextract
pip install pillow
pip install googletrans
pip install bs4

```

## Usage

To execute the project, run the main.py script and provide the necessary input, including the relevant links. The program will then process the data and generate the desired newsletter in Microsoft Word format.





