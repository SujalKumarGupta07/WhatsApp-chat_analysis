import re
import pandas as pd

def preprocess(data):
    # Regex pattern to match WhatsApp timestamps in various formats:
    # Android & iOS, 12-hr & 24-hr, 2-digit & 4-digit years, brackets, am/pm, etc.
    pattern = r'(?:^|\n)(?:\[?(\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}(?::\d{2})?(?:[\s\u202f\u00a0]*[aApP][mM])?)\]?(?:\s-\s|:\s|\s))'

    matches = list(re.finditer(pattern, data))
    if not matches:
        return pd.DataFrame(columns=['date', 'user', 'message', 'only_date', 'year', 'month_num', 'month', 'day', 'day_name', 'hour', 'minute', 'period'])

    raw_dates = []
    messages = []
    for i in range(len(matches)):
        raw_dates.append(matches[i].group(1))
        start_idx = matches[i].end()
        end_idx = matches[i + 1].start() if i + 1 < len(matches) else len(data)
        messages.append(data[start_idx:end_idx].strip('\r\n'))

    # Clean date strings (replace narrow non-breaking spaces and non-breaking spaces)
    cleaned_dates = pd.Series(raw_dates).str.replace('\u202f', ' ', regex=False).str.replace('\u00a0', ' ', regex=False)
    parsed_dates = pd.to_datetime(cleaned_dates, format='mixed', dayfirst=True)

    df = pd.DataFrame({'user_message': messages, 'date': parsed_dates})

    users = []
    msgs = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message, maxsplit=1)
        if len(entry) > 1 and entry[1:]:  # user name
            users.append(entry[1])
            msgs.append(entry[2])
        else:
            users.append('group_notification')
            msgs.append(entry[0])

    df['user'] = users
    df['message'] = msgs
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df