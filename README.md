# Resume Customizer

Purpose: tool to automate the steps in generating a custom resume for each job description, during a job search

### Data models

| Resume |
| ------- |
| title   |
| text    |


| Job     |
| ------- |
| JD urls |
| JD text |
| Job site |
| Date posted |
| Date applied |
| State |
| Output raw |
| Output edited |
| Resume url |


### MVP First Draft:

#### Functional Requirements:

1. Get data from OpenAI ChatGPT API
    a. be able to take in 2 inputs: resume text & job description text
    b. be able to query OpenAI ChatGPT API with 2 inputs in prompt template

2. Display the API result output

3. Improve UX
    a. Store and name resumes
    b. Pick from a list of stored resumes when customizing
    c. Copy buttons to copy output & highlighted text
    d. Save output with Job metadata in persistent storage
    e. View and Edit the prompt template

4. Style the UI
    a. Make UI presentable in a business context

