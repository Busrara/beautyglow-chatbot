# -*- coding: utf-8 -*-
"""Copy of Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fgd-nwHKvcH5Vqb4TddMN88PRuUcE8Bk
"""

from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

#context: Detailed information about the beauty company
context = """
BeautyGlow is a beauty company founded in 2010, known for its premium skincare and makeup products formulated with natural and organic ingredients.
The company specializes in products tailored to different skin types, offering a wide range of skincare, makeup, and personal care items.

**Skin Types:**
- **Dry Skin**: BeautyGlow offers rich moisturizers and hyaluronic acid-based serums, which help restore the skin's moisture balance and leave the skin feeling smooth and nourished.
- **Oily Skin**: Products for oily skin include mattifying moisturizers, oil-control treatments, and toning lotions, all designed to control excess oil and leave skin looking fresh.
- **Sensitive Skin**: BeautyGlow's fragrance-free and allergy-tested products provide gentle cleansing and hydration without causing irritation.
- **Combination Skin**: BeautyGlow offers moisturizers that balance combination skin, controlling excess oil in the T-zone while hydrating dry areas.

**Makeup Products:**
- **Foundations**: BeautyGlow’s wide range of foundations matches various skin tones, providing a natural, long-lasting finish.
- **Blush and Highlighters**: Natural-toned blushes and highlighters sculpt and define facial features with a radiant finish.
- **Mascaras and Eyeliners**: The company is renowned for its waterproof, long-lasting mascaras and eyeliners, perfect for all-day wear.
- **Lipsticks and Lip Glosses**: BeautyGlow’s pigmented lipsticks and moisturizing glosses are ideal for everyday use, offering both comfort and vibrant color.

**Product Features:**
- All products are dermatologically tested, cruelty-free, and certified vegan.
- BeautyGlow offers free shipping on all orders and a 30-day money-back guarantee.
- BeautyGlow provides free online consultations to recommend personalized products based on customers’ skin types.

**Global Presence:**
BeautyGlow products are sold in over 15 countries, including the United States, Canada, the United Kingdom, France, Germany, Australia, Japan, South Korea, India, Brazil, and Mexico. The company’s products are available both online and in select beauty stores across these regions.
"""


# Question-Answer Pipeline
def answer_question(context, question):
    input_text = f"question: {question} context: {context}"
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=50, num_beams=5, early_stopping=True)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

# Example Question
question = "What products are recommended for dry skin?"

# Get the answer
answer = answer_question(context, question)
print(f"Answer: {answer}")