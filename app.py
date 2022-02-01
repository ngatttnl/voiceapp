
from multiapp import MultiApp
from apps import phrase_leaning, phrase, leaning, topic, vocab, translate, text_to_voice
app = MultiApp()

# Add all your application here

#app.add_app("Phrase", phrase.app)
app.add_app("Learning Phrase", phrase_leaning.app)
#app.add_app("Vocabulary", vocab.app)
app.add_app("Learning vocabulary", leaning.app)
#app.add_app("Tiếng Việt", vietnamese.app)

#app.add_app("Topic", topic.app)

app.add_app("Translate", translate.app)
app.add_app("Text To Voice", text_to_voice.app)

#app.add_app("Learning - Candlestick", candlestick.app)

app.run()


 
    

    
   
    

    