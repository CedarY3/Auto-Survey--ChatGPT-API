import time
import re
import pickle
import requests

import random


def randint(a, b):
    return random.SystemRandom().randint(a, b)


country = [
    'Chinese',
    'Japanese',
    'Korean',
    'American',
    'Canadian',
    'British',
    'French',
    'German',
    'Italian',
    'Spanish',
    'Russian',
    'Indian',
    'Australian',
    'Brazilian',
    'Mexican',
    'Argentinian'
]
skin_color = ['white', 'black', 'yellow']
family_wealth_level = ['very wealthy', 'wealthy', 'middle', 'poor', 'very poor']
parents_profession = [
    'farmer',
    'doctor',
    'teacher',
    'engineer',
    'nurse',
    'lawyer',
    'architect',
    'accountant',
    'chef',
    'police officer',
    'firefighter',
    'pilot',
    'mechanic',
    'artist',
    'writer',
    'scientist',
    'entrepreneur',
    'veterinarian',
    'musician',
    'security guard',
    'hotel cleaner',
    'freelancer',
    'unemployed',
    'retail salesperson',
    'waiter/waitress',
    'bartender',
    'cashier',
    'delivery driver',
    'janitor',
    'warehouse worker',
    'farm laborer',
    'fast food worker',
    'cleaning staff',
    'data entry clerk',
    'receptionist',
    'housekeeper',
    'day laborer',
    'food server',
    'street vendor'
]
gender = ['male', 'female']
age = list(range(18, 27))
height = list(range(160, 191))
weight = list(range(40, 90))
degree = ['High School', 'Bachelor', 'Master', 'PhD', 'Other']
major = [
    'computer science',
    'math',
    'engineering',
    'biology',
    'business',
    'psychology',
    'chemistry',
    'economics',
    'physics',
    'art',
    'history',
    'english',
    'sociology',
    'medicine',
    'linguistics',
    'political science',
    'philosophy',
    'environmental science',
    'communication',
    'nursing',
    'architecture',
    'geology',
    'music',
    'anthropology',
    'education',
    'fashion design',
    'graphic design',
    'law',
    'theater',
    'agriculture',
    'film studies',
    'nutrition',
    'social work',
    'public health',
    'urban planning',
    'marketing',
    'finance',
    'geography',
    'statistics',
    'religious studies',
    'environmental engineering',
    'linguistics',
    'mechanical engineering',
    'information technology',
    'media studies',
    'public relations',
    'criminal justice',
    'philosophy',
    'gender studies',
    'forensic science',
    'astronomy',
    'fashion merchandising',
    'international relations',
    'social media management',
    'cybersecurity'
]
like_dislike = [
    'very like',
    'like',
    'neutral',
    'dislike',
    'very dislike'
]
hobby = [
    'reading books',
    'playing sports',
    'painting',
    'watching movies',
    'listening to music',
    'cooking',
    'gardening',
    'photography',
    'traveling',
    'writing',
    'dancing',
    'knitting/crocheting',
    'playing musical instruments',
    'yoga/meditation',
    'playing video games',
    'collecting stamps/coins',
    'fishing',
    'hiking',
    'cycling',
    'volunteering',
    'bird watching',
    'singing',
    'sculpting',
    'playing board games',
    'calligraphy',
    'sewing',
    'woodworking',
    'pottery/ceramics',
    'playing chess',
    'baking',
    'interior decorating',
    'fossil hunting',
    'playing cards',
    'skydiving',
    'surfing',
    'kayaking',
    'rock climbing',
    'sky watching/ stargazing',
    'learning new languages',
    'astronomy',
    'watching sports games',
    'running/jogging',
    'motorcycling',
    'skateboarding',
    'playing tennis',
    'watching documentaries',
    'playing billiards/pool',
    'coin collecting',
    'doing puzzles',
    'genealogy/family history research'
]


def generate_prompt():
    _country = country[randint(0, len(country) - 1)]
    _skin_color = skin_color[randint(0, 2)]
    _family_wealth_level = family_wealth_level[randint(0, len(family_wealth_level) - 1)]
    _parents_profession = parents_profession[randint(0, len(parents_profession) - 1)]
    _gender = gender[randint(0, len(gender) - 1)]
    _age = randint(18, 30)
    _height = randint(160, 190)
    _weight = randint(int((_height-105)*0.7), int((_height-105)*1.5))
    _degree = degree[randint(0, len(degree) - 1)]
    _major = major[randint(0, len(major) - 1)]
    _like_dislike = like_dislike[randint(0, len(like_dislike) - 1)]
    _hobby = hobby[randint(0, len(hobby) - 1)]


    template = f"You are {_country}, you are {_skin_color}. " \
               f"Your family is {_family_wealth_level}. " \
               f"Your parents' profession is {_parents_profession}. " \
               f"You are {_gender}, {_age} years old, {_height}cm tall and {_weight}kg in weight. " \
               f"Your degree is {_degree}, your major is {_major}, and you {_like_dislike} your major. " \
               f"Your hobby is {_hobby}."
    return template, [_country, _skin_color, _family_wealth_level, _parents_profession, _gender,
                      _age, _height, _weight, _degree, _major, _like_dislike, _hobby]


def get_chatgpt_answer(prompt, question):
    api_url = 'https://api.openai.com/v1/chat/completions'  # 假想的ChatGPT API URL
    api_key = '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'  # 替换为你的ChatGPT API密钥

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    data = {
        'model': 'gpt-3.5-turbo',  # 使用ChatGPT的版本，可以根据自己的需求选择合适的版本
        'messages': [{'role': 'system', 'content': prompt},
                     {'role': 'user', 'content': question}]
    }

    response = requests.post(api_url, headers=headers, json=data)
    response_data = response.json()

    if 'choices' in response_data and len(response_data['choices']) > 0:
        return response_data['choices'][0]['message']['content']
    else:
        return "Sorry, I couldn't get an answer for your question."


def extract_data_from_answer(questionnaire):
    # 使用正则表达式匹配并提取数据
    pattern = r"\((.*?),(.*?),(.*?),(.*?),(.*?)\)"
    matches = re.search(pattern, questionnaire)

    # 生成列表
    data_list = [match.strip() if match is not None else None for match in matches.groups()]

    return data_list

    # degree = re.search(degree_pattern, questionnaire, re.IGNORECASE)
    # gender = re.search(gender_pattern, questionnaire, re.IGNORECASE)
    # exercise_times = re.search(exercise_times_pattern, questionnaire, re.IGNORECASE)
    # health_rating = re.search(health_rating_pattern, questionnaire)
    # single = re.search(single_pattern, questionnaire, re.IGNORECASE)
    #
    # if degree:
    #     degree = degree.group(1)
    # if gender:
    #     gender = gender.group(1)
    # if exercise_times:
    #     exercise_times = exercise_times.group(1)
    # if health_rating:
    #     health_rating = health_rating.group(1)
    # if single:
    #     single = single.group(1)

    # return degree, gender, exercise_times, health_rating, single


if __name__ == "__main__":
    all_prompt = []
    all_answer = []
    all_data = []
    for i in range(100):

        start_time = time.time()  # 记录函数开始时的时间戳

        prompt, preset = generate_prompt()

        all_prompt.append(prompt)
        prompt = prompt + 'I will give you a questionnaire and you have to fill it:'
        question = 'You must fill out the questionnaire below: ' \
                   '1, your degree:(); ' \
                   '2, your gender: (); ' \
                   '3, how many times do you exercise per week:();   ' \
                   '4, please rate your health by a number out of 10 points:() ' \
                   '5, are you single？()。' \
                   'You need to output your answer strictly according to the requirements:' \
                   'Enclose your answers in parentheses, separated by commas, for example:(Bachelor, Male, 3, 7, Yes)' \
                   'Do not output any other content, now, start answering.'

        answer = get_chatgpt_answer(prompt, question)
        data = extract_data_from_answer(answer)

        print(answer)
        print(i, data)

        all_data.append([preset, data])
        print(all_data)
        all_answer.append(list(answer))

        with open('prompt-list-01.bin', 'wb') as file:
            pickle.dump(all_prompt, file)

        with open('answer-list-01.bin', 'wb') as file:
            pickle.dump(all_answer, file)

        with open('data-list-01.bin', 'wb') as file:
            pickle.dump(all_data, file)

        end_time = time.time()  # 记录函数结束时的时间戳
        remaining_time = 20 - (end_time - start_time)  # 计算剩余时间
        print(f'wait {remaining_time}s')
        print('+++++++++++++++++++++++++++++++++')
        if remaining_time > 0:
            time.sleep(remaining_time)  # 暂停剩余时间，使函数每20秒运行一次

    with open('prompt-list-02.bin', 'wb') as file:
        pickle.dump(all_prompt, file)

    with open('answer-list-02.bin', 'wb') as file:
        pickle.dump(all_answer, file)

    with open('data-list-02.bin', 'wb') as file:
        pickle.dump(all_data, file)