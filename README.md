{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Employee Performance Analytics: A Data-Driven Approach to Evaluating KPI\n",
        "\n",
        "## 📌 Project Summary\n",
        "\n",
        "I built an automated system to analyze the performance of warehouse order fulfillment staff, replacing a flawed tracking method that relied on Excel pivot tables. For that I used Python, OpenCV, and EasyOCR to read and transform data from low-quality smartphone photos of Excel screens. I processed this highly noisy data of a 130-day period, extracted end-of-day totals, and tracked the performance of 78 employees. Finally, I transformed it into clear, time-series insights that show real employees' efficiency.\n",
        "\n",
        "## 📊 Business Context\n",
        "\n",
        "To optimize efficiency, this large-scale home goods e-commerce warehouse closely tracks the performance of order fulfillment staff. Employees use Mobile Data Terminals (MDTs) to scan item barcodes, making the daily \"click count\" the primary metric for evaluating productivity against a corporate baseline of 350 clicks per shift. However, the company lacked any data API, digital reporting system or dashboard. Management manually tracked performance using spreadsheet screenshots shared as smartphone photos. I brought all the data provided into one form in order to find out whether the corporate targets were realistic or the team was underperforming.\n",
        "\n",
        "## 💡 Findings & Conclusions\n",
        "<div align=\"center\">\n",
        "  <img src=\"./figures/fig_7.png\" width=\"700\">\n",
        "  <p><i> Trend Analysis – 'Roman3' 7-day rolling average vs. company-wide performance baseline.</i></p>\n",
        "</div>\n",
        "The graph tracks my productivity over the entire 130-day observation period. It illustrates not only my individual efficiency, but how external factors impacted overall warehouse operations. A significant company-wide drop in productivity between late February and early March directly correlates with the outbreak of active military conflict in the region. Despite these severe disruptions, my performance recovered much faster than the company average. Following a forced operational pause, my output even hit a major peak driven by a backlog of high order volumes. But most importantly, the data shows my daily output consistently stayed well above both the company average and company's 350-click baseline.\n",
        "\n",
        "## 🎯 The Analytical Objective\n",
        "The goal was to visualize and evaluate performance relative to:\n",
        "1.  **The Baseline:** The minimum required output (350 clicks).\n",
        "2.  **Peer Performance:** Comparison with the rest of the 78-person team.\n",
        "3.  **Contextual Factors:** Accounting for periods of high-stress operations and departmental launches.\n",
        "\n",
        "## 🛠 Tech Stack & Data Pipeline\n",
        "\n",
        "I intentionally split architecture into two distinct notebooks due to the specifics of working with Google Colab. By separating OCR (the resource-heavy part) engine from the analytical workflows, the system allows for rapid iteration on business analytics without the need to re-initialize and rerun the computationally expensive image-processing logic every time.\n",
        "\n",
        "### 1. Computer Vision (OCR) Module\n",
        "Since the raw data existed only as photos of a screen, I developed an OCR pipeline to convert visual noise into structured data.\n",
        "*   **Image Preprocessing:** Implementing Gaussian Blur to remove Moire patterns (screen interference), CLAHE for contrast enhancement, and Unsharp Masking for character definition.\n",
        "*   **Extraction:** Leveraging EasyOCR to detect and recognize text in low-quality images.\n",
        "*   **Transformation & Reconstruction Logic:** Mapping bounding box coordinates to reconstruct logical lines from chaotic text blocks, exporting the cleaned data into a structured format: `[File Date, Filename, Employee Name, Click Count]`.\n",
        "\n",
        "### 2. Analytical Module (Data Integrity & Cleaning)\n",
        "A critical challenge was handling duplicated or incomplete data, as multiple photos were often taken within a single day.\n",
        "*   **Data Consolidation:** I extracted end-of-day totals by filtering out partial intraday updates, ensuring the analysis only used the final, cumulative snapshot for each day.\n",
        "*   **Time-Series Generation:** I parsed date metadata directly from the image filenames to build a continuous, 130-day historical timeline of warehouse performance.\n",
        "*   **Comparative Analysis:** I aggregated the cleaned daily metrics to evaluate my personal output against the 78-person team average and the 350-click baseline."
      ],
      "metadata": {
        "id": "Hk-jGkrysakL"
      }
    }
  ]
}