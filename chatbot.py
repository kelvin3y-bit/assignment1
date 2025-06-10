# crypto_chatbot

print("Hey there! I'm CryptoBot, your AI-powered financial sidekick!")

crypto_db = {
    "Bitcoin": {
        "price_trend": "up",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    },
}

# chatbot logic
def crypto_advisor(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Go with {recommend}! It's eco-friendly with a high sustainability score of {crypto_db[recommend]['sustainability_score']*10}/10."
    
    elif "trending" in user_query or "rising" in user_query:
        trending_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"These cryptos are on the rise: {', '.join(trending_coins)}!"
    
    elif "long-term" in user_query or "growth" in user_query:
        candidates = [
            coin for coin in crypto_db
            if crypto_db[coin]["price_trend"] == "rising"
            and crypto_db[coin]["sustainability_score"] > 0.7
        ]
        if candidates:
            return f"For long-term growth, consider {candidates[0]} - it's trending and sustainable!"
        else:
            return "I couldn't find any perfect match, but keep an eye on the market trends!"
    
    elif "safe" in user_query or "stable" in user_query:
        stable_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "stable"]
        return f"looking for safety? {', '.join(stable_coins)} are showing"
    
    elif "advice" in user_query or "what should i buy" in user_query:
        profitable_coins = [
            coin for coin in crypto_db
            if crypto_db[coin]["price_trend"] == "rising"
            and crypto_db[coin]["sustainability_score"] > 0.5
        ]
        if profitable_coins:
            return f"for profitability, consider investing in {profitable_coins[0]} - it's rising and has high market cap!"
        else:
            return "No top-performing coins found right now. Check back later!"
    elif "help" in user_query:
        return "I'm here to help! Ask me about sustainable cryptos, trending coins, or long-term growth opportunities."
    else:
        return "I didn't quite get that. Can you ask about sustainable cryptos, trending coins, or long-term growth opportunities?"
    

##bot testing

print("welcome to cryptoBuddy - your AI-powered crypto assistant!")
while True:
    query = input("/nYou:")
    if query.lower() in ["exit", "quit", "bye"]:
        print("CryptoBuddy: Take care! Remember, crypto is risky - always do your own research!")
        break
    response = crypto_advisor(query)
    print(f"CryptoBuddy: {response}")