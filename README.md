# Employee Performance Analytics: A Data-Driven Approach to Evaluating KPI

## 📌 Project Summary

I built an automated analytics system to evaluate the performance of warehouse order fulfillment staff, replacing a flawed tracking method that relied on manual spreadsheet screenshots. To capture the missing data, I reconstructed scattered metrics directly from low-quality smartphone photos of Excel screens shared by management. Over a 130-day period, I consolidated these fragmented reports to track the daily output of 78 employees. Ultimately, this system eliminated subjective workplace evaluations and delivered clear, data-driven time-series insights into actual workforce productivity.

## 📊 Business Context & Objectives

### Warehouse Operations
This large e-commerce company coordinates a massive logistics network to ship home goods. At the heart of this operation is the order fulfillment team. Workers use Mobile Data Terminals (MDTs) to scan item barcodes. Each MDT scan counts as a "click," which serves as the primary metric for evaluating daily performance. 

### The Management Problem
Despite the scale of the business, the warehouse completely lacked data APIs, dashboards, or digital reporting tools. Instead, management manually monitored performance by sharing smartphone photos of Excel spreadsheets. This chaotic approach made it impossible to evaluate staff objectively. Management suspected the team was underperforming, but they had no way to prove it.

I consolidated this fragmented data into a single analytical system to solve this blindspot and evaluate performance against three clear benchmarks:
* **The Corporate Baseline:** Prove whether the management's target of 350 clicks per shift was actually realistic.
* **Peer Performance:** Benchmark individual employee output against the rest of the 78-person team to find outliers.
* **Contextual Factors:** Such as high-stress periods, operational pauses, and new department launches.


## 💡 Findings & Conclusions
<div align="center">
  <img src="./figures/fig_7.png" width="700">
  <p><i> Trend Analysis – 'Roman3' 7-day rolling average vs. company-wide performance baseline.</i></p>
</div>
The graph tracks my productivity over the entire 130-day observation period. It illustrates not only my individual efficiency, but how external factors impacted warehouse performance. 

The early phase of the timeline highlights the launch of the new SABON department (January 1 – February 23), which sustained high operational volume. This was followed by a sharp, company-wide drop in productivity in late February, directly correlating with the outbreak of active military conflict in the region and resulting in a forced operational pause between February 28 and March 14. 

Despite these severe disruptions, my performance recovered much faster than the company average. Following a forced operational pause, my output even hit a major peak driven by a backlog of high order volumes. But most importantly, the data shows my daily output consistently stayed well above both the company average and company's 350-click baseline.


## 🛠 Tech Stack & Data Pipeline

I intentionally split architecture into two distinct notebooks due to the specifics of working with Google Colab. By separating OCR (the resource-heavy part) engine from the analytical workflows, the system allows for rapid iteration on business analytics without the need to re-initialize and rerun the computationally expensive image-processing logic every time.

### 1. Computer Vision (OCR) Module
Since the raw data existed only as photos of a screen, I developed an OCR pipeline to convert visual noise into structured data.
*   **Image Preprocessing:** Implementing Gaussian Blur to remove Moire patterns (screen interference), CLAHE for contrast enhancement, and Unsharp Masking for character definition.
*   **Extraction:** Leveraging EasyOCR to detect and recognize text in low-quality images.
*   **Transformation & Reconstruction Logic:** Mapping bounding box coordinates to reconstruct logical lines from chaotic text blocks, exporting the cleaned data into a structured format: `[File Date, Filename, Employee Name, Click Count]`.

### 2. Analytical Module (Data Integrity & Cleaning)
A critical challenge was handling duplicated or incomplete data, as multiple photos were often taken within a single day.
*   **Data Consolidation:** I extracted end-of-day totals by filtering out partial intraday updates, ensuring the analysis only used the final, cumulative snapshot for each day.
*   **Time-Series Generation:** I parsed date metadata directly from the image filenames to build a continuous, 130-day historical timeline of warehouse performance.
*   **Comparative Analysis:** I aggregated the cleaned daily metrics to evaluate my personal output against the 78-person team average and the 350-click baseline.