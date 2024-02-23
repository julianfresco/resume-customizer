REPLACE_RESUME_KEY = '__INPUT_RESUME__'
REPLACE_JD_KEY = '__INPUT_JD__'
DEFAULT_RESUME = './data/resume/20240220-resume.txt'
DEFAULT_JD = './data/jobdescription/jd1.txt'
DEFAULT_SYS_PROMPT = './data/prompt/20240223-system.txt'
DEFAULT_PROMPT = './data/prompt/20240223-prompt.txt'


def get_file_text(filepath):
    with open(filepath) as file:
        file_text = file.read()
    return file_text

def get_resume(resume_file = DEFAULT_RESUME):
    return get_file_text(resume_file)

def get_jd(jd_file = DEFAULT_JD):
    return get_file_text(jd_file)

def get_system_prompt(sys_prompt_file = DEFAULT_SYS_PROMPT):
    return get_file_text(sys_prompt_file)

def compose_prompt(resume_text, job_description, prompt_file = DEFAULT_PROMPT):
    prompt_text =  get_file_text(prompt_file)
    prompt_text = prompt_text.replace(REPLACE_RESUME_KEY, resume_text)
    prompt_text = prompt_text.replace(REPLACE_JD_KEY, job_description)
    return prompt_text
    