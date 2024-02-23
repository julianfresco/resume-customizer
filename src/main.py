from openai import OpenAI
import prompt

resume_text = prompt.get_resume()
jd_text = prompt.get_jd()
system_prompt = prompt.get_system_prompt()

prompt_text = prompt.compose_prompt(resume_text, jd_text)
# print('get_prompt:', prompt_text)


client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": prompt_text}
  ]
)

print(completion.choices[0].message)