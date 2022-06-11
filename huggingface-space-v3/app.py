#Importing Gradio and the trained transformers
import gradio as gr                   # UI library
from transformers import pipeline     # Transformers pipeline

model_checkpoint_en2fil = "SalamaThanks/SalamaThanksTransformer_en2fil_v3"
model_checkpoint_fil2en = "SalamaThanks/SalamaThanksTransformer_fil2en_v3"

translator_en2fil = pipeline("translation", model = model_checkpoint_en2fil)
translator_fil2en = pipeline("translation", model = model_checkpoint_fil2en)


#Function for English-Filipino translation
def transformer_en2fil(from_text):
  results = translator_en2fil(from_text)
  return results[0]['translation_text']


#Function for Filipino-English translation
def transformer_fil2en(from_text):
  results = translator_fil2en(from_text)
  return results[0]['translation_text']


#Function to check the "language to translate"
def check_lang(lang, from_text):
  if lang == "English-to-Filipino":
    return transformer_en2fil(from_text)
  elif lang == "Filipino-to-English":
    return transformer_fil2en(from_text)


#Creating the Gradio interface
interface = gr.Interface(
  fn=check_lang, 
  inputs=[
    gr.inputs.Radio(["English-to-Filipino", "Filipino-to-English"]),
    gr.inputs.Textbox(lines=4, placeholder='Input Text to Translate:')],
  outputs='text'
)


#Running the application
interface.launch(debug=True)