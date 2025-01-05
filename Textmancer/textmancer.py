from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class Textmancer:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)

    def generate_text(self, prompt, max_length=200, temperature=1.0, num_return_sequences=1):
        # Tokenize the input prompt
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        
        # Generate text
        output = self.model.generate(
            input_ids, 
            max_length=max_length, 
            num_return_sequences=num_return_sequences, 
            no_repeat_ngram_size=2,
            repetition_penalty=1.5,
            top_k=50,
            top_p=0.95,
            temperature=temperature,
            do_sample=True,
            early_stopping=True
        )
        
        # Decode the output and return it
        generated_text = [self.tokenizer.decode(output[i], skip_special_tokens=True) for i in range(num_return_sequences)]
        return generated_text

if __name__ == "__main__":
    # Get user input from the console
    prompt = input("Enter a prompt for text generation: ")
    max_length = int(input("Enter maximum length of the generated text (e.g., 150): "))
    temperature = float(input("Enter temperature for the text generation (e.g., 1.0): "))
    num_return_sequences = int(input("Enter the number of sequences to generate (e.g., 1): "))
    
    # Create an instance of the Textmancer
    textmancer = Textmancer(model_name='gpt2-medium')
    
    # Generate text based on user input
    generated_texts = textmancer.generate_text(
        prompt=prompt, 
        max_length=max_length, 
        temperature=temperature, 
        num_return_sequences=num_return_sequences
    )
    
    # Print the generated text(s)
    for i, text in enumerate(generated_texts):
        print(f"\nGenerated Text {i+1}:\n{text}\n")
