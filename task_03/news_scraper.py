import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_bbc_headlines():
    """Scrape BBC news headlines and save to file"""
    url = "https://www.bbc.com/news"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get headlines from h1, h2, h3 tags
            headlines = []
            for tag in soup.find_all(['h1', 'h2', 'h3']):
                text = tag.get_text().strip()
                if len(text) > 20 and len(text) < 150:  # Filter reasonable headline length
                    headlines.append(text)
            
            # Remove duplicates and limit to 10
            unique_headlines = list(dict.fromkeys(headlines))[:10]
            
            # Save to file
            filename = f"task_03/bbc_headlines_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("BBC News Headlines\n")
                f.write("=" * 20 + "\n\n")
                for i, headline in enumerate(unique_headlines, 1):
                    f.write(f"{i}. {headline}\n")
            
            # Display results
            print("BBC News Headlines:")
            print("-" * 20)
            for i, headline in enumerate(unique_headlines, 1):
                print(f"{i}. {headline}")
            print(f"\nSaved to: {filename}")
            
        else:
            print(f"Error: {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_bbc_headlines()