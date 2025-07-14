# Orange vs Grapefruit Binary Classifier

This repository contains a **binary classifier** project developed in `Python` as part of my **B.Tech 4th Year Computer Science and Engineering** coursework at *Graphic Era University* .

--> The classifier distinguishes between oranges and grapefruits based on a simple, two-feature dataset. The project demonstrates a complete machine learning workflow, from data preprocessing to model evaluation and visualization.  
 ->Sample datasets and code are provided in the repository.

-->  **Note:** The project is implemented in **Python 3.x** and requires standard data science libraries like `numpy`, `pandas`, `scikit-learn`, and `matplotlib`.

##  How to Set Up the Project

```bash
git clone https://github.com/raghavshuklaofficial/Orange-vs-Grapefruit-Binary-Classifier.git
cd Orange-vs-Grapefruit-Binary-Classifier
pip install -r requirements.txt
```

--> This will install all required dependencies for running the code and notebooks.

##  Running the Classifier

You can run the project in two ways:

1. **Jupyter Notebook**  
   Open the notebook in the `notebooks/` folder for a step-by-step demonstration of the classification pipeline.

2. **Python Script**  
   Run the main script in the `src/` folder for a command-line workflow.

##  Project Features

- **Binary Classification**: Differentiates between oranges and grapefruits using measurable features.
- **Simple Dataset**: Uses features like *weight* and *diameter* for easy interpretation.
- **End-to-End Pipeline**: Covers data loading, preprocessing, model training, evaluation, and result visualization.
- **Reproducible Results**: All steps are documented for easy replication.

##  Project Structure

```plaintext
Orange-vs-Grapefruit-Binary-Classifier/
├── data/
│   └── oranges_grapefruits.csv      # Dataset with labeled fruit samples
├── notebooks/
│   └── Orange_vs_Grapefruit_Classifier.ipynb  # Interactive notebook
├── src/
│   └── classifier.py                # Main Python script for training and evaluation
├── README.md                        # Project documentation
└── requirements.txt                 # List of Python dependencies
```

##  Dataset

The dataset contains measurements for both oranges and grapefruits. Each record includes:

- **Color** (red , green , blue i.e. RGB Values)
- **Weight** (in grams)
- **Diameter** (in centimeters)
- **Label** ("orange" or "grapefruit")

The dataset is small and ideal for educational purposes.

## Methods Used

| **Step**                | **Description**                                                                 |
|-------------------------|---------------------------------------------------------------------------------|
| Data Preprocessing      | Cleans and normalizes the dataset                                               |
| Exploratory Analysis    | Visualizes feature distributions and class separation                           |
| Model Selection         | Compares Logistic Regression and Decision Tree classifiers                      |
| Model Evaluation        | Uses accuracy, confusion matrix, and cross-validation for assessment            |


## Future Work

- Experiment with more advanced models or additional features.
- Deploy the classifier as a simple web application for interactive use.
- Extend the dataset to include more fruit types.

## Author

**Raghav Shukla**  
B.Tech 4th Year Computer Science and Engineering Student  
*Graphic Era University*

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
