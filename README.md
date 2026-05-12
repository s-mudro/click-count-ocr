# Employee Performance Defense: Data-Driven Analytics vs. Subjective Bias

## 📌 Project Overview
This project was born out of a need to challenge a subjective and unfounded claim regarding the low performance of a specific employee (**Roman3**). The core objective was to use objective data to debunk false assertions and demonstrate the employee's actual efficiency compared to team benchmarks and management requirements.

## 🎯 The Objective
The goal was to visualize and prove the performance of **Roman3** relative to:
1.  **The Baseline:** The minimum required output.
2.  **Peer Performance:** Comparison with the rest of the team, including newly onboarded staff.
3.  **Contextual Factors:** Accounting for periods of high-stress operations and departmental launches.

## 📊 Business Context & Metrics
*   **Primary Metric:** "Clicks" (Successful barcode scans performed via a Mobile Data Terminal - MDT).
*   **Performance Baseline:** A standard shift requirement is **350 clicks**.
*   **The Data Source:** Visual reports (photographs) of Excel pivot tables containing `Employee Name` and `Click Count`.

## 🛠 Tech Stack & Data Pipeline

The project is divided into two main architectural components:

### 1. Computer Vision (OCR) Module
Since the raw data existed only as photos of a screen, a robust OCR pipeline was developed to convert visual noise into structured data.
*   **Image Preprocessing:** Implementing Gaussian Blur to remove Moire patterns (screen interference), CLAHE for contrast enhancement, and Unsharp Masking for character definition.
*   **Extraction:** Leveraging EasyOCR to detect and recognize text in low-quality images.
*   **Transformation:** Mapping coordinates to reconstruct logical lines and exporting data into a structured format: `[File Date, Filename, Employee Name, Click Count]`.

### 2. Analytical Module (Data Integrity & Cleaning)
A critical challenge was that multiple photos were often taken within a single day.
*   **Deduplication Logic:** The system identifies that only the *last* snapshot of a given day contains the final, accurate cumulative totals.
*   **Time-Series Generation:** Extracting metadata from filenames to build a historical performance timeline.
*   **Comparative Analysis:** Aggregating metrics to compare individual output against the 350-click baseline and the team average.

## 💡 Findings & Conclusions
The data-driven analysis revealed that the claim of "low performance" was not only incorrect but demonstrably false and hypocritical.

**Key Insights:**
*   **Consistent Excellence:** Roman3’s performance consistently exceeded the baseline and outperformed the majority of the staff, including recent hires.
*   **Hidden Contributions:** The management's claim failed to account for Roman3’s involvement in launching a new department (**Sabon**) and maintaining operations during active military conflicts (Operation **Epic Furry**).
*   **Final Verdict:** The data suggests that the "poor performance" narrative was likely a fabricated pretext for dismissal, as the empirical evidence confirms the employee’s high efficiency and dedication.

---
*Created as a tool for transparency and labor rights protection.*