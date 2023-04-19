import tkinter as tk
import openai

openai.api_key = "" #fill this in with personal key


def generate_card():
    name = name_entry.get()
    recip = recip_entry.get()
    occ = occ_entry.get()
    style = style_entry.get()
    tone = tone_entry.get()
    
    prompt = ("You are a card writer for celebratory events. Write a " + tone + " card in the form of a " + style + 
              " for " + recip + "'s " + occ)
    
    chatbot = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    message = (chatbot.choices[0].text + "\nFrom, " + name)
    
    card_label.configure(text=message)

    
root = tk.Tk()

name_label = tk.Label(root, text="Enter your name:")
name_entry = tk.Entry(root)

recip_label = tk.Label(root, text="Enter the recipient's name:")
recip_entry = tk.Entry(root)

occ_label = tk.Label(root, text="Enter the occasion:")
occ_entry = tk.Entry(root)

style_label = tk.Label(root, text="Enter the style (prose, couplet, etc):")
style_entry = tk.Entry(root)

tone_label = tk.Label(root, text="Enter the desired tone:")
tone_entry = tk.Entry(root)

generate_button = tk.Button(root, text="Generate card", command=generate_card)
card_label = tk.Label(root, text="")

name_label.pack()
name_entry.pack()
recip_label.pack()
recip_entry.pack()
occ_label.pack()
occ_entry.pack()
style_label.pack()
style_entry.pack()
tone_label.pack()
tone_entry.pack()
generate_button.pack()
card_label.pack()

root.mainloop()

