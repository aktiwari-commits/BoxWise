
# BoxWise – Smart Shipping Box Recommendation System

## 1. Project Overview

BoxWise is a Django-based smart shipping box recommendation system designed to identify the most cost-effective shipping box for customer orders.

The system evaluates product dimensions, product weight, box dimensions, and maximum box weight capacity to recommend a suitable shipping box.

## 2. Key Features

- Product management
- Shipping box management
- Customer order management
- Multiple products and quantities per order
- Product rotation and orientation checking
- Product overlap detection
- Weight capacity validation
- Automatic shipping box recommendation
- Box cost comparison
- Cheapest suitable box selection
- Automated testing

## 3. Technology Stack

- Python
- Django
- HTML
- CSS
- JavaScript (if used in the interface)
- Database configured in Django settings

## 4. How the Recommendation Algorithm Works

The recommendation algorithm follows these steps:

1. Retrieves products associated with an order.
2. Calculates the total order weight.
3. Retrieves available shipping boxes.
4. Sorts shipping boxes by cost.
5. Checks whether the order weight exceeds box capacity.
6. Generates possible product orientations.
7. Checks product dimensions against box dimensions.
8. Checks whether products overlap.
9. Identifies suitable shipping boxes.
10. Recommends the cheapest feasible box.

## 5. Project Structure

```text
BoxWise/
│
├── boxes/
├── products/
├── orders/
├── recommendations/
│   ├── services.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── config/
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── README.md
└── TEST_OUTPUT.txt
```

## 6. Installation and Setup

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the project

```bash
cd BoxWise
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the environment (Windows CMD)

```cmd
venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Apply migrations

```bash
python manage.py migrate
```

### Step 7: Run the development server

```bash
python manage.py runserver
```

Open your browser:

http://127.0.0.1:8000/

## 7. Running Automated Tests

Run the recommendation application tests:

```bash
python manage.py test recommendations
```

The project currently has seven automated tests covering recommendation logic, weight capacity, product rotation, overlapping products, oversized products, and empty orders.

## 8. Test Results

All seven recommendation tests passed during development.

See `TEST_OUTPUT.txt` for the captured test execution output.

## 9. Future Improvements

- Advanced 3D packing optimization
- Multiple-box recommendations
- Shipping cost estimation
- Improved packing efficiency
- Order tracking integration

## 10. Author

Ashutosh Tiwari

Developed as a Python/Django development assignment.
