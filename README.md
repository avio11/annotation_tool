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
- Open internet browser and type "127.0.0.1/5000" to start annotations

### commands
- Select entities and use number keys (0-9) to change entity class.
- Press key "E" to remove entity class (assigns "O" class to selected words)
- Press load next button to load next sentence to be annotated
- Press Retrieve labels to finish labeling of a sentence (And then press load next sentence if desired)

## Note
- The code is still being developed. It can be used, but it's by no means user friendly as of yet.
- Labels must be inserted directly inside anno_tool.js (I hope to change this soon)
- Number keys (from the keyboard) are used to attribute labels to selected text. Letter "E" from keyboard removes labels (assigns "O" labels to all selected words)
