name: AI Text Summarizer
description: A skill that summarizes text using AI models
version: 1.0.0
author: saadelklla0-lab

keywords:
  - ai
  - summarization
  - text-processing
  - llm

requires:
  skills: []

entry_point: main

# This skill provides text summarization capabilities using AI/LLM models.
# It can summarize articles, documents, and other text content.

usage: |
  ## AI Text Summarizer
  
  This skill summarizes text content using AI models.
  
  ### Features
  - Summarize long articles and documents
  - Extract key points from text
  - Generate concise summaries
  - Support for various text lengths
  
  ### Usage Examples
  ```
  # Summarize a given text
  summarize_text("Your long text here...")
  
  # Extract key points
  extract_key_points("Your document content...")
  
  # Generate a short summary
  quick_summary("Your article text...")
  ```

  ### Configuration
  - `max_length`: Maximum length of the summary (default: 200 words)
  - `min_length`: Minimum length of the summary (default: 50 words)
  - `detail_level`: Summary detail level - "brief", "normal", "detailed"

license: MIT
repository: https://github.com/saadelklla0-lab/ai-text-summarizer
