**Steps to run:**

1. Create virtual environment with `python3 python3 -m venv otsenv` and run it by `source otsenv/bin/activate`
2. Run `pip install -r requirements.txt`
3. Export needed environment variables by doing this commands:
    `export SECRET_KEY=arbitrary_secret_key`, `export TRAIN_FILE=path/to/train.csv`
4. Run `python server.py` from webapp folder
5. Enter http://127.0.0.1:5000/ in your browser