import os
import csv
import subprocess
from datetime import datetime
import multiprocessing
from tqdm import tqdm  # For progress bar

# Base directory for all files (update this to match your system)
base_dir = "./Global_Issues"

# Path to the directory where articles will be saved
output_dir = os.path.join(base_dir, "Articles")

# Ensure the directory exists
os.makedirs(output_dir, exist_ok=True)

# Path to the global issues CSV file
issues_file = os.path.join(base_dir, "issues.csv")

# Function to load global issues from the CSV file
def load_issues():
    """Reads the list of global issues from a CSV file and returns them as a list."""
    issues = []
    try:
        with open(issues_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                issues.append(row[0])  # Assuming each issue is in one row
    except FileNotFoundError:
        print("Error: CSV file not found. Make sure 'issues.csv' is in the correct directory.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return issues

# Function to generate a formatted title for saving the article
def generate_title(issue):
    """Generates a filename-friendly title based on the issue name."""
    title = issue.replace(" ", "_").lower()
    title = f"{title}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    return title

# Function to generate an article using the Mistral model
def generate_article(issue, model="mistral"):
    """Generates an academic-style article on the given issue using the Mistral AI model."""
    prompt = (f"Write an academic article about {issue} in the following format:\n"
              "1. Introduction\n"
              "   - Provide background context on the global issue, its significance, and its impact.\n"
              "2. Challenges or Barriers\n"
              "   - Discuss the main challenges or barriers related to the issue.\n"
              "3. Solutions or Strategies\n"
              "   - Propose potential solutions or strategies to address the challenges.\n"
              "4. Conclusion\n"
              "   - Summarize the key points and discuss future implications.\n"
              "The article should be evidence-based and written in a formal tone.")

    try:
        # Call the local Mistral model using Ollama
        response = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        # Check if the command executed successfully
        if response.returncode == 0:
            return response.stdout.strip()
        else:
            return f"Error: Failed to generate content using Mistral. {response.stderr}"
    except Exception as e:
        return f"Error: {e}"

# Function to save generated article to a file
def save_article(issue, article):
    """Saves the generated article as a text file in the output directory."""
    title = generate_title(issue)
    file_path = os.path.join(output_dir, f"{title}.txt")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(article)
        return f"File successfully generated for issue '{issue}': {file_path}"
    except Exception as e:
        return f"Error saving article: {e}"

# Worker function to process each issue in parallel
def process_issue(issue):
    """Handles the end-to-end process of generating and saving an article for an issue."""
    article = generate_article(issue)
    return save_article(issue, article)

# Main function to process all issues using multiprocessing
def main():
    """Loads the issues from CSV and generates articles in parallel."""
    issues = load_issues()
    
    if not issues:
        print("No issues found. Please check the CSV file.")
        return

    # Use multiprocessing to speed up article generation
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = list(tqdm(pool.imap(process_issue, issues), total=len(issues), desc="Generating Articles"))
    
    print("All articles generated successfully!")

# Entry point to run the script
if __name__ == "__main__":
    main()

