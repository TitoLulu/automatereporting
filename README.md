# NEWS API CONTENT AGREGATOR WITH PYTHON AND SHEETS API

This project is influenced by Rob Selgado  [](https://medium.com/@robert.salgado/automate-reporting-no-bi-tools-required-40ae049b75ac)**Automate Reporting - No BI Tools Required** 

The aim of the project is build a scraper to [](https://newsapi.org/docs)**News API** that aggregates content based on the topic **Artificial Intelligence** and populate data on google spreadsheets through [](https://developers.google.com/sheets/api)**Sheets API**

# How to Run the project

<ol>
  <li>Create a developer account with News API </li>
  <li>Create a serivice account with GCP</li>
  <li>Create a service account for sheetsapi on GCP</li>
  <li>Grant edit rights to email provided in the credentials file downloaded from sheets API to the target output gsheet</li>
  <li>Run production.py scrip</li>
</ol>

# Automating the project

To automate the project consider using Airflow scheduler where you can set this up as a daily task .

