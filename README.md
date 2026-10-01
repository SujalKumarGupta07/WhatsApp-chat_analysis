# 📱 WhatsApp Chat Analyzer

A comprehensive, interactive web application built with **Streamlit** and **Python** to visualize, parse, and analyze WhatsApp chat conversations. Whether you want to analyze group dynamics or private one-on-one conversations, this tool provides deep statistical and visual insights into messaging habits.

---

## 🚀 Features

- **📊 High-Level Chat Statistics**:
  - Total messages exchanged
  - Total words sent
  - Media items shared (`<Media omitted>`)
  - Total web links/URLs shared

- **📈 Activity & Timelines**:
  - **Monthly Timeline**: Visualize conversational volume trends across months and years.
  - **Daily Timeline**: Granular daily messaging pattern tracking.
  - **Most Active Days**: Day-of-the-week activity bar chart.
  - **Most Active Months**: Seasonal / monthly chat frequency breakdown.
  - **Weekly Activity Heatmap**: Hourly activity breakdown by day of the week to identify peak chat hours.

- **👥 User-Level & Group-Level Analysis**:
  - Analyze the entire group collectively (**"Overall"**) or filter by any individual participant.
  - **Busiest Users**: Rank group members by message count and contribution percentage.

- **🔤 Text & Language Insights**:
  - **Word Cloud**: Visual representation of the most frequently used words.
  - **Common Words Analysis**: Top 20 most frequent words (automatically filters out custom Hinglish & English stopwords).

- **😀 Emoji Analysis**:
  - Comprehensive breakdown of emojis used.
  - Top emojis visualized in an interactive pie chart alongside tabular counts.

- **🔄 Broad Compatibility**:
  - Robust parser supporting **Android** and **iOS** WhatsApp exports.
  - Handles 12-hour (AM/PM) and 24-hour timestamps, 2-digit and 4-digit years, and Unicode space variations (e.g. `\u202f`, `\u00a0`).

---

## 🛠️ Tech Stack

- **Frontend & App Framework**: [Streamlit](https://streamlit.io/)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
- **Visualizations**: [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
- **NLP & Text Processing**: [WordCloud](https://github.com/amueller/word_cloud), [URLExtract](https://github.com/lopusz/url-extractor), [emoji](https://github.com/carpedm20/emoji)

---

## 📁 Project Structure

```plaintext
whatsapp-chat-analysis/
├── app.py              # Streamlit dashboard and UI rendering
├── helper.py           # Statistical calculations, aggregations, and visual generators
├── preprocessor.py     # Regex parsing, cleaning, and feature extraction pipeline
├── requirements.txt    # Python dependencies
├── stop_hinglish.txt   # Stopwords dictionary for English & Hinglish
├── .gitignore          # Ignored files and directories
└── README.md           # Project documentation
```

---

## 📥 How to Export Your WhatsApp Chat

1. Open **WhatsApp** on your mobile device.
2. Navigate to the chat (individual or group) you want to analyze.
3. Tap the **three dots (⋮)** on Android or the **contact/group name** at the top on iOS.
4. Tap **More** > **Export Chat**.
5. Select **Without Media** *(Important: Media files are not needed and will increase file size)*.
6. Save or transfer the resulting `.txt` file to your computer.

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher installed on your system.
- `pip` package manager.

### 1. Clone the Repository
```bash
git clone https://github.com/SujalKumarGupta07/WhatsApp-chat_analysis.git
cd WhatsApp-chat_analysis
```

### 2. Create and Activate a Virtual Environment

- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```

The web app will launch automatically in your default browser at `http://localhost:8501`.

---

## 🖥️ Usage

1. Open the web interface in your browser.
2. In the sidebar on the left, click **Browse files** and upload your exported WhatsApp `.txt` file.
3. Choose whether to analyze the chat **Overall** or select a specific **user** from the dropdown menu.
4. Click **Show Analysis** to generate the metrics, timelines, charts, and visualizations.

---
