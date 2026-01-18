from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
ANALYSIS_DIR = PROJECT_ROOT / "analysis"
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
FIGURE_DIR = PROJECT_ROOT / "figures"