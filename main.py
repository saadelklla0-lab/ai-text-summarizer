"""
AI Text Summarizer - IronClaw Skill
Summarizes text using AI models with configurable length and style options.
"""

import json
import os
from typing import Optional


def summarize_text(text: str, max_length: int = 150, style: str = "concise") -> str:
    """
    Summarize the given text using AI.
    
    Args:
        text: The text to summarize
        max_length: Maximum length of the summary in characters
        style: Summary style - "concise", "detailed", or "bullet_points"
    
    Returns:
        The summarized text
    """
    if not text or not text.strip():
        return "No text provided for summarization."
    
    # Clean input text
    text = text.strip()
    
    # Basic summarization logic (placeholder for actual AI integration)
    # In a real implementation, this would call an AI API
    sentences = text.split('.')
    
    if style == "bullet_points":
        # Create bullet point summary
        key_points = []
        for sentence in sentences[:3]:
            sentence = sentence.strip()
            if sentence and len(sentence) > 10:
                key_points.append(f"• {sentence}.")
        return "\n".join(key_points) if key_points else "No key points extracted."
    
    elif style == "detailed":
        # More detailed summary
        summary_sentences = sentences[:5]
        summary = ". ".join([s.strip() for s in summary_sentences if s.strip()])
        if not summary.endswith('.'):
            summary += '.'
        return summary
    
    else:  # concise (default)
        # Short summary
        summary_sentences = sentences[:2]
        summary = ". ".join([s.strip() for s in summary_sentences if s.strip()])
        if not summary.endswith('.'):
            summary += '.'
        
        # Truncate if too long
        if len(summary) > max_length:
            summary = summary[:max_length - 3] + "..."
        
        return summary


def summarize_file(file_path: str, max_length: int = 150, style: str = "concise") -> str:
    """
    Summarize text from a file.
    
    Args:
        file_path: Path to the text file
        max_length: Maximum length of the summary
        style: Summary style
    
    Returns:
        The summarized text
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    return summarize_text(text, max_length, style)


def main():
    """Main entry point for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="AI Text Summarizer - Summarize text using AI"
    )
    parser.add_argument(
        "--text", "-t",
        help="Text to summarize",
        required=False
    )
    parser.add_argument(
        "--file", "-f",
        help="Path to text file to summarize",
        required=False
    )
    parser.add_argument(
        "--length", "-l",
        type=int,
        default=150,
        help="Maximum summary length (default: 150)"
    )
    parser.add_argument(
        "--style", "-s",
        choices=["concise", "detailed", "bullet_points"],
        default="concise",
        help="Summary style (default: concise)"
    )
    
    args = parser.parse_args()
    
    try:
        if args.file:
            summary = summarize_file(args.file, args.length, args.style)
        elif args.text:
            summary = summarize_text(args.text, args.length, args.style)
        else:
            # Read from stdin
            import sys
            text = sys.stdin.read()
            summary = summarize_text(text, args.length, args.style)
        
        print(summary)
    
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error during summarization: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()