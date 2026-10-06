# AI-Based IT Helpdesk Ticket Analysis & Resolution Prediction

## Project Overview

This project focuses on analyzing IT helpdesk ticket data to understand ticket patterns, priorities, issue types, project-wise ticket distribution, and resolution time.

The project is developed as a Python data analysis project using Jupyter Notebook, NumPy, Pandas, and Matplotlib.

---

## Industry

**IT Helpdesk / IT Support**

---

## Problem Statement

IT organizations handle a large volume of helpdesk tickets related to technical issues and support requests. However, analyzing these tickets manually makes it difficult to identify recurring problems, understand resolution patterns, and estimate how long a new ticket may take to resolve.

This project focuses on analyzing IT helpdesk ticket data to understand ticket patterns, priority, issue types, project-wise ticket distribution, and resolution time.

---

## Proposed Solution / Analysis Questions

The project uses Python-based data analysis to clean, transform, analyze, and visualize IT helpdesk ticket data.

The analysis focuses on:

- Understanding the structure and quality of the helpdesk ticket dataset
- Analyzing tickets based on priority
- Analyzing different issue types
- Analyzing project-wise ticket distribution
- Calculating ticket resolution time
- Comparing resolution time across ticket priorities
- Comparing resolution time across issue types
- Examining comments and contributors in relation to resolution time
- Analyzing ticket volume over time

The cleaned and analyzed data provides a foundation for future work related to resolution-time prediction.

---

## Dataset

**Dataset Name:** Help Desk Tickets

**Main Dataset File:** `issues.csv`

**Dataset Source:** Help Desk Tickets dataset provided for this project.

The original dataset contains **66,691 records and 58 columns**.

For the Sprint 1 analysis, relevant ticket fields were selected, including:

- `id`
- `issue_proj`
- `issue_contr_count`
- `issue_type`
- `issue_priority`
- `issue_created`
- `issue_resolution_date`
- `issue_resolution`
- `issue_status`
- `issue_comments_count`

---

## Tools & Technologies

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib

> Seaborn and Scikit-learn are not used in the Sprint 1 analysis.

---

## Project Workflow

**Industry Selection → Problem Identification → Dataset Collection → Data Cleaning → Data Transformation → Data Analysis → Data Visualization → Insights → Recommendations**

---

## Data Cleaning & Transformation

The project performs the following data preparation activities:

- Dataset inspection
- Missing-value checking
- Duplicate checking
- Selection of relevant columns
- Date and time conversion
- Resolution-time calculation
- Preparation of data for analysis and visualization

### Resolution Time

Resolution time is calculated using the issue creation date and issue resolution date:

```text
Resolution Time = Issue Resolution Date - Issue Created Date
```

The calculated resolution time is represented in hours as:

```text
resolution_time_hours
```

---

## Data Analysis

The following analysis was performed in the project:

### 1. Ticket Priority Analysis

Analysis of the number of tickets across different priority levels.

### 2. Issue Type Analysis

Analysis of ticket distribution across different issue types.

### 3. Project-wise Ticket Analysis

Analysis of ticket volume across projects.

### 4. Resolution Time Analysis

Statistical analysis of ticket resolution time using NumPy, including:

- Mean
- Median
- Minimum
- Maximum
- Standard deviation

### 5. Resolution Time by Priority

Comparison of resolution time across different ticket priorities.

### 6. Resolution Time by Issue Type

Comparison of resolution time across different issue types.

### 7. Comments and Resolution Time

Analysis of the relationship between the number of comments and ticket resolution time.

### 8. Contributors and Resolution Time

Analysis involving contributor count and ticket resolution time.

### 9. Monthly Ticket Analysis

Analysis of ticket volume based on the month in which tickets were created.

---

## Visualization Screenshots

The following visualizations were created using Matplotlib.

### Tickets by Priority

![Tickets by Priority](Visualizations/tickets_by_priority.png)

### Tickets by Issue Type

![Tickets by Issue Type](Visualizations/tickets_by_issue_type.png)

### Resolution Time Distribution

![Resolution Time Distribution](Visualizations/resolution_time_distribution.png)

### Resolution Time by Priority

![Resolution Time by Priority](Visualizations/resolution_time_by_priority.png)

### Monthly Ticket Trend

![Monthly Ticket Trend](Visualizations/monthly_ticket_trend.png)

### Comments vs Resolution Time

![Comments vs Resolution Time](Visualizations/comments_vs_resolution_time.png)

---

## Key Insights

The project analyzes the following areas to identify patterns in the helpdesk ticket data:

- Ticket distribution by priority
- Ticket distribution by issue type
- Project-wise ticket volume
- Overall resolution-time statistics
- Resolution-time differences across priorities
- Resolution-time differences across issue types
- Monthly ticket volume
- Relationship between comments and resolution time
- Relationship between contributor count and resolution time

The detailed numerical results and analysis outputs are available in the Jupyter Notebook.

---

## Recommendations

The Sprint 1 analysis provides a structured understanding of the helpdesk ticket dataset and its resolution-time patterns.

The cleaned and analyzed dataset can be used as the foundation for future work on resolution-time prediction.

Specific business recommendations are not included in this README because no separate final recommendations were provided as part of the project information.

---

## Project Folder Structure

```text
AI_ticket_helper/
│
├── README.md
│
├── Dataset/
│   ├── raw_dataset/
│   │   └── issues.csv
│   │
│   └── cleaned_dataset/
│       └── cleaned_issues.csv
│
├── Notebook/
│   └── AI_IT_Helpdesk_Ticket_Analysis_Sprint1.ipynb
│
├── Python/
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   └── data_visualization.py
│
├── Visualizations/
│   ├── tickets_by_priority.png
│   ├── tickets_by_issue_type.png
│   ├── resolution_time_distribution.png
│   ├── resolution_time_by_priority.png
│   ├── monthly_ticket_trend.png
│   └── comments_vs_resolution_time.png
│
└── Documentation/
    └── Project_Report.md
```

---

## Project Notebook

The main project analysis is available in:

```text
Notebook/AI_IT_Helpdesk_Ticket_Analysis_Sprint1.ipynb
```

The notebook contains the data loading, dataset inspection, cleaning, transformation, analysis, statistical calculations, and visualizations performed for Sprint 1.

---

## Future Scope

The cleaned and analyzed helpdesk ticket dataset can be used for future work related to **resolution-time prediction**.

---

## Author

- **Name:** Gowtham M
- **Student ID:** AF05309798
- **Organization:** Anudip Foundation
- **Course:** AIML
- **Batch Code:** ANP-D7444
