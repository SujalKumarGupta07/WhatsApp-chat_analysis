import os
from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()

def _get_stop_words():
    stop_words_path = os.path.join(os.path.dirname(__file__), 'stop_hinglish.txt')
    if os.path.exists(stop_words_path):
        with open(stop_words_path, 'r', encoding='utf-8') as f:
            return set(f.read().lower().split())
    return set()

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch number of media messages (handles variations of media omitted)
    num_media_messages = df[df['message'].str.contains(r'<Media omitted>|omitted', case=False, na=False)].shape[0]

    # fetch number of links shared
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)

def most_busy_users(df):
    temp = df[df['user'] != 'group_notification']
    x = temp['user'].value_counts().head()
    new_df = round((temp['user'].value_counts() / temp.shape[0]) * 100, 2).reset_index()
    new_df.columns = ['name', 'percent']
    return x, new_df

def create_wordcloud(selected_user, df):
    stop_words = _get_stop_words()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[~temp['message'].str.contains(r'<Media omitted>|omitted', case=False, na=False)].copy()

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    temp['message'] = temp['message'].apply(remove_stop_words)
    clean_text = temp['message'].str.cat(sep=" ").strip()

    if not clean_text:
        return None

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(clean_text)
    return df_wc

def most_common_words(selected_user, df):
    stop_words = _get_stop_words()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[~temp['message'].str.contains(r'<Media omitted>|omitted', case=False, na=False)]

    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    counts = Counter(words).most_common(20)
    if counts:
        most_common_df = pd.DataFrame(counts)
    else:
        most_common_df = pd.DataFrame(columns=[0, 1])

    return most_common_df

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([e['emoji'] for e in emoji.emoji_list(message)])

    counts = Counter(emojis).most_common()
    if counts:
        emoji_df = pd.DataFrame(counts)
    else:
        emoji_df = pd.DataFrame(columns=[0, 1])

    return emoji_df

def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    if not timeline.empty:
        timeline['time'] = timeline['month'] + "-" + timeline['year'].astype(str)
    else:
        timeline['time'] = []

    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline

def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)
    return user_heatmap
















