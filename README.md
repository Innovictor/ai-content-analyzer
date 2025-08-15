# AI Content Analyzer

A marketing content analysis tool powered by Claude AI for social media managers, content creators, and marketing professionals to get actionable insights about written content.

## Features

- **Sentiment Analysis**: Quantified sentiment scoring (1-10 scale downbeat to upbeat) with contextual explanation
- **Brand Tone Assessment**: Evaluates content alignment with industry and platform expectations  
- **Platform-Specific Optimization**: Tailored analysis for Twitter, LinkedIn, Reddit, Lens and other social platforms
- **Actionable Recommendations**: Concrete suggestions for improving engagement and conversion
- **Historical Tracking**: CSV export for content performance analysis over time

## Use Cases

- **Social Media Management**: Optimize posts before publishing
- **Brand Consistency**: Ensure content aligns with brand voice across platforms
- **Content Strategy**: Analyze competitor content 


## Technical Implementation

- **AI Integration**: Claude API (Anthropic) for advanced natural language processing
- **Data Persistence**: Automated CSV logging for historical analysis
- **Error Handling**: Robust API error management and fallback responses
- **Modular Design**: Easily extensible for additional platforms and metrics

## Sample Analysis Output
- SENTIMENT: 8/10. Upbeat, exciting tone well-suited for product announcements
- BRAND TONE: Aligns with web3 startup - casual, conversational with relevant terminology
- TWITTER EFFECTIVENESS: Concise, visually engaging, highlights key value propositions
- ACTIONABLE IMPROVEMENTS: Add clear CTA and experiment with video formats

## Requirements

- Python 3.7+
- Anthropic API key
- Required packages: `requests`, `anthropic`

## Installation

```bash 
pip3 install anthropic requests
```
### Configuration

- Sign up for Anthropic API at https://console.anthropic.com
- Replace api_key = "your_api_key_here" with your actual API key
- Run: python3 content_analyzer.py

## Professional Applications
This tool demonstrates practical AI integration for marketing workflows, combining technical implementation with industry-specific knowledge to deliver actionable copywriting insights.

---

### Built by: Victor Alagbe

#### Why?

I am a content marketing professional with 12 years of experience in emerging technologies, most recently in Web3. With the explosion of AI solutions for marketing professionals, I have observed that most tools provide generic results that don't offer much value to marketers worthy of the name or recommendations that could be logged under the "AI slop" category. This is an attempt to leverage my domain expertise from a Bachelor's degree in Linguistics and an MSc in Marketing Communications, plus more than a decade's worth of hands-on experience to create AI-powered tools that actually get the job done for marketers.
