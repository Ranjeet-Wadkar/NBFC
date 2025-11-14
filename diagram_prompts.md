# LoanMitra - Diagram Generation Prompts

This document contains specific prompts for generating various diagrams for the LoanMitra Credit Scoring Platform project. Copy and paste each prompt into your preferred diagramming tool (draw.io, Lucidchart, PlantUML, Mermaid, etc.) or AI diagram generator.

---

## 1. Data Flow Diagram (DFD) Prompt

**Create a Level 1 Data Flow Diagram (DFD) for LoanMitra - An AI-powered Credit Scoring Platform for NBFCs.**

**System Context:**

- External Entities: Borrower, NBFC/Lender, Identity Verification APIs (PAN/Aadhaar), UPI Payment Gateways, Utility Providers (Electricity, Telecom), Government Databases, Admin/System Administrator

**Main Processes (at Level 1):**

1. **Onboarding & Data Collection Process**

   - Input: User Registration Data, Identity Documents (PAN, Aadhaar)
   - Output: Verified User Profile, Collected Data
   - Data Stores: User Database, Document Repository

2. **Alternative Data Integration Process**

   - Input: UPI Transaction Data, Electricity Bill Data, Phone Payment Data, Microfinance History
   - Output: Aggregated Alternative Data
   - Data Stores: Transaction Database, Consumption Database

3. **Feature Engineering & Preprocessing Process**

   - Input: Raw User Data, Alternative Data, Credit History
   - Output: Engineered Features (23 features including DerogCnt, CollectCnt, UPI_Avg_Expenditure, etc.)
   - Data Stores: Feature Store, Processed Data Warehouse

4. **Credit Scoring Engine Process**

   - Input: Engineered Features (23 features)
   - Output: Credit Score (0-900), Score Reasoning, Feature Contributions
   - Data Stores: Model Repository, Scoring Results Database

5. **Explainability & Transparency Process**

   - Input: Model Predictions, Feature Contributions
   - Output: SHAP Explanations, Score Breakdown, Decision Reasoning
   - Data Stores: Explanation Logs

6. **Decision Intelligence & Risk Classification Process**

   - Input: Credit Score, Risk Thresholds
   - Output: Risk Classification (Low/High Risk × High/Low Need), Loan Decision, Recommendations
   - Data Stores: Decision Logs, Risk Database

7. **Dashboard & Visualization Process**
   - Input: Scores, Decisions, Analytics Data
   - Output: Admin Dashboard, User Dashboard, Reports, Visualizations
   - Data Stores: Analytics Database

**Data Flows:**

- User Registration → Onboarding Process
- Identity Documents → Identity Verification APIs → Onboarding Process
- UPI/Utility Data → Alternative Data Integration
- Raw Data → Feature Engineering → Credit Scoring Engine
- Score Results → Explainability Process → Decision Intelligence
- Decisions → Dashboard Visualization
- All processes should show data flows to/from respective data stores

**Security Flows:**

- AES-256 encryption for data at rest
- SSL/TLS for data in transit
- API authentication tokens
- Audit logs for compliance

---

## 2. Activity Diagram Prompt

**Create an Activity Diagram for LoanMitra Credit Scoring Workflow - From Borrower Onboarding to Loan Decision.**

**Main Swimlanes:** Borrower, System, Credit Scoring Engine, Decision Intelligence, Admin/NBFC

**Activities (in sequence):**

1. **Initial Node → Borrower Registration**

   - Borrower initiates registration via Dashboard or IVR

2. **Identity Verification Activity**

   - System: Request PAN/Aadhaar verification
   - External API: Verify identity
   - Decision: Identity Verified? (Yes/No)
     - If No: Reject and send rejection message
     - If Yes: Continue

3. **Data Collection Activity**

   - Borrower: Upload documents (Income proofs, Bank statements)
   - System: Collect alternative data:
     - Connect UPI payment APIs
     - Fetch electricity bill data
     - Get phone payment history
     - Retrieve microfinance loan history
   - System: Request credit bureau data (if available)

4. **Data Preprocessing Activity**

   - System: Clean and normalize data
   - System: Handle missing values (imputation)
   - System: Feature engineering:
     - Calculate DerogCnt, CollectCnt
     - Compute repayment-to-income ratios
     - Extract transaction patterns
     - Derive 23 model features

5. **Credit Score Calculation Activity**

   - Credit Scoring Engine: Load trained Logistic Regression model
   - Credit Scoring Engine: Input 23 features to model
   - Credit Scoring Engine: Calculate probability
   - Credit Scoring Engine: Compute CBCS score (0-900)
   - Credit Scoring Engine: Generate feature contributions and reasoning

6. **Explainability Generation Activity**

   - System: Calculate SHAP values
   - System: Generate score breakdown
   - System: Identify top contributing features

7. **Risk Classification Activity**

   - Decision Intelligence: Receive credit score
   - Decision Intelligence: Classify into risk bands:
     - Low Risk + High Need
     - Low Risk + Low Need
     - High Risk + High Need
     - High Risk + Low Need

8. **Decision Making Activity**

   - Decision Node: Risk Level?
     - If Low Risk: Auto-approve loan
     - If Medium Risk: Route to AI-assisted review or Manual review
     - If High Risk: Defer with financial literacy recommendations

9. **Notification & Dashboard Update Activity**

   - System: Update borrower dashboard with:
     - Credit score
     - Score breakdown
     - Decision status
     - Recommendations
   - System: Update admin dashboard with analytics

10. **Final Node** - Process complete

**Parallel Activities:**

- Data collection can happen in parallel (UPI, Electricity, Phone payments)
- Score calculation and explainability can run simultaneously

**Exception Handling:**

- API failures → Retry mechanism or use cached data
- Model errors → Fallback to manual review
- Data quality issues → Request additional verification

---

## 3. Project Flow Diagram Prompt

**Create a Project Flow Diagram showing the end-to-end flow of LoanMitra Credit Scoring Platform.**

**Flow Stages:**

**Stage 1: User Onboarding & Registration**

- Borrower accesses platform (Web Dashboard or IVR)
- Registration form with personal details
- Multi-language support for rural users
- → Output: Registered User Account

**Stage 2: Identity & Document Verification**

- Upload PAN/Aadhaar documents
- API integration with government verification services
- Document validation
- → Output: Verified Identity

**Stage 3: Multi-Source Data Collection**

- **Branch A:** Traditional Credit Data
  - Credit bureau reports (if available)
  - Bank statements
  - Income documents
- **Branch B:** Alternative Data Sources
  - UPI transaction APIs → UPI_Avg_Expenditure
  - Electricity provider APIs → Electricity_Bill_AvgPerMonth
  - Telecom provider APIs → Phone_Payments_AvgPerMonth
  - Microfinance databases → Other_Microfinance_Loans_Count, Other_Microfinance_AvgMonthly
- **Branch C:** Behavioral Data
  - Transaction frequency
  - Payment patterns
  - Consumption regularity
- → Output: Comprehensive Data Profile

**Stage 4: Data Preprocessing & Feature Engineering**

- Data cleaning and normalization
- Missing value imputation
- Feature extraction:
  - Credit history features (DerogCnt, CollectCnt, BankruptcyInd)
  - Inquiry features (InqCnt06, InqTimeLast, InqFinanceCnt24)
  - Trade line features (TLTimeFirst, TLTimeLast, TL50UtilCnt, etc.)
  - Delinquency features (TLDel3060Cnt24, TLDel90Cnt24, etc.)
  - Alternative data features (UPI, Phone, Electricity)
- → Output: 23 Engineered Features

**Stage 5: ML Model Scoring**

- Load trained Logistic Regression model (credit_score_model.pkl)
- Input 23 features
- Model inference:
  - Calculate probability of default
  - Compute Composite Beneficiary Credit Score (CBCS) = (1 - prob_default) × 900
  - Generate feature contributions using model coefficients
- → Output: Credit Score (0-900), Feature Contributions, Reasoning

**Stage 6: Explainability & Transparency**

- SHAP value calculation (if implemented)
- Feature contribution analysis
- Score breakdown generation
- Top contributors identification
- → Output: Explainable Score Report

**Stage 7: Risk Assessment & Classification**

- Score interpretation:
  - Excellent: 720-900
  - Good: 650-719
  - Fair: 580-649
  - Poor: 0-579
- Risk band classification:
  - Low Risk + High Need
  - Low Risk + Low Need
  - High Risk + High Need
  - High Risk + Low Need
- → Output: Risk Classification

**Stage 8: Automated Decision Intelligence**

- Decision logic:
  - If Low Risk (Score ≥ 650): Instant Approval
  - If Medium Risk (580-649): AI-Assisted Review → Manual Review (if needed)
  - If High Risk (< 580): Defer with Financial Literacy Program
- → Output: Loan Decision, Approval/Rejection, Recommendations

**Stage 9: Dashboard Visualization & Reporting**

- **Borrower Dashboard:**
  - Credit score display
  - Score breakdown visualization
  - Feature impact chart
  - Decision status
  - Improvement recommendations
- **Admin/NBFC Dashboard:**
  - Portfolio analytics
  - Risk segmentation charts
  - SHAP visualizations
  - Performance metrics
  - Compliance reports
- → Output: Interactive Dashboards

**Stage 10: Feedback Loop & Model Retraining**

- Collect loan performance data
- Track repayment behavior
- Update model with new data
- Continuous improvement
- → Feedback to Stage 5 (ML Model)

**Security & Compliance Layer (across all stages):**

- AES-256 encryption
- API authentication
- Audit logging
- RBI compliance
- GDPR compliance
- Data localization

---

## 4. UML Class Diagram Prompt

**Create a UML Class Diagram for LoanMitra Credit Scoring Platform showing the system's class structure and relationships.**

**Main Classes:**

1. **User (Abstract Class)**

   - Attributes: userId, name, email, phoneNumber, registrationDate, language
   - Methods: login(), logout(), viewDashboard()

2. **Borrower (extends User)**

   - Attributes: panNumber, aadhaarNumber, income, address, verificationStatus
   - Methods: submitApplication(), uploadDocuments(), viewCreditScore()

3. **Admin (extends User)**

   - Attributes: adminId, role, permissions
   - Methods: viewAnalytics(), manageUsers(), configureModel()

4. **NBFC (extends User)**

   - Attributes: nbfcId, companyName, licenseNumber
   - Methods: viewPortfolio(), generateReports(), approveLoan()

5. **Application**

   - Attributes: applicationId, borrowerId, applicationDate, status
   - Methods: submit(), getStatus(), updateStatus()

6. **Document**

   - Attributes: documentId, borrowerId, documentType, filePath, uploadDate, verificationStatus
   - Methods: upload(), verify(), download()

7. **IdentityVerificationService**

   - Attributes: apiKey, endpoint
   - Methods: verifyPAN(), verifyAadhaar(), validateDocuments()

8. **AlternativeDataCollector**

   - Attributes: upiApiKey, utilityApiEndpoint
   - Methods: fetchUPIData(), fetchElectricityData(), fetchPhonePaymentData(), fetchMicrofinanceData()

9. **DataPreprocessor**

   - Attributes: preprocessingConfig
   - Methods: cleanData(), normalizeData(), imputeMissingValues(), extractFeatures()

10. **FeatureEngineer**

    - Attributes: featureList (23 features)
    - Methods: calculateDerogCnt(), calculateUPIAvgExpenditure(), engineerFeatures(), getFeatureList()

11. **CreditScoringModel**

    - Attributes: modelPath, modelType (LogisticRegression), features (list of 23)
    - Methods: loadModel(), predict(), predictProba(), getCoefficients(), getFeatureContributions()

12. **CreditScore**

    - Attributes: scoreId, borrowerId, scoreValue (0-900), calculationDate, features, contributions
    - Methods: calculateScore(), getReasoning(), getBreakdown()

13. **ExplainabilityEngine**

    - Attributes: shapEnabled
    - Methods: calculateSHAP(), generateExplanation(), getTopContributors()

14. **RiskClassifier**

    - Attributes: riskThresholds (580, 650, 720)
    - Methods: classifyRisk(), getRiskBand(), getRecommendations()

15. **DecisionEngine**

    - Attributes: decisionRules, autoApproveThreshold
    - Methods: makeDecision(), approveLoan(), rejectLoan(), recommendReview()

16. **Dashboard**

    - Attributes: dashboardType (Borrower/Admin), userId
    - Methods: displayScore(), showAnalytics(), generateVisualizations(), exportReport()

17. **Loan**

    - Attributes: loanId, borrowerId, amount, interestRate, tenure, status, approvalDate
    - Methods: create(), updateStatus(), calculateEMI()

18. **AuditLog**
    - Attributes: logId, userId, action, timestamp, ipAddress
    - Methods: logEvent(), retrieveLogs(), generateAuditReport()

**Relationships:**

- User (1) ──< (0..\*) Application
- Borrower (1) ──< (0..\*) Document
- Application (1) ── (1) CreditScore
- CreditScoringModel (1) ── (1) CreditScore (calculates)
- CreditScore (1) ── (1) RiskClassifier (uses)
- RiskClassifier (1) ── (1) DecisionEngine (informs)
- DecisionEngine (1) ── (0..1) Loan (creates)
- Borrower (1) ── (0..\*) Loan
- DataPreprocessor (1) ── (1) FeatureEngineer (uses)
- FeatureEngineer (1) ── (1) CreditScoringModel (provides features)
- ExplainabilityEngine (1) ── (1) CreditScore (explains)
- Dashboard (1) ── (0..\*) User (displays for)
- All entities ── (0..\*) AuditLog (logged in)

**Design Patterns:**

- Strategy Pattern: Different scoring strategies
- Factory Pattern: Model loading
- Observer Pattern: Dashboard updates
- Repository Pattern: Data access

---

## 5. ER Diagram (Entity Relationship Diagram) Prompt

**Create an Entity Relationship Diagram (ERD) for LoanMitra Credit Scoring Platform database schema.**

**Entities and Attributes:**

1. **Users**

   - Primary Key: user_id (INT, PK)
   - user_type (ENUM: 'Borrower', 'Admin', 'NBFC')
   - name (VARCHAR)
   - email (VARCHAR, UNIQUE)
   - phone_number (VARCHAR)
   - registration_date (DATETIME)
   - language_preference (VARCHAR)
   - status (ENUM: 'Active', 'Inactive')

2. **Borrowers**

   - Primary Key: borrower_id (INT, PK, FK → Users.user_id)
   - pan_number (VARCHAR, UNIQUE)
   - aadhaar_number (VARCHAR, UNIQUE)
   - income (DECIMAL)
   - address (TEXT)
   - identity_verification_status (ENUM: 'Pending', 'Verified', 'Rejected')
   - verification_date (DATETIME)

3. **Applications**

   - Primary Key: application_id (INT, PK)
   - Foreign Key: borrower_id (INT, FK → Borrowers.borrower_id)
   - application_date (DATETIME)
   - status (ENUM: 'Pending', 'Under Review', 'Approved', 'Rejected')
   - loan_amount_requested (DECIMAL)

4. **Documents**

   - Primary Key: document_id (INT, PK)
   - Foreign Key: borrower_id (INT, FK → Borrowers.borrower_id)
   - document_type (ENUM: 'PAN', 'Aadhaar', 'Income Proof', 'Bank Statement')
   - file_path (VARCHAR)
   - upload_date (DATETIME)
   - verification_status (ENUM: 'Pending', 'Verified', 'Rejected')

5. **Alternative_Data**

   - Primary Key: data_id (INT, PK)
   - Foreign Key: borrower_id (INT, FK → Borrowers.borrower_id)
   - data_source (ENUM: 'UPI', 'Electricity', 'Phone', 'Microfinance')
   - data_period_start (DATE)
   - data_period_end (DATE)
   - upi_avg_expenditure (DECIMAL, nullable)
   - phone_payments_avg_per_month (DECIMAL, nullable)
   - electricity_bill_avg_per_month (DECIMAL, nullable)
   - other_microfinance_loans_count (INT, nullable)
   - other_microfinance_avg_monthly (DECIMAL, nullable)
   - collection_date (DATETIME)

6. **Credit_History**

   - Primary Key: history_id (INT, PK)
   - Foreign Key: borrower_id (INT, FK → Borrowers.borrower_id)
   - derog_cnt (INT)
   - collect_cnt (INT)
   - bankruptcy_ind (BOOLEAN)
   - inq_cnt_06 (INT)
   - inq_time_last (INT)
   - inq_finance_cnt_24 (INT)
   - tl_time_first (INT)
   - tl_time_last (INT)
   - tl_50_util_cnt (INT)
   - tl_bal_hc_pct (DECIMAL)
   - tl_sat_pct (DECIMAL)
   - tl_del_3060_cnt_24 (INT)
   - tl_del_90_cnt_24 (INT)
   - tl_del_60_cnt_all (INT)
   - tl_open_pct (DECIMAL)
   - tl_bad_derog_cnt (INT)
   - tl_del_60_cnt_24 (INT)
   - tl_open_24_pct (DECIMAL)
   - last_updated (DATETIME)

7. **Feature_Engineered_Data**

   - Primary Key: feature_id (INT, PK)
   - Foreign Key: borrower_id (INT, FK → Borrowers.borrower_id)
   - Foreign Key: application_id (INT, FK → Applications.application_id, nullable)
   - All 23 features as columns (matching model_features.pkl)
   - engineering_date (DATETIME)

8. **Credit_Scores**

   - Primary Key: score_id (INT, PK)
   - Foreign Key: borrower_id (INT, FK → Borrowers.borrower_id)
   - Foreign Key: application_id (INT, FK → Applications.application_id, nullable)
   - score_value (DECIMAL, 0-900)
   - score_rating (ENUM: 'Excellent', 'Good', 'Fair', 'Poor')
   - calculation_date (DATETIME)
   - model_version (VARCHAR)

9. **Score_Reasoning**

   - Primary Key: reasoning_id (INT, PK)
   - Foreign Key: score_id (INT, FK → Credit_Scores.score_id)
   - feature_name (VARCHAR)
   - feature_value (DECIMAL)
   - contribution (DECIMAL)
   - effect (ENUM: 'increase', 'decrease')
   - rank (INT) -- ranking by absolute contribution

10. **Risk_Classifications**

    - Primary Key: risk_id (INT, PK)
    - Foreign Key: score_id (INT, FK → Credit_Scores.score_id)
    - risk_level (ENUM: 'Low', 'High')
    - need_level (ENUM: 'High', 'Low')
    - risk_band (VARCHAR) -- combination like "Low Risk - High Need"

11. **Loan_Decisions**

    - Primary Key: decision_id (INT, PK)
    - Foreign Key: application_id (INT, FK → Applications.application_id)
    - Foreign Key: score_id (INT, FK → Credit_Scores.score_id)
    - Foreign Key: risk_id (INT, FK → Risk_Classifications.risk_id)
    - decision_type (ENUM: 'Auto-Approved', 'AI-Reviewed', 'Manual Review', 'Deferred')
    - decision_status (ENUM: 'Approved', 'Rejected', 'Pending', 'Deferred')
    - decision_date (DATETIME)
    - decision_reason (TEXT)
    - reviewer_id (INT, FK → Users.user_id, nullable)

12. **Loans**

    - Primary Key: loan_id (INT, PK)
    - Foreign Key: application_id (INT, FK → Applications.application_id)
    - Foreign Key: borrower_id (INT, FK → Borrowers.borrower_id)
    - loan_amount (DECIMAL)
    - interest_rate (DECIMAL)
    - tenure_months (INT)
    - emi_amount (DECIMAL)
    - disbursement_date (DATETIME)
    - status (ENUM: 'Active', 'Closed', 'Defaulted')

13. **Audit_Logs**

    - Primary Key: log_id (INT, PK)
    - Foreign Key: user_id (INT, FK → Users.user_id, nullable)
    - action_type (VARCHAR)
    - action_description (TEXT)
    - ip_address (VARCHAR)
    - timestamp (DATETIME)
    - affected_entity_type (VARCHAR)
    - affected_entity_id (INT)

14. **Model_Versions**
    - Primary Key: version_id (INT, PK)
    - model_version (VARCHAR, UNIQUE)
    - model_path (VARCHAR)
    - training_date (DATETIME)
    - accuracy_metrics (JSON)
    - features_list (JSON) -- list of 23 features

**Relationships:**

- Users (1) ──< (0..1) Borrowers (one-to-one, user_type = 'Borrower')
- Users (1) ──< (0..\*) Audit_Logs (one-to-many)
- Borrowers (1) ──< (0..\*) Applications (one-to-many)
- Borrowers (1) ──< (0..\*) Documents (one-to-many)
- Borrowers (1) ──< (0..\*) Alternative_Data (one-to-many)
- Borrowers (1) ──< (0..1) Credit_History (one-to-one)
- Borrowers (1) ──< (0..\*) Feature_Engineered_Data (one-to-many)
- Borrowers (1) ──< (0..\*) Credit_Scores (one-to-many)
- Applications (1) ──< (0..\*) Feature_Engineered_Data (one-to-many, nullable)
- Applications (1) ──< (0..1) Credit_Scores (one-to-one, nullable)
- Applications (1) ──< (0..1) Loan_Decisions (one-to-one)
- Applications (1) ──< (0..1) Loans (one-to-one, nullable)
- Credit_Scores (1) ──< (0..\*) Score_Reasoning (one-to-many)
- Credit_Scores (1) ──< (0..1) Risk_Classifications (one-to-one)
- Credit_Scores (1) ──< (0..1) Loan_Decisions (one-to-one)

**Indexes:**

- Users.email (UNIQUE INDEX)
- Borrowers.pan_number (UNIQUE INDEX)
- Borrowers.aadhaar_number (UNIQUE INDEX)
- Credit_Scores.calculation_date (INDEX)
- Audit_Logs.timestamp (INDEX)

---

## 6. Use Case Diagram Prompt

**Create a Use Case Diagram for LoanMitra Credit Scoring Platform showing all actors and their use cases.**

**Actors:**

1. **Borrower** (Primary Actor)
2. **NBFC/Lender** (Primary Actor)
3. **System Administrator** (Primary Actor)
4. **Identity Verification API** (Secondary Actor - External System)
5. **UPI Payment Gateway** (Secondary Actor - External System)
6. **Utility Provider APIs** (Secondary Actor - External System)
7. **Microfinance Database** (Secondary Actor - External System)
8. **Credit Bureau** (Secondary Actor - External System, optional)

**Borrower Use Cases:**

1. **Register Account**

   - Precondition: Borrower has internet access or phone for IVR
   - Postcondition: Account created, verification email sent

2. **Login to Dashboard**

   - Precondition: Borrower has registered account
   - Postcondition: Borrower logged into system

3. **Submit Loan Application**

   - Precondition: Borrower is logged in and verified
   - Postcondition: Application submitted for processing

4. **Upload Documents**

   - Includes: Upload PAN, Upload Aadhaar, Upload Income Proof, Upload Bank Statements
   - Precondition: Borrower is logged in
   - Postcondition: Documents uploaded and queued for verification

5. **Link UPI Account**

   - Precondition: Borrower has UPI account
   - Postcondition: UPI transaction data accessible

6. **Provide Alternative Data Access**

   - Includes: Authorize Electricity Bill Access, Authorize Phone Payment Access, Provide Microfinance History
   - Precondition: Borrower wants to improve credit score
   - Postcondition: Alternative data sources connected

7. **View Credit Score**

   - Precondition: Credit score has been calculated
   - Postcondition: Borrower views score and breakdown

8. **View Score Breakdown & Reasoning**

   - Includes: View Feature Contributions, View Top Impact Factors
   - Precondition: Credit score exists
   - Postcondition: Detailed explanation displayed

9. **View Loan Decision Status**

   - Precondition: Application submitted
   - Postcondition: Current status displayed

10. **View Recommendations**

    - Precondition: Score calculated
    - Postcondition: Improvement suggestions displayed

11. **Contact Support via IVR**
    - Precondition: Borrower has phone access
    - Postcondition: Support request initiated

**NBFC/Lender Use Cases:**

12. **Login to Admin Dashboard**

    - Precondition: NBFC account exists
    - Postcondition: Access to lender dashboard

13. **View Portfolio Analytics**

    - Includes: View Risk Segmentation, View Portfolio Health Metrics
    - Precondition: NBFC is logged in
    - Postcondition: Analytics dashboard displayed

14. **View Borrower Applications**

    - Precondition: NBFC is logged in
    - Postcondition: List of applications displayed

15. **Review Loan Application**

    - Precondition: Application exists and requires review
    - Postcondition: Application reviewed, decision made

16. **Approve/Reject Loan Manually**

    - Precondition: Application in review status
    - Postcondition: Loan approved or rejected

17. **View Credit Score Details**

    - Precondition: Score exists for borrower
    - Postcondition: Score details and reasoning displayed

18. **Generate Reports**

    - Includes: Generate Portfolio Report, Generate Compliance Report, Export Analytics
    - Precondition: NBFC is logged in
    - Postcondition: Reports generated and downloadable

19. **View SHAP Visualizations**

    - Precondition: Model explainability enabled
    - Postcondition: Feature importance visualizations displayed

20. **Configure Risk Thresholds**

    - Precondition: Admin privileges
    - Postcondition: Risk thresholds updated

21. **View Audit Logs**
    - Precondition: Admin privileges
    - Postcondition: Audit trail displayed

**System Administrator Use Cases:**

22. **Manage Users**

    - Includes: Create User, Deactivate User, Reset Password
    - Precondition: Admin logged in
    - Postcondition: User management actions completed

23. **Configure ML Model**

    - Includes: Upload New Model, Update Feature List, Test Model
    - Precondition: Admin privileges
    - Postcondition: Model configuration updated

24. **Monitor System Health**

    - Includes: View System Metrics, Check API Status, Monitor Database
    - Precondition: Admin logged in
    - Postcondition: System status displayed

25. **Manage Data Sources**

    - Includes: Configure API Integrations, Update Data Collection Rules
    - Precondition: Admin privileges
    - Postcondition: Data source configuration updated

26. **View System Analytics**
    - Precondition: Admin logged in
    - Postcondition: System performance metrics displayed

**External System Use Cases (by System):**

27. **Verify Identity** (Identity Verification API)

    - Triggered by: System during onboarding
    - Postcondition: Identity verification result returned

28. **Fetch UPI Transactions** (UPI Payment Gateway)

    - Triggered by: System after borrower authorization
    - Postcondition: UPI transaction data retrieved

29. **Fetch Utility Data** (Utility Provider APIs)

    - Triggered by: System after borrower authorization
    - Postcondition: Electricity/Phone payment data retrieved

30. **Fetch Microfinance History** (Microfinance Database)
    - Triggered by: System during data collection
    - Postcondition: Microfinance loan history retrieved

**Common/System Use Cases:**

31. **Calculate Credit Score**

    - Actors: System (automatic)
    - Precondition: Required data collected and features engineered
    - Postcondition: Credit score calculated and stored

32. **Engineer Features**

    - Actors: System (automatic)
    - Precondition: Raw data available
    - Postcondition: 23 features generated

33. **Classify Risk**

    - Actors: System (automatic)
    - Precondition: Credit score calculated
    - Postcondition: Risk classification assigned

34. **Make Automated Decision**

    - Actors: System (automatic)
    - Precondition: Risk classified
    - Postcondition: Initial decision made (approve/review/defer)

35. **Generate Explanations**
    - Actors: System (automatic)
    - Precondition: Score calculated
    - Postcondition: Score reasoning generated

**Relationships:**

- Borrower <<extends>> User (generalization)
- NBFC <<extends>> User (generalization)
- Upload Documents <<includes>> Verify Documents (include relationship)
- View Credit Score <<includes>> Generate Explanations (include relationship)
- Calculate Credit Score <<includes>> Engineer Features (include relationship)
- Submit Loan Application <<extends>> Upload Documents (extend relationship - optional)

**System Boundaries:**

- Draw a rectangle labeled "LoanMitra Credit Scoring System"
- All use cases (except external system use cases) should be inside this boundary
- External actors outside the boundary

---

## Usage Instructions

1. **For DFD**: Use these prompts with tools like draw.io, Lucidchart, or Visio. Focus on data flows between processes and external entities.

2. **For Activity Diagram**: Use UML-compliant tools like PlantUML, StarUML, or draw.io. Follow the swimlane structure and decision nodes.

3. **For Project Flow**: Can be created as a flowchart in any tool. Show sequential stages with branching where data collection happens in parallel.

4. **For UML Class Diagram**: Use standard UML tools. Focus on class attributes, methods, and relationships (inheritance, composition, aggregation).

5. **For ER Diagram**: Use database design tools like dbdiagram.io, MySQL Workbench, or draw.io. Include all relationships with cardinalities.

6. **For Use Case Diagram**: Use UML tools. Show actors as stick figures, use cases as ovals, and clearly define system boundaries.

**Tips:**

- Customize prompts based on specific requirements
- Add more detail for lower-level diagrams (DFD Level 2, etc.)
- Include security and compliance aspects where relevant
- Consider adding sequence diagrams for complex interactions
