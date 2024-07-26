# Car price forecast 🚗

Watch the video review: https://github.com/touge13/CarPricePrediction/blob/main/videoReview.mp4

This project focuses on predicting car prices using a machine learning model. The data set contains various characteristics associated with cars such as make, mileage, engine size, etc. The purpose of the model is to determine the estimated selling price based on these characteristics.

## Project structure

– **Data cleaning and preparation**. The data set is cleaned by removing unnecessary columns, handling missing values, and coding categorical variables.
- **Model Training**: A linear regression model is trained on a cleaned dataset to predict car prices.
- **Web Application**: A simple web application has been developed to interact with the model and predict prices based on user data.

## Dependencies

The project uses the following Python libraries:

- pandas
- scikit-learn
- pickle
- streamlit

## Data set

This project uses the Cardetails.csv dataset, which contains various vehicle attributes. Here's a quick overview of the speakers:

- `name`: car make and model.
- “year”: year of manufacture.
- `km_driven`: number of kilometers driven.
- “fuel”: the type of fuel used.
- `seller_type`: seller type (e.g. dealer, individual).
- `transmission`: type of gearbox (manual or automatic).
- `owner`: number of previous owners.
- “mileage”: fuel consumption.
- `engine`: engine size.
- `max_power`: amount of horsepower.
- `seats`: number of seats.
- `selling_price`: car selling price (target variable).

## Data preprocessing

1. **Remove unnecessary columns**. Columns that do not significantly affect price, such as "torque", are removed.
2. **Missing Value Handling**: Rows with missing values ​​are removed.
3. **Remove Duplicates**: Duplicate rows are removed.
4. **Coding categorical variables**. Categorical variables are encoded into numeric values ​​for model training.

## Model training

The linear regression model is trained using the 'scikit-learn' library. The data set is divided into training and test sets with a split of 80-20. The model is then adapted to the training data.

## Web application

The project includes a simple web application running using 'streamlit' that provides an interface for users to enter vehicle data and get a predicted price. The application uses a pre-trained model saved as model.pkl.

## Usage

To use this project, follow these steps:

1. Clone the repository and go to the project directory.
2. Install the required dependencies using `pip3 install numpy pandas sickit-learn pickle streamlit`.
3. Use the web application using `streamlit run app.py`.
