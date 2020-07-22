# annotation_tool
Annotation tool for named entities with ~active learning~ Not yet :(

## Requirements:
- Flask (>= 1.1.2)
- sklearn_crfsuite (>= 0.3)
- pandas (>= 1.0.5)
- joblib (>= 0.15.1)

## Know this before running:
- Unlabeled sentences should be in a .csv file named "unlabeled.csv" inside the data folder. One sentence as a string per cell as in the example.
- As sentences are labeled they will be saved in the labeled.csv file (labels will follow the IOB2 notation)

## To run:
- execute "python app.py"
