# Auto Questionnaires：
![img_2.png](imgs/img_2.png)

## 1) User story

### Role:  
Those who need to collect a large number of dummy questionnaires and surveys

### Action:
1. Open the system, 
2. import the questionnaire template,
3. select the characteristics of the survey population,
4. select the number of generated questionnaires,
5. run the App


### Goal:
Users get a sufficient number of high-quality fully-filled questionnaires and surveys

## 2) Impement - Frontend:

**Tool used**: Figma
1. Did the Wireframing of the solution web app
2. Implemented the wireframes in Figma

![image](https://media.github.tools.sap/user/78707/files/b99521f5-4044-4f02-a3aa-e3c2d142755e)
![image](https://media.github.tools.sap/user/78707/files/b397affc-821f-48e5-acca-ee6fa5d8b7df)
![image](https://media.github.tools.sap/user/78707/files/9f586c2d-8b34-4696-89d7-8eb56b1bde16)
![image](https://media.github.tools.sap/user/78707/files/dc26a893-9548-4b58-92a7-80378224c823)
![image](https://media.github.tools.sap/user/78707/files/1299e92e-9151-471c-baa7-af3a2cf99b49)
![image](https://media.github.tools.sap/user/78707/files/84e06925-2181-4483-91f7-e8a50a251f51)
![image](https://media.github.tools.sap/user/78707/files/bfca2896-08ba-49e5-9806-582559db00c8)
![image](https://media.github.tools.sap/user/78707/files/57a0965c-88c9-4c27-9f61-2fd99ca532da)


## 3) Implement - Backend:
![MicrosoftTeams-image (5).png](imgs%2FMicrosoftTeams-image%20%285%29.png)
### Summary:
1. **Write prompt**  and **character information preset**
_(prompt how ChatGPT will answer)__(set the basic information of the role that ChatGPT will play)_
2. **Ask ChatGPT to answer the questionnaire and receive ChatGPT's answers** 
_（according to presets and prompts）_ 
3. **Extract key information from answers**
4. **Statistical Analysis and Visualization**

### step 1：
```python
country = [
    'Chinese',
    'German',
    'Indian',……
]
skin_color = ['white', 'black', 'yellow']
family_wealth_level = ['very wealthy', 'wealthy', 'middle', 'poor', 'very poor']
parents_profession = [
    'farmer',
    'doctor',
    'teacher',……
]
gender = ['male', 'female']……


```
```python
def generate_prompt():
    _country = country[randint(0, len(country) - 1)]
    _skin_color = skin_color[randint(0, 2)]
    ……
    _height = randint(160, 190)
    _weight = randint(int((_height-105)*0.7), int((_height-105)*1.5))
    ……
    template = f"You are {_country}, you are {_skin_color}. Your family is {_family_wealth_level}. " \
               f"Your parents' profession is {_parents_profession}. " \
               f"You are {_gender}, {_age} years old, {_height}cm tall and {_weight}kg in weight. " \
               f"Your degree is {_degree}, your major is {_major}, and you {_like_dislike} your major. " \
               f"Your hobby is {_hobby}."
```

### step2
```python
def get_chatgpt_answer(prompt, question, num):
    api_url = 'https://api.openai.com/v1/chat/completions'  # 假想的ChatGPT API URL
    api_key01 = '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'  # 替换为你的ChatGPT API密钥
    api_key02 = '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'  # 替换为你的ChatGPT API密钥
    if num % 1:
        api_key = api_key01
    else:
        api_key = api_key02
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
    ……
```
```python
**The questions**

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
```
### step 3:
```python
def extract_data_from_answer(questionnaire):
    # 使用正则表达式匹配并提取数据
    pattern = r"\((.*?),(.*?),(.*?),(.*?),(.*?)\)"
    matches = re.search(pattern, questionnaire)

    # 生成列表
    data_list = [match.strip() if match is not None else None for match in matches.groups()]

    return data_list
```
### step 4:
```python
# 可视化男性和女性的占比
gender_counts = data['Gender'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.axis('equal')
plt.show()

# 可视化男性和女性学历的占比
gender_education_counts = data.groupby(['Gender', 'Education']).size().unstack()
gender_education_counts.plot(kind='bar', stacked=True, figsize=(8, 6))
plt.title('Gender and Education Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()
```
## 4) Some result show:
![img_6.png](imgs/img_6.png)
![img_4.png](imgs/img_4.png)
![img.png](imgs/img_7.png)
![img_8.png](imgs%2Fimg_8.png)
![img_9.png](imgs%2Fimg_9.png)

## 5) Future Scope:
1. Continue building the Frontend in HTML, CSS, Javascript, ReactJS
2. Use Flask/Django as the Backend Framework
