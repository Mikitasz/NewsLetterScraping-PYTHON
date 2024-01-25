# NewsLetterScraping

## Project Description

NewsLetterScraping is an educational project created for the purpose of learning and practicing web scraping to gather articles on the topic of cybersecurity from

- https://thehackernews.com/
- https://www.bleepingcomputer.com/ and etc.

and generating a newsletter based on the collected data.

### Project Goal

The main goal of the project is to extract information about cybersecurity articles from the websites: x

- https://thehackernews.com/
- https://www.bleepingcomputer.com/ and etc.

and create a newsletter in Microsoft Word based on the gathered data.

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

Simple run main.py, input all necessary links and that's all.
