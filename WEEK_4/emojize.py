import emoji

emojis = input("Que emoji quieres ver:   ")
emo = emoji.emojize(emojis, language="alias")
print(f"output: {emo}")
