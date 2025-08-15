import requests
import json
from datetime import datetime

def analyze_content(text_to_analyze):
    """ 
    Use Claude AI to analyze text content for marketing insights 
    """

    print("🤖 Analyzing content with AI...")
    print(f"📝 Text to analyze: '{text_to_analyze[:50]}...'")

    # My Anthropic AP key
    api_key = "your_api_key_here"  # Replace with your actual API key
    # Import anthropic library
    import anthropic

    try:
        # Initialize the client
        client = anthropic.Anthropic(api_key=api_key)

        #Create the analysis prompt
        prompt = f"""
        You are a social media marketing expert analyzing content for Twitter.

        CONTEXT:
        - Platform: Twitter (280 character limit, fast-paced, visual-first)
        - Content type: Product announcement with video
        - Industry: Crypto/DeFi trading

        Analyze this Twitter content:
        "{text_to_analyze}"

        Provide CONCISE analysis (2-3 sentences each):

        1. SENTIMENT: Rate 1-10 and explain briefly
        2. BRAND TONE: Does this sound like a web3 startup? Too casual/formal?
        3. TWITTER EFFECTIVENESS: Does this work for Twitter specifically?
        4. ACTIONABLE IMPROVEMENTS: What would you change for better Twitter engagement?

        Keep suggestions Twitter-appropriate (brevity, engagement tactics).
        """

        # Call Claude
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )

        analysis_result = response.content[0].text

        print("\n🔍 DEBUG: Full AI response length:", len(analysis_result))
        print("🔍 DEBUG: Last 200 characters:")
        print(analysis_result[-200:])
        print("🔍 End of debug\n")  

        print("✅ AI Analysis Complete!")
        print("📊 Analysis Results:")
        print("-" * 50)
        print(analysis_result)

        return analysis_result
    except Exception as e:
        print(f"❌ Error calling AI: {e}")
        return None
    

def save_analysis_to_csv(original_text, analysis_result): 
    """
    Save analysis results for tracking over time
    """

    if not analysis_result:
        print("❌ No analysis to save")
        return
    
    import os
    import csv

    filename = "content_analysis_history.csv"
    file_exists = os.path.exists(filename)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(['Timestamp', 'Original_Text', 'AI_Analysis'])
            print(f"📁 Created new analysis history file")

        writer.writerow([timestamp, original_text, analysis_result])
        print(f"💾 Analysis saved to {filename}")



if __name__ == "__main__":
    # Test with sample marketing text

    sample_text = """
                Introducing: Phantom Perps 👻 ♾
                Go long or short in just a few taps.
                100+ markets. Up to 40x leverage. All in your pocket.
                Powered by @HyperliquidX
                """
    analysis = analyze_content(sample_text)
    save_analysis_to_csv(sample_text, analysis)
    print("🌟 Content analysis complete")