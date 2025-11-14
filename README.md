# LoanMitra - Credit Score Prediction Platform

LoanMitra is an AI-powered credit scoring platform that provides transparent, explainable credit assessments for NBFCs and financial institutions.

## Features

- **Credit Score Prediction**: AI-powered credit score calculation (0-900 scale)
- **Explainable AI**: Detailed breakdown of factors affecting the credit score
- **Modern UI**: Beautiful, responsive web interface
- **Fast API**: FastAPI-based REST API for predictions

## Project Structure

```
NBFC/
├── app.py                    # FastAPI backend server
├── credit_score_model.pkl    # Trained ML model
├── model_features.pkl        # Model feature list
├── index.html               # Frontend UI
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Setup Instructions

### 1. Install Dependencies

Create a virtual environment (recommended):

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

### 2. Run the API Server

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

API Documentation (Swagger UI) will be available at:

- `http://localhost:8000/docs`
- `http://localhost:8000/redoc`

### 3. Open the UI

Open `index.html` in your web browser, or serve it using a simple HTTP server:

```bash
# Python 3
python -m http.server 8080

# Then open: http://localhost:8080
```

**Note**: If you serve the HTML on a different port, update the `API_URL` in `index.html` (line 376) to match your FastAPI server URL.

## Usage

1. **Fill in Customer Information**:

   - Enter all the required fields in the form
   - Click "📝 Fill Sample Data" to populate with sample values
   - Fields include credit history, trade lines, UPI transactions, utility bills, etc.

2. **Calculate Credit Score**:

   - Click "Calculate Credit Score" button
   - Wait for the prediction (usually takes a few seconds)

3. **View Results**:
   - See your credit score (0-900 scale)
   - Review detailed breakdown of factors affecting the score
   - Understand which features increased or decreased your score

## API Endpoints

### POST `/predict`

Predict credit score for customer data.

**Request Body:**

```json
{
  "data": {
    "DerogCnt": 0,
    "CollectCnt": 0,
    "BankruptcyInd": 0,
    ...
  }
}
```

**Response:**

```json
{
  "credit_score": 750.25,
  "reasoning": [
    {
      "feature": "UPI_Avg_Expenditure",
      "value": 15000.0,
      "contribution": 45.123,
      "effect": "increase"
    },
    ...
  ]
}
```

### GET `/`

Health check endpoint.

## Model Features

The model uses 23 features:

- **Credit History**: DerogCnt, CollectCnt, BankruptcyInd
- **Inquiries**: InqCnt06, InqTimeLast, InqFinanceCnt24
- **Trade Lines**: TLTimeFirst, TLTimeLast, TL50UtilCnt, TLBalHCPct, TLSatPct
- **Delinquency**: TLDel3060Cnt24, TLDel90Cnt24, TLDel60CntAll, TLDel60Cnt24
- **Open Accounts**: TLOpenPct, TLOpen24Pct
- **Alternative Data**: UPI_Avg_Expenditure, Phone_Payments_AvgPerMonth, Electricity_Bill_AvgPerMonth
- **Microfinance**: Other_Microfinance_Loans_Count, Other_Microfinance_AvgMonthly

## Technologies Used

- **Backend**: FastAPI, Python
- **ML**: scikit-learn, joblib
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Data Processing**: pandas, numpy

## Notes

- The model files (`credit_score_model.pkl` and `model_features.pkl`) must be in the same directory as `app.py`
- CORS is enabled for all origins in development. For production, restrict `allow_origins` in `app.py`
- Default API URL in the UI is `http://localhost:8000`. Update if your server runs on a different address/port

## Troubleshooting

**Issue**: UI cannot connect to API

- **Solution**: Ensure the FastAPI server is running on `http://localhost:8000`
- Check browser console for CORS errors
- Update `API_URL` in `index.html` if using a different server address

**Issue**: Model file not found

- **Solution**: Ensure `credit_score_model.pkl` and `model_features.pkl` are in the project root directory

**Issue**: Import errors

- **Solution**: Make sure all dependencies are installed: `pip install -r requirements.txt`

## License

This project is part of a final year project for credit scoring in NBFCs.
