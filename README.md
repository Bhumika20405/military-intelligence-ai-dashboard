# 🛡️ Military Intelligence Dashboard

## AI-Powered Global Terrorism Analysis & Threat Intelligence System

An interactive **Streamlit-based dashboard** for analyzing historical terrorism incidents using the **Global Terrorism Database (GTD)**, data visualization, machine learning, forecasting, and intelligence-reporting modules.

> **Disclaimer:** This project is intended for educational, academic, research, and data-analysis purposes. Predictions and forecasts are based on historical data and should not be treated as real-world operational intelligence.

---

## 📌 Project Overview

The **Military Intelligence Dashboard** is a Python-based data analytics and machine learning application designed to provide an interactive platform for exploring historical terrorism data.

The system combines:

- 📊 Exploratory Data Analysis
- 🌍 Geographic Threat Visualization
- 🤖 Attack Type Prediction
- 🚨 Threat Level Classification
- 📈 Terrorism Attack Forecasting
- 🧠 AI-Assisted Intelligence Reporting
- 📥 Data and Report Download
- ⚙️ Dashboard Configuration

The application is developed using **Python, Streamlit, Pandas, NumPy, Plotly, Scikit-learn, and Joblib**.

---

# ✨ Key Features

## 🏠 1. Home Dashboard

The Home page provides an overview of the terrorism dataset.

### Displays

- Total number of incidents
- Total fatalities
- Total injured
- Number of countries
- Attacks over the years

It also provides navigation guidance to the other dashboard modules.

---

## 🌍 2. Global Threat Map

The Global Threat Map provides an interactive geographic visualization of terrorism incidents.

### Features

- Interactive world map
- Year-based filtering
- Latitude and longitude visualization
- Attack-type visualization
- Country information
- City information
- Terrorist group information
- Number of fatalities

The map is implemented using **Plotly Express geographic visualization**.

---

## 🤖 3. Attack Type Prediction

The Attack Prediction module uses a **Random Forest Classifier** to predict the type of attack.

### Input Features

The model uses:

- Country
- Region
- Weapon Type
- Target Type
- Terrorist Group
- Attack Success
- Suicide Attack
- Number of Fatalities
- Number of Injuries

Categorical variables are converted into numerical values using `LabelEncoder`.

### Output

The system provides:

- Predicted Attack Type
- Prediction Confidence

The trained model and encoders are stored in the `models` directory.

---

## 🚨 4. Threat Level Prediction

The Threat Level module classifies an incident into three levels:

- 🟢 LOW
- 🟡 MEDIUM
- 🔴 HIGH

The project calculates an incident's impact using:

```python
impact = nkill + nwound
```

The current classification logic is:

```text
Impact <= 2       → LOW
Impact <= 10      → MEDIUM
Impact > 10       → HIGH
```

A Random Forest classifier is then trained using incident-related features.

### Output

The module displays:

- Threat Level
- Confidence Score
- Probability Distribution

---

## 📈 5. Terrorism Attack Forecasting

The Forecasting module estimates future attack counts using historical yearly data.

### Workflow

```text
Select Country
      ↓
Collect Historical Data
      ↓
Group Attacks by Year
      ↓
Train Linear Regression
      ↓
Generate Future Years
      ↓
Predict Future Attack Counts
      ↓
Display Forecast
```

### Features

- Country selection
- Forecast period selection
- Historical attack visualization
- Future attack forecast
- Growth percentage
- Trend indication
- Forecast table
- Download forecast as CSV

The current implementation uses **Linear Regression** for forecasting.

> Forecast values are statistical estimates based on historical observations and should not be interpreted as guaranteed future events.

---

## 🧠 6. AI Intelligence Report

The AI Intelligence module generates an analytical intelligence summary from the selected GTD data.

### Key Statistics

The system calculates:

- Total incidents
- Total fatalities
- Total injuries
- Number of countries
- Number of terrorist groups
- Top countries
- Most active terrorist groups
- Most common attack types
- Most frequently used weapon types

### Intelligence Assessment

The dashboard generates a structured assessment based on the calculated statistics.

The report includes:

1. Key intelligence indicators
2. Executive summary
3. Top affected countries
4. Active terrorist groups
5. Common attack types
6. Weapon analysis
7. Threat-level assessment
8. Analytical recommendations

The generated report can be downloaded as a text file.

---

## 📊 7. Data Explorer

The Data Explorer provides an interactive interface for exploring the GTD dataset.

### Filters

Users can filter data by:

- Year
- Country
- Region
- Attack Type
- Weapon Type
- Terrorist Group

### Search

Users can search by:

- City
- Country

### Dashboard Metrics

The system displays:

- Number of incidents
- Number of countries
- Total fatalities
- Total injuries

### Visual Analytics

The Data Explorer provides:

#### Country Analysis

Top 10 countries by number of incidents.

#### Attack Type Analysis

Distribution of different attack types.

#### Weapon Analysis

Distribution of different weapon types.

#### Missing Value Analysis

Displays missing values for dataset columns.

#### Dataset Information

Displays:

- Number of rows
- Number of columns
- Memory usage
- Column names

Filtered data can also be downloaded as CSV.

---

## ⚙️ 8. Dashboard Settings

The Settings module provides configuration options for the dashboard.

### Appearance

- Dashboard Theme
- Dashboard Layout
- Chart Style

### Default Dashboard

- Default Country
- Forecast Years
- Minimum Prediction Confidence

### Global Threat Map

- Map Style
- Marker Clustering
- Heatmap

### Forecasting

Available algorithm options in the interface:

- Linear Regression
- ARIMA
- Prophet

### Machine Learning

Available model options in the interface:

- Random Forest
- Decision Tree
- Gradient Boosting

Additional options include:

- Prediction Probability
- Feature Importance

### Reports

Available report format options:

- PDF
- Word
- Text

Additional options:

- Include Charts
- Include Tables

### Notifications

Options include:

- Attack Alerts
- Forecast Alerts
- Report Notifications

> Some Settings options are currently interface-level configuration choices and are not connected to separate implementations in the current code.

---

# 🏗️ Project Architecture

```text
Military_Intelligence_Dashboard/
│
├── app.py
├── train_attack_model.py
│
├── data/
│   └── globalterrorism.csv
│
├── models/
│   ├── attack_prediction_model.pkl
│   ├── feature_encoders.pkl
│   └── target_encoder.pkl
│
├── pages/
│   ├── 1_🏠 Home.py
│   ├── 2_🌍 Global_Threat_Map.py
│   ├── 4_🤖 Attack_Prediction.py
│   ├── 5_🚨 Threat_Level.py
│   ├── 6_📈 Forecasting.py
│   ├── 7_🧠 AI_Intelligence.py
│   ├── 8_📊 Data_Explorer.py
│   └── 9_⚙ Setting.py
│
├── utils/
│   └── data_loader.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🔄 System Workflow

```text
                ┌─────────────────────────┐
                │ Global Terrorism        │
                │ Database (GTD)           │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Data Loading &           │
                │ Preprocessing            │
                └────────────┬────────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
   Data Explorer       Global Threat Map   ML Pipeline
                                                │
                                    ┌───────────┴───────────┐
                                    │                       │
                                    ▼                       ▼
                              Attack Prediction       Threat Level
                                    │                       │
                                    └───────────┬───────────┘
                                                │
                                                ▼
                                         Forecasting
                                                │
                                                ▼
                                      Intelligence Report
                                                │
                                                ▼
                                      Streamlit Dashboard
```

---

# 🤖 Machine Learning Pipeline

## Attack Prediction Model

The attack prediction model is trained using `train_attack_model.py`.

### Training Process

```text
Load Dataset
     ↓
Select Features
     ↓
Remove Missing Values
     ↓
Encode Categorical Features
     ↓
Encode Target
     ↓
Train/Test Split
     ↓
Random Forest Training
     ↓
Model Evaluation
     ↓
Save Model
```

### Selected Features

```text
country_txt
region_txt
weaptype1_txt
targtype1_txt
gname
success
suicide
nkill
nwound
```

### Target

```text
attacktype1_txt
```

The project uses an **80/20 train-test split** and a Random Forest classifier with **300 estimators**.

---

# 📁 Generated Model Files

After successful model training, the following files are generated:

```text
models/
│
├── attack_prediction_model.pkl
├── feature_encoders.pkl
└── target_encoder.pkl
```

### `attack_prediction_model.pkl`

Contains the trained Random Forest model.

### `feature_encoders.pkl`

Contains the LabelEncoders used for categorical input features.

### `target_encoder.pkl`

Contains the encoder used for converting predicted numerical labels back to attack-type names.

---

# 📊 Dataset

This project is designed to use the:

**Global Terrorism Database (GTD)**

The application expects the dataset at:

```text
data/globalterrorism.csv
```

The project uses fields such as:

```text
iyear
country_txt
region_txt
city
latitude
longitude
attacktype1_txt
weaptype1_txt
targtype1_txt
gname
success
suicide
nkill
nwound
```

The exact column structure should match the GTD CSV version used by the project.

---

# ⚠️ Dataset Important Note

The raw GTD dataset should only be redistributed if its applicable terms and licensing permit redistribution.

For a public GitHub repository, check the dataset's terms before uploading the complete CSV.

If necessary, keep the dataset outside GitHub and add it locally to:

```text
data/globalterrorism.csv
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Streamlit | Interactive web dashboard |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Plotly | Interactive charts and maps |
| Scikit-learn | Machine learning |
| Joblib | Model saving/loading |
| Global Terrorism Database | Historical dataset |

---

# 📦 Installation

## Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Military_Intelligence_Dashboard
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual GitHub repository URL.

---

## Step 2: Create Virtual Environment

### Windows

```powershell
python -m venv venv
```

Activate:

```powershell
venv\Scriptsctivate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

Create a file named:

```text
requirements.txt
```

Add:

```text
streamlit
pandas
numpy
plotly
scikit-learn
joblib
```

Then run:

```bash
pip install -r requirements.txt
```

---

# 📁 Step 4: Add the Dataset

Create the data folder:

```text
data/
```

Place the GTD dataset inside:

```text
data/globalterrorism.csv
```

Verify that the file is a valid CSV file and contains the required columns.

---

# 🧠 Step 5: Train the Machine Learning Model

Run:

```bash
python train_attack_model.py
```

The training script will:

1. Load the dataset
2. Select required features
3. Remove missing values
4. Encode categorical variables
5. Train the Random Forest model
6. Evaluate the model
7. Save the model and encoders

The generated files will be placed inside:

```text
models/
```

---

# ▶️ Step 6: Run the Dashboard

Run the Streamlit application using:

```bash
streamlit run app.py
```

Do **not** start the dashboard using:

```bash
python app.py
```

After starting Streamlit, open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

---

# 🧪 Testing Checklist

## Application

- [ ] Streamlit starts successfully
- [ ] Home page loads
- [ ] Sidebar navigation works
- [ ] All available modules open

## Dataset

- [ ] GTD CSV exists
- [ ] CSV is readable
- [ ] Required columns are present
- [ ] Missing values are handled

## Global Threat Map

- [ ] Map loads correctly
- [ ] Year filter works
- [ ] Geographic points display
- [ ] Hover information works

## Attack Prediction

- [ ] Model files exist
- [ ] Encoders load correctly
- [ ] Input form works
- [ ] Prediction is generated
- [ ] Confidence is displayed

## Threat Level

- [ ] Input fields work
- [ ] Threat level is generated
- [ ] Confidence score appears
- [ ] Probability distribution appears

## Forecasting

- [ ] Country selection works
- [ ] Historical data appears
- [ ] Forecast is generated
- [ ] Forecast chart works
- [ ] CSV download works

## Data Explorer

- [ ] Year filter works
- [ ] Country filter works
- [ ] Region filter works
- [ ] Attack filter works
- [ ] Weapon filter works
- [ ] Group filter works
- [ ] Search works
- [ ] Charts work
- [ ] Download works

## Intelligence Report

- [ ] Statistics load
- [ ] Executive summary appears
- [ ] Intelligence assessment appears
- [ ] Report downloads successfully

---

# ❗ Common Errors

## 1. Pandas ParserError

Example:

```text
pandas.errors.ParserError:
Error tokenizing data.
Expected 4 fields in line 29, saw 5
```

This indicates a problem with the CSV formatting or the file being read.

Check:

```text
data/globalterrorism.csv
```

Make sure it is an actual CSV file and that the rows have a consistent structure.

---

## 2. FileNotFoundError

If you receive:

```text
FileNotFoundError
```

check that the project contains:

```text
Military_Intelligence_Dashboard/
└── data/
    └── globalterrorism.csv
```

Also make sure you are running the command from the project root.

---

## 3. Streamlit ScriptRunContext Warning

If you run:

```bash
python app.py
```

you may see a warning similar to:

```text
missing ScriptRunContext
```

Start the application correctly with:

```bash
streamlit run app.py
```

---

## 4. Model Not Found

If Attack Prediction cannot find:

```text
models/attack_prediction_model.pkl
```

run:

```bash
python train_attack_model.py
```

This should generate:

```text
models/
├── attack_prediction_model.pkl
├── feature_encoders.pkl
└── target_encoder.pkl
```

---

# 🔐 GitHub Security

Do not upload sensitive or unnecessary files.

Recommended `.gitignore`:

```text
# Virtual Environment
venv/
.venv/

# Python
__pycache__/
*.pyc

# Environment Variables
.env

# Dataset
data/*.csv

# Temporary files
*.tmp
*.log
```

If the dataset is not permitted to be redistributed, keeping:

```text
data/*.csv
```

in `.gitignore` prevents accidental upload.

---

# 📈 Future Enhancements

Possible future improvements include:

- Real-time data integration
- Advanced time-series forecasting
- ARIMA implementation
- Prophet implementation
- Model comparison
- Cross-validation
- Hyperparameter tuning
- Explainable AI
- SHAP-based feature importance
- Advanced anomaly detection
- Country-specific analytical dashboards
- SQL database integration
- Authentication
- Role-based access control
- Automated data updates
- Automated model retraining
- PDF intelligence reports
- Interactive dashboards
- Advanced statistical analysis

---

# 🎓 Academic Applications

This project demonstrates practical concepts from:

- Machine Learning
- Data Science
- Data Analytics
- Exploratory Data Analysis
- Predictive Analytics
- Data Visualization
- Python Programming
- Web Application Development
- Geographic Data Visualization
- Statistical Forecasting

It demonstrates how a large historical dataset can be transformed into an interactive analytical platform.

---

# 📚 Project Modules

| Module | Description |
|---|---|
| 🏠 Home | Dashboard overview and key statistics |
| 🌍 Global Threat Map | Geographic visualization of incidents |
| 🤖 Attack Prediction | Random Forest attack-type prediction |
| 🚨 Threat Level | Threat-level classification |
| 📈 Forecasting | Future attack-count estimation |
| 🧠 AI Intelligence | Intelligence summary and assessment |
| 📊 Data Explorer | Filtering, searching, and visualization |
| ⚙️ Settings | Dashboard configuration |

---

# 🔬 Methodology

The overall methodology of the project is:

```text
                 Historical GTD Data
                         │
                         ▼
                 Data Preprocessing
                         │
                         ▼
                  Data Exploration
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
      Visualization   ML Prediction   Forecasting
          │              │              │
          └──────────────┼──────────────┘
                         │
                         ▼
                Intelligence Analysis
                         │
                         ▼
                 Interactive Dashboard
```

---

# 📊 Model Evaluation

The attack prediction training script calculates:

- Accuracy
- Classification Report
- Confusion Matrix

The model evaluation is performed on the test dataset after the train-test split.

The actual accuracy should be obtained by running:

```bash
python train_attack_model.py
```

> The README intentionally does not state a fixed accuracy because the actual value should come from the model run on the specific dataset being used.

---

# ⚠️ Limitations

The current project has several limitations:

1. Predictions depend on the quality of the historical dataset.
2. The attack prediction model does not represent real-time intelligence.
3. Forecasting currently uses Linear Regression.
4. Historical terrorism patterns may not represent future events.
5. Threat-level thresholds are rule-based.
6. Some Settings options are currently UI-level selections rather than fully connected configurations.
7. The project requires a correctly formatted GTD CSV.
8. Predictions may be affected by missing or unseen categorical values.

---

# 🛡️ Responsible Use

This project should be used responsibly.

It is designed for:

- Education
- Academic projects
- Research
- Data analysis
- Machine-learning experimentation
- Visualization

It should **not** be used as a substitute for verified intelligence, professional security analysis, or operational decision-making.

---

# 👩‍💻 Author

**Tanisha Shishir Yadapadithaya**

---

# 📄 License

If you are publishing this project on GitHub, add an appropriate open-source license if required.

For example:

```text
MIT License
```

However, the license of the project code does not automatically apply to third-party datasets.

Check the applicable terms of the Global Terrorism Database before redistributing the dataset.

---

# ⭐ Project Summary

The **Military Intelligence Dashboard** is an interactive Python and Streamlit application that transforms historical terrorism data into meaningful visualizations, machine-learning predictions, threat classifications, forecasts, and intelligence summaries.

### Core Pipeline

```text
GTD Dataset
     ↓
Data Processing
     ↓
Exploratory Analysis
     ↓
Visualization
     ↓
Machine Learning
     ↓
Prediction
     ↓
Forecasting
     ↓
Intelligence Analysis
     ↓
Interactive Dashboard
```

---

## ⭐ If you find this project useful

Give the repository a ⭐ on GitHub.

