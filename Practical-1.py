def sentiment_analysis(text): 
    positive_words = ["good", "happy", "excellent", "love", "great"] 
    negative_words = ["bad", "sad", "hate", "poor", "worst"] 
    text = text.lower() 
 
    if any(word in text for word in positive_words): 
        return "Positive Sentiment" 
    elif any(word in text for word in negative_words): 
        return "Negative Sentiment" 
    else: 
        return "Neutral Sentiment" 
 
def math_solver(expression): 
    try: 
        result = eval(expression) 
        return f"Answer: {result}" 
    except: 
        return "Invalid mathematical expression." 
 
def movie_bot(user_input): 
    user_input = user_input.lower() 
    if "recommend" in user_input: 
 
 
        return "I recommend watching 'Inception' or 'The Matrix'." 
    elif "genre" in user_input: 
        return "I like sci-fi and action movies!" 
    elif "bye" in user_input: 
        return "Goodbye! Enjoy your movie night!" 
    else: 
        return "I'm a movie bot. Ask me about movies!" 
 
def show_ai_systems(): 
    systems = { 
        "Reactive Machines": "Example: IBM Deep Blue (chess playing)", 
        "Limited Memory": "Example: Self-driving car systems", 
        "Theory of Mind": "Example: Future AI with emotional understanding", 
        "Self-aware": "Example: Hypothetical AI with consciousness" 
    } 
    return systems 
 
def main(): 
    print("\n=== AI Simulation Program ===") 
    while True: 
        print("\nChoose an AI Feature:") 
        print("1. Sentiment Analysis (Learning)") 
        print("2. Math Solver (Reasoning)") 
 
 
        print("3. Movie Bot (NLP & Interaction)") 
        print("4. AI System Types") 
        print("5. Real-World AI Applications") 
        print("6. Exit") 
         
        choice = input("Enter your choice (1-6): ")
        match choice:
            case "1":
                text = input("Enter a sentence to analyze sentiment: ") 
                print(sentiment_analysis(text))
            case "2":
                exp = input("Enter a math expression (e.g., 2+3*5): ") 
                print(math_solver(exp))
            case "3": 
                message = input("You: ") 
                print("MovieBot:", movie_bot(message))
            case "4": 
                systems = show_ai_systems() 
                for key, value in systems.items():
                    print(f"{key}: {value}")
            case "5":
                print("\n--- Real World AI Applications ---") 
                print("- Social media sentiment analysis") 
                print("- AI-based tutors and learning apps") 
                print("- Movie and music recommendations") 
                print("- Virtual customer service agents") 
                print("- Autonomous drones and robots")
            case "6": 
                print("Exiting... Thank you for exploring AI!") 
                break 
 
        
 
if __name__ == "__main__": 
    main() 
    print("\n Mahi Shah \n 240905041030")
