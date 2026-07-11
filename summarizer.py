#!/usr/bin/env python3
"""
AI Text Summarizer - IronClaw Skill
Provides text summarization capabilities using AI analysis.
"""

import asyncio
import sys
from typing import Dict, List, Optional, Any


class TextSummarizer:
    """Main class for text summarization operations."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the summarizer with configuration.
        
        Args:
            config: Configuration dictionary with optional keys:
                - max_sentences: Maximum sentences in summary (default: 5)
                - language: Language code (default: "en")
                - style: Summary style - neutral, formal, casual (default: "neutral")
        """
        self.config = config or {}
        self.max_sentences = self.config.get('max_sentences', 5)
        self.language = self.config.get('language', 'en')
        self.style = self.config.get('style', 'neutral')
    
    async def summarize(self, text: str, max_sentences: Optional[int] = None) -> str:
        """
        Summarize the input text using AI analysis.
        
        Args:
            text: The text to summarize
            max_sentences: Override default max sentences for this summary
            
        Returns:
            A summarized version of the text
        """
        if not text or not text.strip():
            return ""
        
        # Use the max_sentences parameter if provided, otherwise use default
        sentences_limit = max_sentences or self.max_sentences
        
        # Build the prompt based on style
        style_instructions = {
            'neutral': "Provide a neutral, factual summary",
            'formal': "Provide a formal, professional summary",
            'casual': "Provide a casual, easy-to-understand summary"
        }
        
        style_instruction = style_instructions.get(self.style, style_instructions['neutral'])
        
        # Create the summarization prompt
        prompt = f"""{style_instruction} of the following text in exactly {sentences_limit} sentences.

TEXT TO SUMMARIZE:
{text}

SUMMARY:"""
        
        try:
            # Use llm_query for AI-powered summarization
            summary = await llm_query(prompt=prompt, context=text)
            return summary.strip() if summary else "Unable to generate summary."
        except Exception as e:
            return f"Error generating summary: {str(e)}"
    
    async def summarize_extractive(self, text: str, num_sentences: int = 3) -> str:
        """
        Perform extractive summarization by selecting key sentences.
        
        Args:
            text: The text to summarize
            num_sentences: Number of sentences to extract
            
        Returns:
            Extractive summary as a string
        """
        if not text or not text.strip():
            return ""
        
        # Split text into sentences
        sentences = self._split_into_sentences(text)
        
        if len(sentences) <= num_sentences:
            return text
        
        # Score sentences based on importance indicators
        scored_sentences = []
        for i, sentence in enumerate(sentences):
            score = self._score_sentence(sentence, i, len(sentences))
            scored_sentences.append((i, sentence, score))
        
        # Sort by score (descending) and take top sentences
        top_sentences = sorted(scored_sentences, key=lambda x: x[2], reverse=True)[:num_sentences]
        
        # Sort back by original position
        top_sentences.sort(key=lambda x: x[0])
        
        return ' '.join([s[1] for s in top_sentences])
    
    def _split_into_sentences(self, text: str) -> List[str]:
        """Split text into sentences."""
        # Simple sentence splitting on common delimiters
        import re
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        return [s for s in sentences if s and len(s) > 10]
    
    def _score_sentence(self, sentence: str, position: int, total: int) -> float:
        """
        Score a sentence based on importance indicators.
        
        Scoring factors:
        - Position (first sentences often more important)
        - Length (moderate length is better)
        - Keywords (contains important terms)
        - Structure (contains indicators of importance)
        """
        score = 0.0
        
        # Position scoring (first and last sentences get bonus)
        if position == 0:
            score += 2.0
        elif position == total - 1:
            score += 1.0
        elif position < total * 0.2:
            score += 1.5
        
        # Length scoring (prefer medium-length sentences)
        word_count = len(sentence.split())
        if 10 <= word_count <= 30:
            score += 1.0
        elif 5 <= word_count <= 40:
            score += 0.5
        
        # Keyword indicators
        important_phrases = [
            'important', 'significant', 'key', 'main', 'primary',
            'conclusion', 'result', 'finding', 'shows', 'demonstrates',
            'therefore', 'thus', 'hence', 'in summary', 'in conclusion'
        ]
        sentence_lower = sentence.lower()
        for phrase in important_phrases:
            if phrase in sentence_lower:
                score += 0.5
        
        # Capitalization indicator (proper nouns, start of paragraph)
        if sentence[0].isupper():
            score += 0.3
        
        return score
    
    async def compare_summaries(self, text: str, methods: List[str] = None) -> Dict[str, str]:
        """
        Generate summaries using multiple methods and return comparison.
        
        Args:
            text: The text to summarize
            methods: List of methods to use ['ai', 'extractive', 'both']
            
        Returns:
            Dictionary with summaries from each method
        """
        if methods is None:
            methods = ['both']
        
        results = {}
        
        if 'ai' in methods or 'both' in methods:
            results['ai_summary'] = await self.summarize(text)
        
        if 'extractive' in methods or 'both' in methods:
            results['extractive_summary'] = await self.summarize_extractive(text)
        
        return results


async def main():
    """Main entry point for the skill."""
    # Example usage
    summarizer = TextSummarizer(config={
        'max_sentences': 3,
        'style': 'neutral'
    })
    
    # Example text
    test_text = """
    Artificial intelligence has revolutionized many industries in recent years. 
    Machine learning algorithms can now process vast amounts of data and identify 
    patterns that humans might miss. This has led to breakthroughs in healthcare, 
    finance, and transportation. However, concerns about AI ethics and job displacement 
    remain important topics of discussion. Researchers are working on developing 
    more transparent and explainable AI systems to address these concerns.
    """
    
    # Generate summary
    summary = await summarizer.summarize(test_text)
    print(f"AI Summary:\n{summary}\n")
    
    # Generate extractive summary
    extractive = await summarizer.summarize_extractive(test_text)
    print(f"Extractive Summary:\n{extractive}\n")
    
    # Compare both methods
    comparison = await summarizer.compare_summaries(test_text)
    print("Comparison:")
    for method, result in comparison.items():
        print(f"{method}: {result}\n")


if __name__ == "__main__":
    asyncio.run(main())