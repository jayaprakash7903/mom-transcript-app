from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

def generate_wordcloud(text, timestamp, save_dir):
    wordcloud = WordCloud(width=1000,
                          height=500,
                          background_color='white',
                          colormap='coolwarm',
                          max_words=200,
                          contour_color='steelblue',
                          contour_width=1,
                          prefer_horizontal=0.9,
                          collocations=False).generate(text)
    
    wordcloud_path = os.path.join(save_dir, f"wordcloud_{timestamp}.png")
    wordcloud.to_file(wordcloud_path)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud from MoM", fontsize=16)
    plt.tight_layout()
    plt.show()