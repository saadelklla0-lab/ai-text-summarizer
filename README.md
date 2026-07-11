# AI Text Summarizer

A powerful IronClaw skill for summarizing text content using AI/LLM models.

## Features

- **Text Summarization**: Summarize long articles, documents, and content
- **Key Point Extraction**: Extract the most important information from text
- **Flexible Length**: Configure summary length from brief to detailed
- **Multiple Detail Levels**: Choose from brief, normal, or detailed summaries

## Installation

This skill is part of the IronClaw ecosystem. To use it:

1. Clone this repository
2. Install the skill using the IronClaw skill manager
3. Follow the usage examples below

## Usage

### Basic Summarization

```python
# Summarize a given text
result = summarize_text("Your long text content here...")
print(result)
```

### Extract Key Points

```python
# Extract key points from a document
points = extract_key_points("Your document content...")
for point in points:
    print(f"- {point}")
```

### Quick Summary

```python
# Generate a quick, concise summary
summary = quick_summary("Your article text...")
print(summary)
```

## Configuration

You can configure the summarization behavior:

```python
config = {
    "max_length": 200,      # Maximum words in summary
    "min_length": 50,       # Minimum words in summary
    "detail_level": "normal"  # Options: "brief", "normal", "detailed"
}
```

## API Reference

### `summarize_text(text, config=None)`

Summarizes the given text using AI models.

**Parameters:**
- `text` (str): The text to summarize
- `config` (dict, optional): Configuration options

**Returns:**
- `str`: The summarized text

### `extract_key_points(text)`

Extracts key points from the given text.

**Parameters:**
- `text` (str): The text to extract key points from

**Returns:**
- `List[str]`: List of key points

### `quick_summary(text)`

Generates a quick, concise summary.

**Parameters:**
- `text` (str): The text to summarize

**Returns:**
- `str`: A brief summary

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please open an issue on the GitHub repository.