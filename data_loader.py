import pandas as pd
import io

def load_data(uploaded_file):
    if uploaded_file is not None:
        try:
            return pd.read_csv(uploaded_file)  # Try default UTF-8 first
        except UnicodeDecodeError:
            uploaded_file.seek(0)  # Reset file pointer
            try:
                return pd.read_csv(uploaded_file, encoding='ISO-8859-1')  # Fallback
            except Exception as e:
                return f"Failed to load data: {e}"
    return None
