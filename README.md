# Global Issues Article Generator

This project allows users to generate academic-style articles on various global issues using AI. The script reads a list of issues from a CSV file, generates structured articles, and saves them as text files.

## Features

- Automatically generates articles on multiple global issues.
- Uses the Mistral AI model for structured, evidence-based content.
- Supports parallel processing to speed up article generation.
- Saves articles in a clean, organized format.

## Getting Started

This project enables users to generate AI-assisted academic articles efficiently.

### Installation

#### Clone the Repository

```sh
git clone https://github.com/chanda-mandisa/GlobalIssues.git
cd GlobalIssues
```

### System Requirements

- Python 3.x
- Ollama (for running Mistral AI model)
- Required Python libraries: `tqdm`, `csv`, `multiprocessing`

### Running the Script

Generate a set of articles:

```sh
python generate_global_issues_article.py
```

- A new set of article text files will be saved in the `Articles` directory.

## Usage

### Viewing Generated Articles

- Open the `Articles` folder to access the generated text files.
- Each file is named based on the issue and the timestamp of creation.

### Modifying Input Data

- Edit `issues.csv` to add or remove topics before running the script.

## Customization

### Changing AI Model

- Modify the `generate_article` function in `generate_global_issues_article.py` to use a different AI model.

### Adjusting Article Structure

- Update the `prompt` inside `generate_article` to change how articles are formatted.

## Troubleshooting

### Errors While Running the Script

- Ensure `issues.csv` exists in the same directory as the script.
- Confirm that `ollama` is installed and configured correctly.
- Check if Python dependencies are installed.

### Articles Not Generating Correctly

- Ensure your input issues are formatted correctly in the CSV.
- Try reducing the number of issues if experiencing processing delays.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contributions

Contributions are welcome! Feel free to submit a pull request or report issues.

## Author
Developed by [chanda-mandisa].


