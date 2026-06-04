from IPython.display import display, HTML

GITHUB_REPO_PATH = "https://uonphysicscoding.github.io/exercises/"

def button(button_text, problem_name):
    full_url = GITHUB_REPO_PATH + problem_name
    
    # We use the HTML class instead of Markdown for better rendering
    button_html = f"""
    <a href="{full_url}" target="_blank" style="
        display: inline-block;
        padding: 12px 24px;
        background: linear-gradient(135deg, #007bff, #0056b3);
        color: white;
        text-decoration: none;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        font-weight: bold;
        font-family: sans-serif;
    ">
        {button_text}
    </a>
    """
    return HTML(button_html)

# Now call the function
from jupyterquiz import display_quiz



def quiz(json_file):
    # A consistent, professional Blue/Indigo palette
    color_dict = {
        # Question backgrounds (Main theme)
        '--jq-multiple-choice-bg': '#007bff',   # Strong Blue for Multiple Choice
        '--jq-many-choice-bg': '#0056b3',       # Deeper Blue for Many Choice
        '--jq-numeric-bg': '#2c3e50',           # Dark Navy for Numeric
        
        # Button and Text
        '--jq-mc-button-bg': '#ffffff',         # Clean white buttons
        '--jq-mc-button-border': '#dee2e6',     # Light grey border
        '--jq-mc-button-inset-shadow': '#007bff', # Subtle blue highlight when pressed
        '--jq-text-color': '#212529',           # Dark grey text for readability
        
        # Feedback Colors
        '--jq-incorrect-color': '#dc3545',      # Soft red
        '--jq-correct-color': '#28a745',        # Soft green
        
        # Numeric specific
        '--jq-numeric-input-bg': '#f8f9fa',
        '--jq-numeric-input-label': '#212529',
        '--jq-numeric-input-shadow': '#007bff'
    }

# Usage:
# display_quiz("quiz1.json", colors=color_dict)
    display_quiz(GITHUB_REPO_PATH + json_file, colors=color_dict)