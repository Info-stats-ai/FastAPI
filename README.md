# 🏥 Health Insurance Premium Prediction API

> A full-stack machine learning application that predicts health insurance premium categories using FastAPI backend and Streamlit frontend.

---

## ✨ Features

- **🤖 ML-Powered Predictions** - Uses trained scikit-learn model for accurate predictions
- **📊 Interactive Frontend** - Beautiful Streamlit UI with real-time BMI calculation
- **🔒 Data Validation** - Pydantic models ensure robust input validation
- **⚡ Fast API** - RESTful endpoints with automatic documentation
- **🎯 Auto Calculations** - BMI, lifestyle risk, age groups, and city tiers computed automatically

---

## 📋 Prerequisites

- Python 3.8+
- pip package manager

---

## 🚀 Quick Start

### Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

**Step 1: Start Backend (Terminal 1)**
```bash
uvicorn app:app --reload
```
🌐 Backend: http://localhost:8000

**Step 2: Start Frontend (Terminal 2)**
```bash
streamlit run frontend.py
```
🌐 Frontend: http://localhost:8501

> ⚠️ **Note:** Both servers must run simultaneously for the application to work.

---

## 📖 Usage

### Using Streamlit Frontend (Recommended)

1. Fill in the form in the left sidebar:
   - Age, Weight, Height, Income
   - Smoker status, City, Occupation

2. View calculated metrics:
   - BMI with health status indicators
   - Summary of all inputs

3. Click **"🔮 Predict Premium Category"** button

4. View prediction result

### Using API Directly

**Interactive Documentation:** http://localhost:8000/docs

**POST** `/predict`

```json
{
  "age": 30,
  "weight": 70.0,
  "height": 1.75,
  "income_lpa": 10.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Response:**
```json
{
  "predicted_category": "premium_category"
}
```

---

## 📁 Project Structure

```
FastAPI/
├── app.py              # FastAPI backend
├── frontend.py         # Streamlit frontend
├── model.pkl           # Trained ML model (required)
├── requirements.txt    # Dependencies
└── README.md          # This file
```

---

## 🔧 Input Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `age` | integer | Age (1-100 years) | 30 |
| `weight` | float | Weight in kg | 70.0 |
| `height` | float | Height in meters | 1.75 |
| `income_lpa` | float | Annual income in lakhs | 10.0 |
| `smoker` | boolean | Smoker status | false |
| `city` | string | City name | "Mumbai" |
| `occupation` | string | Job type | "private_job" |

**Occupation Options:**
`retired`, `freelancer`, `goverment_job`, `student`, `business_owner`, `private_job`, `unemployed`

---

## 🎯 Computed Fields

Automatically calculated from inputs:

- **BMI** - Body Mass Index (weight / height²)
- **Lifestyle Risk** - `high`, `medium`, or `low`
- **Age Group** - `young`, `adult`, `middle aged`, or `senior`
- **City Tier** - `1`, `2`, or `3`

---

## 📦 Dependencies

- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `pydantic` - Data validation
- `pandas` - Data manipulation
- `scikit-learn==1.6.1` - ML library
- `numpy` - Numerical computing
- `streamlit` - Frontend framework
- `requests` - HTTP library

---

## ⚠️ Troubleshooting

| Error | Solution |
|-------|----------|
| **Connection Error** | Ensure backend is running on port 8000 |
| **Module Error** | Run `pip install -r requirements.txt` |
| **Version Error** | Use `scikit-learn==1.6.1` |
| **Port in Use** | Use `--port` flag to change port |

---

## 📝 Important Notes

- ⚠️ Model requires `scikit-learn==1.6.1` for compatibility
- 📄 `model.pkl` file must be in project directory
- 📚 API docs available at http://localhost:8000/docs
- 🔄 Both servers must run simultaneously

---

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

---

**Made with ❤️ using FastAPI and Streamlit**
