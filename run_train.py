from chatbot_core import ChatbotAssistant

# Initialize chatbot assistant without any function mappings
assistant = ChatbotAssistant("intents.json")

# Step 1: Parse intents
assistant.parse_intents()

# Step 2: Prepare training data
assistant.prepare_data()

# Step 3: Train model
assistant.train_model(batch_size=8, lr=0.001, epochs=100)

# Step 4: Save model and its dimensions
assistant.save_model("chatbot_model.pth", "dimensions.json")

print("Model training complete and saved.")
