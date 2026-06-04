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
