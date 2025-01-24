from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt):
    # Add context to guide the model
    formatted_prompt = (
        "You are a knowledgeable assistant. Provide concise and factual information only. "
        f"Here is the user's question: {prompt}"
    )
    inputs = tokenizer(formatted_prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        max_length=150,
        temperature=0.3,
        top_p=0.9,
        num_return_sequences=1
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def clean_response(response):
    # Filter out unwanted content
    if "smiling" in response or "laughing" in response:
        return "Sorry, I can only provide factual information about cats."
    return response.strip()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your AI assistant. Ask me anything!")

async def ask_llm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = generate_response(user_message)
    response = clean_response(response)  # Clean the response
    await update.message.reply_text(response)

if __name__ == "__main__":
    application = ApplicationBuilder().token("7815659675:AAHiAzqQTXlkV7wgvepmXE7f87MVDJq2jf8").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ask_llm))

    application.run_polling()
