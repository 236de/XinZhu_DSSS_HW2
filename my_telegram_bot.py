from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Function to generate responses from LLM 
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the Hugging Face model and tokenizer
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt):
    # Tokenize the input
    inputs = tokenizer(prompt, return_tensors="pt")
    # Generate the response
    outputs = model.generate(inputs["input_ids"], max_length=100, num_return_sequences=1)
    # Decode and return the response
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Ask me anything about your favorite animals or other topics!")

async def ask_llm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = generate_response(user_message)  # Send user input to LLM
    await update.message.reply_text(response)

if __name__ == "__main__":
    application = ApplicationBuilder().token("7815659675:AAHiAzqQTXlkV7wgvepmXE7f87MVDJq2jf8").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ask_llm))

    application.run_polling()

