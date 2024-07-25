# tests/test_analysis.py
from src.analysis import run_analysis

def test_run_analysis():
    results = run_analysis()
    assert 'mean' in results
    assert isinstance(results['mean'], (int, float))  # Ensure mean is a number
    assert results['mean'] > 0
