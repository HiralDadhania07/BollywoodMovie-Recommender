
def load_css():
    css = """
    <style>
    .stApp {
        background: linear-gradient(-45deg, #1e3a8a, #2563eb, #3b82f6, #60a5fa, #21f5fd, #1e3a8a, #2563eb, #3b82f6, #60a5fa);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        min-height: 100vh;
        padding: 0 !important;
        color: #f9fafb;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .st-emotion-cache-12fmjuu {
        background: transparent;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .header-container {
        text-align: center;
        padding: 40px 20px 20px 20px;
        background: linear-gradient(45deg, darkblue, transparent 70%);
        color: white;
        border-radius: 16px;
        margin-bottom: 30px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(5px);
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 10px;
        color: #ffffff;
    }

    .subtitle {
        font-size: 20px;
        font-weight: 400;
        color: #dbeafe;
    }

    .movie-card {
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.2s ease-in-out;
    }

    .movie-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
        background-color: honeydew;
    }

    .movie-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 12px;
        color: #333333;
    }

    .movie-info {
        font-size: 16px;
        color: #555555;
        margin-bottom: 8px;
    }

    .similarity-score {
        font-size: 14px;
        color: #c7d2fe;
        margin-top: 12px;
    }

    .stButton > button {
        color: #ffffff !important;
        font-weight: 600 !important;
        padding: 12px 24px;
        font-size: 16px;
        border-radius: 8px;
        border: none;
        background: linear-gradient(40deg, darkblue 10%, transparent 90%);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.2s ease;
        cursor: pointer;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        background: linear-gradient(45deg, rgb(4, 184, 184), transparent);
    }

    .stButton > button:active {
        background-color: #1e3a8a !important;
        transform: translateY(1px);
    }

    /* Pagination page info */
    .page-info {
        text-align: center;
        font-size: 16px;
        margin-top: 10px;
        color: #f3f4f6;
    }

    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
    }

    ::-webkit-scrollbar-thumb {
        background-color: rgba(96, 165, 250, 0.7);
        border-radius: 10px;
    }

    </style>
    """
    return css