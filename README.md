# E-Commerce Shipment & Last-Mile Logistics Analysis

##  Project Overview

This project focuses on analyzing e-commerce shipment and last-mile logistics data to improve delivery reliability, 
control transportation costs, and understand logistics resource utilization.
The project uses synthetic demonstration data containing shipment, route, delivery, cost, vehicle utilization, tracking,
and damage-related information.

##  Project Objectives

- Measure delivery performance using logistics KPIs.
- Identify routes associated with delays or high transportation costs.
- Understand the relationship between distance, shipment weight, and transport cost.
- Perform descriptive and exploratory data analysis.
- Apply regression and clustering techniques for logistics planning.
- Develop a roadmap from data collection to predictive analytics and optimization.

##  Key Performance Indicators

The project focuses on the following logistics KPIs:

- On-time Delivery Rate
- Average Delivery Time
- Average Shipment Cost
- Vehicle Utilization
- Damage Rate

## Technologies & Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

##  Analysis Performed

### 1. Data Cleaning & Preparation

The analysis includes:

- Handling missing shipment weight values using the median.
- Handling missing tracking information using an `Unknown` category.
- Checking invalid distance and cost values.
- Creating derived fields such as:
  - Delay Days
  - On-time Flag
  - Cost per Kilometre
- Checking duplicate shipment IDs.

### 2. Exploratory Data Analysis

Route-level analysis is performed using:

- Shipment count
- Average delivery days
- On-time delivery rate
- Average transportation cost

The analysis helps identify routes with poor delivery performance or higher transportation costs.

### 3. Regression Analysis

Linear Regression is used to analyze transportation cost based on:

- Distance
- Shipment Weight

### 4. Clustering

K-Means clustering is applied using:

- Distance
- Shipment Weight
- Transportation Cost
- Vehicle Utilization

This helps group shipments into different operational profiles.

## 📈 Expected Outcomes

- A repeatable KPI framework for logistics performance monitoring.
- Identification of routes with weak on-time performance or high costs.
- Better understanding of transportation cost drivers.
- Shipment segmentation for differentiated planning.
- A roadmap toward predictive analytics and optimization.

## 📄 Project Report

[View Detailed Project Report](Logistics_Data_Analyst_Internship_Task1_Report.pdf)

## 👩‍💻 Author

**Suhani Sallam**

B.Tech IT | Aspiring Data Analyst & SQL Developer
