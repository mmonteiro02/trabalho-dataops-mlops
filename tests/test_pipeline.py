from app.pipeline import process_data
import os

def test_pipeline():
    result = process_data()

    assert not result.empty
    assert "product" in result.columns
    assert "amount" in result.columns
    assert os.path.exists("output/summary.csv")