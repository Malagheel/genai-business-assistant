from app.translator import translate_business_need_to_spec

if __name__ == "__main__":
    sample_input = "We want to use AI to reduce customer service wait times."
    output = translate_business_need_to_spec(sample_input)
    print("\n--- AI Assistant Output ---\n")
    print(output)
